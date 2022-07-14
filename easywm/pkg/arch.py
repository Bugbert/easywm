def system_wide_update():
    from easywm.pkg import ESCALATION_PROGRAM
    import os
    os.system(ESCALATION_PROGRAM + ' pacman -Syu')
    
def install(package):
    from easywm.pkg import ESCALATION_PROGRAM
    import os
    os.system(ESCALATION_PROGRAM + ' pacman -S ' + package)

def update(package):
    from easywm.pkg.arch import install
    install(package)
