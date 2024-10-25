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


def shortcut_script(pth_str: str, startup_path: str, title: str):
    print("Linux: Need to implement shortcut_script")
    return True


# uses the above script to create a shortcut on desktop with given specs
def make_shortcut(tList: list) -> bool:
    print("Linux: Need to implement make_shortcut")
    return True


def toggle_start_on_logon(path: Path, state: bool):
    print("Linux: Need to implement toggle_start_on_logon")
    return True