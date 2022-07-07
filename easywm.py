#!/bin/python

import os

import easywm

if os.getenv('XDG_SESSION_TYPE') == "wayland" or os.getenv('XDG_SESSION_TYPE') == "x11":
    #easywm.gui.main()
    print("detected gui session")
elif os.getenv('XDG_SESSION_TYPE') == "tty":
    #easywm.cli.main()
    print("detected tty session")
else:
    print("Unknown Session Type")
    exit(1)
