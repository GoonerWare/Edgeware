import ctypes
import os
import subprocess
import tempfile
from pathlib import Path
import logging


HIDDEN_ATTR = 0x02
SHOWN_ATTR = 0x08


def hide_file(path: Path | str):
    if isinstance(path, Path):
        path = str(path.absolute())
    ctypes.windll.kernel32.SetFileAttributesW(path, HIDDEN_ATTR)


def expose_file(path: Path | str):
    if isinstance(path, Path):
        path = str(path.absolute())
    ctypes.windll.kernel32.SetFileAttributesW(path, SHOWN_ATTR)


def create_shortcut_script(
    path: Path,
    icon: str,
    script: str,
    title: str | None = None,
    startup_path: str | None = None,
):
    # strings for batch script to write vbs script to create shortcut on desktop
    # stupid and confusing? yes. the only way i could find to do this? also yes.
    if title is None:
        title = f"Edgeware_{script}"

    if startup_path is None:
        startup_path = "%USERPROFILE%\\Desktop"

    path_str = str(path.absolute())

    return [
        "@echo off\n" 'set SCRIPT="%TEMP%\\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"\n',
        'echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%\n',
        f'echo sLinkFile = "{startup_path}\\{title}.lnk" >> %SCRIPT%\n',
        "echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%\n",
        f'echo oLink.WorkingDirectory = "{path_str}\\" >> %SCRIPT%\n',
        f'echo oLink.IconLocation = "{path_str}\\default_assets\\{icon}_icon.ico" >> %SCRIPT%\n',
        f'echo oLink.TargetPath = "{sys.executable}" >> %SCRIPT%\n',
        f'echo oLink.Arguments = "{path_str}\\{script}" >> %SCRIPT%\n',
        "echo oLink.Save >> %SCRIPT%\n",
        "cscript /nologo %SCRIPT%\n",
        "del %SCRIPT%",
    ]


# uses the above script to create a shortcut on desktop with given specs
def make_shortcut(
    path: Path,
    icon: str,
    script: str,
    title: str | None = None,
    startup_path: str | None = None,
) -> bool:
    success = False
    with tempfile.NamedTemporaryFile(
        "w",
        suffix=".bat",
        delete=False,
    ) as bat:
        bat.writelines(
            create_shortcut_script(path, icon, script, title, startup_path)
        )  # write built shortcut script text to temporary batch file

    try:
        logging.info(f"making shortcut to {script}")
        subprocess.run(bat.name)
        success = True
    except Exception as e:
        print("failed")
        logging.warning(
            f"failed to call or remove temp batch file for making shortcuts\n\tReason: {e}"
        )

    if os.path.exists(bat.name):
        os.remove(bat.name)

    return success


def toggle_start_on_logon(path: Path, state: bool):
    try:
        startup_path = os.path.expanduser(
            "~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        )
        logging.info(f"trying to toggle startup bat to {state}")
        if state:
            make_shortcut(path, "default", "start.pyw", "EdgeWare", startup_path)
            logging.info("toggled startup run on.")
        else:
            os.remove(os.path.join(startup_path, "edgeware.lnk"))
            logging.info("toggled startup run off.")
    except Exception as e:
        errText = (
            str(e)
            .lower()
            .replace(
                os.environ["USERPROFILE"].lower().replace("\\", "\\\\"),
                "[USERNAME_REDACTED]",
            )
        )
        logging.warning(f"failed to toggle startup bat.\n\tReason: {errText}")


def does_desktop_shortcut_exist(name: str):
    file = Path(name)
    return Path(
        os.path.expanduser("~/Desktop") / file.with_name(f"{file.name}.lnk")
    ).exists()


def set_wallpaper(wallpaper_path: Path | str):
    if isinstance(wallpaper_path, Path):
        wallpaper_path = str(wallpaper_path.absolute())

    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
