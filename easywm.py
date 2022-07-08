#!/bin/python

from __future__ import (absolute_import)
import os

# Import and start all of the code
import easywm

if os.getenv('XDG_SESSION_TYPE') == "wayland" or os.getenv('XDG_SESSION_TYPE') == "x11":
    #easywm.gui.main()

    easywm.cli.main()   # For testing, comment before merging
elif os.getenv('XDG_SESSION_TYPE') == "tty":
    easywm.cli.main()
else:
    print("Unknown Session Type")
    exit(1)
