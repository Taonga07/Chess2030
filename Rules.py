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
        # this is a comment, with the space before the text
        #this = code
        # I would add a variable here
        #self.first_turn = True

    def check_move(self, row_number, column_number, piece_to_move, turn):
    #def check_move(self, piece_to_move, attacking)
        #new_row, new_column = piece_to_move
        # you already know what colour your chess piece is
        # it's saved in self.colour - and you only call the check_move() function
        # if it's that colour's turn
        # I assume that row_number and column_number are the row and column you are moving to
        # we already know the row and column we are on self.row and self.column
        if turn == 0: #if white
            if piece_to_move[0] == 6: #if whites piece first go
                # we probably don't need lines 27 & 28, I'm going to split the next code bit over several lines, but it's all one code
                #if (
                    # if it's our first move, and we move 2
                    #( self.first_move and (abs(self.row - new_row) == 2) )
                        #or 
                        # or we just move one square (doesn't matter first move or not)
                        #abs(self.row - new_row) == 1 
                        #)
                        # and we're going in the right direction
                        #and (
                            #(self.colour == 'white' and self.row - new_row > 0)
                            #or
                            #(self.colour == 'black' and self.row - new_row < 0)
                        # )
                        # and we don't change column - check for attacking
                        #and (
                            #self.column == new_column or
                            #(attacking and abs(self.column - new_column = 1)
                            # ):
                    # abs returns the absolute value without + or - so abs(1-3) = 2 and abs(6-4) = 2
                    # you don't care which direction the piece is moving, only that it's moving 2 or less on the first go
                    # if all the above is True then we have a valid move
                    # you could check the state of self.first_move, but to be honest, it's probably not worth it
                    #self.first_move = False
                    #return True
                #don't need this code
                #if ((piece_to_move[0]-1 or piece_to_move[0]-2) == row_number) and (piece_to_move[1] == column_number):
                #    print('first go')
                #    return True
                else:
                    # I'd just
                    #return False
                    # and let your main code print the 'invalid move' statement
# you don't need any of this code
                    mssg = 'Pawns can only move forwards'
                    return mssg
            else: #not first go 
                if piece_to_move[0]-1 == row_number:
                    return True
                else:
                    mssg = 'Pawns can only move forwards once'
                    return mssg
        else: #blacks turn
            if piece_to_move[0] == 1: #if blacks piece first go
                if ((piece_to_move[0]+1 or piece_to_move[0]+2) == row_number) and (piece_to_move[1] == column_number):
                    return True
                else:
                    mssg = 'Pawns can only move forwards'
                    return mssg
            else: #not first go 
                if piece_to_move[0]+1 == row_number:
                    return True
                else:
                    mssg = 'Pawns can only move forwards once'
                    return mssg
#down to here

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
