def validate_choice(choice) -> bool:
    
    if choice == 'y' or choice == 'n' or choice == 'Y' or choice == 'N':
        return True
    
    return False