from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button_one = Button(topFrame, text='click here', fg='blue')
button_two = Button(topFrame, text='click here', fg='red')
button_three = Button(bottomFrame, text='click here', fg='pink')



button_one.pack(side=LEFT)
button_two.pack(side=RIGHT)
button_three.pack(side=BOTTOM)

root.mainloop()
