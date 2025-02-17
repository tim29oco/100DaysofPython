from tkinter import *
import random
import json
from tkinter import messagebox
import pyperclip

# --------------------------- Load Password ------------------------------------- #
def get_data():
    website_search_key = website_entry.get().title()  # Ensure it's in title case
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found.")
    else:
        if website_search_key in data:
            # Get the associated values
            email_value = data[website_search_key]["email"]
            password_value = data[website_search_key]["password"]
            messagebox.showinfo(title=f"{website_search_key} Data Found!", message=f"Email: {email_value}\nPassword: {password_value}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_search_key} found.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    passwordlist = []

    nr_letters = random.randint(3,8)
    nr_symbols = random.randint(3,8)
    nr_numbers = random.randint(3,8)

    for _ in range(nr_letters):
      passwordlist.append(random.choice(letters))

    for _ in range(nr_numbers):
        passwordlist.append(random.choice(numbers))

    for _ in range(nr_symbols):
      passwordlist.append(random.choice(symbols))

    random.shuffle(passwordlist)

    rand_password = ''.join(passwordlist)
    password_entry.delete(0, END)
    password_entry.insert(END, rand_password)
    pyperclip.copy(rand_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_data = website_entry.get().title()
    email_data = email_username_entry.get()
    password_data = password_entry.get()
    new_data = {website_data: {"email":email_data, "password":password_data}}

    if len(password_data) == 0 or len(website_data) == 0:
        messagebox.showerror(title="Error", message="Please do not leave fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # --- Read old data --- #
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # --- Updating old data --- #
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            messagebox.showinfo(title="Success", message=f"Added {website_data} to the data store.")
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# --- Window Creation --- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)

# --- Picture Creation --- #
canvas = Canvas(width=200, height=200)
myPassLogo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image = myPassLogo)
canvas.grid(column=1, row=0)

# --- Labels --- #
website = Label(text='Website:')
website.grid(column=0, row = 1, sticky = 'E')
email_username = Label(text='Email/Username:')
email_username.grid(column=0, row = 2, sticky = 'E')
password = Label(text='Password:')
password.grid(column=0, row = 3, sticky = 'E')

# --- Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan= 2, sticky = 'W')
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan= 2, sticky = 'W')
email_username_entry.insert(END,"timothy@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1, sticky = 'W', padx=0)


# --- Buttons --- #
generate = Button(text="Generate Password", command=generatepassword)
generate.grid(column=2, row=3, sticky = 'W')
add = Button(text="Add", width=36, padx=0, command=save)
add.grid(row=4, column=1, columnspan=2, sticky = 'W')
search = Button(text="Search", command=get_data)
search.grid(column=2, row=1)

# ----- Last Line of Code ----- #
window.mainloop()
