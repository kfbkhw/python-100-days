from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=30)


# Label
my_label = Label(text="This is a Label", font=("Arial", 24, "normal"))
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=20, pady=20)
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
# my_label.pack()


# Button


def button_clicked():
    print("clicked")
    my_label.config(text=entry_input.get())


button = Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry

entry_input = Entry(width=20)
entry_input.grid(column=3, row=2)


window.mainloop()
