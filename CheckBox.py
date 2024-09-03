from tkinter import *
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')
root.geometry("400x400")

var = StringVar()


def show():
    myLabel = Label(root, text=var.get()).pack()


cb = Checkbutton(root, text="check this box", variable=var, command=show, onvalue="On", offvalue="Off")
cb.deselect()
cb.pack()


# Start the event loop
root.mainloop()
