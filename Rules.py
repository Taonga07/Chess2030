import Chess, Rules, os

class GameObject():
    def __init__(self, piece, icon, colour, column, row, value):
        self.icon = icon
        self.colour = colour
        self.piece = piece
        self.row = row
        self.column = column
        self.possible_moves = []
        self.value = value

    def move_piece(self, new_position):
        self.row, self.column = new_position

    def highlight_moves(self, window, board):
        for i in self.possible_moves:
            row_number, column_number = i # get row and column of position i in board
            square = window.grid_slaves(row = row_number, column = column_number)[0] 
            if board[row_number][column_number] == None: #if there is nothing at position i
                square.config(bg='green') # highlight position i green
            else: # none has no attrubrite to clour this stops this error
                print(self.colour, board[row_number][column_number].color) 
                if board[row_number][column_number].color != self.colour:
                    square.config(bg='red') # highlight position i red

    def check_move(self, destination_square):
        for i in self.possible_moves: # goes through each possple move possition
            if i == destination_square: # if where we are moving to is an postion in possible moves
                return True # say yes you can move
        #if we go through loop and none of the squares is our hopful next square
        return False # say no you can not mve there

class Pawn(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 1)
        self.piece = 'Pawn'
        self.first_move = True
    
    def find_moves(self, board):
        self.possible_moves = []
        if self.colour == 'white':
            if board[self.row - 1][self.column] == None: 
                self.possible_moves.append((self.row - 1, self.column))
                if ( board[self.row - 2][self.column] == None ) and (self.first_move == True):
                    self.possible_moves.append((self.row - 2, self.column))
            if self.column < 7:
                if board[self.row - 1][self.column + 1] != None:
                    self.possible_moves.append((self.row - 1, self.column + 1))
            if self.column > 0:
                if board[self.row - 1][self.column - 1] != None:
                    self.possible_moves.append((self.row - 1, self.column - 1))
        elif self.colour == 'black':
            if board[self.row + 1][self.column] == None: 
                self.possible_moves.append((self.row + 1, self.column))
                if ( board[self.row + 2][self.column] == None ) and (self.first_move == True):
                    self.possible_moves.append((self.row + 2, self.column))
            if self.column < 7:
                if board[self.row + 1][self.column + 1] != None :
                    self.possible_moves.append((self.row + 1, self.column + 1))
            if self.column > 0:
                if board[self.row + 1][self.column - 1] != None:
                    self.possible_moves.append((self.row + 1, self.column - 1))

class Rook(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
        self.value = 4

    def find_moves(self, board):
        self.possible_moves = []
        if self.row < 0: #up 
            for i in range(1, (self.row+1)):
                if board[self.row - i][self.column] == None :
                    self.possible_moves.append((self.row - i, self.column))
                else:
                    self.possible_moves.append((self.row - i, self.column))
                    break
        if self.row < 7: #down 
            for i in range(1, (8 - self.row)):
                if board[self.row + i][self.column] == None :
                    self.possible_moves.append((self.row + i, self.column))
                else:
                    self.possible_moves.append((self.row + i , self.column))
                    break
        if self.column < 0: #left 
            for i in range(1, (self.column+1)):
                if board[self.row][self.column - i ] == None :
                    self.possible_moves.append((self.row, self.column - i ))
                else:
                    self.possible_moves.append((self.row, self.column - i ))
                    break
        if self.column < 7: #right 
            for i in range(1, (8 - self.column)):
                if board[self.row][self.column + i ] == None :
                    self.possible_moves.append((self.row, self.column + i ))
                else:
                    self.possible_moves.append((self.row, self.column + i ))
                    break

class Bishop(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Bishop'
        self.value = 3

    def find_moves(self, board): 
        self.possible_moves = []
        pass

        
class Queen(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Queen'
        self.value = 9

    def find_moves(self, board):
        self.possible_moves = []
        Bishop_Moves = Bishop.find_moves(board)
        Rook_Moves = Rook.find_moves(board)
        self.possible_moves = Bishop_Moves + Rook_Moves

class Knight(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Knight'
        self.value = 5

    def find_moves(self, board): 
        self.possible_moves = []
        self.possible_moves.append((self.row+2, self.column-1))
        self.possible_moves.append((self.row+2, self.column+1))
        self.possible_moves.append((self.row-2, self.column-1))
        self.possible_moves.append((self.row-2, self.column+1))
        self.possible_moves.append((self.row-1, self.column+2))
        self.possible_moves.append((self.row+1, self.column+1))
        self.possible_moves.append((self.row-1, self.column-2))
        self.possible_moves.append((self.row+1, self.column-2))


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