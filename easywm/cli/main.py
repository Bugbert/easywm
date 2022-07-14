def main():
    from easywm.cli.survey import Survey
    import distro

    DIST = distro.id()
    match DIST:
        case "arch":
            from easywm.pkg.arch import system_wide_update, install, update
        case default:
            print("os not recognized")
            exit(5)

    print("started cli app")
    
    answers = Survey()

    system_wide_update()
    install(answers.wm)
    install(answers.term)
