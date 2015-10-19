from tkinter import *

class myButtons:
    
    def __init__(self, master):
        print('[BOT] init method called')
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = 'print message', command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = 'QUIT', command = frame.quit)
        self.quitButton.pack(side = RIGHT)

    def printMessage(self):
        print('[DEF] print test')
        
root = Tk()
b = myButtons(root)
root.mainloop()
