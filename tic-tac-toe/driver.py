from src.game import Game
from src.validate import validate_choice

def main():

    while True:

        game = Game()
        game.execute()

        while True:

            choice = input("\nDo you want to play again? (y/n) ")

            if validate_choice(choice):
                break
            else:
                print("Wrong Choice. Try again !! ")
            
        if choice == 'N' or choice == 'n':
            break

if __name__ == "__main__":
    main()