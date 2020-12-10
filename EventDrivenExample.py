from tkinter import *

def leftClickButton(event):
    print("Left Click!!")

def RightClickButton(event):
    print("Right Click!!")

def DoubleClickButton(event):
    print("Double Click!!")

main = Tk()
button = Button(main,text = "My Button !!")
button.pack()
button.bind('<Button-1>',leftClickButton)
button.bind('<Button-3>',RightClickButton)
button.bind('<Double-1>',DoubleClickButton)
main.mainloop()