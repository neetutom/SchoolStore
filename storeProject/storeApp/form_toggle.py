from tkinter import *

root = Tk()

Frame(root).pack()

label = Label(root, text="Hello Neetu", fg='blue')
label.pack()
button = Button(root, text='OK', fg='red')
button.pack()
root.mainloop()