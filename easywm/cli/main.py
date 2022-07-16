def main():
    from easywm.cli.survey import Survey
    import distro

    DIST = distro.id()
    match DIST:
        case "arch":
            import easywm.pkg.arch as sys
        case default:
            print("os not recognized")
            exit(5)

    print("started cli app")
    
    answers = Survey()

    sys.system_wide_update()
    sys.install(answers.wm)
    sys.install(answers.term)

    if answers.server == "wayland":
        sys.seatd_enable()
    elif answers.server == "x11":
        sys.install('startx')

