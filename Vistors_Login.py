from tkinter import messagebox
from tkinter import*
import mysql.connector
root = Tk()


class Admin:

    def __init__(self, master):
        self.master = master
        self.master.title('Lifechoices Online')
        self.master.geometry('400x400')
        self.master.configure(bg='#F49F1C')

        self.admin_header = Label(master,  bg='#F49F1C', fg='#0F52BA', text='Administrator Login Page')
        self.admin_header.place(x=50, y=50, width=300)
        self.admin_header.config(font=('courier', '14', 'bold'))

        self.admin_username = Label(master,  bg='#F49F1C', fg='white', text='Please Enter Admin Username')
        self.admin_username.place(x=150, y=100)

        self.admin_entry = Entry(master, width=45)
        self.admin_entry.place(x=140, y=150, width=120)

        self.admin_password = Label(master,  bg='#F49F1C', fg='#0F52BA', text='Please Enter Admin Password')
        self.admin_password.place(x=150, y=150)

        self.password_entry = Entry(master, width=45)
        self.password_entry

        reg_btn = Button(root, text='Login', bg='#0F52BA', fg='white', command=login_ad)
        reg_btn.place(x=155, y=200, width=80)



    def admin_login(self):
    adminPassword = entUserPass.get()

    mydb = mysql.connector.connect(
                                    host="127.0.0.1",
                                    user="lifechoices",
                                    password="@Lifechoices1234",
                                    database="LifechoicesOnline")
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Registration =%s'
    mycursor.execute(sql, [adminPassword])
    res = mycursor.fetchall()
    if res:
        for i in res:
            logged()
            break
    else:
        failed()


def logged():
    messagebox.showinfo('Correct', 'you have successfully logged into admin')
    pass



def failed():
    messagebox.showinfo('Failed', 'Please enter correct admin password')
    entUserPass.focus()









root.mainloop()
