#Railway Ticket Generation
from tkinter import *
win = Tk()
win.title("Ticket Generation")
win.geometry("2000x2000")
'''
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="test123"
)
cursor = conn.cursor()

def fetch_and_display():
    # Replace 'passenger_data' with your actual table name
    query = "SELECT * FROM passenger_data"
    cursor.execute(query)
    data = cursor.fetchone()  # Assuming you want to display the first row

    # Display data in Entry widgets
    e0.insert(0, data[7])  # Booking ID
    e1.insert(0, data[0])  # Name
    e2.insert(0, data[1])  # Age
    e3.insert(0, data[2])
'''
label1=Label( text="Booking ID: " , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e1=Entry()
label2=Label( text="Name :" , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e2=Entry()
label3=Label( text= "Age : " , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e3=Entry()
label4=Label( text = "Category :" , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e4=Entry()
label5=Label( text ="Gender :" ,  fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e5=Entry()
label7=Label( text = "Seat No. : " ,   fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e7=Entry()
label9=Label( text = "Coach No(A,B,C):" ,  fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =20)
e9=Entry()
label10=Label( text= "From Station : " , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e10=Entry()
label11=Label( text = "Departure Time :" , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e11=Entry()
label12=Label( text = "To Station :" , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e12=Entry()
label13=Label( text = "Arrival Time :" , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e13=Entry()
label14=Label( text = "Journey Duration :" , fg="blue" , bg="#FF0000" , font=("calibri" ,13 , "bold") , height = 3,width =15)
e14=Entry()
label1.place(relx=0.3,rely=0.0)
e1.place(relx=0.3, rely=0.1)
label2.place(relx=0.7, rely=0.0)
e2.place(relx=0.7, rely = 0.1)
label3.place(relx=0.35 , rely = 0.2)
e3.place(relx = 0.35 , rely = 0.3)
label4.place(relx = 0.50 ,  rely=0.2) 
e4.place(relx = 0.50 ,  rely=0.3)
label5.place(relx = 0.65 , rely = 0.2)
e5.place(relx = 0.65 , rely = 0.3)
label7.place(relx = 0.35 , rely = 0.4)
e7.place(relx = 0.35 , rely = 0.5)
label9.place(relx = 0.7 , rely = 0.4)
e9.place(relx = 0.7 , rely = 0.5)
label10.place( relx = 0.1 , rely = 0.6)
e10.place( relx = 0.1 , rely = 0.7)
label11.place( relx = 0.3 , rely = 0.6)
e11.place( relx = 0.3 , rely = 0.7)
label12.place(relx = 0.5 , rely = 0.6)
e12.place(relx = 0.5 , rely = 0.7)
label13.place(relx = 0.7 , rely = 0.6)
e13.place(relx = 0.7 , rely = 0.7) 
label14.place(relx = 0.5 , rely = 0.8)
e14.place(relx = 0.5 , rely = 0.9)
win.bind("<Return>" , lambda e : win.destroy())
win.mainloop()
#Railway Ticket Printing 
from tkinter import *
import pyautogui 
import tempfile
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os 
import subprocess
file_to_print = ''
def print_any_file(file=None):
    if os.path.exists(file):
        try:
            print(file)
            runticket = subprocess.run(f"python {file}")
            pyautogui.screenshot().save("Ticket.pdf")
            l1.config(text='')
        except Exception as e:
            showerror('Error',message='printing Error',detail=e)
    else:
        showerror('Printing Error',message='Please Select a file to print.')
        
def selectfile():
    global file_to_print
    file= askopenfilename(filetypes =[('Text Files', '*.txt'),('py Files', '*.py')])
    if file:
        file_to_print=file
        l1.config(text=file)
win1 = Tk()
win1.title('Ticket Printing')
win1.geometry("300x200")
l = Label(win1,text='Select ur desired file to print',bg='orange')
l.pack(fill=X)
btn_select = Button(win1,text='Select File',width=15,bg='blue',command=selectfile)
btn_select.pack(fill=X)
l1 = Label(text='')
l1.pack(fill=X)
btn = Button(win1,text='Print',width=15,command=lambda:print_any_file(file_to_print))
btn.pack(fill=X)
win1.bind("<Return>" , lambda e : win1.destroy())
win1.mainloop()