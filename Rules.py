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
        # first lets check we have some valid moves and we can figure out if we're moving a piece or taking a piece
        for i in self.possible_moves:
            row_number, column_number = i
            # .grid_slaves returns a list of widget objects in the parent widget
            # in this case we're getting the list of widgets in a particular row/column
            # there's only one thing in the list, but it's still a list, so we assign the [0] to pull out the object as square
            square = window.grid_slaves(row = row_number, column = column_number)[0]
            if board[row_number][column_number] == None:
                # this works
                #print('clear square at', i)
                square.config(bg='green')
            else:
                #print('take piece at:', i)
                square.config(bg='red')

    def check_move(self, destination_square):
        ##if self.possible_moves == []:
            ##return True
        for i in self.possible_moves:
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
    
    def find_moves(self, board):
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
                    if board[self.row - 1][self.column + 1].colour != 'white':
                        self.possible_moves.append((self.row - 1, self.column + 1))
            # and if we're on the first column, we can't check column - 1
            if self.column > 0:
                if board[self.row - 1][self.column - 1] != None:
                    if board[self.row - 1][self.column - 1].colour != 'white':
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
                if board[self.row + 1][self.column + 1] != None :
                    if board[self.row + 1][self.column + 1].colour != 'black':
                        self.possible_moves.append((self.row + 1, self.column + 1))
            # and if we're on the first column, we can't check column - 1
            if self.column > 0:
                if board[self.row + 1][self.column - 1] != None:
                    if board[self.row + 1][self.column - 1].colour != 'black':
                        self.possible_moves.append((self.row + 1, self.column - 1))
            #if board[self.row + 1][self.column] == board[7][self.column]:
                
        print('possible moves', self.possible_moves)

class Rook(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
        self.value = 4

    def find_moves(self, board):
        self.possible_moves = []
        #right 
        if self.column < 7:
            for i in range(1, (8 - self.column)):
                if board[self.row][self.column + i ] == None :
                    self.possible_moves.append((self.row, self.column + i ))
                else:
                    # need to be able to stop i loop
                    # you want to check if the first other piece you encounter is the opposite colour to this peice
                    if self.colour != board[self.row][self.column + i ].colour:
                        self.possible_moves.append((self.row, self.column + i ))
                    break
        #left
        # then make similar changes to the other three directions Rook's can move
        if self.column > 0:
            for i in range(1, self.column):
                if board[self.row][self.column - i ] == None :
                    self.possible_moves.append((self.row, self.column + i ))
                else:
                    # need to be able to stop i loop
                    if self.colour != board[self.row][self.column - i ].colour:
                        self.possible_moves.append((self.row, self.column - i ))
                    break
        #up
        if self.row > 0:
            for i in range(1, self.row + 1):
                if board[self.row - i  ][self.column] == None :
                    self.possible_moves.append((self.row - i , self.column))
                else:
                    # need to be able to stop i loop
                    if self.colour != board[self.row - i ][self.column].colour:
                        self.possible_moves.append((self.row - i , self.column))
                    break
        #down
        if self.row < 7:
            for i in range(1, 8 - self.row):
                if board[self.row + i  ][self.column] == None :
                    self.possible_moves.append((self.row + i , self.column))
                else:
                    if self.colour != board[self.row + i ][self.column].colour:
                        self.possible_moves.append((self.row + i , self.column))
                    break

class Bishop(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Bishop'
        self.value = 3

    def find_moves(self, board): 
        pass

class King(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'King'
        self.value = 1

    def find_moves(self, board): 
        self.possible_moves = []
        # remember, you need to check if you're on the edge of the board
        # otherwise, row = 8 will be a valid move on the first move
        # when it's off the board
        if self.row > 0:
            self.possible_moves.append((self.row-1, self.column))
            if self.column > 0:
                self.possible_moves.append((self.row-1, self.column-1))
            if self.column < 7:
                self.possible_moves.append((self.row-1, self.column+1))
        if self.row < 7:
            self.possible_moves.append((self.row+1, self.column))
            if self.column > 0:
                self.possible_moves.append((self.row-1, self.column+1))
            if self.column < 7:
                self.possible_moves.append((self.row+1, self.column-1))
        if (self.column < 7) and (self.column > 0):
            self.possible_moves.append((self.row, self.column+1))
            self.possible_moves.append((self.row, self.column-1))
            
        for i in self.possible_moves:
            row, column = i
            # delete line below once the code worksc q2222222
            print('row:', row, 'column', column)
            print('possible moves:', i)
            if board[row][column] != None:
                if board[row][column].colour != self.colour:
                    self.possible_moves.remove(i)

        
class Queen(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Queen'
        self.value = 9

    def find_moves(self, board): 
        pass

class Knight(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Knight'
        self.value = 5

    def find_moves(self, board): 
        self.possible_moves = []
        # knight will have same issue King has/had
        self.possible_moves.append((self.row+2, self.column-1))
        self.possible_moves.append((self.row+2, self.column+1))
        self.possible_moves.append((self.row-2, self.column-1))
        self.possible_moves.append((self.row-2, self.column+1))
        self.possible_moves.append((self.row-1, self.column+2))
        self.possible_moves.append((self.row+1, self.column+1))
        self.possible_moves.append((self.row-1, self.column-2))
        self.possible_moves.append((self.row+1, self.column-2))
        for i in self.possible_moves:
            row, column = i
            if board[row][column] != None:
                if board[row][column].colour != self.colour:
                    self.possible_moves.remove(i)

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