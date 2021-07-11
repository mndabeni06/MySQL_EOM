from tkinter import messagebox
from tkinter import*
import mysql.connector
reg = Tk()


class Registration:

    def __init__(self, master):
        self.master = master
        self.master.title('Lifechoices Online')
        self.master.geometry('500x360')
        self.master.configure(bg='#8dc63f')



        self.name = Label(master, text="Please Enter Your Fullname")
        self.name.place(x=10, y=5)
        self.name_entry = Entry(master, borderwidth=5)
        self.name_entry.place(x=250, y=5)

        self.surname = Label(master, text="Please Enter Your Lastname")
        self.surname.place(x=10, y=50)
        self.surname_entry = Entry(master, borderwidth=5)
        self.surname_entry.place(x=250, y=50)

        self.phone_number = Label(master, text="Please Enter Your Phone_number")
        self.phone_number.place(x=10, y=100)
        self.phone_number_entry = Entry(master, borderwidth=5)
        self.phone_number_entry.place(x=250, y=100)


        self.next_of_kin_name = Label(master, text="Next of Kin Name")
        self.next_of_kin_name.place(x=10, y=150)
        self.next_of_kin_name_entry = Entry(master, borderwidth=5)
        self.next_of_kin_name_entry.place(x=250, y=150)

        self.next_of_kin_mobile_number = Label(master, text="Next of Kin Mobile Number")
        self.next_of_kin_mobile_number.place(x=10, y=200)
        self.next_of_kin_mobile_number_entry = Entry(master, borderwidth=5)
        self.next_of_kin_mobile_number_entry.place(x=250, y=200)


        self.register = Button(master, text="Click Here For Registration", borderwidth=5, bg="orange", command=self.register)
        self.register.place(x=5, y=300)

        self.exit_btn = Button(master, text="Exit", borderwidth=5, bg="red", command=self.exit)
        self.exit_btn.place(x=400, y=300)



    def register(self):

         global mydb

         if self.name_entry.get() == "" and self.surname_entry.get() == "" and self.phone_number_entry.get() and self.next_of_kin_name_entry.get() == "" and self.next_of_kin_mobile_number_entry.get() == "":
                messagebox.showerror("STATUS", "PLEASE ENTER VALID DETAILS")

         else:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                           database='LifechoicesOnline',
                                           auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            sql = "INSERT INTO Registration (name, surname, phone_number, next_of_kin_name, next_of_kin_mobile_numbe) VALUES (%s, %s, %s, %s, %s)"
            val = (self.name_entry.get(), self.surname_entry.get(), self.phone_number_entry.get(), self.next_of_kin_name_entry.get(), self.next_of_kin_mobile_number_entry.get())
            mycursor.execute(sql, val)
            messagebox.showinfo("PERMISSION", "Successfully Registered")
            self.name_entry.delete(0, END)
            self.surname_entry.delete(0, END)
            self.phone_number_entry.delete(0, END)
            self.next_of_kin_name_entry.delete(0, END)
            self.next_of_kin_mobile_number_entry.delete(0, END)
            mydb.commit()



    def exit(self):
        self.messagebox = messagebox.askquestion('Exit Application', 'Are you sure you want to Logout?')
        if self.messagebox == 'yes':
            self.master.destroy()
        else:
            pass









    #def admin_login(self):
   # adminPassword = entUserPass.get()

   # mydb = mysql.connector.connect(
                                   # host="127.0.0.1",
                                    #user="lifechoices",
                                    #password="@Lifechoices1234",
                                    #database="LifechoicesOnline")
   # mycursor = mydb.cursor()
   # sql = 'SELECT * FROM Registration =%s'
    #mycursor.execute(sql, [adminPassword])
   # res = mycursor.fetchall()
    #if res:
        #for i in res:
            #logged()
           # break
    #else:
       # failed()


#def logged():
    #messagebox.showinfo('Correct', 'you have successfully logged into admin')
    #pass



#def failed():
    #messagebox.showinfo('Failed', 'Please enter correct admin password')
   # entUserPass.focus()








Z = Registration(reg)
reg.mainloop()
