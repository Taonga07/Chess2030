import tkinter, Rules, File, os
from tkinter import messagebox

board = None
window = None

def set_up_window():
    global window
    window = tkinter.Tk()
    window.title('chess')
    window.tk.call('wm', 'iconphoto', window._w, tkinter.PhotoImage(file=Rules.path + 'Icon.png'))
    play_chess(window)
    window.mainloop()

def play_chess(window):
    global board
    board = reset_board()
    layout_board(window, board)

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
                for piece in Rules.pieces:
                    rowlist.append(Rules.Rook(piece, Rules.path+'Black_'+piece+'.gif', 'black', column, row))
            elif row == 1:
                rowlist.append(Rules.Pawn('Pawn', Rules.path+'Black_Pawn.gif', 'black', column, row))
            elif row == 6:
                rowlist.append(Rules.Pawn('Pawn', Rules.path+'White_Pawn.gif', 'white', column, row))
            elif row == 7:
                for piece in Rules.pieces:
                    rowlist.append(Rules.Rook(piece, Rules.path+'White_'+piece+'.gif', 'white', column, row))
            else:
                rowlist.append(None)
        board.append(rowlist)
    return board

def layout_board(window, board):
    bttnclr=Rules.light_bttnlcr
    for column_number in range(0, 8):
        for row_number in range(0, 8):
            if board[row_number][column_number] == None:
                square = tkinter.Label(window, text = "                 \n\n\n", bg = bttnclr)
            else:
                img = tkinter.PhotoImage(file = board[row_number][column_number].icon)
                square = tkinter.Label(window, bg = bttnclr, image = img)
                square.image = img

            if bttnclr == Rules.light_bttnlcr:
                bttnclr = Rules.dark_bttnlcr
            else:
                bttnclr = Rules.light_bttnlcr

            square.grid(row = row_number, column = column_number, sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
            square.bind("<Button-1>", on_click)
            
        if bttnclr == Rules.light_bttnlcr:
            bttnclr = Rules.dark_bttnlcr
        else:
            bttnclr = Rules.light_bttnlcr

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
            Rules.square_clicked = square_clicked #row_number,column_number
            piece_clicked.find_moves(board)
            piece_clicked.highlight_moves(window, board)
            mssg_bar(window, mssg)
            return
        else: # this is our second click, we are selecting the square to move to
            if piece_clicked == None: # nothing at the square we're moving to
                move_piece = True
            else: # click a square with piece on
                if (isinstance(piece_clicked, Rules.GameObject) and Rules.old_colour != piece_clicked.colour):
                    move_piece = True
                else:
                    tkinter.messagebox.showinfo("Move Not Allowed", "You can not take your own piece!")
                    mssg = "You can not take your own piece!"
                    move_piece = False
                    mssg_bar(window, mssg)
            if move_piece == True:
                old_click = Rules.square_clicked
                piece_to_move = board[old_click[0]][old_click[1]]
                valid_move = piece_to_move.check_move(square_clicked)
                if valid_move:
                    if isinstance(piece_to_move, Rules.Pawn) and piece_to_move.first_move:
                        piece_to_move.first_move = False
                    board[row_number][column_number] = piece_to_move
                    board[row_number][column_number].row = row_number
                    board[row_number][column_number].column = column_number
                    board[old_click[0]][old_click[1]] = None
                    Rules.onclick = 0
                    if Rules.turn == 0:
                        Rules.turn = 1
                    else:
                        Rules.turn = 0
                else:
                    mssg = piece_to_move.piece + '\'s can not do that'
                    tkinter.messagebox.showinfo(mssg, mssg)
                    mssg_bar(window, mssg)
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
    layout_board(window, board)

if __name__ =="__main__":
    set_up_window()