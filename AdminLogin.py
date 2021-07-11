from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

root.config(bg="#8dc63f")



class Admin:
    def __init__(self, master):
        self.root = root
        self.root.title('LoginWindow')
        self.root.geometry("700x400")

        self.Admin_username = Label(master, text="AdminUsername", borderwidth=5)
        self.Admin_username.place(x=5, y=5)
        self.Admin_username_entry = Entry(master, borderwidth=5)
        self.Admin_username_entry.place(x=200, y=5)

        self.Admin_password = Label(master, text="AdminPassword", borderwidth=5)
        self.Admin_password.place(x=5, y=50)
        self.Admin_password_entry = Entry(master, borderwidth=5, show="*")
        self.Admin_password_entry.place(x=200, y=50)

        self.Admin_login_btn = Button(master, text="AdminLogin", borderwidth=5, command=self.login, bg="goldenrod")
        self.Admin_login_btn.place(x=10, y=200)

        self.exit_btn = Button(master, text="Exit", borderwidth=5, bg="red", command=self.exit)
        self.exit_btn.place(x=400, y=200)

    def login(self):

        global i
        if self.Admin_username_entry.get() == "" and self.Admin_password_entry.get() == "":
            messagebox.showerror("STATUS", "PLEASE ENTER VALID DETAILS")
        else:
            admin = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                            database='LifechoicesOnline',
                                            auth_plugin='mysql_native_password')
            mycursor = admin.cursor()
            xy = mycursor.execute('Select * from Admin')
            for i in mycursor:
                if i[1] == self.Admin_password_entry.get() and i[0] == self.Admin_username_entry.get():
                    messagebox.showinfo("PERMISSION", "LOGIN SUCCESSFUL!")
                    root.destroy()
                    import AdminRights
            if i[1] != self.Admin_password_entry.get() or i[0] != self.Admin_username_entry.get():
                messagebox.showerror("STATUS", "ACCESS DENIED")
                self.Admin_username_entry.delete(0, END)
                self.Admin_password_entry.delete(0, END)

    def exit(self):
        self.messagebox = messagebox.askquestion('Exit Application', 'Are you sure you want to Logout?')
        if self.messagebox == 'yes':
            self.root.destroy()
        else:
            pass


A = Admin(root)
root.mainloop()
