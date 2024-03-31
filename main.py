
from tkinter import messagebox
import random
# from random import choice, randint,shuffle   # if this line used, remove random from the codes below
import pyperclip       # Pyperclip provides a cross-platform Python module for copying and pasting text to the clipboard.
import json
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get().upper()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message='please fill in all the blamks')
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------------------------Search---------------------------------------- #
def find_password():
    website = entry_web.get().upper()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{website}:\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="info", message=(f"No {website} exists"))




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='resized_logre.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_web = Label(text='Website:')
label_web.grid(column=0, row=1)
label_email = Label(text='Email/Username:')
label_email.grid(column=0, row=2)
label_password = Label(text='Password:')
label_password.grid(column=0, row=3)

entry_web = Entry(width=21)
entry_web.grid(column=1, row=1)
entry_web.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, columnspan=2, row=2)
entry_email.insert(0, 'mail@gmail.com')

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

bn_password = Button(text='Generate Password', command=password)
bn_password.grid(column=2, row=3)

bn_add = Button(text='Add', width=36, command=save)
bn_add.grid(column=1, columnspan=2, row=4)

bn_search = Button(text='Search', width=13, command=find_password)
bn_search.grid(column=2, row=1)

window.mainloop()
