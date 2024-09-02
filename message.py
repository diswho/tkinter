from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')


def popup():
    response = messagebox.askyesno("This is popup", "Hi every one")
    Label(root, text=response).pack()
    if (response == 1):
        Label(root, text="Clicked Yes").pack()
    else:
        Label(root, text="Clicked No").pack()


Button(root, text="Popup", command=popup).pack()

# Start the event loop
root.mainloop()
