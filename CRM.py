import psycopg2
# from tkinter import *

conn = psycopg2.connect(
    host="localhost",
    database="app",
    user="postgres",
    password="I536ib9E6HVxgc"
)

cursor = conn.cursor()
conn.autocommit = True

cursor.execute("CREATE DATABASE tkinter") 
conn.commit()
conn.close()

# Create the main window
# root = Tk()
# root.title("My Tkinter Application")
# # root.iconbitmap("resources/icons/home.ico")
# root.geometry("400x400")


# def create_database(cursor):
#     cursor.execute("CREATE DATABASE tkinter")    
#     print(cursor.execute("SHOW DATABASE"))


# create_database(cursor)


# Start the event loop
# root.mainloop()