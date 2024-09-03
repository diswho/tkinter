from tkinter import *
from PIL import ImageTk, Image
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')


def open():
    global img
    top = Toplevel()
    top.title("My Second windows")
    top.iconbitmap('resources/icons/home.ico')
    img = ImageTk.PhotoImage(Image.open("resources/images/01.jpeg").resize([200, 200]))
    lbl = Label(top, image=img).pack()
    btn = Button(top, text="Close windows", command=top.destroy).pack()


btn = Button(root, text="Open", command=open).pack()

# Start the event loop
root.mainloop()
