import ctypes
from pathlib import Path


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


def shortcut_script(pth_str: str, startup_path: str, title: str):
    # strings for batch script to write vbs script to create shortcut on desktop
    # stupid and confusing? yes. the only way i could find to do this? also yes.
    print(pth_str)
    return [
        "@echo off\n" 'set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"\n',
        'echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%\n',
        f'echo sLinkFile = "{startup_path}\\{title}.lnk" >> %SCRIPT%\n',
        "echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%\n",
        f'echo oLink.WorkingDirectory = "{pth_str}\\" >> %SCRIPT%\n',
        f'echo oLink.TargetPath = "{pth_str}\\start.pyw" >> %SCRIPT%\n',
        "echo oLink.Save >> %SCRIPT%\n",
        "cscript /nologo %SCRIPT%\n",
        "del %SCRIPT%",
    ]


# uses the above script to create a shortcut on desktop with given specs
def make_shortcut(tList: list) -> bool:
    with open(PATH + "\\tmp.bat", "w", encoding="utf-8") as bat:
        bat.writelines(
            shortcut_script(tList[0], tList[1], tList[2])
        )  # write built shortcut script text to temporary batch file
    try:
        logging.info(f"making shortcut to {tList[2]}")
        subprocess.call(PATH + "\\tmp.bat")
        os.remove(PATH + "\\tmp.bat")
        return True
    except Exception as e:
        print("failed")
        logging.warning(
            f"failed to call or remove temp batch file for making shortcuts\n\tReason: {e}"
        )
        return False


def toggle_start_on_logon(path: Path, state: bool):
    # FIXME: Find a crossplatform way to add edgeware to startup aplication
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
        print("uwu")