from src.board import Board
from src.tools.clear import clear_screen

def refresh_screen(board):

    clear_screen()

    print("Welcome to 𝕿𝖎𝖈-𝖙𝖆𝖈-𝖙𝖔𝖊 by Zeo")

    board.display()