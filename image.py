from tkinter import *
from PIL import ImageTk, Image
# Create the main window
root = Tk()
root.title("My Tkinter Application")
# root.iconbitmap('resources/icons/home.ico')
img = Image.open("resources/images/01.jpeg").resize((300, 300), Image.Resampling.LANCZOS)
my_image1 = ImageTk.PhotoImage(img)
img = Image.open("resources/images/02.jpeg").resize((300, 300), Image.Resampling.LANCZOS)
my_image2 = ImageTk.PhotoImage(img)
img = Image.open("resources/images/03.jpeg").resize((300, 300), Image.Resampling.LANCZOS)
my_image3 = ImageTk.PhotoImage(img)
img = Image.open("resources/images/04.jpeg").resize((300, 300), Image.Resampling.LANCZOS)
my_image4 = ImageTk.PhotoImage(img)

image_list = [my_image1, my_image2, my_image3, my_image4]
length = len(image_list)
image_number = 1


my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=lambda: back(image_number), state=DISABLED)
button_exit = Button(root, text="exit program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

status = Label(root, text="Image 1 of "+str(length), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number >= length:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image "+str(image_number)+" of "+str(length), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image "+str(image_number)+" of "+str(length), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Start the event loop
root.mainloop()
