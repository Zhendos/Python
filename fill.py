from tkinter import *

root = Tk()

one = Label(root, text='One', bg='red', fg='white')
one.pack(fill=X)
two = Label(root, text='Green', bg='green', fg='black')
two.pack(side=LEFT, fill=Y)
root.mainloop()
