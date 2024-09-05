from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')
# root.geometry("400x400")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 250)
    plt.show()


btn = Button(root, text="Click", command=graph).pack()
# lbl = Label(root, image=graph())

# Start the event loop
root.mainloop()
