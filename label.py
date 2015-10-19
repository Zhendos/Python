from tkinter import *

root = Tk()

label_name = Label(root, text='Name')
label_pass = Label(root, text='Password')

entry_one = Entry(root)
entry_two = Entry(root)

label_name.grid(row = 0, column = 0) #North, East, South, West
label_pass.grid(row = 1, column = 0) # North, East, South, West

entry_one.grid(row = 0, column = 1)
entry_two.grid(row = 1, column = 1)

c = Checkbutton(root, text='keep me logged in')
c.grid(columnspan = 2)


root.mainloop()
