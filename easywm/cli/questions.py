# All functions asking the user for something will be labled af (ask for) and then
# the name of what it's getting

def af_server():    # This is question 1
    import easywm.misc.variables as var

    answer = input('''
Choose a display server:
    1) wayland
    2) x11

> ''')
    
    match answer:
        case '0':
            print("this is the first question")
            return
        case '1':
            var.current_question += 1
            return "wayland"
        case '2':
            var.current_question += 1
            return "x11"
        case default:
            print("please choose a valid option")
            return

def af_wm(server):  # Question 2
    import easywm.misc.variables as var

    if server == "wayland":
        answer = input('''
Choose a window manager:
    1) sway

> ''')
        match answer:
            case '0':
                var.current_question -= 1
                return
            case '1':
                var.current_question += 1
                return "sway"
            case default:
                print("please choose a valid option")
                return
    elif server == "x11":
        answer = input('''
Choose a window manager:
    1) i3

> ''')
        match answer:
            case '0':
                var.current_question -= 1
                return
            case '1':
                var.current_question += 1
                return "i3"
            case default:
                print("please choose a valid option")
                return
    else:
        print("error: unknown server")
        exit(2)                       

def af_term(server):    # Question 3
    import easywm.misc.variables as var

    if server == "wayland":
        answer = input('''
Choose a terminal emulalator:
    1) foot
    2) alacritty

> ''')
        match answer:
            case '0':
                var.current_question -= 1
                return
            case '1':
                var.current_question += 1
                return "foot"
            case '2':
                var.current_question += 1
                return "alacritty"
            case default:
                print("please choose a valid option")
                return
    elif server == "x11":
        answer = input('''
Choose a terminal emulalator:
    1) alacritty
    2) xterm
    
> ''')
        match answer:
            case '0':
                var.current_question -= 1
                return
            case '1':
                var.current_question += 1
                return "alacritty"
            case '2':
                var.current_question += 1
                return "xterm"
            case default:
                print("please choose a valid option")
                return
    else:
        print("error: unknown server")
        exit(2)                       

def af_los():   # Question 4, askes weather it should lanch on start
    import easywm.misc.variables as var

    answer = input('''
Should this program launch a graphical session on start?
    1) Yes
    2) No

> ''')
    match answer:
        case '0':
            var.current_question -= 1
            return
        case '1':
            var.current_question += 1
            return True
        case '2':
            var.current_question += 1
            return False
        case default:
            print("please choose a valid option")
            return

def af_confirm(server, wm, term, los):
    import easywm.misc.variables as var

    print('''
Are these answers good?
    display server: ''', server, '''
    window manager: ''', wm, '''
    terminal emulalator: ''', term, '''
    launch on start: ''', los, '''

''')

    answer = input("(yes/no) ").lower().strip()
    
    match answer:
        case '0':
            var.current_question -= 1
            return
        case 'yes':
            var.current_question += 1
            return True
        case 'no':
            var.current_question += 1
            return False
        case default:
            print("please choose a valid option")
            return

