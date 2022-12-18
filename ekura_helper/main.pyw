﻿import os
import sys
import re
import time
from pathlib import Path

import pandas as pd
from ctypes import windll
from pynput.keyboard import Key, HotKey, Controller
import pytesseract #Text recognition
import win32.win32gui as win32gui

from scripts.base import Base, InGameBot
from scripts.gui import GUI
from scripts.launcher import Launcher
from scripts.fisher import Fisher
from scripts.miner import Miner
from scripts.screenalysis import Screenalysis
from tools import static
from tools import localsettings
from tools.directkeys import click, queryMousePosition, PressKey, ReleaseKey, moveMouseTo

windll.user32.SetProcessDPIAware() #Make windll properly aware of your hardware
pytesseract.pytesseract.tesseract_cmd = static.PYTESSERACT_PATH # Pytesseract path
keyboard = Controller()

def main():
    G = GUI()
    G.main()

    # M = Miner(char_name = localsettings.CHAR_NAME)
    # F = Fisher(char_name = 'Stand')
    # F.convertExcelToDict()
    # F.main()

    # L = Launcher()
    # L.launch('Bloodbath')

    # M.main() # Mine

if __name__ == '__main__':
    main() 