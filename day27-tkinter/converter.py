from tkinter import *
FONT = ("Arial", 24, "normal")


def button_clicked():
    km_value = round(float(miles_input.get())*1.609, 2)
    output_label.config(text=km_value)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=30)

miles_input = Entry(width=15)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.config(padx=20, pady=20)
miles_label.grid(column=3, row=1)

text_label = Label(text="is equal to", font=FONT)
text_label.config(padx=20, pady=20)
text_label.grid(column=1, row=2)

output_label = Label(text="", font=FONT)
output_label.config(padx=20, pady=20)
output_label.grid(column=2, row=2)

km_label = Label(text="Km", font=FONT)
km_label.config(padx=20, pady=20)
km_label.grid(column=3, row=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
