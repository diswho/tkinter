from tkinter import *
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')
root.geometry("400x400")

options = ["Mon", "Tue", "Wed", "Thu", "Fri", "Set", "Sun"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options).pack()


def show():
    Label(root, text=clicked.get()).pack()


btn = Button(root, text="Show", command=show).pack()


# Start the event loop
root.mainloop()
