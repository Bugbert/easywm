import os

os.system('sh /etc/os-release') # Makes version info environment variables

# Constants

DIST = os.getenv('ID')

# Starts program

if os.getenv('XDG_SESSION_TYPE') == "wayland" or os.getenv('XDG_SESSION_TYPE') == "x11":
    from easywm.gui.main import main
elif os.getenv('XDG_SESSION_TYPE') == "tty":
    from easywm.cli.main import main
else:
    print("unknown session type")
    exit(1)
