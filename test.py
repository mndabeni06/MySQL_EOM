from tkinter import *
from tkinter import messagebox
from datetime import datetime
import mysql.connector

now = datetime.now()
formatted = now.strftime('%Y-%m-%d %H:%M:%S')


def logging():
    id1 = entUserId.get()
    mydb = mysql.connector.connect(user='lifechoices',
                                    password='@Lifechoices1234',
                                    host='127.0.0.1',
                                    database='LifechoicesOnline',
                                    auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM Users WHERE id=%s', [id1])
    result = mycursor.fetchall()
    if result:
        messagebox.showinfo('Successful', 'You have successfully logged')
        sql = "INSERT INTO Login_out (id, login_logout) VALUES (%s, %s)"
        val = (id1, formatted)
        mycursor.execute(sql, val)
        mydb.commit()
        import User_number
        root.withdraw()
    else:
        messagebox.showinfo('Failed', 'Please check if you have used correct Id')
        entUserId.focus()


def reg():
     messagebox.showinfo('Admin', 'You are in admin please enter your admin id')
     import admin_login


root = Tk()
root.title('Lifechoices Online')
root.geometry('600x600')
root.configure(bg='#F49F1C')
photo = PhotoImage(file="img1.png")
w = Label(root, image=photo, width=350, height=133)
w.pack()

lblId = Label(root, bg='#F49F1C', fg='white', text='Enter User id',)
lblId.place(x=200, y=200)

entUserId = Entry(root, width=45)
entUserId.place(x=350, y=200, width=100)

btnlogin = Button(root, text='Login', bg='#0F52BA', fg='white', command=logging)
btnlogin.place(x=150, y=300, width=80)

btnadmin = Button(root, text='Admin', bg='#0F52BA', fg='white', command=reg)
btnadmin.place(x=350, y=300, width=80)



 global x, mycursor
        if self.username_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror("STATUS", "PLEASE ENTER VALID DETAILS")
        else:
            lifechoices = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='LifechoicesOnline',
                                               auth_plugin='mysql_native_password')
            mycursor = lifechoices.cursor()
            xy = mycursor.execute('Select * from Login')


            for x in mycursor:
                if x[0] == self.password_entry.get() and x[1] == self.username_entry.get():
                 messagebox.showinfo("PERMISSION", "LOGIN SUCCESSFUL")
                 root.destroy()
                if x[0] != self.password_entry.get() or x[1] != self.username_entry.get():
                    messagebox.showerror("STATUS", "ACCESS DENIED")
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)

root.mainloop()
