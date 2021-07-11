class Board():

    def __init__(self) -> None:

        self.cells = {1 : " ", 2 : " ", 3 : " ",
                      4 : " ", 5 : " ", 6 : " ", 
                      7 : " ", 8 : " ", 9 : " "}
    

    def display(self) -> None:

        print(' ' + self.cells[1] + ' | ' + self.cells[2] + ' | ' + self.cells[3])
        print("---+---+---")
        print(' ' + self.cells[4] + ' | ' + self.cells[5] + ' | ' + self.cells[6])
        print("---+---+---")
        print(' ' + self.cells[7] + ' | ' + self.cells[8] + ' | ' + self.cells[9])
    

    def check_if_cell_is_valid(self, index) -> bool:

        if index.isdigit() and int(index) >= 1 and int(index) <= 9 and self.cells[int(index)] == " ":
            return True

        return False
    

    def is_winner(self, player) -> bool:

        # check rows probabilities
        for i in range(1, 10, 3):
            if self.cells[i] == player and self.cells[i + 1] == player and self.cells[i + 2] == player:
                return True

        # check column probabilities
        for i in range(1, 4):
            if self.cells[i] == player and self.cells[i + 3] == player and self.cells[i + 6] == player:
                return True
        
        # check diagonal probabilities
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        
        return False
        

    def update_cell(self, index, player) -> None:

        self.cells[int(index)] = player


    def is_full(self) -> bool:
        
        for i in range(1, 10):
            if self.cells[i] == " ":
                return False
        
        return True