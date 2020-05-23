import Chess, Rules, os

class GameObject():
    def __init__(self, piece, icon, colour, column, row, value):
        self.icon = icon
        self.colour = colour
        self.piece = piece
        self.row = row
        self.column = column
        self.value = value

    def move_piece(self, new_position):
        self.row, self.column = new_position

    def check_move(self, destination_square, square, board):
        for i in self.possible_moves:
            row, column = i
            if i != board[row][column]:
                square.config('green')
            else:
                square.config('red')
            if i == destination_square:
                return True
            # if you put else here, it will check your destination against the first possible move
            # and if it's not valid, it'll exit without checking the others
            
        # you want to check all possible moves, and then exit with False if none are valid
        return False

class Pawn(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 1)
        self.piece = 'Pawn'
        self.first_move = True
    
    def highlight_move(self, board):
        self.possible_moves = []
        if self.colour == 'white':
            # if the square in front of us is clear, we can move to it
            if board[self.row - 1][self.column] == None: 
                self.possible_moves.append((self.row - 1, self.column))
                # if its our first move the the square 2 in front is clear, we can move to it also
                if ( board[self.row - 2][self.column] == None ) and (self.first_move == True):
                    self.possible_moves.append((self.row - 2, self.column))
            # these are not elif, they are new if conditional statements
            # if we're on column 7 (the last one on the row), we can't check column + 1 because it's off the board
            if self.column < 7:
                if board[self.row - 1][self.column + 1] != None:
                    self.possible_moves.append((self.row - 1, self.column + 1))
            # and if we're on the first column, we can't check column - 1
            if self.column > 0:
                if board[self.row - 1][self.column - 1] != None:
                    self.possible_moves.append((self.row - 1, self.column - 1))
        
        elif self.colour == 'black':
            # if the square in front of us is clear, we can move to it
            if board[self.row + 1][self.column] == None: 
                self.possible_moves.append((self.row + 1, self.column))
                # if its our first move the the square 2 in front is clear, we can move to it also
                if ( board[self.row + 2][self.column] == None ) and (self.first_move == True):
                    self.possible_moves.append((self.row + 2, self.column))
            # if we're on column 7 (the last one on the row), we can't check column + 1 because it's off the board
            if self.column < 7:
                if board[self.row + 1][self.column + 1] != None:
                    self.possible_moves.append((self.row + 1, self.column + 1))
            # and if we're on the first column, we can't check column - 1
            if self.column > 0:
                if board[self.row + 1][self.column - 1] != None:
                    self.possible_moves.append((self.row + 1, self.column - 1))
            #if board[self.row + 1][self.column] == board[7][self.column]:
                
        
        print('possible moves', self.possible_moves)
        #how would i highlight pieces from here i kow it is like:
        ## square.config('green')
        # but it dose not work
        #attacking piece colour == 'red'
        #my piece == 'blue'
        #normal alowed moves == 'green'

class Rook(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
        self.value = 4

#    def check_move(self, new_row_number,new_column_number):
#        return True

class Bishop(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Bishop'
        self.value = 3

class King(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'King'
        self.value = 1

class Queen(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Queen'
        self.value = 9

class Knight(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Knight'
        self.value = 5

# our varibles/lists

path = os.getcwd() + '/Chess_Resources/'
icons = ['White_Rook.gif', 'White_Bishop.gif', 'White_Knight.gif', 'White_Queen.gif', 'White_King.gif', 'White_Knight.gif', 'White_Bishop.gif', 'White_Rook.gif', 'Black_Rook.gif', 'Black_Bishop.gif', 'Black_Knight.gif', 'Black_King.gif', 'Black_Queen.gif', 'Black_Knight.gif', 'Black_Bishop.gif', 'Black_Rook.gif'] #/media/barton_hill/THOMAS/ Digi@Local/MyCode/Python/4 - Green/Code/Chess_Resources/ gameOver = False
pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Kight', 'Rook']

light_bttnlcr ='white'
dark_bttnlcr = 'black'

turn = 0
onclick = 0
square_clicked = (0, 0) 
old_colour = 'white'