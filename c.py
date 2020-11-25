import tkinter, Rules, File, os
from tkinter import messagebox

def set_up_window():
    global window
    window = tkinter.Tk()
    window.title('chess')
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
                rowlist.append(Rules.Pawn('Pawn', Rules.path+'White_Pawn.gif', 'white', column, row))
            elif row == 7:
                if column == 0:
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

def on_click(event):
    Rules.onclick += 1
    square = event.widget
    row_number = int(square.grid_info()["row"])
    column_number  = int(square.grid_info()["column"])
    square_clicked = (row_number, column_number)
    if Rules.onclick == 1: # this is our fist click we are selecting the piece we want to move
        if board[row_number][column_number] == None: # if there is no piece where we clicked
            tkinter.messagebox.showinfo("Move Not Allowed","No piece there, try again")
        else: # if there is a pice where we clicked
            square.config(bg='blue') # set clicked square background to blue
            Rules.square_clicked = square_clicked #row_number,column_number
    else: # this is our second click, we are selecting the square to move to
        old_click = Rules.square_clicked # this was saved when we clicked a square the first time
        piece_to_move = board[old_click[0]][old_click[1]]
        if piece_to_move.colour != board[row_number][column_number].colour: # if we not are taking our own piece
            valid_move = piece_to_move.check_move(square_clicked)
            if valid_move:
                board[row_number][column_number] = piece_to_move
                board[row_number][column_number].row = row_number # move piece to new row
                board[row_number][column_number].column = column_number # move piece to new column
                board[old_click[0]][old_click[1]] = None # set old square to blank
            else:
                tkinter.messagebox.showinfo("Move Not Allowed", valid_move)
        else:
            tkinter.messagebox.showinfo("Move Not Allowed","You can not take your own piece")
        layout_board(window, board) #reset board
        Rules.onclick = 0 #seond click we want to alternate bettwen click 1 and 2

if __name__ =="__main__":
    play_chess()