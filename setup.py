import sys
from cx_Freeze import setup, Executable

packages = ["tkinter","pynput","threading","time","functools"]

options = {
        'build_exe': {    
            'packages':packages,
        }, 
}

setup(
    name = "BotTPAO",
    version = "0.1",
    options = options,
    description = "Alpha",
    executables = [Executable("main.py", base = "Win32GUI")]
)