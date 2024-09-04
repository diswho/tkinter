import psycopg2
# from tkinter import *

conn = psycopg2.connect(
    host="localhost",
    database="app",
    user="postgres",
    password="I536ib9E6HVxgc"
)

cursor = conn.cursor()


# cursor.execute("CREATE DATABASE tkinter") 

cursor.execute("SELECT datname FROM pg_database")
cursor.fetchall()
for db in cursor:
    print(db)

# Create the main window
# root = Tk()
# root.title("My Tkinter Application")
# # root.iconbitmap("resources/icons/home.ico")
# root.geometry("400x400")


# def create_database(cursor):
#     conn.autocommit = True
#     cursor.execute("CREATE DATABASE tkinter")    


# create_database(cursor)

conn.commit()
conn.close()

# Start the event loop
# root.mainloop()