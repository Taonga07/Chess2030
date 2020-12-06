import tkinter, Rules, File, os
from tkinter import messagebox

board = None
window = None

def set_up_window():
    window = tkinter.Tk()
    window.title('chess')
    Rules.reset_varibles()
    File.start(window)
    File.menu(window)
    window.mainloop()

def play_chess(window):
    destroy_all_widgets(window)
    Rules.reset_varibles()
    File.menu(window)
    board = reset_board()
    layout_board(window, board)

def destroy_all_widgets(window):
    for widget in window.winfo_children():
        if widget.winfo_class() != 'menubar':
            widget.destroy()


def mssg_bar(window, mssg):
    messageLabel = tkinter.Label(window, text=mssg)
    messageLabel.grid(
        row=9,
        column=3,
        columnspan=5,
        sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)


def reset_board():
    board = []
    for row in range(0, 8):
        rowlist = []
        for column in range(0,8):
            if row == 0:
                if column == 0:
                    rowlist.append(Rules.Rook('Rook', Rules.path+'Black_Rook.gif', 'black', column, row))
                elif column == 1:
                    rowlist.append(Rules.Knight('Knight', Rules.path+'Black_Knight.gif', 'black', column, row))
                elif column == 2:
                    rowlist.append(Rules.Bishop('Bishop', Rules.path+'Black_Bishop.gif', 'black', column, row))
                elif column == 3:
                    rowlist.append(Rules.Queen('Queen', Rules.path+'Black_Queen.gif', 'black', column, row))
                elif column == 4:
                    rowlist.append(Rules.King('King', Rules.path+'Black_King.gif', 'black', column, row))
                elif column == 5:
                    rowlist.append(Rules.Bishop('Bishop', Rules.path+'Black_Bishop.gif', 'black', column, row)) 
                elif column == 6:
                    rowlist.append(Rules.Knight('Knight', Rules.path+'Black_Knight.gif', 'black', column, row))
                elif column == 7:
                    rowlist.append(Rules.Rook('Rook', Rules.path+'Black_Rook.gif', 'black', column, row))
            elif row == 1:
                rowlist.append(Rules.Pawn('Pawn', Rules.path+'Black_Pawn.gif', 'black', column, row))
            elif row == 6:
                # I think this should be a 'black' piece
                rowlist.append(Rules.Pawn('Pawn', Rules.path+'White_Pawn.gif', 'white', column, row))
            elif row == 7:
                if column == 0:
                    # in your on_click() function you check to see if the piece is 'white', but below they are all 'White'
                    # python is case sensitive - make them all lower case 'white'
                    rowlist.append(Rules.Rook('Rook', Rules.path+'White_Rook.gif', 'white', column, row))
                elif column == 1:
                    rowlist.append(Rules.Knight('Knight', Rules.path+'White_Knight.gif', 'white', column, row))
                elif column == 2:
                    rowlist.append(Rules.Bishop('Bishop', Rules.path+'White_Bishop.gif', 'white', column, row))
                elif column == 3:
                    rowlist.append(Rules.Queen('Queen', Rules.path+'White_Queen.gif', 'white', column, row))
                elif column == 4:
                    rowlist.append(Rules.King('King', Rules.path+'White_King.gif', 'white', column, row))
                elif column == 5:
                    rowlist.append(Rules.Bishop('Bishop', Rules.path+'White_Bishop.gif', 'white', column, row)) 
                elif column == 6:
                    rowlist.append(Rules.Knight('Knight', Rules.path+'White_Knight.gif', 'white', column, row))
                elif column == 7:
                    rowlist.append(Rules.Rook('Rook', Rules.path+'White_Rook.gif', 'white', column, row))
            else:
                rowlist.append(None)
        board.append(rowlist)
    return board

def layout_board(window, board):
    bttnclr=Rules.light_bttnlcr
    # for simplicity, we know the board is 8x8 so lets just use that
    for column_number in range(0, 8):
        for row_number in range(0, 8):
            if board[row_number][column_number] == None:
                square = tkinter.Label(window, text = "                 \n\n\n", bg = bttnclr)
            else:
                img = tkinter.PhotoImage(file = board[row_number][column_number].icon)
                square = tkinter.Label(window, bg = bttnclr, image = img)
                square.image = img

            if bttnclr == "white":
                bttnclr = "grey"
            else:
                bttnclr = "white"

            square.grid(row = row_number, column = column_number, sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
            square.bind("<Button-1>", on_click)

        if bttnclr == "white":
            bttnclr = "grey"
        else:
            bttnclr = "white"

    mssg_turn = ''
    mssg = ''

    if Rules.turn == 0:
        mssg_turn  = 'White\'s Move'
    else:
        mssg_turn  = 'Black\'s Move'  
    
    mssg_bar(window, mssg)
    turnLabel = tkinter.Label(window, text = mssg_turn)
    turnLabel.grid(row=9, column=0 , columnspan = 2, sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
    
def on_click(event):
    square = event.widget
    Rules.onclick += 1
    row_number = int(square.grid_info()["row"])
    column_number  = int(square.grid_info()["column"])
    # lets save our row and column numbers in a tuple here, rather than in several places
    square_clicked = (row_number, column_number)
    piece_clicked = board[row_number][column_number]
    if (Rules.onclick == 1) and (piece_clicked == None):
        tkinter.messagebox.showinfo("Move Not Allowed","Your/No piece there, try again")
        mssg = 'Your/No piece there, try again'
        mssg_bar(window, mssg)
    elif ((Rules.onclick == 1 and ((Rules.turn == 0 and piece_clicked.colour == 'white') or (Rules.turn == 1 and piece_clicked.colour == 'black'))) or Rules.onclick == 2):            
        if Rules.onclick == 1: # this is our first click, we should be selecting a piece
            square.config(bg='blue')
            mssg = "Where would you like to move your " + piece_clicked.piece + " to!"
            Rules.old_colour = piece_clicked.colour
            # you're not actually saving the piece, you're saving the square that has been clicked
            Rules.square_clicked = square_clicked #row_number,column_number
            # lets use piece_clicked
            piece_clicked.find_moves(board)
            # instead of passing the square (the one we're on), we'll pass the whole window of widgets
            piece_clicked.highlight_moves(window, board)
            mssg_bar(window, mssg)
            return
        else: # this is our second click, we are selecting the square to move to
            if piece_clicked == None: # nothing at the square we're moving to
                move_piece = True
            else: # click a square with piece on
                if (isinstance(piece_clicked, Rules.GameObject) and Rules.old_colour != piece_clicked.colour): # check were not tacking the same colour piece
                    move_piece = True
                else:
                    tkinter.messagebox.showinfo("Move Not Allowed", "You can not take your own piece!")
                    mssg = "You can not take your own piece!"
                    move_piece = False
                    mssg_bar(window, mssg)

            if move_piece == True:
                # you have two check_move's : one is a variable, the second is a method for your GameObject class
                # I would rename your variable to something like valid_move
                # also piece_clicked is the object at the square we clicked on, not the piece we selected on our first click
                #check_move = Rules.GameObject.check_move(piece_clicked, board)

                # let's set the piece we are moving
                old_click = Rules.square_clicked # this was saved when we clicked a square the first time
                piece_to_move = board[old_click[0]][old_click[1]] # this was the piece we clicked on first time
                # now we can check if our move is valid
                # but we need to tell our piece_to_move, where we want it to move to, which is square_clicked
                print('square_clicked', square_clicked)
                print('piece_to_move.possible_moves', piece_to_move.possible_moves)
                valid_move = piece_to_move.check_move(square_clicked) # we also need to change some code on Rules.py
                # valid_move is now True or False, which makes our if statment easier
                #if check_move == True : #checks rules ## did not have == True on end
                if valid_move:
                    # if a pawn and was first move set firstmove to false
                    # these lines are wrong, you don't need the .piece
                    # you also had a captialisation error 'Pawn' != 'pawn'
                    #if (piece_to_move.piece == 'Pawn') and (piece_to_move.first_move == True):
                    # there's actually a better way of checking this
                    if isinstance(piece_to_move, Rules.Pawn) and piece_to_move.first_move:
                        #piece_to_move.piece.first_move = False
                        piece_to_move.first_move = False
                    #we have already set our piece to move above, so we can use that below to simplify the code below
                    #board[row_number][column_number] = board[Rules.square_clicked[0]][Rules.square_clicked[1]]#moves piece there
                    board[row_number][column_number] = piece_to_move
                    board[row_number][column_number].row = row_number
                    board[row_number][column_number].column = column_number
                    # we can also use old_click to simplify the code below
                    #board[Rules.square_clicked[0]][Rules.square_clicked[1]] = None # sets square was at to None
                    board[old_click[0]][old_click[1]] = None
                    Rules.onclick = 0  # reset our click counter 
                    #change turn
                    if Rules.turn == 0:
                        Rules.turn = 1
                    else:
                        Rules.turn = 0
                else:
                    # here is where we can set our error message
                    mssg = piece_to_move.piece + '\'s can not do that'
                    tkinter.messagebox.showinfo(mssg, mssg)
                    mssg_bar(window, mssg)
                # stop
                move_piece = False 
    
    elif (Rules.turn == 0 and piece_clicked.colour == 'black') or (Rules.turn == 1 and piece_clicked.colour == 'white'):
        tkinter.messagebox.showerror("move not allowed", "It is not your turn!")
        mssg = "It is not your turn!"
        mssg_bar(window, mssg)
    else:
        tkinter.messagebox.showerror("Error","An error has ocurred!")
        mssg = "An error has ocurred!"
        mssg_bar(window, mssg)

    Rules.onclick = 0

    layout_board(window, board) # tkinter grid to board list

if __name__ =="__main__":
    set_up_window()

# Globals #
#could be replaced with Chess.________
#______ being varible name
