from tkinter import filedialog
#from tkinter.colorchooser import askcolor
import tkinter, Chess, os

def onOpen(window, board):
    Open = filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("main files","*txt*"),("All files","*.*")))
    f = open(Open,"r")
    Chess.board = f.read()
    Chess.create_board(window, board)

def onSave(board):
    Save = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("main files","*txt*"),("All files","*.*")))
    file = open(Save,"w+")
    file.write(board)
    file.close() 

def openGuide():
    try:
        os.system("gedit Guide.txt")
    except:
        try:
            os.system("notepad Guide.txt")
        except:
            print("Neither gedit nor notepad could be used to open the file.")

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