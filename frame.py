from tkinter import *
from PIL import ImageTk, Image
# Create the main window
root = Tk()
root.title("My Tkinter Application")

frame= LabelFrame(root,text="This is my frame...",padx=15,pady=5)
frame.pack(padx=100,pady=10)

b1=Button(frame,text="Quit",command=root.quit)
b2=Button(frame,text="Click",command=root.quit)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)

root.mainloop()