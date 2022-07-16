def main():
    from easywm.cli.survey import Survey
    import distro

    DIST = distro.id()
    match DIST:
        case "arch":
            import easywm.pkg.arch
            from arch import *
        case default:
            print("os not recognized")
            exit(5)

    print("started cli app")
    
    answers = Survey()

    system_wide_update()
    install(answers.wm)
    install(answers.term)

    if answers.server == "wayland":
        seatd_enable()
    elif answers.server == "x11":
        install('startx')

