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

# toolbaar

toolbar = Frame(root, bg = 'blue')
insertButt = Button(toolbar, text = 'Insert Image', command = doNothing)
insertButt.pack(side = LEFT, padx = 2, pady = 2) # padx is extra space ( pixels )

printButt = Button(toolbar, text = 'print', command = doNothing)
printButt.pack(side = LEFT, padx = 2, pady = 3)

toolbar.pack(side = TOP, fill = X)

root.mainloop()
