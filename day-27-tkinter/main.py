from tkinter import *

def conversion():
    miles = float(input.get())
    kilo = miles * 1.60934
    result.config(text=kilo)


#configure window
window = Tk()
window.title("Miles to Kilos Converter")
window.minsize(width=300, height=300)
window.config(padx=25, pady=25)

#Labels
label1 = Label(font=("Arial", 16), text="Miles")
label1.grid(column=2, row=0)

label2 = Label(font=("Arial", 16), text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(font=("Arial", 16), text="Kilos")
label3.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)






window.mainloop()























window.mainloop()