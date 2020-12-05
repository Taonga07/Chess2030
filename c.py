import tkinter, CC, CP, File, os
from tkinter import messagebox

def set_up_window():
    global window
    window = tkinter.Tk()
    window.title('chess')
    window.tk.call('wm', 'iconphoto', window._w, tkinter.PhotoImage(file=CC.path + 'Icon.png'))
    return window

def play_chess():
    global board
    board = reset_board()
    window = set_up_window()
    layout_board(window, board)
    window.mainloop()

def reset_board():
    board = []
    for row in range(0, 8):
        rowlist = []
        for column in range(0,8):
            if row == 0:
                for piece in CC.pieces:
                    rowlist.append(CP.Rook(piece, CC.path+'Black_'+piece+'.gif', 'black', column, row))
            elif row == 1:
                rowlist.append(CP.Pawn('Pawn', CC.path+'Black_Pawn.gif', 'black', column, row))
            elif row == 6:
                rowlist.append(CP.Pawn('Pawn', CC.path+'White_Pawn.gif', 'white', column, row))
            elif row == 7:
                for piece in CC.pieces:
                    rowlist.append(CP.Rook(piece, CC.path+'White_'+piece+'.gif', 'white', column, row))
            else:
                rowlist.append(None)
        board.append(rowlist)
    return board

def layout_board(window, board):
    for column_number in range(0, 8):
        for row_number in range(0, 8):
            if board[row_number][column_number] == None:
                square = tkinter.Label(window, text = "                 \n\n\n", bg = CC.bttnclrs[CC.bttnclr_turn])
            else:
                img = tkinter.PhotoImage(file = board[row_number][column_number].icon)
                square = tkinter.Label(window, bg = CC.bttnclrs[CC.bttnclr_turn], image = img)
                square.image = img
            square.grid(row = row_number, column = column_number, sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
            square.bind("<Button-1>", on_click)
            CC.bttnclr_turn = 1-CC.bttnclr_turn
        CC.bttnclr_turn = 1-CC.bttnclr_turn

def on_click(event):
    CC.onclick += 1
    square = event.widget
    row_number = int(square.grid_info()["row"])
    column_number  = int(square.grid_info()["column"])
    square_clicked = (row_number, column_number)
    piece_clicked = board[square_clicked[0]][square_clicked[1]]
    if CC.onclick == 1: # this is our fist click we are selecting the piece we want to move
        if (board[row_number][column_number] == None): # if there is no piece where we clicked
            tkinter.messagebox.showinfo("Move Not Allowed","No piece there, try again")
        else: # if there is a pice where we clicked
            square.config(bg='blue') # set clicked square background to blue
            CC.square_clicked = square_clicked #row_number,column_number
            piece_clicked.find_moves(board)
            piece_clicked.highlight_moves(window, board)
    else: # this is our second click, we are selecting the square to move to
        if board[row_number][column_number] != None:
            if piece_clicked.colour == board[row_number][column_number].colour: # if we are taking our own piece
                tkinter.messagebox.showinfo("Move Not Allowed","You can not take your own piece")
                CC.onclick = 0
                return
            valid_move = piece_clicked.check_move(square_clicked)
            if not valid_move:
                tkinter.messagebox.showinfo("Move Not Allowed", "Move Not Allowed")
                layout_board(window, board) #reset board
                CC.onclick = 0 #seond click we want to alternate bettwen click 1 and 2
                return
        board[row_number][column_number].row = row_number # move piece to new row
        board[row_number][column_number].column = column_number # move piece to new column
        board[square_clicked[0]][square_clicked[1]] = None # set old square to blank
        layout_board(window, board) #reset board
        CC.turn = 1 - CC.turn
        CC.onclick = 0

if __name__ =="__main__":
    play_chess()