from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

root = Tk()

root.config(bg="#8dc63f")

now = datetime.now()
formatted = now.strftime('%Y-%m-%d %H:%M:%S')

class Login:
    def __init__(self, master):
        self.root = root
        self.root.title('LoginWindow')
        self.root.geometry("700x400")

        self.username = Label(master, text="Please Enter Username", borderwidth=5)
        self.username.place(x=5, y=5)
        self.username_entry = Entry(master, borderwidth=5)
        self.username_entry.place(x=200, y=5)

        self.password = Label(master, text="Please Enter password", borderwidth=5)
        self.password.place(x=5, y=50)
        self.password_entry = Entry(master, borderwidth=5, show="*")
        self.password_entry.place(x=200, y=50)

        self.login_btn = Button(master, text="User Login", borderwidth=5, command=self.login, bg="goldenrod")
        self.login_btn.place(x=10, y=300)

        self.register_user_btn = Button(master, text=" New User Registration", borderwidth=5, command=self.register,
                                        bg="yellow")
        self.register_user_btn.place(x=150, y=300)

        self.admin = Button(master, text="Admin", borderwidth=5, command=self.admin_log,
                                        bg="green" )
        self.admin.place(x=380, y=300)
        self.exit_btn = \
            Button(master, text="Exit", borderwidth=5, bg="red", command=self.exit)
        self.exit_btn.place(x=500, y=300)

    def login(self):


        global mydb
        if self.username_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror("STATUS", "PLEASE ENTER VALID DETAILS")
        else:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                           database='LifechoicesOnline',
                                           auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            sql = "INSERT INTO Login (username, password) VALUES (%s, %s)"
            val = (self.username_entry.get(), self.password_entry.get())
            mycursor.execute(sql, val)
            messagebox.showinfo("PERMISSION", "Login Successful! Enjoy Your Day")
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            mydb.commit()








    def register(self):
        messagebox.showinfo('PERMISSION', 'WELCOME TO LIFECHOICES REGISTRATION')
        self.root.destroy()
        import Registration



    def admin_log(self):
        messagebox.showinfo('PERMISSION', 'ADMIN ACCESS GRANTED')
        self.root.destroy()
        import AdminLogin

    def exit(self):
        self.messagebox = messagebox.askquestion('Exit Application', 'Are you sure you want to Logout?')
        if self.messagebox == 'yes':
            self.root.destroy()
        else:
            pass


Y = Login(root)
root.mainloop()
