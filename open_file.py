from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')


def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir="resources\images", title="Select A File", filetypes=(("jpeg file", "*.jpeg"), ("png file", "*.png"), ("all file", "*.*")))
    label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename).resize([200, 200]))
    Label(root, image=img).pack()


btn = Button(root, text="Click", command=open).pack()
btn_quit = Button(root, text="Exit", command=root.quit).pack()
# Start the event loop
root.mainloop()
