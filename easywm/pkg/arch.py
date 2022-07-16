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

def seatd_enable():
    from easywm.pkg import ESCALATION_PROGRAM
    from easywm.pkg import USERNAME
    import os
    os.system(ESCALATION_PROGRAM + ' systemctl enable seatd')
    os.system(ESCALATION_PROGRAM + ' systemctl start seatd')
    os.system(ESCALATION_PROGRAM + ' usermod -G seat ' + USERNAME)
