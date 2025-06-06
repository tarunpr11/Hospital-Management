import tkinter as tk
import mysql.connector as sqltor
import appointment
import bill
import doctor
import lab
import mr
import nurse
import patient
import prescription
import room
import staff


def mainPage():

    def app_func():
        root1.destroy()
        appointment.AppointmentPage()
        mainPage()
    def bill_func():
        root1.destroy()
        bill.BillPage()
        mainPage()
    def doctor_func():
        root1.destroy()
        doctor.DoctorPage()
        mainPage()
    def lab_func():
        root1.destroy()
        lab.LabPage()
        mainPage()
    def mr_func():
        root1.destroy()
        mr.MRPage()
        mainPage()
    def nurse_func():
        root1.destroy()
        nurse.NursePage()
        mainPage()
    def patient_func():
        root1.destroy()
        patient.PatientPage()
        mainPage()
    def pres_func():
        root1.destroy()
        prescription.PrescriptionPage()
        mainPage()
    def room_func():
        root1.destroy()
        room.RoomPage()
        mainPage()
    def staff_func():
        root1.destroy()
        staff.StaffPage()
        mainPage()
    def destroy():
        root1.destroy()
    root1 = tk.Tk()
    root1.config(bg='white')
    root1.attributes('-fullscreen', True)

    label1 = tk.Label(root1, text='Hospital Management System', fg='#57a1f8', bg='white',
                     font=('Microsoft YaHei UI Light', 49, 'bold'))
    label1.place(x=390, y=20)

    logo1 = tk.PhotoImage(file='hospital_icon.png')
    tk.Label(root1, image=logo1, bg='white').place(x=230, y=0)

    mainpage_pic10 = tk.PhotoImage(file='mainpage_pic3.png',height=614)
    tk.Label(root1, image=mainpage_pic10, bg='white').place(x=170, y=140)

    buttonframe1 = tk.Frame(root1, bg='white')
    buttonframe1.columnconfigure(0, weight=1)
    buttonframe1.columnconfigure(1, weight=1)

    btn10 = tk.Button(buttonframe1, text='Patient', font=('Arial', 22), width=15,command=patient_func)
    btn10.grid(row=0, column=0, pady=15, padx=15)

    btn12 = tk.Button(buttonframe1, text='Doctor', font=('Arial', 22), width=15,command=doctor_func)
    btn12.grid(row=0, column=1, pady=15, padx=15)

    btn13 = tk.Button(buttonframe1, text='Lab', font=('Arial', 22), width=15,command=lab_func)
    btn13.grid(row=1, column=0, pady=15, padx=15)

    btn14 = tk.Button(buttonframe1, text='Appointment', font=('Arial', 22), width=15,command=app_func)
    btn14.grid(row=1, column=1, pady=15, padx=15)

    btn15 = tk.Button(buttonframe1, text='Medical Record', font=('Arial', 22), width=15,command=mr_func)
    btn15.grid(row=2, column=0, pady=15, padx=15)

    btn16 = tk.Button(buttonframe1, text='Nurse', font=('Arial', 22), width=15,command=nurse_func)
    btn16.grid(row=2, column=1, pady=15, padx=15)

    btn17 = tk.Button(buttonframe1, text='Staff', font=('Arial', 22), width=15,command=staff_func)
    btn17.grid(row=3, column=0, pady=15, padx=15)

    btn18 = tk.Button(buttonframe1, text='Prescription', font=('Arial', 22), width=15,command=pres_func)
    btn18.grid(row=3, column=1, pady=15, padx=15)

    btn19 = tk.Button(buttonframe1, text='Room', font=('Arial', 22), width=15,command=room_func)
    btn19.grid(row=4, column=0, pady=15, padx=15)

    btn20 = tk.Button(buttonframe1, text='Bill', font=('Arial', 22), width=15,command=bill_func)
    btn20.grid(row=4, column=1, pady=15, padx=15)

    buttonframe1.place(x=800, y=240)
    btn30 = tk.Button(root1, text='Exit', font=('Arial', 22), width=15,command=destroy)
    btn30.place(x=970,y=700)
    root1.mainloop()

if __name__ == '__main__':
    mainPage()

import mysql.connector

# Create a connection to the database
db = mysql.connector.connect(
    host="localhost",  # replace with your host name
    user="root",  # replace with your username
    password="Jigsaw#1134",
    auth_plugin='mysql_native_password'  # replace with your password
)

if db:
    print("Connected")
