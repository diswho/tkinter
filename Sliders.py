from tkinter import *
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizotal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizotal.pack(anchor=W)


def click():
    # global lbl
    # lbl.pa
    lbl = Label(root, text=horizotal.get()).pack()


btn = Button(root, text="click", command=click).pack()
# Start the event loop
root.mainloop()
