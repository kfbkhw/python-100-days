from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pwd():
    pwd_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pwd():

    website = website_entry.get().title()
    email = id_entry.get()
    pwd = pwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    if len(pwd) < 1 or len(website) < 1:
        messagebox.showinfo(title="Warning", message="Invalid password or website")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pwd_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    site = website_entry.get().title()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            site_data = data[site]
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Warning", message="No details for the website exists")
    else:
        email = site_data["email"]
        pwd = site_data["password"]
        messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {pwd}")
    finally:
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=2, row=1)

# Label
website_label = Label(text="Website: ")
website_label.config(padx=5, pady=5)
website_label.grid(column=1, row=2)

id_label = Label(text="Email/Username: ")
id_label.config(padx=5, pady=5)
id_label.grid(column=1, row=3)

pwd_label = Label(text="Password: ")
pwd_label.config(padx=5, pady=5)
pwd_label.grid(column=1, row=4)

# Entry
website_entry = Entry(width=20)
website_entry.grid(column=2, row=2)
website_entry.focus()

id_entry = Entry(width=38)
id_entry.grid(column=2, row=3, columnspan=2)
id_entry.insert(0, "username@gmail.com")

pwd_entry = Entry(width=20)
pwd_entry.grid(column=2, row=4)

# Button
website_button = Button(text="Search", command=find_password)
website_button.config(padx=30, pady=2)
website_button.grid(column=3, row=2)

pwd_button = Button(text="Generate Password", command=generate_pwd)
pwd_button.config(padx=2, pady=2)
pwd_button.grid(column=3, row=4)

add_button = Button(text="Add", width=34, command=save_pwd)
add_button.config(padx=5, pady=5)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
