from pathlib import Path
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
def make_shortcut(tList: list) -> bool:
    print("Linux: Need to implement make_shortcut")
    pass


def toggle_start_on_logon(path: Path, state: bool):
    print("Linux: Need to implement toggle_start_on_logon")
    pass


def does_desktop_shortcut_exist(name: str):
    print("Linux: Need to implement does_desktop_shortcut_exist")
    pass


def set_wallpaper(wallpaper_path: Path | str):
    print("Linux: Need to implement set_wallpaper")
    pass


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
