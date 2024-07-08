from tkinter import *
import mysql.connector
from tkinter.messagebox import showerror, showinfo

# Establish MySQL connection
db = mysql.connector.connect(host="localhost", user="root", passwd="root123", database="test123")
mycur = db.cursor()

win = Tk()
win.title("Ticket Generation")
win.geometry("800x600")

def getdata():
    booking_id = e1.get()
    slt = f"SELECT * FROM passenger_data WHERE booking_id = '{booking_id}'"
    mycur.execute(slt)
    data = mycur.fetchone()

    # Display data in Tkinter labels and entry widgets
    if data:
        label2.config(text=f"Name: {data[0]}")  # Assuming the first column is 'name'
        e2.delete(0, END)
        e2.insert(0, data[0])

        label3.config(text=f"Age: {data[1]}")  # Assuming the second column is 'age'
        e3.delete(0, END)
        e3.insert(0, data[1])

        label5.config(text=f"Gender: {data[2]}")  # Assuming the third column is 'gender'
        e5.delete(0, END)
        e5.insert(0, data[2])

        label7.config(text=f"Seat No.: {data[8]}")  # Assuming the ninth column is 'seatno'
        e7.delete(0, END)
        e7.insert(0, data[8])

        label9.config(text=f"Coach No(A,B,C): {data[9]}")  # Assuming the tenth column is 'coach'
        e9.delete(0, END)
        e9.insert(0, data[9])
    else:
        showerror('Data Error', message='No data found for the given Booking ID.')

def print_ticket():
    booking_id = e1.get()
    slt = f"SELECT * FROM passenger_data WHERE booking_id = '{booking_id}'"
    mycur.execute(slt)
    data = mycur.fetchone()

    if data:
        # Add the code to print the ticket here
        showinfo('Print Ticket', message='Ticket printed successfully.')
    else:
        showerror('Data Error', message='No data found for the given Booking ID.')

label1 = Label(text="Booking ID:", fg="blue", bg="#FF0000", font=("calibri", 13, "bold"), height=3, width=15)
e1 = Entry()

label2 = Label(text="Name:", font=("calibri", 13, "bold"))
e2 = Entry()

label3 = Label(text="Age:", font=("calibri", 13, "bold"))
e3 = Entry()

label5 = Label(text="Gender:", font=("calibri", 13, "bold"))
e5 = Entry()

label7 = Label(text="Seat No.:", font=("calibri", 13, "bold"))
e7 = Entry()

label9 = Label(text="Coach No(A,B,C):", font=("calibri", 13, "bold"))
e9 = Entry()

label2.pack(pady=10)
e2.pack(pady=10)
label3.pack(pady=10)
e3.pack(pady=10)
label5.pack(pady=10)
e5.pack(pady=10)
label7.pack(pady=10)
e7.pack(pady=10)
label9.pack(pady=10)
e9.pack(pady=10)

get_data_button = Button(text="Get Data", command=getdata)
get_data_button.pack(pady=10)

label1.pack(pady=10)
e1.pack(pady=10)

print_ticket_button = Button(text="Print Ticket", command=print_ticket)
print_ticket_button.pack(pady=10)

win.mainloop()

import Emailing_Akshaj
