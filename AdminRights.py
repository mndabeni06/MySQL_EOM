from tkinter import messagebox
from tkinter import*
import mysql.connector

window = Tk()



class AdminRights:
    def __init__(self, master):
        self.root = window
        self.root.title('AdminRights')
        self.root.geometry("1000x600")

        # Creating widgets for the frame1
        self.frame1 = Frame(master, width=400, height=300, highlightbackground="blue", highlightthickness=2)
        self.frame1.place(x=5, y=100)

        self.frame2 = Frame(master, width=430, height=300, highlightbackground="blue", highlightthickness=2)
        self.frame2.place(x=550, y=100)


        self.Login_username = Label(self.frame1, text="Please Enter Username", borderwidth=5)
        self.Login_username.place(x=5, y=5)
        self.Login_username_entry = Entry(self.frame1, borderwidth=5)
        self.Login_username_entry.place(x=200, y=5)


        self.Login_password = Label(self.frame1, text="Please Enter Password", borderwidth=5)
        self.Login_password.place(x=5, y=50)
        self.Login_password_entry = Entry(self.frame1, borderwidth=5)
        self.Login_password_entry.place(x=200, y=50)


        self.Add_btn = Button(self.frame1, text="AddUser", borderwidth=5)
        self.Add_btn.place(x=5, y=250)

        self.Remove_btn = Button(self.frame1, text="RemoveUser", borderwidth=5)
        self.Remove_btn.place(x=200, y=250)

        # creating widgets for frame2

        self.name = Label(self.frame2, text="Fullname")
        self.name.place(x=5, y=5)
        self.name_entry = Entry(self.frame2, borderwidth=5)
        self.name_entry.place(x=250, y=5)

        self.surname = Label(self.frame2, text="Lastname")
        self.surname.place(x=5, y=50)
        self.surname_entry = Entry(self.frame2, borderwidth=5)
        self.surname_entry.place(x=250, y=50)

        self.phone_number = Label(self.frame2, text=" Phone_number")
        self.phone_number.place(x=5, y=100)
        self.phone_number_entry = Entry(self.frame2, borderwidth=5)
        self.phone_number_entry.place(x=250, y=100)


        self.next_of_kin_name = Label(self.frame2, text="Next of Kin Name")
        self.next_of_kin_name.place(x=5, y=150)
        self.next_of_kin_name_entry = Entry(self.frame2, borderwidth=5)
        self.next_of_kin_name_entry.place(x=250, y=150)

        self.next_of_kin_mobile_number = Label(self.frame2, text="Next of Kin Mobile Number")
        self.next_of_kin_mobile_number.place(x=5, y=200)
        self.next_of_kin_mobile_number_entry = Entry(self.frame2, borderwidth=5)
        self.next_of_kin_mobile_number_entry.place(x=250, y=200)


        self.AddUser_button = Button(self.frame2, text="AddUser", borderwidth=5)
        self.AddUser_button.place(x=5, y=250)

        self.RemoveUser_button = Button(self.frame2, text="RemoveUser", borderwidth=5)
        self.RemoveUser_button.place(x=200, y=250)


        self.Login_heading = Label(window, width=10,
                                   font="Calibri 20", text="USERSLOGIN")
        self.Login_heading.place(x=50, y=50)
        self.Registration_heading = Label(window, width=25, font="Calibri 20", text="NEW USERS REGISTRATION")
        self.Registration_heading.place(x=550, y=50)






A = AdminRights(window)
window.mainloop()
