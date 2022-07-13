def main():
    from easywm.cli.survey import Survey
    import distro

    DIST = distro.id()
    match DIST:
        case "arch":
            from easywm.pkg.arch import update

    print("started cli app")
    
    answers = Survey()
    update.system_wide_update()
