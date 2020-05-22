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

    # we don't need to pass the piece_to_move as each sub-class will inherit this method
    # we also don't need to pass the board, as we're not referencing it here, but
    # we do need to tell it where it's trying to move to
    #def check_move(self, piece_to_move, board):
    def check_move(self, destination_square):
        # because all our sub-classes will inherity this method, we don't need to set cliked
        #cliked = board[Rules.square_clicked[0]][Rules.square_clicked[1]]
        # we can call our self.variables / functions
        #for i in range(len(cliked.possible_moves)):
        # and you're not iterating through a loop a number of times, you want to check against each in the list
        for i in self.possible_moves:
        # go throught list of lits of possible moves
        # example posible_moves == [[5, 3], [4, 3]]
            # you haven't passed in anything for piece_to_move (and i think you mean destination_square)
            #if i == piece_to_move:
            if i == destination_square:
                return True
            #else: # this else will activate if the first possible_move is not the destination_square, and return False
                #mssg = board[Rules.square_clicked[0]][Rules.square_clicked[1]] + "'s can not do this"
                # it's very confusing to have function that returns True, False, or a string
                # to keep it simple, just return True or False
                #return mssg
                return False
        # you want to return False if none of the possible_moves == destination_square
        return False
        # this is only for Pawns, so shouldn't be here
        # also it will never be run as you return False before it
        if cliked.first_move == True:
            cliked.first_move = False
        # you don't need to clear the possible_moves, they may click on another square that is valid
        #cliked.possible_moves.clear()

class Pawn(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 1)
        self.piece = 'Pawn'
        self.first_move = True
    
    def highlight_move(self, board):
        self.possible_moves = []
        print('my square', self.row, self.column)
        if self.colour == 'white':
            # this is a bit technical but you want to save tuples (row, column), not lists [row, column]
            #self.possible_moves.append([self.row - 1, self.column])
            self.possible_moves.append((self.row - 1, self.column))
            if self.first_move == True:
                self.possible_moves.append((self.row - 2, self.column))
        # I'm not quite sure your logic here is quite right - are you trying to code the 'take a piece' option?
        # I don't think it's quite working as intended
        elif board[self.row][self.column + 1] != None:
            self.possible_moves.append((self.row, self.column + 1))
        elif board[self.row][self.column - 1] != None:
            self.possible_moves.append((self.row, self.column - 1))
        # for some reason, this isn't producing a correct list
        # seems to be adding 1 to the column, and not recognising that it's a first move
        # # more digging needed
        elif self.colour == 'black':
            self.possible_moves.append((self.row + 1, self.column))
            if self.first_move == True:
                self.possible_moves.append((self.row + 2, self.column))   
        
        print('possible moves', self.possible_moves)
        #how would i highlight pieces from here i kow it is like:
        ## square.config('green')
        # but it dose not work
        #attacking piece colour == 'red'
        #my piece == 'blue'
        #normal alowed moves == 'green'

# you have a check_move in your GameObject class, use that
#    def check_move(self, piece_to_move):
#        for i in range(len(self.possible_moves)):
#          # go throught list of lits of possible moves
#          #example posible_moves == [[5, 3], [4, 3]]
#            if self.item[i] == piece_to_move:
#                return True
#            else:
#                mssg = 'Pawns can not do this!'
#                return mssg
#
#        if self.first_move == True:
#            self.first_move = False
#
#        self.possible_moves.clear()

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