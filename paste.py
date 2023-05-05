# -*- coding: utf-8 -*-
#python -m PyInstaller -F -w *.py
from time import sleep
from pynput.keyboard import Controller
import win32clipboard as wcd
import win32con

def get_text():
    wcd.OpenClipboard()
    try:
        contents = wcd.GetClipboardData(win32con.CF_TEXT)
        legal = 1
    except:
        legal = 0
    wcd.CloseClipboard()
    if legal == 1:
         return contents.decode('GBK')
    else:
         return '<ContentsERROR>'

if __name__ == "__main__":
    keyboard = Controller()
    str = get_text()
    for i in range(0,3):
        sleep(1)
        print(3-i)
    keyboard.type(str)