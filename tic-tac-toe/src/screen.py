from src.board import Board
from src.tools.clear import clear_screen

def refresh_screen(board):

    clear_screen()

    print("Welcome to πΏππ-πππ-πππ by Zeo")

    board.display()