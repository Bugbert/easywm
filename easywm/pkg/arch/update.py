def system_wide_update():
    from easywm.pkg import ESCALATION_PROGRAM
    import os

    COMMAND = ESCALATION_PROGRAM + ' pacman -Syu'
    os.system(COMMAND)

def update_pkg(package):
    from easywm.pkg import ESCALATION_PROGRAM
    import os

    COMMAND = ESCALATION_PROGRAM + ' pacman -S ' + package
    os.system(COMMAND)
