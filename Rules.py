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
            square = window.grid_slaves(row = row_number, column = column_number)[0] #returns list of widgets
            if board[row_number][column_number] == None: #if there is nothing at position i
                square.config(bg='green') # highlight position i green
            else: # none has no attrubrite to clour this stops this error 
                if board[row_number][column_number].colour != self.colour:
                    square.config(bg='red') # highlight position i red

    def check_move(self, destination_square):
        for i in self.possible_moves: # goes through each possple move possition
            if i == destination_square: # if where we are moving to is an postion in possible moves
                return True # say yes you can move
        #if we go through loop and none of the squares is our hopful next square
        return False # say no you can not mve there

    def find_validSquare(self, working_value):
        # check if working row and column is in the board
        x,y = working_value
        if x >=0 and x <= 7 and y >= 0 and y <=7:
            return True
        return False
    def explore_moves(self, direction, board):
        # find posissible moves acording to what has been passed into it
        # find posissible moves acording to what has been passed into it
        ##example 1
        ## we ge direction= 1, 1
        ## bishop curren sqare is 7,4
        # we get an empty list 
        ##example 2
        ## we ge direction= 1, 1
        ## bishop curren sqare is 3,4
        # we get an list with the values (4,5), (5,6), (6,7)
        working_value = self.row, self.column
        moves = []
        while True:
            ##find_validSquare(working_value) and working_value != None:
            working_value = ((working_value[0] + direction[0]), (working_value[1] + direction[1])) 
            if self.find_validSquare(working_value) == True:
                if board[working_value[0]][working_value[1]] == None:
                    moves.append(working_value)
                else:
                    moves.append(working_value)
                    break
            else:
                break
        return moves

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
        self.possible_moves.extend(self.explore_moves((-1, 0), board))# up
        self.possible_moves.extend(self.explore_moves((0, +1), board))# right
        self.possible_moves.extend(self.explore_moves((0, -1), board))# left
        self.possible_moves.extend(self.explore_moves((+1, 0), board))# down

class Bishop(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Bishop'
        self.value = 3

    def find_moves(self, board): 
        self.possible_moves = []
        self.possible_moves.extend(self.explore_moves((-1, -1), board))# up left
        self.possible_moves.extend(self.explore_moves((-1, +1), board))# up right
        self.possible_moves.extend(self.explore_moves((+1, -1), board))# down left
        self.possible_moves.extend(self.explore_moves((+1, +1), board))# down right

class King(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'King'
        self.value = 1

    def find_moves(self, board): 
        self.possible_moves = []
        if self.row > 0:
            self.possible_moves.append((self.row-1, self.column))
            if self.column > 0:
                self.possible_moves.append((self.row-1, self.column-1))
            if self.column < 7:
                self.possible_moves.append((self.row-1, self.column+1))
        if self.row < 7:
            self.possible_moves.append((self.row+1, self.column))
            if self.column > 0:
                self.possible_moves.append((self.row+1, self.column-1))
            if self.column < 7:
                self.possible_moves.append((self.row+1, self.column+1))
        if self.column < 7: 
            self.possible_moves.append((self.row, self.column+1))
        if self.column > 0:
            self.possible_moves.append((self.row, self.column-1))
            

        
class Queen(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Queen'
        self.value = 9

    def find_moves(self, board):
        self.possible_moves = []
        ##BISHOP MOVES
        self.possible_moves.extend(self.explore_moves((-1, -1), board))# up left
        self.possible_moves.extend(self.explore_moves((-1, +1), board))# up right
        self.possible_moves.extend(self.explore_moves((+1, -1), board))# down left
        self.possible_moves.extend(self.explore_moves((+1, +1), board))# down right
        #ROOK MOVES
        self.possible_moves.extend(self.explore_moves((-1, 0), board))# up
        self.possible_moves.extend(self.explore_moves((0, +1), board))# right
        self.possible_moves.extend(self.explore_moves((0, -1), board))# left
        self.possible_moves.extend(self.explore_moves((+1, 0), board))# down

class Knight(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Knight'
        self.value = 5

    def find_moves(self, board): 
        self.possible_moves = []
        if self.row < 6 and self.column > 0:
            self.possible_moves.append((self.row+2, self.column-1))
        if self.row < 6 and self.column < 7:
            self.possible_moves.append((self.row+2, self.column+1))
        if self.row > 1 and self.column > 0:
            self.possible_moves.append((self.row-2, self.column-1))
        if self.row > 1 and self.column < 7:
            self.possible_moves.append((self.row-2, self.column+1))
        if self.row > 0 and self.column < 6:
            self.possible_moves.append((self.row-1, self.column+2))
        if self.row < 7 and self.column < 6:
            self.possible_moves.append((self.row+1, self.column+2))
        if self.row > 0 and self.column > 1:
            self.possible_moves.append((self.row-1, self.column-2))
        if self.row < 7 and self.column > 1:
            self.possible_moves.append((self.row+1, self.column-2))


    path = os.getcwd() + '/Chess_Resources/'
    icons = ['White_Rook.gif', 'White_Bishop.gif', 'White_Knight.gif', 'White_Queen.gif', 'White_King.gif', 'White_Knight.gif', 'White_Bishop.gif', 'White_Rook.gif', 'Black_Rook.gif', 'Black_Bishop.gif', 'Black_Knight.gif', 'Black_King.gif', 'Black_Queen.gif', 'Black_Knight.gif', 'Black_Bishop.gif', 'Black_Rook.gif'] #/media/barton_hill/THOMAS/ Digi@Local/MyCode/Python/4 - Green/Code/Chess_Resources/ gameOver = False
    pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Kight', 'Rook']

    light_bttnlcr ='white'
    dark_bttnlcr = 'black'

    turn = 0
    onclick = 0
    square_clicked = (0, 0) 
    old_colour = 'white'

# our varibles/lists
def reset_varibles():
    path = os.getcwd() + '/Chess_Resources/'
    icons = ['White_Rook.gif', 'White_Bishop.gif', 'White_Knight.gif', 'White_Queen.gif', 'White_King.gif', 'White_Knight.gif', 'White_Bishop.gif', 'White_Rook.gif', 'Black_Rook.gif', 'Black_Bishop.gif', 'Black_Knight.gif', 'Black_King.gif', 'Black_Queen.gif', 'Black_Knight.gif', 'Black_Bishop.gif', 'Black_Rook.gif'] #/media/barton_hill/THOMAS/ Digi@Local/MyCode/Python/4 - Green/Code/Chess_Resources/ gameOver = False
    pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Kight', 'Rook']

    light_bttnlcr ='white'
    dark_bttnlcr = 'black'

    turn = 0
    onclick = 0
    square_clicked = (0, 0) 
    old_colour = 'white'