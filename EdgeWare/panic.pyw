import os
from pathlib import Path
from multiprocessing.connection import Client
from array import array
from utilities import utilities
from panic_listener import ADDRESS, AUTH_KEY

PATH: Path = Path(__file__).parent

timeObjPath = PATH / "hid_time.dat"

# checking timer
try:
    utilities.expose_file(timeObjPath)
except:
    if os.path.exists(os.path.join(PATH, "hid_time.dat")):
        utilities.hide_file(timeObjPath)
        # sudoku if timer after hiding file again
        os.kill(os.getpid(), 9)


with Client(ADDRESS, authkey=AUTH_KEY) as conn:
    utilities.set_wallpaper(PATH / "default_assets" / "default_win10.jpg")
    conn.send("panic_close")
