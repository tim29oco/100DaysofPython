from tkinter import *

def button_clicked():
    miles = float(input.get())
    kilometers = miles * 1.609
    print(kilometers)
    label_answer.config(text=f"{kilometers:.3f}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

label_miles = Label(text="Miles", font=("Times New Roman", 14, "italic"))
label_miles.grid(column=3, row=0)
label_miles.config(padx=20, pady=20)

label_km = Label(text='Km', font=("Times New Roman", 14, "italic"))
label_km.grid(column=3, row=1)
label_km.config(padx=20, pady=20)

label_answer = Label(text='#', font=("Times New Roman", 14, "italic"))
label_answer.grid(column=2, row=1, sticky='w')
label_answer.config(padx=20, pady=20)

label_equal_to = Label(text='is equal to', font=("Times New Roman", 14, "italic"))
label_equal_to.grid(column=0, row=1)

button = Button(text="Convert!", command=button_clicked)
button.grid(column=1, row=3)

input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
