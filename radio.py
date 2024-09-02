from tkinter import *
from PIL import ImageTk, Image
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')

r = IntVar()
r.set(2)

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked():
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked()).pack()
# Radiobutton(root, text="Option 1", variable=r, value=2, command=lambda: clicked()).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click Here", command=lambda: clicked()).pack()
# Start the event loop
root.mainloop()
