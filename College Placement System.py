import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#import openpyxl
import ttkthemes
import time
import os
from tkhtmlview import HTMLLabel
import mysql.connector

# Function to save details to an Excel file
'''def save_to_excel():
    id_val = id_entry.get()
    name_val = name_entry.get()
    email_val = email_entry.get()
    course_val = course_entry.get()
    address_val = address_entry.get()
    gender_val = gender_entry.get()
    hsc_percent_val = hsc_percent_entry.get()
    cgpa_val = cgpa_entry.get()

    # Check if all fields are filled
    if not all([id_val, name_val, email_val, course_val, address_val, gender_val, hsc_percent_val, cgpa_val]):
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    # Prepare the data to be written
    data = {
        'Id': [id_val],
        'Name': [name_val],
        'Email': [email_val],
        'Course': [course_val],
        'Address': [address_val],
        'Gender': [gender_val],
        'HSC %': [hsc_percent_val],
        'CGPA': [cgpa_val]
    }

    # Convert data to a DataFrame
    df = pd.DataFrame(data)

    # Try to read existing data from Excel if it exists
    try:
        existing_data = pd.read_excel(r'C:\\Users\\shrihari shinde\\Documents\\register.xlsx')
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        # If the file doesn't exist, a new one will be created
        pass

    # Save to Excel
    file_path = 'C:\\Users\\shrihari shinde\\Documents\\register.xlsx'
    df.to_excel(file_path, index=False, engine='openpyxl')

    # Adjust column widths
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    # Set specific widths for each column
    column_widths = {
        'A': 10,  # 'Id' column width
        'B': 20,  # 'Name' column width
        'C': 25,  # 'Email' column width
        'D': 15,  # 'Course' column width
        'E': 25,  # 'Address' column width
        'F': 10,  # 'Gender' column width
        'G': 15,  # 'HSC %' column width
        'H': 10  # 'CGPA' column width
    }

    # Apply column widths
    for col, width in column_widths.items():
        ws.column_dimensions[col].width = width

    # Save the updated file with adjusted column widths
    wb.save(file_path)

    messagebox.showinfo("Success", "Details saved successfully!")

'''
# Function to create labeled entries
def create_labeled_entry(row, label_text, entry_var, parent_frame):
    label = Label(parent_frame, text=label_text, font=('times new roman', 12, 'bold'))
    label.grid(row=row, column=0, padx=10, pady=10, sticky='e')
    entry = Entry(parent_frame, font=('times new roman', 12), bg='lightyellow', textvariable=entry_var)
    entry.grid(row=row, column=1, padx=10, pady=10, sticky='w')
    return entry


def exit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        window.destroy()
    else:
        pass
# Function to create the employee registration form
def employee_form():
    employee_frame = Frame(window, width=1200, height=800)
    employee_frame.place(x=200, y=100)
    headingLabel = Label(employee_frame, text="Student Details", font=('times new roman', 18, 'bold'), bg='blue',
                         fg='white')
    headingLabel.place(x=0, y=0, relwidth=1)

    back_button = Button(employee_frame, text='Back', bg='white', command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)



    # Detail Frame (this remains unchanged)
    detail_frame = Frame(employee_frame)
    detail_frame.place(x=0, y=50)



#Set the grid configuration to align all labels and entries centrally
    detail_frame.grid_columnconfigure(0, weight=1, minsize=150)
    detail_frame.grid_columnconfigure(1, weight=3, minsize=250)

    detail_frame.grid_columnconfigure(0, weight=1, minsize=150)
    detail_frame.grid_columnconfigure(1, weight=3, minsize=250)
    detail_frame.grid_columnconfigure(2, weight=1, minsize=250)  # Create space for the image

    # Create the right_frame for the image
    right_frame = Frame(detail_frame)
    right_frame.grid(row=0, column=2, padx=10, pady=10)

    # Add image to the right_frame
    try:
        photo = PhotoImage(file='campus2.png')
        img1Label = Label(right_frame, image=photo)
        img1Label.photo = photo  # Keep a reference to prevent garbage collection
        img1Label.grid(row=0, column=0, padx=10, pady=10)
    except Exception as e:
        print(f"Error loading image: {e}")

    # First group of fields
    group1_frame = Frame(detail_frame)
    group1_frame.grid(row=0, column=0, padx=20, pady=20)

    global id_entry, name_entry, email_entry, course_entry, address_entry, gender_entry, hsc_percent_entry, cgpa_entry, college_entry

    # Create labeled entry fields for group 1
    id_entry = create_labeled_entry(0, 'Id', StringVar(), group1_frame)
    name_entry = create_labeled_entry(1, 'Name', StringVar(), group1_frame)
    email_entry = create_labeled_entry(2, 'Email', StringVar(), group1_frame)
    course_entry = create_labeled_entry(3, 'Course', StringVar(), group1_frame)
    address_entry = create_labeled_entry(4, 'Address', StringVar(), group1_frame)
    gender_entry = create_labeled_entry(5, 'Gender', StringVar(), group1_frame)
    hsc_percent_entry = create_labeled_entry(6, 'HSC %', StringVar(), group1_frame)
    cgpa_entry = create_labeled_entry(7, 'CGPA', StringVar(), group1_frame)
    college_entry = create_labeled_entry(8, 'College', StringVar(), group1_frame)
    

    company_entry = create_labeled_entry(9, 'Company', StringVar(), group1_frame)
    phone_entry = create_labeled_entry(10, 'Phone', StringVar(), group1_frame)
    

    save_button = Button(employee_frame, text='Save', font=('times new roman', 12, 'bold'), bg='blue', fg='white',
                         command=save_to_excel)
    save_button.place(x=400, y=600)


# Admin Module
def admin_show():
    

    def exit():
        result=messagebox.askyesno('Confirm','Do you want to exit?')
        if result:
            root.destroy()
        else:
            pass
    def show_student():
        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    def delete_student():
        def delete_data():
            query='DELETE FROM student WHERE id=%s AND name=%s;'
            idE=idEntry.get()
            nameE=nameEntry.get()
            val=[]
            val.append(idE)
            val.append(nameE)
            mycursor.execute(query,val)
            con.commit()
            messagebox.showinfo('Deleted')
            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('',END,values=data)
        
        search_window = Toplevel()
        search_window.title('Search Student')
        search_window.grab_set()

        idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
        idLabel.grid(row=0, column=0, padx=30, pady=15)
        idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
        idEntry.grid(row=0, column=1, pady=15, padx=10)

        nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
        nameLabel.grid(row=1, column=0, padx=30, pady=15)
        nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
        nameEntry.grid(row=1, column=1, pady=15, padx=10)

        search_student_button = ttk.Button(search_window, text='Delete', command=delete_data)
        search_student_button.grid(row=6, columnspan=2, pady=15)

    def search_student():
        def search_data():
            query='select * from student where id=%s and name=%s'
            mycursor.execute(query,(idEntry.get(),nameEntry.get()))
            studentTable.delete(*studentTable.get_children())
            fetched_data=mycursor.fetchall()
            for data in fetched_data:
                studentTable.insert('',END,values=data)

        search_window = Toplevel()
        search_window.title('Search Student')
        search_window.grab_set()

        idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
        idLabel.grid(row=0, column=0, padx=30, pady=15)
        idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
        idEntry.grid(row=0, column=1, pady=15, padx=10)

        nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
        nameLabel.grid(row=1, column=0, padx=30, pady=15)
        nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
        nameEntry.grid(row=1, column=1, pady=15, padx=10)

        search_student_button = ttk.Button(search_window, text='SEARCH', command=search_data)
        search_student_button.grid(row=6, columnspan=2, pady=15)

    def add_student():
        def add_data():
            if idEntry.get() =='' or nameEntry.get() =='' or emailEntry.get() =='' or addressEntry.get() =='' or companyEntry.get() =='' or packageEntry.get() =='':
                messagebox.showerror('Error','All Fields are required', parent=add_window)
            else:
                query='insert into student values(%s,%s,%s,%s,%s,%s)'
                idE=idEntry.get()
                nameE=nameEntry.get()
                emailE=emailEntry.get()
                addressE=addressEntry.get()
                companyE=companyEntry.get()
                packageE=packageEntry.get()

                val=[]
                val.append(idE)
                val.append(nameE)
                val.append(emailE)
                val.append(addressE)
                val.append(companyE)
                val.append(packageE)
                mycursor.execute(query,val)#(idEntry.get(),nameEntry.get(),emailEntry.get(),addressEntry.get(),companyEntry.get(),packageEntry.get()))
                con.commit()
                
                result=messagebox.askyesno('Confirm', 'Data added successfully', parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    companyEntry.delete(0,END)
                    packageEntry.delete(0,END)
                else:
                    pass
                query='select *from student'
                mycursor.execute(query)
                fetched_data=mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())
                for data in fetched_data:
                    datalist=list(data)
                    studentTable.insert('',END,values=datalist)


        add_window=Toplevel()
        add_window.grab_set()

        idLabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
        idLabel.grid(row=0,column=0,padx=30,pady=15)
        idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)

        nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
        nameLabel.grid(row=1, column=0, padx=30, pady=15)
        nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
        nameEntry.grid(row=1, column=1, pady=15, padx=10)

        emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
        emailLabel.grid(row=2, column=0, padx=30, pady=15)
        emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
        emailEntry.grid(row=2, column=1, pady=15, padx=10)

        addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
        addressLabel.grid(row=3, column=0, padx=30, pady=15)
        addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
        addressEntry.grid(row=3, column=1, pady=15, padx=10)

        companyLabel = Label(add_window, text='Company', font=('times new roman', 20, 'bold'))
        companyLabel.grid(row=4, column=0, padx=30, pady=15)
        companyEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
        companyEntry.grid(row=4, column=1, pady=15, padx=10)

        packageLabel = Label(add_window, text='Package', font=('times new roman', 20, 'bold'))
        packageLabel.grid(row=5, column=0, padx=30, pady=15)
        packageEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
        packageEntry.grid(row=5, column=1, pady=15, padx=10)

        add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
        add_student_button.grid(row=6,columnspan=2,pady=15)
    def connect_database():
        def connect():
            global mycursor,con
            try:
                con=mysql.connector.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
                mycursor=con.cursor()
                messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
            except:
                messagebox.showerror('Error','Invalid Details',parent=connectWindow)
                return
            try:
                query='create database college'
                mycursor.execute(query)
                query='use college'
                mycursor.execute(query)
                query='CREATE TABLE IF NOT EXISTS student (id VARCHAR(255), name VARCHAR(255), email VARCHAR(255), address VARCHAR(255), company VARCHAR(50), package VARCHAR(50))'
                mycursor.execute(query)
            except:
                query='use college'
                mycursor.execute(query)
            connectWindow.destroy()
            addstudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            showstudentButton.config(state=NORMAL)
            deletestudentButton.config(state=NORMAL)

        connectWindow=Toplevel()
        connectWindow.geometry('500x260+720+230')
        connectWindow.title('Database Connection')
        connectWindow.resizable(0,0)

        hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
        hostnameLabel.grid(row=0,column=0,padx=20)
        hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
        hostEntry.grid(row=0,column=1,padx=40,pady=20)

        usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
        usernameLabel.grid(row=1, column=0, padx=20)
        usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
        usernameEntry.grid(row=1, column=1, padx=40, pady=20)

        passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
        passwordLabel.grid(row=2, column=0, padx=20)
        passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
        passwordEntry.grid(row=2, column=1, padx=40, pady=20)

        connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
        connectButton.grid(row=3,columnspan=2)


    root=ttkthemes.ThemedTk()
    root.get_themes()
    root.set_theme('radiance')
    root.geometry('1170x680+0+0')
    root.resizable(0,0)
    root.title('college placement cell')

    s= 'COLLEGE PLACEMENT CELL'
    sliderLabel=Label(root,text=s,font=('times new roman',20,'bold',),width=30)
    sliderLabel.place(x=200,y=0)
    #slider()
    connectButton=ttk.Button(root,text='Connect database',command=connect_database)
    connectButton.place(x=1000,y=0)

    leftFrame=Frame(root)
    leftFrame.place(x=50,y=80,width=300,height=600)

    addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
    addstudentButton.grid(row=1,column=0,pady=20)

    searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED, command=search_student)
    searchstudentButton.grid(row=2,column=0,pady=20)

    deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED, command=delete_student)
    deletestudentButton.grid(row=3,column=0,pady=20)


    showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED, command=show_student)
    showstudentButton.grid(row=5,column=0,pady=20)


    exitButton=ttk.Button(leftFrame,text='Exit',width=25, command=exit)
    exitButton.grid(row=7,column=0,pady=20)

    rightFrame=Frame(root)
    rightFrame.place(x=350,y=80,width=800,height=600)

    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

    studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Email','City','Company','Package'),
                              xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

    scrollBarX.config(command=studentTable.xview)
    scrollBarY.config(command=studentTable.yview)

    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)
    studentTable.pack(fill=BOTH,expand=1)

    studentTable.heading('Id',text='Id')
    studentTable.heading('Name',text='Name')
    studentTable.heading('Email',text='Email')
    studentTable.heading('City',text='City')
    studentTable.heading('Company',text='Company')
    studentTable.heading('Package',text='Package')

    studentTable.column('Id',width=100,anchor=CENTER)
    studentTable.column('Name',width=300,anchor=CENTER)
    studentTable.column('Email',width=400,anchor=CENTER)
    studentTable.column('City',width=200,anchor=CENTER)
    studentTable.column('Company',width=300,anchor=CENTER)
    studentTable.column('Package',width=300,anchor=CENTER)

    studentTable.config(show='headings')
    root.mainloop()
    


def contact_show():
    contact_frame = Frame(window, width=1200, height=800)
    contact_frame.place(x=200, y=100)
    back_button = Button(contact_frame, text='Back', bg='white', command=lambda: contact_frame.place_forget())
    back_button.place(x=10, y=30)
    headingLabel = Label(contact_frame, text="TPC Contact", font=('times new roman', 18, 'bold'),
                         bg='blue', fg='white')
    headingLabel.place(x=0, y=0, relwidth=1)
    # Create a Treeview widget (Table)
    tree = ttk.Treeview(contact_frame, columns=("Name", "Position", "Phone", "Email"), show="headings")
    tree.place(x=20, y=60, width=900, height=500)  # Adjust placement and size as needed

    # Define headings (column titles)
    tree.heading("Name", text="Name")
    tree.heading("Position", text="Position")
    tree.heading("Phone", text="Phone")
    tree.heading("Email", text="Email")

    # Define column widths
    tree.column("Name", width=100)
    tree.column("Position", width=100)
    tree.column("Phone", width=100)
    tree.column("Email", width=100)

    # Sample data (You can replace this with real data)
    sample_data = [
        ("John Doe", "Manager", "123-456-7890", "john@example.com"),
        ("Jane Smith", "Developer", "234-567-8901", "jane@example.com"),
        ("Alice Brown", "HR", "345-678-9012", "alice@example.com"),
        ("Bob Johnson", "Intern", "456-789-0123", "bob@example.com")
    ]

    # Insert data into the Treeview (table)
    for row in sample_data:
        tree.insert("", "end", values=row)

def recruiters_show():
    recruiters_frame = Frame(window, width=1200, height=800)
    recruiters_frame.place(x=200, y=100)
    back_button = Button(recruiters_frame, text='Back', bg='white', command=lambda: recruiters_frame.place_forget())
    back_button.place(x=10, y=30)
    headingLabel = Label(recruiters_frame, text="TPC Contact", font=('times new roman', 18, 'bold'),
                         bg='blue', fg='white')
    headingLabel.place(x=0, y=0, relwidth=1)
    # Left Frame for first image
    left_frame = Frame(recruiters_frame, width=500, height=700)
    left_frame.place(x=0, y=60)
    recruiters_image = PhotoImage(file='picss.png')  # Change path to your image
    recruiters_img_label = Label(left_frame, image=recruiters_image)
    recruiters_img_label.place(x=40, y=40)  # Adjust placement as needed
    recruiters_img_label.image = recruiters_image  # Keep a reference to the image to avoid garbage collection

    # Right Frame for second image
    right_frame = Frame(recruiters_frame, width=500, height=700)
    right_frame.place(x=600, y=60)  # Adjust x position for the right frame
    second_image = PhotoImage(
        file='picss.png')  # Change path to your second image
    second_img_label = Label(right_frame, image=second_image)
    second_img_label.place(x=40, y=40)  # Adjust placement as needed
    second_img_label.image = second_image  # Keep a reference to the image to avoid garbage collection


def open_excel_file():
    file_path = 'C:\\Users\\shrihari shinde\\Documents\\register.xlsx'
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        messagebox.showerror("File Not Found", "The Excel file does not exist.")


def placed_show():
    
    root=ttkthemes.ThemedTk()
    root.get_themes()
    root.set_theme('radiance')
    root.geometry('1170x680+0+0')
    root.resizable(0,0)
    root.title('college placement cell')

    s= 'COLLEGE PLACEMENT CELL'
    sliderLabel=Label(root,text=s,font=('times new roman',20,'bold',),width=30)
    sliderLabel.place(x=200,y=0)
    #slider()
    

    leftFrame=Frame(root)
    leftFrame.place(x=50,y=80,width=300,height=600)

    

    rightFrame=Frame(root)
    rightFrame.place(x=350,y=80,width=800,height=600)

    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

    studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Email','City','Company','Package'),
                              xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

    def exit():
        result=messagebox.askyesno('Confirm','Do you want to exit?')
        if result:
            root.destroy()
        else:
            pass
    def show_student():
        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)


    def connect_database():
        def connect():
            global mycursor,con
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="",database="college")
                mycursor=con.cursor()
            except:
                return
            try:
                query='use college'
                mycursor.execute(query)
                query='CREATE TABLE IF NOT EXISTS student (id VARCHAR(255), name VARCHAR(255), email VARCHAR(255), address VARCHAR(255), company VARCHAR(50), package VARCHAR(50))'
                mycursor.execute(query)
            except:
                query='use college'
                mycursor.execute(query)
                show_student()
        connect()
        show_student()


    
    exitButton=ttk.Button(leftFrame,text='Exit',width=25, command=exit)
    exitButton.grid(row=7,column=0,pady=20)
    connect_database()
    scrollBarX.config(command=studentTable.xview)
    scrollBarY.config(command=studentTable.yview)

    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)
    studentTable.pack(fill=BOTH,expand=1)

    studentTable.heading('Id',text='Id')
    studentTable.heading('Name',text='Name')
    studentTable.heading('Email',text='Email')
    studentTable.heading('City',text='City')
    studentTable.heading('Company',text='Company')
    studentTable.heading('Package',text='Package')

    studentTable.column('Id',width=100,anchor=CENTER)
    studentTable.column('Name',width=300,anchor=CENTER)
    studentTable.column('Email',width=400,anchor=CENTER)
    studentTable.column('City',width=200,anchor=CENTER)
    studentTable.column('Company',width=300,anchor=CENTER)
    studentTable.column('Package',width=300,anchor=CENTER)

    studentTable.config(show='headings')
    root.mainloop()
    


def graph_show():
    graph_frame = Frame(window, width=1200, height=800)
    graph_frame.place(x=200, y=100)
    back_button = Button(graph_frame, text='Back', bg='white', command=lambda: graph_frame.place_forget())
    back_button.place(x=10, y=30)
    headingLabel = Label(graph_frame, text="Students Graph", font=('times new roman', 18, 'bold'),
                         bg='blue', fg='white')
    headingLabel.place(x=0, y=0, relwidth=1)

    

#Initialize main window
window = Tk()
window.geometry("700x500")  # Increased width to give more space
window.config(bg='white')

# Title Label
titleLabel = Label(window, text='College Placement System', font=('times new roman', 40, 'bold'), bg='red', fg='white')
titleLabel.place(x=0, y=0, relwidth=1)

exitButton=Button(window,text='Exit',font=('times new roman',20,'bold'),fg='#010c48', command=exit)
exitButton.place(x=1400,y=10)

# Add current date and time below the title
def update_time():
    current_time = time.strftime('%H:%M:%S')  # Current time
    current_date = time.strftime('%A, %B %d, %Y')  # Current date
    time_label.config(text=f"{current_date} - {current_time}")
    time_label.after(1000, update_time)  # Update the time every 1000 ms (1 second)

time_label = Label(window, font=('times new roman', 18), bg='white', fg='black', width=35)
time_label.place(x=0, y=60, relwidth=1)  # Position it below the title

update_time()  # Call the function to update the time


# Create the left frame and menu buttons
leftFrame = Frame(window)
leftFrame.place(x=0, y=80, width=350, height=700)  # Increased width for the left frame

menuLabel = Label(leftFrame, text="Menu", font=('times new roman', 20), bg='#009688', width=35)
menuLabel.pack(fill=X)

button_width= 40

employee_button = Button(leftFrame, text="Student\nRegistration", font=('times new roman', 20, 'bold'),
                         padx=10, pady=10, width=button_width, command=employee_form)
employee_button.pack(fill=X)

admin_button = Button(leftFrame, text="Admin\nModule", font=('times new roman', 20, 'bold'),
                      padx=10, pady=10, width=button_width, command=admin_show)
admin_button.pack(fill=X)

placed_button = Button(leftFrame, text="Placed\nStudents", font=('times new roman', 20, 'bold'),
                       padx=10, pady=10, width=button_width, command=placed_show)
placed_button.pack(fill=X)

graph_button = Button(leftFrame, text="Graph", font=('times new roman', 20, 'bold'),
                      padx=10, pady=10, width=button_width, command=graph_show)
graph_button.pack(fill=X)

# Add new buttons below the "Graph" button
tpc_contact_button = Button(leftFrame, text="TPC\nContact", font=('times new roman', 20, 'bold'),
                            padx=10, pady=10, width=button_width, command=contact_show)
tpc_contact_button.pack(fill=X)

our_recruiters_button = Button(leftFrame, text="Our Recruiters", font=('times new roman', 20, 'bold'),
                               padx=10, pady=10, command=recruiters_show)
our_recruiters_button.pack(fill=X)

# Add image
photo = PhotoImage(file='campus.png')
img1Label = Label(window, image=photo)
img1Label.place(x=460, y=90)  # Adjusted x position to fit the window size

# Main loop
window.mainloop()
