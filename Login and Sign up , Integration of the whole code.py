#actual login and sign up
from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror, showinfo
db = mysql.connector.connect(host="localhost",user="root",passwd="root123",database="test123")
mycur = db.cursor()

def failed():
    global fail
    fail = Toplevel(root1)

    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", width=8, height=1, command=fail_destroy).pack()

def error_destroy():
    err.destroy()

def succ_destroy():
    root2.destroy()
    root1.destroy()

def succ_destroy1():
    root3.destroy()
def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="gray", width=8, height=1, command=succ_destroy1).pack()



def register_user():
    if username == "":
        error()
    elif password == "":
        error()
    else:
        sql = "insert into login(username,password) values(%s,%s)"
        t = (username.get(), password.get())
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        success()


def login():        #insert get variables in this def and make it global
    global root2
    root2=Tk()
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", fg="black", font="bold", width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2,textvariable=password_varify,show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In",command=login_varify).pack()
    Label(root2, text="")
    root2.mainloop()

def signup():       #insert get variables in this def and make it global
    global root3
    root3=Tk()
    root3.title("Registration Portal")
    root3.geometry("300x300")
    global username
    global password
    Label(root3, text="Register your account", fg="black", font="bold", width=300).pack()
    username= StringVar()
    password= StringVar()
    Label(root3, text="").pack()
    Label(root3, text="Username:").pack()
    Entry(root3, textvariable=username).pack()
    Label(root3, text="").pack()
    Label(root3, text="Password:").pack()
    Entry(root3, textvariable=password,show="*").pack()
    Label(root3, text="").pack()
    Button(root3, text="Register", command=register_user).pack()
    root3.mainloop()

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root1)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg,text="Ok",width=8,height=1,command=bookwin).pack()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",width=8,height=1).pack()

def login_varify():
    global user_varify
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    if user_varify=="admin" and pas_varify=="admin":
        adminpriv()
    else:
        sql = "select * from login where username = %s and password = %s"
        mycur.execute(sql,[(user_varify),(pas_varify)])
        results = mycur.fetchall()
        if results:
            for i in results:
                logged()
                break
        else:
            failed()
def mainwindow():
    global root1
    root1=Tk()
    root1.geometry("400x400")
    root1.title("PESPRESSO RESERVATIONS")
    Label(root1, text="Log-In Portal", fg="black", font="bold", width=300).pack()
    log_b=Button(root1,text="LOG IN",command = login)#add command to go to next widget
    orl=Label(root1,text="OR")
    signin_b=Button(root1,text="SIGN UP",command = signup)
    log_b.pack()
    orl.pack()
    signin_b.pack()
    root.destroy()
    root1.mainloop()

def bookwin():
    global win
    win=Tk()
    win.geometry("400x400")
    win.title("PESPRESSO RESERVATIONS")
    Label(win, text="Booking portal", fg="black", font="bold", width=300).pack()
    log_b = Button(win, text="MY TICKETS",command=myticket)  # add command to go to next widget
    log_b.pack()
    orl = Label(win, text="OR")
    orl.pack()
    signin_b = Button(win, text="NEW BOOKINGS",command=newbookings)
    signin_b.pack()
    succ_destroy()
    win.mainloop()

def myticket():
    import sample69
def newbookings():
    # Importing modules
    from tkinter import ttk
    from tkinter import messagebox
    from tkcalendar import Calendar
    import mysql.connector

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="test123"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Window
    root7 = Tk()
    root7.title('Starting and end station')
    f1 = Frame(root7, width=700, height=700)
    f1.place(relx=0, rely=0)
    f1_label = LabelFrame(f1, text="Trains Available", font=("calibri", 15, "bold"))
    f1_label.grid(row=0, column=0)

    f2 = Frame(root7, width=700, height=700)
    f2.place(relx=0, rely=0.37)
    f2_label = LabelFrame(f2, text="Select Trains", font=("calibri", 15, "bold"))
    f2_label.grid(row=0, column=1)

    # Changing the position where the trains are displayed
    my_tree = ttk.Treeview(f1_label)

    # Drop down menu
    starting_station = ['Select departing station', 'Hyderabad', 'Bangalore', 'Mysore', 'Chennai', 'Mumbai',
                        'Ahmedabad']

    # Combobox for starting_station

    myCombo1 = ttk.Combobox(f2_label, value=starting_station)
    myCombo1.current(0)
    myCombo1.bind("<<ComboboxSelected>>")
    myCombo1.grid(row=1, column=0)

    # Creating destination station dropdown menu

    destination_station = ['Select destination station', 'Hyderabad', 'Bangalore', 'Mysore', 'Chennai', 'Mumbai',
                           'Ahmedabad']

    # Combobox for destination_station

    myCombo2 = ttk.Combobox(f2_label, value=destination_station)
    myCombo2.current(0)
    myCombo2.bind("<<ComboboxSelected>>")
    myCombo2.grid(row=2, column=0)

    # Defining columns

    my_tree['columns'] = (
    "Train number", "Train name", 'Starting station', 'Duration', 'Date', 'Destination', 'Number of seats',
    'Active Days', 'Arrival Time', 'Departure Time')

    # Formatting columns

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Train number", width=120, minwidth=120)
    my_tree.column("Train name", width=120, minwidth=120)
    my_tree.column("Starting station", width=120, minwidth=120)
    my_tree.column("Duration", width=120, minwidth=120)
    my_tree.column("Date", width=120, minwidth=120)
    my_tree.column("Destination", width=120, minwidth=120)
    my_tree.column("Number of seats", width=120, minwidth=120)
    my_tree.column("Active Days", width=220, minwidth=220)

    # Creating Heading

    my_tree.heading("#0", text="#0", anchor=CENTER)
    my_tree.heading("Train number", text="Train number", anchor=CENTER)
    my_tree.heading("Train name", text="Train name", anchor=CENTER)
    my_tree.heading("Starting station", text="Starting station", anchor=CENTER)
    my_tree.heading("Duration", text="Duration", anchor=CENTER)
    my_tree.heading("Date", text="Date", anchor=CENTER)
    my_tree.heading("Destination", text="Destination", anchor=CENTER)
    my_tree.heading("Number of seats", text="Number of seats", anchor=CENTER)
    my_tree.heading("Active Days", text="Active Days", anchor=CENTER)
    my_tree.heading("Arrival Time", text="Arrival Time", anchor=CENTER)
    my_tree.heading("Departure Time", text="Departure Time", anchor=CENTER)
    my_tree.grid(row=0, column=1)

    clicked1 = "Bangalore"
    clicked2 = "Hyderabad"

    # Confirm button command
    def confirm():
        date1 = str(cal.get_date())
        click1 = str(myCombo1.get())
        click2 = str(myCombo2.get())

        train_data = {
            'Hyderabad_Bangalore': (
            '20703', 'YPR Vande Bharat', 'Hyderabad', '10 hours 25 minutes', 'Bangalore', '5:30', '15:55'),
            'Bangalore_Hyderabad': (
            '20704', 'KCG Vande Bharat', 'Bangalore', '10 hours 25 minutes', 'Hyderabad', '20:00', '6:25'),
            'Mysore_Chennai': ('20608', 'MAS Vande Bharat', 'Mysore', '9 hours 10 minutes', 'Chennai', '6:00', '15:10'),
            'Chennai_Mysore': ('20607', 'YPR Vande Bharat', 'Chennai', '9 hours 10 minutes', 'Mysore', '17:00', '2:10'),
            'Mumbai_Ahmedabad': (
            '20901', 'VANDE BHARAT EXP', 'Mumbai', '8 hours 20 minutes', 'Ahmedabad', '12:00', '8:20'),
            'Ahmedabad_Mumbai': (
            '20902', 'VANDE BHARAT EXP', 'Ahmedabad', '8 hours 20 minutes', 'Mumbai', '22:00', '6:20')
        }

        # Check if the selected route exists in the train_data dictionary
        route_key = f"{click1}_{click2}"
        if route_key in train_data:
            train_info = train_data[route_key]
            train_id, train_name, starting_station, duration, destination, dep_time, arr_time = train_info
            my_tree.insert(parent='', index='end', iid=0, text=' ', values=(train_id, train_name, starting_station,
                                                                            duration, date1, destination, '75',
                                                                            'All days',
                                                                            dep_time, arr_time))

            update_query = "UPDATE trains SET coach_a = coach_a - 1 WHERE TrainID = %s"
            cursor.execute(update_query, (train_id,))
            db.commit()

        else:
            messagebox.showinfo("Trains", "No trains available")

    # Confirm button
    button1 = Button(f2_label, text="CONFIRM", command=confirm)
    button1.grid(row=4, column=0)

    def booktrain():
        import mysql.connector
        from tkinter import ttk
        import uuid

        # Creating MySQL connection
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="test123"
        )

        # Creating cursor
        mycursor = mydb.cursor()

        # Creating window object
        root = Tk()

        # Frame labels
        f1 = Frame(root, width=700, height=700)
        f1.place(relx=0, rely=0)
        f1_label = LabelFrame(f1, text="Details and seat preference", font=("calibri", 15, "bold"))
        f1_label.grid(row=0, column=0)

        f3 = Frame(root, width=2100, height=700)
        f3.place(relx=0, rely=0.52)
        f3_label = LabelFrame(f3, text="Food choices", font=("calibri", 15, "bold"))
        f3_label.grid(row=0, column=1)

        def create_ticket_widgets(num_tickets):
            entry_widgets = []  # List to store entry widgets for names
            age_entries = []  # List to store entry widgets for ages
            gender_combos = []  # List to store combobox widgets for gender
            seat_combos = []  # List to store combobox widgets for seat preference
            reservation_combos = []  # List to store combobox widgets for reservation
            food_choice_combos = []  # List to store combobox widgets for food choices

            # String variables to retrieve data from checkboxes which tell if a person is a minor or not
            var_list = [StringVar() for _ in range(num_tickets)]

            # Creating widgets for each ticket
            for i in range(num_tickets):
                # Name
                label_name = Label(f1_label, text=f"Name {i + 1}: ", font=("calibri", 10, "bold"))
                label_name.grid(row=i * 5, column=0)
                entry_name = Entry(f1_label, fg='black', borderwidth=5)
                entry_name.grid(row=i * 5, column=1)
                entry_widgets.append(entry_name)  # Add the entry widget to the list

                c = Checkbutton(f1_label, text=f'Is a minor {i + 1}: ', variable=var_list[i], onvalue='yes',
                                offvalue='no')
                c.deselect()
                c.grid(row=i * 5, column=2)

                # Empty label
                label_empty = Label(f1_label, text='')
                label_empty.grid(row=i * 5 + 3, column=0)

                # Age
                label_age = Label(f1_label, text=f"Age {i + 1}: ", font=("calibri", 10, "bold"))
                label_age.grid(row=i * 5 + 1, column=0)
                entry_age = Entry(f1_label, fg='black', borderwidth=5)
                entry_age.grid(row=i * 5 + 1, column=1)
                age_entries.append(entry_age)  # Add the entry widget to the list

                # Gender
                gender = ['--Select Gender--', 'Male', 'Female', 'Others']
                label_gender = Label(f1_label, text=f"Gender {i + 1}: ", font=("calibri", 10, "bold"))
                label_gender.grid(row=i * 5 + 2, column=0)
                myCombo_gender = ttk.Combobox(f1_label, value=gender)
                myCombo_gender.current(0)
                myCombo_gender.bind("<<ComboboxSelected>>")
                myCombo_gender.grid(row=i * 5 + 2, column=1)
                gender_combos.append(myCombo_gender)  # Add the combobox widget to the list

                # Seat preference
                seat = ['Any seat', 'Window seat', 'Normal seat']
                label_seat = Label(f1_label, text=f'Seat Preference {i + 1}: ', font=("calibri", 10, "bold"))
                label_seat.grid(row=i * 5 + 1, column=3)
                myCombo_seat = ttk.Combobox(f1_label, value=seat)
                myCombo_seat.current(0)
                myCombo_seat.bind("<<ComboboxSelected>>")
                myCombo_seat.grid(row=i * 5 + 1, column=4)
                seat_combos.append(myCombo_seat)  # Add the combobox widget to the list

                # Reservation
                reservation = ['General', 'PWD', 'Ladies', 'Senior Citizens']
                label_reservation = Label(f1_label, text=f'Reservation {i + 1}: ', font=("calibri", 10, "bold"))
                label_reservation.grid(row=i * 5 + 2, column=3)
                myCombo_reservation = ttk.Combobox(f1_label, value=reservation)
                myCombo_reservation.current(0)
                myCombo_reservation.bind("<<ComboboxSelected>>")
                myCombo_reservation.grid(row=i * 5 + 2, column=4)
                reservation_combos.append(myCombo_reservation)  # Add the combobox widget to the list

                # Food choices
                food_choice = ['Veg', 'Non-Veg']
                label_food_choice = Label(f3_label, text=f'Food Choice {i + 1}: ', font=("calibri", 10, "bold"))
                label_food_choice.grid(row=i, column=0)
                myCombo_food_choice = ttk.Combobox(f3_label, value=food_choice)
                myCombo_food_choice.current(0)
                myCombo_food_choice.bind("<<ComboboxSelected>>")
                myCombo_food_choice.grid(row=i, column=1)
                food_choice_combos.append(myCombo_food_choice)  # Add the combobox widget to the list

            def data():
                seat_counter = {'A': 1, 'B': 1, 'C': 1}  # Track seat numbers for each coach
                for j in range(num_tickets):
                    booking_id = str(uuid.uuid4())  # Generate a unique ID
                    name = entry_widgets[j].get()
                    is_minor = var_list[j].get()
                    age = age_entries[j].get()
                    gender = gender_combos[j].get()
                    seat_preference = seat_combos[j].get()
                    reservation_type = reservation_combos[j].get()
                    food_choice = food_choice_combos[j].get()

                    # Assign seat number and coach
                    if seat_counter['A'] <= 75:
                        seat_number = seat_counter['A']
                        coach = 'A'
                    elif seat_counter['B'] <= 75:
                        seat_number = seat_counter['B']
                        coach = 'B'
                    else:
                        seat_number = seat_counter['C']
                        coach = 'C'

                    # Increment seat number for the corresponding coach
                    seat_counter[coach] += 1

                    # Inserting data into MySQL table
                    sql = "INSERT INTO passenger_data (booking_id, name, age, gender, is_minor, seat_preference, reservation_type, food_choice, seatno, coach) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        booking_id, name, age, gender, is_minor, seat_preference, reservation_type, food_choice,
                        seat_number,
                        coach)
                    mycursor.execute(sql, val)
                    mydb.commit()

                    print(
                        f'Data for passenger {j + 1} with Booking ID {booking_id}, Seat Number {seat_number}, and Coach {coach} inserted into the database')

            labelA = Label(f3_label, text='')
            labelA.grid(row=num_tickets, column=3)

            def paymentwin():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root123",
                    database="test123"
                )

                # Creating cursor
                mycursor = mydb.cursor()

                def fetch_booking_id():
                    # Query to fetch the booking ID from the database
                    query = "SELECT booking_id FROM passenger_data LIMIT 1"  # Replace 'passenger_data' with your actual table name
                    mycursor.execute(query)
                    result = mycursor.fetchone()

                    return result[0] if result else None

                def validate_password(password):
                    # Query to check if the entered password exists in the database
                    query = "SELECT * FROM login WHERE password = %s"
                    values = (password,)
                    mycursor.execute(query, values)
                    result = mycursor.fetchall()

                    return len(result) > 0

                def payment():
                    # Get the entered password from the user input
                    entered_password = paswd_entry.get()

                    # Validate the password
                    if validate_password(entered_password):
                        messagebox.showinfo("Payment Successful", "Payment has been processed successfully.")
                    else:
                        messagebox.showerror("Invalid Password", "Invalid password. Payment failed.")

                win1 = Tk()
                win1.title("Payment Gateway")
                win1.geometry('650x450')

                # Fetch the booking ID from the database
                booking_id = fetch_booking_id()

                # Booking ID label and entry
                booking_id_label = Label(text='Booking ID:')
                booking_id_label.place(x=100, y=50)
                booking_id_entry = Entry(win1)
                booking_id_entry.insert(0, booking_id)  # Set the retrieved booking ID
                booking_id_entry.place(x=250, y=50)

                # Password label and entry
                paswd_label = Label(text='Password:')
                paswd_label.place(x=100, y=100)
                paswd_entry = Entry(show='*')
                paswd_entry.place(x=250, y=100)

                # Captcha label, entry, and image
                captcha_label = Label(text='Enter the captcha shown:')
                captcha_label.place(x=100, y=200)
                captcha_entry = Entry()
                captcha_entry.place(x=250, y=200)

                cv = Canvas(win1, height=700, width=700)
                filename = PhotoImage(file=r'C:\Users\Sharmistha\Downloads\CAPTCHA_2 (1).png')
                cv.create_image(150, 60, image=filename)
                cv.place(x=120, y=250)

                # Pay button
                pay_button = Button(win1, text='Pay', command=payment)
                pay_button.place(x=225, y=425)

                win1.mainloop()

            def pull():
                root7.destroy()
                data()
                paymentwin()

            confirm_button = Button(f3_label, text="Confirm", command=pull)
            confirm_button.grid(row=num_tickets + 1, column=3)

        def get_num_tickets():
            num_tickets = int(entry_num_tickets.get())
            create_ticket_widgets(num_tickets)

        # Ask for the number of tickets
        label_num_tickets = Label(f1_label, text="Number of Tickets:")
        label_num_tickets.grid(row=0, column=6)
        entry_num_tickets = Entry(f1_label, fg='black', borderwidth=5)
        entry_num_tickets.grid(row=0, column=7)
        button_num_tickets = Button(f1_label, text="Submit", command=get_num_tickets)
        button_num_tickets.grid(row=0, column=8)
        root.mainloop()

        def frrootdes():
            root.destroy()

    # Book button
    button1 = Button(f1_label, text="BOOK TRAIN",command=booktrain)
    button1.grid(row=3, column=1)

    # Calendar
    cal = Calendar(f2_label, selectmode='day', day=18, month=12, year=2023, date_pattern="dd-mm-yyyy")
    cal.grid(row=0, column=0)
    win.destroy()
    root7.mainloop()
    db.close()

def printticket():
    db = mysql.connector.connect(host="localhost", user="root", passwd="root123", database="test123")
    mycur = db.cursor()

    win3 = Tk()
    win3.title("Ticket Generation")
    win3.geometry("800x600")

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

    win3.mainloop()
def adminpriv():
    # Replace with your actual database connection details
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="test123"
    )

    # Create a cursor
    db_cursor = db_connection.cursor()

    # Fetch data from the database
    db_cursor.execute("SELECT reservation_type, food_choice, age FROM passenger_data")
    data = db_cursor.fetchall()

    # Close the database connection
    db_cursor.close()
    db_connection.close()

    # Prepare data for plotting
    reservations = [row[0] for row in data]
    food_choices = [row[1] for row in data]
    ages = [row[2] for row in data]

    def show_graph(title, x_label, data_values):
        fig, ax = plt.subplots()
        ax.bar(data_values, [1] * len(data_values))  # Y-values are not relevant for this example
        ax.set_xlabel(x_label)
        ax.set_ylabel("Count")
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=Toplevel())
        canvas.get_tk_widget().pack()
        canvas.draw()
    # Create Tkinter window
    root8 = Tk()
    root8.title("Graphs with Tkinter")

    # Buttons to show graphs
    reservations_button = ttk.Button(root8, text="Show Reservations Graph",
                                     command=lambda: show_graph("Reservation Distribution", "Reservation Type",
                                                                reservations))
    reservations_button.pack(pady=10)

    food_choices_button = ttk.Button(root8, text="Show Food Choices Graph",
                                     command=lambda: show_graph("Food Choice Distribution", "Food Choice",
                                                                food_choices))
    food_choices_button.pack(pady=10)

    age_distribution_button = ttk.Button(root8, text="Show Age Distribution Graph",
                                         command=lambda: show_graph("Age Distribution", "Age", ages))
    age_distribution_button.pack(pady=10)

    # Run the Tkinter event loop
    root8.mainloop()


root = Tk()
root.geometry("400x400")
root.title("PESPRESSO RESERVATIONS")
bg = PhotoImage(file = "C:/Users/Sharmistha/Downloads/PESPRESSO RESERVATIONS.png")
canvas1 = Canvas(root)
canvas1.pack(fill = BOTH, expand = True)
canvas1.create_image( 20,20, image = bg,anchor = "nw")
Label(root,text="Welcome!!",font=("times new roman",20,"bold")).pack()
root.after(2000,mainwindow)
root.mainloop()
