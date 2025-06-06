import tkinter as tk

from tkinter import ttk
from mysql.connector import connect, Error



# Connect to MySQL

connection = connect(
    host="localhost",
    user="root",
    password="Jigsaw#1134",
    database="Hospital",
    auth_plugin='mysql_native_password'
)
cursor = connection.cursor()

def searchForm():
    def getDetails():
        values = [pid.get(),first_name.get()]
        if values[0] == '':
            values[0] = 0
        if values[1] == '':
            values[1] = 0
        search(values,root)
    root = tk.Tk()
    root.config(bg='white')
    title = tk.Label(root, text='Search Record', bg='white', fg='#57a1f8',
                     font=('Microsoft YaHei UI Light', 49, 'bold'))
    title.place(x=600, y=10)
    pid_label = tk.Label(root, text="MRID:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                         fg='#00a0da')
    pid_label.place(x=100, y=150)
    pid = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    pid.place(x=315, y=150)

    firstname_label = tk.Label(root, text="PID:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                 fg='#00a0da')
    firstname_label.place(x=100, y=250)
    first_name = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    first_name.place(x=315, y=250)

    btn1 = tk.Button(root, text='Search Record', font=('Arial', 18), width=20, height=2, command=getDetails)
    btn1.place(x=600, y=600)

    root.mainloop()

def search(details,root):
    query = f"SELECT * FROM MedicalRecord WHERE MRID = {details[0]} OR PID = {details[1]}"
    cursor.execute(query)
    rows = cursor.fetchall()
    display_records(rows,root,root)

def fetch_records(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def create_frame(root):

    main_frame = tk.Frame(root)
    main_frame.pack(fill='both', expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side='left', fill='both', expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
    my_scrollbar.pack(side='right', fill='y')

    my_canvas.configure(yscrollcommand=my_scrollbar.set, )
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = tk.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

    return second_frame
# Display records in Tkinter GUI
def display_records(rows,second_frame,root):

    buttonframe = tk.Frame(second_frame, bg='white',highlightcolor='white', highlightbackground="green", highlightthickness=1)

    buttonframe.columnconfigure(2, weight=1,uniform='same')

    btn1 = tk.Label(buttonframe,text="MRID",bg='#00a0da',fg='white',height=2,borderwidth=1, relief=tk.RAISED)
    btn1.grid(row=0, column=0, sticky="nsew")

    btn2 = tk.Label(buttonframe, text="PID",bg='#00a0da',fg='white',borderwidth=1, relief=tk.RAISED)
    btn2.grid(row=0, column=1, sticky="nsew")

    btn3 = tk.Label(buttonframe, text="Symptoms",bg='#00a0da',fg='white',borderwidth=1, relief=tk.RAISED)
    btn3.grid(row=0, column=2, sticky="nsew")
    btn9 = tk.Label(buttonframe, text="Diagnosis",bg='#00a0da',fg='white',borderwidth=1, relief=tk.RAISED)
    btn9.grid(row=0, column=3, sticky="nsew")

    btn4 = tk.Label(buttonframe, text="Drugs",bg='#00a0da',fg='white',borderwidth=1, relief=tk.RAISED)
    btn4.grid(row=0, column=4, sticky="nsew")

    btn5 = tk.Label(buttonframe, text="DocID", bg='#00a0da', fg='white', borderwidth=1, relief=tk.RAISED)
    btn5.grid(row=0, column=5, sticky="nsew")

    index = 1

    for row in rows:
        btn1 = tk.Label(buttonframe, text=row[0],bg='#57a1f8',fg='black',borderwidth=1, relief=tk.GROOVE)
        btn1.grid(row=index, column=0, sticky="nsew")
        btn2 = tk.Label(buttonframe, text=row[1],bg='#57a1f8',fg='black',borderwidth=1, relief=tk.GROOVE)
        btn2.grid(row=index, column=1, sticky="nsew")
        btn3 = tk.Label(buttonframe, text=row[2],bg='#57a1f8',fg='black',borderwidth=1, relief=tk.GROOVE)
        btn3.grid(row=index, column=2, sticky="nsew")
        btn4 = tk.Label(buttonframe, text=row[3],bg='#57a1f8',fg='black',borderwidth=1, relief=tk.GROOVE)
        btn4.grid(row=index, column=3, sticky="nsew")
        btn5 = tk.Label(buttonframe, text=row[4],bg='#57a1f8',fg='black',borderwidth=1, relief=tk.GROOVE)
        btn5.grid(row=index, column=4, sticky="nsew")
        btn6 = tk.Label(buttonframe, text=row[5], bg='#57a1f8', fg='black', borderwidth=1, relief=tk.GROOVE)
        btn6.grid(row=index, column=5, sticky="nsew")
        index += 1


    buttonframe.pack(fill='both',expand=True)

    root.mainloop()


def updateForm():
    details = []

    def getDetails():
        details = [pid.get(),column.get(),value.get()]
        update(details, root)

    root = tk.Tk()
    root.config(bg='white')
    title = tk.Label(root, text='Update Medical Record', bg='white', fg='#57a1f8', font=('Microsoft YaHei UI Light', 49, 'bold'))
    title.place(x=460, y=10)
    pid_label = tk.Label(root, text="MRID:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                fg='#00a0da')
    pid_label.place(x=100, y=150)
    pid = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    pid.place(x=315, y=150)

    column_label = tk.Label(root, text="Column:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                 fg='#00a0da')
    column_label.place(x=100, y=250)
    column = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    column.place(x=315, y=250)

    value_label = tk.Label(root, text="Value:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                               fg='#00a0da')
    value_label.place(x=100, y=350)
    value = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    value.place(x=315, y=350)

    btn1 = tk.Button(root, text='Update Medical Record', font=('Arial', 18), width=20, height=2, command=getDetails)
    btn1.place(x=600, y=600)

    root.mainloop()

def update(details,root):
    query = f"UPDATE MedicalRecord SET {details[1]} = '{details[2]}' WHERE MRID = {int(details[0])}"
    cursor.execute(query)
    connection.commit()
    success = tk.Label(root, text="Record Updated Successfully", bg='white',
                       font=('Microsoft YaHei UI Light', 24, 'bold'), fg='#00a0da')
    success.place(x=520, y=700)


def showDetails():
    wind = tk.Tk()
    table_name = "medicalrecord"
    rows = fetch_records(table_name)
    frame = create_frame(wind)
    display_records(rows,frame,wind)


def insertDetails(details,root):
    query = f"INSERT INTO MedicalRecord(PID,Symptoms,Diagnosis,Drugs,DocID) VALUES({details[0]},'{details[1]}','{details[2]}','{details[3]}',{details[4]})"
    cursor.execute(query)
    connection.commit()
    success = tk.Label(root, text="Medical Record Added Successfully", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),fg='#00a0da')
    success.place(x=500,y=700)

def entryForm(root):
    details = []
    def getDetails():
        details = [first_name.get(),middle_name.get(),last_name.get(),gender.get(),doc.get()]
        insertDetails(details,root)

    first_name_label = tk.Label(root, text="PID:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),fg='#00a0da')
    first_name_label.place(x=100, y=150)
    first_name = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    first_name.place(x=315, y=150)

    middle_name_label = tk.Label(root, text="Symptoms:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                fg='#00a0da')
    middle_name_label.place(x=100, y=250)
    middle_name = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    middle_name.place(x=315, y=250)

    last_name_label = tk.Label(root, text="Diagnosis:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                fg='#00a0da')
    last_name_label.place(x=100, y=350)
    last_name = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    last_name.place(x=315, y=350)

    gender_label = tk.Label(root, text="Drugs:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                fg='#00a0da')
    gender_label.place(x=100, y=450)
    gender = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    gender.place(x=315, y=450)

    doc_label = tk.Label(root, text="DocID:", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'),
                                fg='#00a0da')
    doc_label.place(x=800, y=150)
    doc = tk.Entry(root, font=('Microsoft YaHei UI Light', 22, 'bold'), borderwidth=2)
    doc.place(x=1015, y=150)

    btn1 = tk.Button(root, text='Add Medical Record', font=('Arial', 18), width=20, height=2, command=getDetails)
    btn1.place(x=600,y=600)

def AddMR():
    root = tk.Tk()
    root.config(bg='white')
    title = tk.Label(root,text='Add Medical Record',bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light', 49, 'bold'))
    title.place(x=600,y=10)
    entryForm(root)
    root.mainloop()



def MRPage():
    def destroy():
        root.destroy()
        return
    root = tk.Tk()
    root.config(bg='white')
    root.attributes('-fullscreen', True)
    label = tk.Label(root, text='Hospital Management System', fg='#57a1f8', bg='white',
                     font=('Microsoft YaHei UI Light', 49, 'bold'))
    label.place(x=390, y=20)

    label = tk.Label(root, text='Medical Record', fg='#00a0da', bg='white',
                     font=('Arial', 39, 'bold'))
    label.place(x=610, y=120)

    logo = tk.PhotoImage(file=r'hospital_icon.png')
    tk.Label(root, image=logo, bg='white').place(x=230, y=0)

    # mainpage_pic = tk.PhotoImage(file='mainpage_pic.png')
    # tk.Label(root,image=mainpage_pic,bg='black').place(x=80,y=160)

    mainpage_pic2 = tk.PhotoImage(file=r'medrec.png')
    tk.Label(root, image=mainpage_pic2, bg='white').place(x=105, y=210)

    buttonframe = tk.Frame(root, bg='white')
    buttonframe.columnconfigure(0, weight=1)

    btn1 = tk.Button(buttonframe, text='Add Record', font=('Arial', 18), width=20,height=2,command=AddMR)
    btn1.grid(row=0, column=0, pady=15, padx=15)

    btn2 = tk.Button(buttonframe, text='Show Details', font=('Arial', 18), width=20,height=2,command=showDetails)
    btn2.grid(row=1, column=0, pady=15, padx=15)

    btn3 = tk.Button(buttonframe, text='Update Details', font=('Arial', 18), width=20,height=2,command=updateForm)
    btn3.grid(row=2, column=0, pady=15, padx=15)

    btn5 = tk.Button(buttonframe, text='Search Record', font=('Arial', 18), width=20,height=2,command=searchForm)
    btn5.grid(row=4, column=0, pady=15, padx=15)
    btn10 = tk.Button(buttonframe, text='Exit', font=('Arial', 18), width=20,height=2,command=destroy)
    btn10.grid(row=5, column=0, pady=15, padx=15)
    buttonframe.place(x=940, y=220)

    root.mainloop()

if __name__ == '__main__':
    MRPage()