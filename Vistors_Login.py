from tkinter import *
from tkinter import messagebox
from datetime import datetime
import mysql.connector

now = datetime.now()
formatted = now.strftime('%Y-%m-%d %H:%M:%S')

from PIL import Image, ImageTk

root = Tk()

background_img = Image.open("background.png")
bg_img = ImageTk.PhotoImage(background_img)
img = Label(root, image=bg_img)
img.place(x=0, y=0)


class Database:
    def __init__(self, master):
        self.root = root
        self.root.title('')
        self.root.geometry("500x360")

        self.username = Label(master, text="Please Enter Username", borderwidth=5)
        self.username.place(x=5, y=5)
        self.username_entry = Entry(master, borderwidth=5)
        self.username_entry.place(x=200, y=5)

        self.password = Label(master, text="Please Enter password", borderwidth=5)
        self.password.place(x=5, y=50)
        self.password_entry = Entry(master, borderwidth=5)
        self.password_entry.place(x=200, y=50)

        self.login_btn = Button(master, text="Login", borderwidth=5, command=self.login, bg="goldenrod")
        self.login_btn.place(x=10, y=200)

        self.register_user_btn = Button(master, text="Register New User", borderwidth=5, command=self.register,
                                        bg="yellow")
        self.register_user_btn.place(x=150, y=200)

        self.exit_btn = Button(master, text="Exit", borderwidth=5, bg="red", command=self.exit)
        self.exit_btn.place(x=400, y=200)

    def login(self):

        if self.username_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror("STATUS", "PLEASE ENTER VALID DETAILS")
        else:
            hospital = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='lifechoicesonline',
                                               auth_plugin='mysql_native_password')
            mycursor = hospital.cursor()
            xy = mycursor.execute('Select * from users')
            for x in mycursor:
                if x[1] == self.password_entry.get() and x[0] == self.username_entry.get():
                    messagebox.showinfo("PERMISSION", "SUCCESSFUL! Enjoy Your Day")
                    root.destroy()
            if x[1] != self.password_entry.get() or x[0] != self.username_entry.get():
                messagebox.showerror("STATUS", "ACCESS DENIED")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)

    def register(self):

        global reg
        if self.username_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror("STATUS", "PLEASE ENTER VALID DETAILS")
        else:
            reg = mysql.connector.connect(user='sql6423129', password=' rutppuWASF', host='sql6.freesqldatabase.com',
',
                                          database='sql6423129',
                                          auth_plugin='mysql_native_password')

            mycursor = reg.cursor()
            sql = "INSERT INTO Login (user, password) VALUE (%s, %s)"
            val = (self.username_entry.get(), self.password_entry.get())
            mycursor.execute(sql, val)
            messagebox.showinfo("PERMISSION", "YOU HAVE SUCCESSFULLY REGISTERED")
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            reg.commit()

    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to Logout?')
        if self.message_box == 'yes':
            self.root.destroy()
        else:
            pass


Y = Database(root)
root.mainloop()
