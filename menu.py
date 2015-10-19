from tkinter import *

def doNothing():
    print('ok ok I will not...')
        
root = Tk()

menu_one = Menu(root)
root.config(menu = menu_one)

subMenu = Menu(menu_one)
menu_one.add_cascade(label = 'File', menu = subMenu)
subMenu.add_command(label = 'Now Project...', command = doNothing)

subMenu.add_separator()

subMenu.add_command(label = 'Exit', command = doNothing)

root.mainloop()
