from tkinter import messagebox
from tkinter import*
import mysql.connector

root = Tk()

mydb = mysql.connector.connect(
                                host="localhost",
                                user="lifechoices",
                                password="@Lifechoices1234",
                                database="LifechoicesOnline"
    )
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM Registration')
i=0
for Registration in mycursor:
    for j in range(len(Registration)):
        lstUsers = Listbox(root, width='75', height='5')
        lstUsers.place(x=20, y=300)

        lstUsers.insert(END, Registration[j])
        i= i+1


def saveTodb():
    username = entusername.get()
    password = entpassword.get()
    mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="lifechoices",
                                    password="@Lifechoices1234",
                                    database="LifechoicesOnline"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO Registration (usurname  ,password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    # mycursor.execute()
    mydb.commit()
    messagebox.showinfo("STATUS", "Successfully Updated")

    print(mycursor.rowcount, "record inserted.")


def delete():
    lstUsers.delete(ANCHOR)
    # lstUsers.config(text='')


def update():
    id1 = entid.get()
    fullname = entfullname.get()
    username = entusername.get()
    password = entpassword.get()
    mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="lifechoices",
                                    password="@Lifechoices1234",
                                    database="LifechoicesOnline"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE Users SET (id, full_name, username, password) VALUES (%s, %s, %s, %s)"
    val = (id1, fullname, username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Info', 'Record Update')



root.title('Lifechoices Online')
root.geometry('650x500')
root.configure(bg='#F49F1C')

lbl_register = Label(root,  bg='#F49F1C', fg='#0F52BA', text='Register')
lbl_register.place(x=250, y=50)
lbl_register.config(font=('courier', '30', 'bold'))

lbl_id = Label(root,  bg='#F49F1C', fg='white', text='User id',)
lbl_id.place(x=200, y=100)

entid = Entry(root, width=45)
entid.place(x=300, y=100, width=120)

lbl_fullname = Label(root,  bg='#F49F1C', fg='white', text='Full name',)
lbl_fullname.place(x=200, y=140)

entfullname = Entry(root, width=45)
entfullname.place(x=300, y=140, width=120)

lbl_password = Label(root,  bg='#F49F1C', fg='white', text='Password',)
lbl_password.place(x=200, y=220)

entpassword = Entry(root, width=45)
entpassword.place(x=300, y=220, width=120)

lbl_username = Label(root,  bg='#F49F1C', fg='white', text='Username',)
lbl_username.place(x=200, y=180)

entusername = Entry(root, width=45)
entusername.place(x=300, y=180, width=120)

btnInsert = Button(root, text='Insert', bg='#0F52BA', fg='white', command=saveTodb)
btnInsert.place(x=160, y=450, width=80)

btnUpdate = Button(root, text='Update', bg='#0F52BA', fg='white', command=update)
btnUpdate.place(x=260, y=450, width=80)

btnDelete = Button(root, text='Delete', bg='#0F52BA', fg='white', command=delete)
btnDelete.place(x=360, y=450, width=80)

root.mainloop()
