from tkinter import *


def calculate():
    miles_entry = float(miles_input.get())
    converted = round(miles_entry * 1.609, 2)
    answer.config(text=f"{converted}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

text_label = Label(text="is equal to: ", font=("Constantia", 16))
text_label.grid(row=1, column=0)

miles_input = Entry(width=20)
miles_input.grid(row=0, column=1)

calculate = Button(text="calculate", font="Constantia, 16", command=calculate)
calculate.grid(row=2, column=1)

miles = Label(text="Miles", font=("Constantia", 16))
miles.grid(row=0, column=2)

kilo = Label(text="Kilometers", font="Constantia, 16")
kilo.grid(row=1, column=2)

answer = Label(text="0", font="Constantia, 16")
answer.grid(row=1, column=1)

window.mainloop()
