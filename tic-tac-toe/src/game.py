from src.board import Board
from src.screen import refresh_screen

class Game():

    def __init__(self) -> None:
        self.board = Board()
    
    def execute(self) -> None:

        while True:

            # getting X input
            refresh_screen(self.board)
            x_cell = input("Player X -> Choose your cell (1 - 9) : ")

            while True:

                if self.board.check_if_cell_is_valid(x_cell):

                    self.board.update_cell(x_cell, "X")
                    break

                refresh_screen(self.board)
                print("Sorry! Invalid Input. Try Again!")
                
                x_cell = input("Player X -> Choose your cell (1 - 9) : ")

            refresh_screen(self.board)

            # checking whether player X have won
            if self.board.is_winner("X"):
                print("Congrats Player X !! You Won!")
                break
            
            # checking if the game is draw
            if self.board.is_full():
                print("Game ended as a Draw !!")
                break
            
            # getting O input
            refresh_screen(self.board)
            o_cell = input("Player O -> Choose your cell (1 - 9) : ")

            while True:

                if self.board.check_if_cell_is_valid(o_cell):
    
                    self.board.update_cell(o_cell, "O")
                    break

                refresh_screen(self.board)
                print("Sorry! Invalid Input. Try Again!")

                o_cell = input("Player O -> Choose your cell (1 - 9) : ")
            
            refresh_screen(self.board)

            # checking whether player O have won
            if self.board.is_winner("O"):
                print("Congrats Player O !! You Won!")
                break
