from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')

root = Tk()
root.title("AdminRights")
root.geometry("1200x1200")
root.config(bg="#8dc63f")




# Registration tree view

trv = ttk.Treeview(root, selectmode ='browse')
trv.grid(row=1,column=1,pady=40)

trv["columns"] = ("1", "2", "3","4","5","6","7","8")
trv['show'] = 'headings'

trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 100, anchor ='c')
trv.column("3", width = 100, anchor ='c')
trv.column("4", width = 150, anchor ='c')
trv.column("5", width = 150, anchor ='c')
trv.column("6",width =250, anchor = 'c')
trv.column("7", width = 150, anchor = 'c')
trv.column("8", width = 150, anchor = 'c')




trv.heading("1", text ="ID")
trv.heading("2", text ="Name")
trv.heading("3", text ="Surname")
trv.heading("4", text ="Phone_number")
trv.heading("5", text = "Next_of_kin_name")
trv.heading("6", text = "Next_of_kin_mobile_number")
trv.heading("7", text = "Sigin_time")
trv.heading("8", text = "Sigin_date")



mycursor = mydb.cursor()
xy = mycursor.execute('SELECT *  FROM Registration')

for dt in mycursor:
    trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6]))

def delete():

    selected = trv.focus()
    values = trv.item(selected,'values')
    mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')
    mycursor = mydb.cursor()
    sql = "DELETE FROM Registration WHERE id = %s"
    val = (values[0],)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo(title='STATUS', message='Successfully Deleted.')


def update():
    update_label = Label(root, text ='Update Record:')
    update_label.place(x=750, y=350)
    update_entry = Entry(root)
    update_entry.place(x=860, y=350)
    what_label = Label(root, text = 'Update: ')
    what_label.place(x=750,y=400)
    what_entry = Entry(root)
    what_entry.place(x=860,y=400)
    into_label = Label(root, text= 'update to:')
    into_label.place(x=750, y=450)
    into_entry = Entry(root)
    into_entry.place(x=860,y=450)
    update2 = Button(root, text ='update', command =update)
    update2.place(x=870, y=500)

    if update_entry.get() == 'name':
        mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE Registration SET name = %s WHERE name = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'surname':
        mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LlifechoicesOnline', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE Registration SET surname = %s WHERE surname = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'phone_number':
        mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE Registration SET phone_number = %s WHERE phone_number= %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'next_of_kin_name':
        mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE next_of_kin_name SET next_of_kin_name = %s WHERE next_of_kin_name = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'next_of_kin_mobile_number':
        mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE next_of_kin_mobile_number SET next_of_kin_mobile_number = %s WHERE next_of_kin_mobile_number = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        pass



##def add_admin():
    ##selected = trv.focus()
    ##values = trv.item(selected,'values')
   ## mydb = mysql.connector.connect(user='lifechoices', password = '@LifechoicesOnline1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')
   ## mycursor = mydb.cursor()
   ## sql = "INSERT INTO Admin (Username, password) VALUES (%s, %s)"
   ## val = (values[1],values[2],values[3],)
   ## mycursor.execute(sql,val)
   ## mydb.commit()
   ## messagebox.showinfo(title='PERMISSION', message='ADMIN ADDED SUCCESSFULLY.')




delete_btn = Button(root, text = 'Delete selected row', command = delete)
delete_btn.place(x=850,y=800)

update_btn = Button(root, text = 'Update', command = update)
update_btn.place(x=870,y=900)

#add_btn = Button(root, text = 'Add new user', command=add_admin)
#add_btn.place(x=850, y=700)

#logout_btn = Button(root, text = 'Logout user', command = logout_user)
#logout_btn.place(x=850,y=600)

exit_btn = Button(root, text = 'Go to main page', command = exit)
exit_btn.place(x=850, y=500)


def exit():
    root.destroy()
    import Vistors_Login





root.mainloop()
