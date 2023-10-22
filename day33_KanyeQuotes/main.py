from tkinter import *
import requests


def get_quote():
    quote_api = requests.get(url="https://api.kanye.rest")
    quote_api.raise_for_status()
    quote = quote_api.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightbackground="white")
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightbackground="white", command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
