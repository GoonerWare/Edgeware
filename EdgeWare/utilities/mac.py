from pathlib import Path
import os
import shlex
import subprocess
import sys


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


# uses the above script to create a shortcut on desktop with given specs
def make_shortcut(
    path: Path,
    icon: Path | str,
    script_or_command: str | list[str],
    title: str | None = None,
    file_name: str | None = None,
) -> bool:
    if title is None:
        if isinstance(script_or_command, str):
            title = script_or_command
        elif isinstance(icon, str):
            title = icon
        else:
            title = icon.name.replace("_icon", "")

    if isinstance(icon, str):
        icon = path / "default_assets" / f"{icon}_icon.ico"

    if file_name is None:
        file_name = title

    if isinstance(script_or_command, str):
        script_path = str((path / f"{script_or_command}").absolute())
        script_or_command = [sys.executable, script_path]

    shortcut_content = f"""#!/bin/zsh
    {shlex.join(script_or_command)}
    """

    file_name = f"{file_name}.command"
    desktop_file = Path(os.path.expanduser("~/Desktop")) / file_name
    try:
        desktop_file.write_text(shortcut_content, "UTF-8")
        os.chmod(desktop_file, 0o755)  # Need to make sure the shortcut is executable
    except Exception as e:
        print(f"Shortcut error.\n\nReason: {e}")
        return False
    return True


def toggle_start_on_logon(path: Path, state: bool):
    print("Mac: Need to implement toggle_start_on_logon")
    pass


def does_desktop_shortcut_exist(name: str):
    file = Path(name)
    return Path(
        os.path.expanduser("~/Desktop") / file.with_name(f"{file.name}.command")
    ).exists()


def set_wallpaper(wallpaper_path: Path | str):
    global first_run
    if isinstance(wallpaper_path, Path):
        wallpaper_path = str(wallpaper_path.absolute())

    try:

        SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

        subprocess.Popen(SCRIPT % wallpaper_path, shell=True)

        if first_run:
            first_run = False
        return True
    except:
        sys.stderr.write("ERROR: Failed to set wallpaper. There might be a bug.\n")
        return False
