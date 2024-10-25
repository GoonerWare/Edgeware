from pathlib import Path


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
    print("Mac: Need to implement create_shortcut_script")
    pass


# uses the above script to create a shortcut on desktop with given specs
def make_shortcut(
    path: Path,
    icon: str,
    script: str,
    title: str | None = None,
    startup_path: str | None = None,
) -> bool:
    print("Mac: Need to implement make_shortcut")
    pass


def toggle_start_on_logon(path: Path, state: bool):
    print("Mac: Need to implement toggle_start_on_logon")
    pass


def does_desktop_shortcut_exist(name: str):
    print("Mac: Need to implement does_desktop_shortcut_exist")
    pass


def set_wallpaper(wallpaper_path: Path | str):
    print("Mac: Need to implement set_wallpaper")
    pass