from tkinter import filedialog, messagebox
#from tkinter.colorchooser import askcolor
import tkinter, Chess, os

def menu(window):
    menubar = tkinter.Menu(window)

    filemenu = tkinter.Menu(menubar, tearoff=0)
    editmenu = tkinter.Menu(menubar, tearoff=0)
    viewmenu = tkinter.Menu(menubar, tearoff=0)
    toolmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu = tkinter.Menu(menubar, tearoff=0)

    filemenu.add_command(label="New", command=lambda: Chess.play_chess(window))
    filemenu.add_command(
        label="Open", command=lambda: onOpen(window, Chess.board))
    filemenu.add_command(label="Save", command=lambda: onSave(Chess.board))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=lambda: window.destroy())

    editmenu.add_command(
        label="custormise pieces", command=lambda: openGuide())
    editmenu.add_command(
        label="custormise board", command=lambda: openGuide())
    editmenu.add_checkbutton(
        label='Blindfold Chess', command=lambda: openGuide())

    viewmenu.add_checkbutton(label='points', command=lambda: openGuide())
    viewmenu.add_checkbutton(
        label='pieces taken', command=lambda: openGuide())
    viewmenu.add_checkbutton(
        label='computer evaluation', command=lambda: openGuide())
    viewmenu.add_command(
        label="game history", command=lambda: openGuide())

    toolmenu.add_command(label="takeback", command=lambda: openGuide())
    toolmenu.add_command(label="flip board", command=lambda: openGuide())
    toolmenu.add_command(
        label="Request stalemate", command=lambda: openGuide())
    toolmenu.add_command(label="Resighn", command=lambda: openGuide())
    toolmenu.add_command(label="hint", command=lambda: openGuide())

    helpmenu.add_command(label="Open Guide", command=lambda: openGuide())

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="View", menu=viewmenu)
    menubar.add_cascade(label="Tools", menu=toolmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)

def onOpen(window, board):
    try:
        Open = filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("main files","*txt*"),("All files","*.*")))
        f = open(Open,"r")
        Chess.board = f.read()
        Chess.layout_board(window, board)
    except:
        tkinter.messagebox.showerror("Error","This is not possible!")

def onSave(board):
    try:
        Save = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("main files","*txt*"),("All files","*.*")))
        file = open(Save,"w+")
        write(board)
        close()
    except:
        tkinter.messagebox.showerror("Error","This is not possible!")


def openGuide():
    try:
        os.system("gedit Guide.txt")
    except:
        try:
            os.system("notepad Guide.txt")
        except:
            print("Neither gedit nor notepad could be used to open the ")

#def Set_BoardColor():
#    win = Window(Tk())
#    win.mainloop()
#    def __init__(self, master=None, cnf={}, **kw):
#            super().__init__(master, cnf, **kw)
#            self.open = Button(self, text='Pick a color', command=self.pick_a_color)
#            self.exit = Button(self, text='Exit', command=self.quit)
#    
#            for b in (self.open, self.exit):
#                b.pack(side=LEFT, expand=YES, fill=BOTH)
#            self.pack()
#    
#        def pick_a_color(self):
#            print(askcolor(parent=self, title='Pick a color'))
