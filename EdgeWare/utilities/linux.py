import codecs
from collections.abc import Callable
import os
from pathlib import Path
import re
import shutil
import subprocess
from tkinter import messagebox
from utilities.dependencies import DEPENDENCIES


def hide_file(path: Path | str):
    if isinstance(path, str):
        path = Path(path)
    hidden_path = path.parent / f".{path.name}"
    if path.exists():
        path.rename(hidden_path)


def expose_file(path: Path | str):
    if isinstance(path, str):
        path = Path(path)
    hidden_path = path.parent / f".{path.name}"
    if hidden_path.exists():
        hidden_path.rename(path)


def create_shortcut_script(pth_str: str, startup_path: str, title: str):
    print("Linux: Need to implement create_shortcut_script")
    pass


# uses the above script to create a shortcut on desktop with given specs
def make_shortcut(
    path: Path,
    icon: str,
    script: str,
    title: str | None = None,
    startup_path: str | None = None,
) -> bool:
    print("Linux: Need to implement make_shortcut")
    pass


def toggle_start_on_logon(path: Path, state: bool):
    print("Linux: Need to implement toggle_start_on_logon")
    pass


def does_desktop_shortcut_exist(name: str):
    print("Linux: Need to implement does_desktop_shortcut_exist")
    pass


def set_wallpaper(wallpaper: Path) -> None:
    desktop = get_desktop_environment()
    commands = get_wallpaper_commands(wallpaper, desktop)
    function = get_wallpaper_function(wallpaper, desktop)

    if len(commands) > 0:
        for command in commands:
            try:
                subprocess.Popen(command, shell=True)
            except Exception as e:
                logging.warning(f"Failed to run {command}. Reason: {e}")
    elif function:
        try:
            function()
        except Exception as e:
            logging.warning(f"Failed to set wallpaper. Reason: {e}")
    else:
        logging.info(f"Can't set wallpaper for desktop environment {desktop}")


def open_directory(url: str) -> None:
    subprocess.Popen(["xdg-open", url])


def check_dependencies() -> tuple[list[DEPENDENCIES], str]:
    missing_dependencies: list[DEPENDENCIES] = []
    messages: list[str] = []
    try:
        subprocess.check_output(["which", "ffmpeg"])
    except Exception as e:
        missing_dependencies.append(DEPENDENCIES.FFMPEG)
        messages.append("Couldn't find dependency FFMPEG.")

    try:
        import sounddevice
    except Exception as e:
        if len(e.args) == 1 and e.args[0] == "PortAudio library not found":
            missing_dependencies.append(DEPENDENCIES.PORT_AUDIO)
            messages.append(
                f"{e.args[0]}(Search for: 'libportaudio2' or 'libportaudio-dev')"
            )

    message = ""
    if messages:
        message = "\n".join((f"- {msg}" for msg in messages))
        messagebox.showerror("Missing dependencies", message)

    return missing_dependencies, message


def get_desktop_environment() -> str:
    desktop = os.environ.get("XDG_CURRENT_DESKTOP") or os.environ.get("DESKTOP_SESSION")
    if desktop:
        desktop = desktop.lower()

        special_cases = [
            ("xubuntu", "xfce4"),
            ("ubuntustudio", "kde"),
            ("ubuntu", "gnome"),
            ("lubuntu", "lxde"),
            ("kubuntu", "kde"),
            ("razor", "razor-qt"),  # e.g. razorkwin
            ("wmaker", "windowmaker"),  # e.g. wmaker-common
            ("pop", "gnome"),
        ]

        for special, actual in special_cases:
            if desktop.startswith(special):
                return actual
        if "xfce" in desktop:
            return "xfce4"
        return desktop
    if os.environ.get("KDE_FULL_SESSION") == "true":
        return "kde"
    if is_running("xfce-mcs-manage"):
        return "xfce4"
    if is_running("ksmserver"):
        return "kde"

    return "unknown"


def get_wallpaper_commands(wallpaper: Path, desktop: str) -> list[str]:
    commands = {
        "xfce4": [
            f'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s "{wallpaper}"',
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-style -s 3",
            "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-show -s true",
        ],
        "mate": [f'gsettings set org.mate.background picture-filename "{wallpaper}"'],
        "icewm": [f'icewmbg "{wallpaper}"'],
        "blackbox": [f'bsetbg -full "{wallpaper}"'],
        "lxde": [f'pcmanfm --set-wallpaper "{wallpaper}" --wallpaper-mode=scaled'],
        "windowmaker": [f'wmsetbg -s -u "{wallpaper}"'],
        "sway": [f'swaybg -o "*" -i "{wallpaper}" -m fill'],
        "hyprland": [
            f'hyprctl hyprpaper preload "{wallpaper}"',
            f'hyprctl hyprpaper wallpaper ",{wallpaper}"',
        ],
        **dict.fromkeys(
            ["gnome", "unity", "cinnamon"],
            [
                f'gsettings set org.gnome.desktop.background picture-uri "file://{wallpaper}"',
                f'gsettings set org.gnome.desktop.background picture-uri-dark "file://{wallpaper}"',
            ],
        ),
        **dict.fromkeys(
            ["trinity"],
            [f'dcop kdesktop KBackgroundIface setWallpaper 0 "{wallpaper}" 6'],
        ),
        **dict.fromkeys(
            ["fluxbox", "jwm", "openbox", "afterstep"], [f'fbsetbg "{wallpaper}"']
        ),
    }

    return commands.get(desktop) or (
        get_wm_wallpaper_commands()
        if desktop in ["i3", "awesome", "dwm", "xmonad", "bspwm"]
        else []
    )


def get_wm_wallpaper_commands(wallpaper: Path) -> list[str]:
    session = os.environ.get("XDG_SESSION_TYPE", "").lower()  # "x11" or "wayland"
    setters = {
        "x11": [
            ("nitrogen", [f'nitrogen --set-zoom-fill "{wallpaper}"']),
            ("feh", [f'feh --bg-scale "{wallpaper}"']),
            ("habak", [f'habak -ms "{wallpaper}"']),
            ("hsetroot", [f'hsetroot -fill "{wallpaper}"']),
            ("chbg", [f'chbg -once -mode maximize "{wallpaper}"']),
            ("qiv", [f'qiv --root_s "{wallpaper}"']),
            ("xv", [f'xv -max -smooth -root -quit "{wallpaper}"']),
            (
                "xsri",
                [
                    f'xsri --center-x --center-y --scale-width=100 --scale-height=100 "{wallpaper}"'
                ],
            ),
            ("xli", [f'xli -fullscreen -onroot -quiet -border black "{wallpaper}"']),
            ("xsetbg", [f'xsetbg -fullscreen -border black "{wallpaper}"']),
            ("fvwm-root", [f'fvwm-root -r "{wallpaper}"']),
            ("wmsetbg", [f'wmsetbg -s -S "{wallpaper}"']),
            ("Esetroot", [f'Esetroot -scale "{wallpaper}"']),
            (
                "display",
                [
                    f'display -sample `xwininfo -root 2> /dev/null|awk "/geom/{{print $2}}"` -window root "{wallpaper}"'
                ],
            ),
        ],
        "wayland": [],
    }

    for program, commands in setters.get(session, []):
        if shutil.which(program):
            return commands

    return []


def get_wallpaper_function(wallpaper: Path, desktop: str) -> Callable[[], None] | None:
    def razor_qt():
        desktop_conf = ConfigParser()

        config_home = os.environ.get("XDG_CONFIG_HOME") or os.environ.get(
            "XDG_HOME_CONFIG", os.path.expanduser(".config")
        )
        config_dir = os.path.join(config_home, "razor")

        # Development version
        desktop_conf_file = os.path.join(config_dir, "desktop.conf")
        if os.path.isfile(desktop_conf_file):
            config_option = r"screens\1\desktops\1\wallpaper"
        else:
            desktop_conf_file = os.path.expanduser(".razor/desktop.conf")
            config_option = r"desktops\1\wallpaper"
        desktop_conf.read(os.path.join(desktop_conf_file))
        try:
            if desktop_conf.has_option(
                "razor", config_option
            ):  # only replacing a value
                desktop_conf.set("razor", config_option, wallpaper)
                with codecs.open(
                    desktop_conf_file,
                    "w",
                    encoding="utf-8",
                    errors="replace",
                ) as f:
                    desktop_conf.write(f)
        except Exception:
            pass

    functions = {"razor-qt": razor_qt}

    return functions.get(desktop)


def is_running(process: str) -> bool:
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    if s.stdout:
        return any(re.search(process, line.decode().strip()) for line in s.stdout)
    return False
