import tkinter

window = tkinter.Tk()

window.title("My GUI Program")
window.minsize(width=200, height=160)
#
# #Label
# new_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
# new_label["text"] = "New Text"
# new_label.config(text="New Text")
# # new_label.place(x=0,y=0)
# new_label.grid(column=0, row=0)
#
# #Button
# def button_clicked():
#     new_label.config(text=input.get())
#
#
# button = tkinter.Button(text="Click me", command=button_clicked)
# # button.pack()
# button.grid(column=1,row=1)
#
# #Entry
#
# input = tkinter.Entry(width=10)
# input.grid(column=3,row=2)
#
# button = tkinter.Button(text="New Button", command=button_clicked)
# # button.pack()
# button.grid(column=2,row=0)


#
# def add(*args):
#     total = 0
#     for n in args:
#         total = total + n
#     return total
#
# print(add(1,2,5,6,7,8,9,124))


#Label "Miles"
miles_label = tkinter.Label(text="Label", font=("Arial", 12))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

#Label "Km"
km_label = tkinter.Label(text="Label", font=("Arial", 12))
km_label.config(text="Km")
km_label.grid(column=2, row=1)

#Label "is equal to"
equal_label = tkinter.Label(text="Label", font=("Arial", 12))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)

#Label "Km value"
km_value_label = tkinter.Label(text="Label", font=("Arial", 12))
km_value_label.config(text="0")
km_value_label.grid(column=1, row=1)

#Button

def button_clicked():
    miles_value = input.get()
    km_value = float(miles_value)*1.6
    km_value_label.config(text=km_value)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)





window.mainloop()

