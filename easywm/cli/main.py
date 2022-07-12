def main():
    from easywm.cli.survey import Survey

    print("started cli app")
    
    answers = Survey()
    print(answers.server)
