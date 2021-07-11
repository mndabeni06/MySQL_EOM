from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(user='lifechoices', password = '@Lifechoices1234', host = 'localhost', database = 'LifechoicesOnline', auth_plugin = 'mysql_native_password')

root = Tk()
root.title("AdminRights")
root.geometry("1200x700")
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





delete_btn = Button(root, text = 'Delete selected row', command = delete)
delete_btn.place(x=850,y=600)


exit_btn = Button(root, text = 'Go to main page', command = exit)
exit_btn.place(x=850, y=500)


def exit():
    root.destroy()
    import Vistors_Login





root.mainloop()
