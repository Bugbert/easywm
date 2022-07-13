def escalation_program():
    from os.path import exists

    if exists('/usr/bin/doas'):
        return "doas"
    elif exists('/usr/bin/sudo'):
        return "sudo"
    else:
        print("error: no escalation program recognized")
        exit(5)

# Constants
ESCALATION_PROGRAM = escalation_program()
