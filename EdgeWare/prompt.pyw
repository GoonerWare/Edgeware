import json
import os
import pathlib
import random as rand
import tkinter as tk
import utilities
from tkinter import *
from tkinter import messagebox
from screeninfo import get_monitors

hasData = False
textData = {}
maxMistakes = 3
submission_text = "I Submit <3"
command_text = "Type for me, slut~"

PATH = pathlib.Path(__file__).parent
os.chdir(PATH)

CONFIG_FILE = PATH / "config.cfg"

maxMistakes = int(json.loads(CONFIG_FILE.read_text())["promptMistakes"])

PROMPT_FILE = PATH / "resource" / "prompt.json"
if PROMPT_FILE.exists():
    hasData = True
    textData = json.loads(PROMPT_FILE.read_text("UTF-8"))
    try:
        submission_text = textData["subtext"]
    except:
        print("no subtext")
    try:
        command_text = textData["commandtext"]
    except:
        print("no commandtext")

if not hasData:
    messagebox.showerror(
        "Prompt Error",
        'Resource folder contains no "prompt.json". Either set prompt freq to 0 or add "prompt.json" to resource folder.',
    )


def unborderedWindow():
    if not hasData:
        exit()
    root = Tk()
    label = tk.Label(root, text="\n" + command_text + "\n")
    label.pack()

    txt = buildText()

    monitor = next(m for m in get_monitors() if m.is_primary)
    wid = monitor.width / 4
    hgt = monitor.height / 2

    textLabel = Label(root, text=txt, wraplength=wid)
    textLabel.pack()

    root.geometry(
        "%dx%d+%d+%d"
        % (wid, hgt, monitor.x + 2 * wid - wid / 2, monitor.y + hgt - hgt / 2)
    )

    if utilities.is_windows():
        root.overrideredirect(True)

    root.frame = Frame(root, borderwidth=2, relief=RAISED)
    root.frame.pack_propagate(True)
    root.wm_attributes("-topmost", 1)

    inputBox = Text(root)
    inputBox.pack()

    subButton = Button(
        root,
        text=submission_text,
        command=lambda: checkTotal(root, txt, inputBox.get(1.0, "end-1c")),
    )
    subButton.place(
        x=wid - 5 - subButton.winfo_reqwidth(), y=hgt - 5 - subButton.winfo_reqheight()
    )
    root.mainloop()


def buildText():
    moodList = textData["moods"]
    freqList = textData["freqList"]
    outputPhraseCount = rand.randint(int(textData["minLen"]), int(textData["maxLen"]))
    strVar = ""
    selection = rand.choices(moodList, freqList, k=1)
    for i in range(outputPhraseCount):
        strVar += (
            textData[selection[0]][rand.randrange(0, len(textData[selection[0]]))] + " "
        )
    return strVar.strip()


def checkTotal(root, a, b):
    if checkText(a, b):
        root.destroy()


def checkText(a, b):
    mistakes = 0
    if len(a) != len(b):
        mistakes += abs(len(a) - len(b))
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            mistakes += 1
    return mistakes <= maxMistakes


try:
    unborderedWindow()
except Exception as e:
    messagebox.showerror(
        "Prompt Error", "Could not create prompt window.\n[" + str(e) + "]"
    )
