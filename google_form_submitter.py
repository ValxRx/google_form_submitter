import time
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Frame, Label, Button, Entry
from tkinter.font import BOLD

def submit_form():
    t1 = time.time()
    # Get Google form URL from user
    url = entry.get() 
    BASE_URL = "https://docs.google.com/forms/d/e/" + url.split("/")[6] + "/"
    
    # Request the page
    r = requests.get(BASE_URL + "viewform")
    entries_numbers = []
    
    # Here is the data to be sent (Form answers)
    # The choice for radio button has to the EXACT text of the choice
    # For example, the choices include "python", you should put "python" :)
    entries_data = ["test", "123", "456", "choice"]
    
    soup = BeautifulSoup(r.text, "html.parser").body
    
    for element in soup.find_all():
        if element.has_attr("data-params"):
            entries_numbers.append(element["data-params"].split("[")[3].replace(",",""))
    
    # This could be dynamic but i'm lazy...
    URL = BASE_URL + f"formResponse?entry.{entries_numbers[0]}={entries_data[0]}&entry.{entries_numbers[1]}={entries_data[1]}&entry.{entries_numbers[2]}={entries_data[1]}&entry.{entries_numbers[3]}={entries_data[3]}&submit=Submit"
    r = requests.get(URL)
    t2 = time.time()
    
    exec_label.config(text=f"Time taken to submit: {round(t2-t1,5)} s")


root = Tk()
root.geometry("550x350")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

label = Label(frame, text="Form Submitter",font=("Century Gothic", 30, BOLD))
label.pack()

exec_label = Label(frame,text="Make sure your keyboard is english",font=("Cambria Math", 17, BOLD))
exec_label.pack()

prompt_label = Label(frame, text="Please Enter a Google Form link",font=("Century Gothic", 12, BOLD))
prompt_label.pack()

entry = Entry(frame, width=70)
entry.pack()

button = Button(frame, text="Submit",font=("Century Gothic", 15, BOLD), padx=10, pady=10, bd=3, command=submit_form)
button.pack(pady=30)

root.mainloop()