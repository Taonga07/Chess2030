import Chess, os

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

    def check_move(self, piece_to_move, cliked):
        for i in range(len(cliked.possible_moves)):
          # go throught list of lits of possible moves
          #example posible_moves == [[5, 3], [4, 3]]
            if i == piece_to_move:
                return True
            else:
                mssg = board[Rules.square_clicked[0]][Rules.square_clicked[1]] + "'s can not do this"
                return mssg

        if cliked.first_move == True:
            cliked.first_move = False

        cliked.possible_moves.clear()

class Pawn(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 1)
        self.piece = 'Pawn'
        self.first_move = True
    
    def highlight_move(self, board):
        self.possible_moves = []
        if self.colour == 'white':
            self.possible_moves.append([self.row - 1, self.column])
            if self.first_move == True:
                self.possible_moves.append([self.row - 2, self.column])
        elif board[self.row][self.column + 1] != None:
            self.possible_moves.append([self.row, self.column + 1])
        elif board[self.row][self.column - 1] != None:
            self.possible_moves.append([self.row, self.column - 1])
        elif self.colour == 'black':
            self.possible_moves.append([self.row + 1, self.column])
            if self.first_move == True:
                self.possible_moves.append([self.row + 2, self.column])   
        
        print(self.possible_moves)
        #how would i highlight pieces from here i kow it is like:
        ## square.config('green')
        # but it dose not work
        #attacking piece colour == 'red'
        #my piece == 'blue'
        #normal alowed moves == 'green'


    def check_move(self, piece_to_move):
        for i in range(len(self.possible_moves)):
          # go throught list of lits of possible moves
          #example posible_moves == [[5, 3], [4, 3]]
            if self.item[i] == piece_to_move:
                return True
            else:
                mssg = 'Pawns can not do this!'
                return mssg

        if self.first_move == True:
            self.first_move = False

        self.possible_moves.clear()

class Rook(GameObject):
    def __init__(self, piece, icon, colour, column, row):
        super().__init__(piece, icon, colour, column, row, 4)
        self.piece = 'Rook'
        self.value = 4

    def check_move(self, new_row_number,new_column_number):
        return True

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