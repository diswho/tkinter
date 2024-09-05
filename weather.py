import json
from tkinter import *
import sqlite3

import requests
# Create the main window
root = Tk()
root.title("My Tkinter Application")
root.iconbitmap('resources/icons/home.ico')
# root.geometry("400x400")

url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=17.9667&longitude=102.6&current=european_aqi&timezone=Asia%2FBangkok"

try:
    # api_request = requests.get(url)
    payload = {}
    headers = {}
    api_request = requests.request("GET", url, headers=headers, data=payload)
    api = json.loads(api_request.content)
    print(api)
except Exception as error:
    print(error)
    api = "Error..."

label = Label(root, text="Air Quality " + str(api['current']['european_aqi'])).pack()
# Start the event loop
root.mainloop()
