from os import system, name

def clear_screen():

    # for windows
    if name == 'nt':
        system('cls')
    
    # for mac and linux
    else:
        system('clear')