# https://nitratine.net/blog/post/python-gui-using-chrome/
from __future__ import unicode_literals

import os
import sys
import platform
import traceback

import eel

# Python function for testing it is reachable by Javascript
@eel.expose
def test_eel_function():
    try:
        test_result = "I am a Python string"

    except Exception as ex:
        ErrorMessage = ''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))
        print("ERROR:\n" + ErrorMessage)

    return test_result

def eel_start():
    page = "main.html"
    default_mode = "chrome"

    eel_kwargs = dict(
        host="localhost",
        port=8080,
        size=(800, 600)     # open at this window size
    )

    eel.init('gui')  # Give folder containing web files

    try:
        eel.start(page, mode=default_mode, **eel_kwargs)
    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, mode='edge', **eel_kwargs)
        else:
            raise

if __name__ == '__main__':
    eel_start()

# block=False serve per far eseguire altri comandi alle righe successive a eel.start
#eel.start('main.html', block=False)
