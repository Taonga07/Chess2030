import Chess, os

class GameObject():
    def __init__(self, piece, icon, colour, column, row, value):
        self.icon = icon
        self.colour = colour
        self.piece = piece
        self.row = row
        self.column = column
        self.value = value
        
class Pawn(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 1)
        self.piece = 'Pawn'
#        self.value = 1

    def check_move(self, row_number, column_number, piece_to_move):
        #if white
        if piece_to_move[0] == 2:
            if (piece_to_move[0]+1 or piece_to_move[0]+2) == row_number:
                return True
            else:
                Chess.mssg = 'Pawns can oly move forwards'
                return False
        else:
            if  piece_to_move[1]+2 == row_number:
                return True
            else:
                Chess.mssg = 'Pawns can oly move forwards'
                return False

class Rook(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
#        self.value = 4

    def check_move(self, new_row_number,new_column_number):
        return True

class Bishop(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
#        self.value = 4

    def check_move(self, new_row_number,new_column_number):
        return True

class King(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
#        self.value = 4

    def check_move(self, new_row_number,new_column_number):
        return True

class Queen(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
#        self.value = 4

    def check_move(self, new_row_number,new_column_number):
        return True

class Knight(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
#        self.value = 4

    def check_move(self, new_row_number,new_column_number):
        return True

# our varibles/lists

path = os.getcwd() + '/Chess_Resources/'
icons = ['White_Rook.gif', 'White_Bishop.gif', 'White_Knight.gif', 'White_Queen.gif', 'White_King.gif', 'White_Knight.gif', 'White_Bishop.gif', 'White_Rook.gif', 'Black_Rook.gif', 'Black_Bishop.gif', 'Black_Knight.gif', 'Black_King.gif', 'Black_Queen.gif', 'Black_Knight.gif', 'Black_Bishop.gif', 'Black_Rook.gif'] #/media/barton_hill/THOMAS/ Digi@Local/MyCode/Python/4 - Green/Code/Chess_Resources/ gameOver = False
pieces = ['Rook', 'Bishop', 'Knight', 'Queen', 'King', 'Knight', 'Bishop', 'Rook']

light_bttnlcr ='white'
dark_bttnlcr = 'black'

turn = 0
onclick = 0
piece_to_move = (0) 
old_colour = 'white'
