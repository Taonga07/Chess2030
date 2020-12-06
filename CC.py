import os

def reset_varibles():
    turn = 0
    onclick = 0
    bttnclr_turn = 0
    old_click = (0,0)
    square_clicked = (0, 0) 
    bttnclrs = 'white', 'grey'
    path = os.getcwd() + '/Chess_Resources/'
    return turn, onclick, bttnclr_turn, old_click, square_clicked, bttnclrs, path

turn, onclick, bttnclr_turn, old_click, square_clicked, bttnclrs, path = reset_varibles()