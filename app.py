import os 
import sys
import time
import random 
import tempfile
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from time import strftime
from datetime import datetime 
from datetime import datetime, date, timedelta 
from db import Database



blue_color = "#4b8598"
bg1_color = "#c7c7c7"
bg2_color = "#e2e2e2"
chocolate_color = "#72404d"
white_color = "white"
grey_color = "gray"
red_color = "red"
green_color = "green"
title_color = "#4f234f"

db =  Database('shalele_hotel_db.db')
root = Tk() 

def move_window(event):
    root.geometry('+{0}+{0}'.format(event.x_root, y_root))



class LoginPageView(object):
    """docstring for LoginPageView"""
    def get_admin_page(self):
        self.root.withdraw()
        self.newWindow = Toplevel()
        self.app = HomePageView(self.newWindow)

    def get_staff_page(self):
        self.root.withdraw()
        self.newWindow = Toplevel()
        self.app = StaffHomePageView(self.newWindow)

    def exit_app(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=self.root)
        if sure == True:
            global root
            root.quit()

    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry('600x400+200+100')
        self.root.config(bd=1, bg=white_color, relief='raised')
        self.root.resizable(0, 0)

        lg_username = StringVar()
        lg_password = StringVar() 
        lg_designation = StringVar()

        # date 
        today = date.today()
        set_login_date = today.strftime("%B %d, %Y")
        set_login_time = str(time.strftime("%I:%M:%S %p"))


        def clearAll():
            lg_username.set('')
            lg_password.set('')
            lg_designation.set('')


        # login function
        def get_login(): 
            username = entry_username.get()
            password = entry_password.get()
            designation = entry_designation.get()

            if username=="" or password=="" or designation=="":
                messagebox.showerror("Error","The Fields Cannot Be Empty", parent=root)
                clearAll()

            elif username=="admin" and password=="9090" and designation=="admin":
                db.insert_login_history(username, set_login_date, set_login_time)
                self.get_admin_page()
                clearAll()

            elif username and password and designation=="admin":
                row = db.login_account(username, password, designation)
                print(row)
                if row==None:
                    messagebox.showerror("Error","No Match To Your Inputs Information", parent=root)
                    clearAll()
                else:
                    messagebox.showinfo("Login","Successfully login", parent=root)
                    db.insert_login_history(username, set_login_date, set_login_time)
                    self.get_admin_page()
                    clearAll()
            
            elif username and password and designation=="staff":
                row = db.login_account(username, password, designation)
                print(row)
                if row==None:
                    messagebox.showerror("Error","No Match To Your Inputs Information", parent=root)
                    clearAll()
                else:
                    messagebox.showinfo("Login","Successfully login", parent=root)
                    db.insert_login_history(username, set_login_date, set_login_time)
                    self.get_staff_page()
                    clearAll()
            
            else:
                messagebox.showerror("Error","Invalid Inputs", parent=root)
                clearAll()
        

        # =======================frames==========================
        top_frame = LabelFrame(self.root, bd=1, relief='raised', bg=bg1_color, height=80, pady=5)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, pady=20, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1,)

        # add staff label
        header2_title = Label(top_frame, 
            text='Login Page', 
            font=('arial', 30, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # first name
        lab_username = Label(bottom_frame, 
          text='Username: ', 
          padx=2, 
          pady=2, 
          font=('arial', 16), 
          fg='grey', 
          bg=white_color)
        lab_username.grid(row=0, column=0, sticky='w', pady=10)
        entry_username = Entry(bottom_frame, 
          bg='white', 
          width=20, 
          font=('arial',16), 
          bd=2, 
          textvariable=lg_username)
        entry_username.grid(row=0, column=1, pady=10) 

        # password
        lab_password = Label(bottom_frame, 
          text='Password: ', 
          padx=2,
          pady=2, 
          font=('arial',16), 
          fg='grey', 
          bg=white_color)
        lab_password.grid(row=1, column=0, sticky='w', pady=10)
        entry_password = Entry(bottom_frame, 
          bg='white', 
          width=20, 
          font=('arial',16), 
          bd=2, 
          show="*",
          textvariable=lg_password)
        entry_password.grid(row=1, column=1, pady=10)

        # designation
        lab_designation = Label(bottom_frame, 
          text='Designation: ', 
          padx=2, 
          pady=2, 
          font=('arial',16), 
          fg='grey', 
          bg=white_color)
        lab_designation.grid(row=2, column=0, sticky='w', pady=10)
        entry_designation = ttk.Combobox(bottom_frame, 
          width=19, 
          font=('arial',16), 
          state='readonly', 
          textvariable=lg_designation)
        entry_designation['values'] = ('admin', 'staff')
        entry_designation.grid(row=2, column=1, pady=10) 

        # btn frame
        btn_frame = Frame(bottom_frame, padx=10, pady=2, relief='flat', bg=white_color)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky='e')

        # login btn
        add_btn = Button(btn_frame, 
            text='Login', 
            bg='gray',
            fg='white', 
            relief='flat',
            width=10, 
            height=1, 
            font=('arial',12, 'bold'), 
            bd=2,
            pady=4,  
            activeforeground='white',
            activebackground='#4b8598',
            command=get_login)
        add_btn.grid(row=0, column=0, pady=10, padx=4)

        # exit btn
        exit_app_btn = Button(btn_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            relief='flat',
            width=10, 
            height=1, 
            font=('arial',12, 'bold'), 
            bd=2,
            pady=4, 
            activeforeground='white',
            activebackground='#4b8598',
            command=self.exit_app)
        exit_app_btn.grid(row=0, column=1, pady=10, padx=4)



class StaffHomePageView(object):

    def get_customer_page(self):
        self.newWindow = Toplevel()
        self.app = CustomerPageView(self.newWindow)

    def get_booking_page(self):
        self.newWindow = Toplevel()
        self.app = BookingPageView(self.newWindow)

    def get_order_page(self):
        self.newWindow = Toplevel()
        self.app = OrderPageView(self.newWindow) 

    def about_message(self):
        msg = """
        Owner: SHALELE PLACE\n
        App Type: Hotel Management System\n
        Built Date: September 2021\n
        Vesion: 1.0\n
        Developer: Denamse Angono Derkos Tirel\n
        Email: tirelangono@gmail.com\n"""
        messagebox.showinfo("About System", msg)


    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry('1350x700+0+0')
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.state('zoomed')

        def back_page_view():
            root.withdraw()
            newWindow = Toplevel()
            app = LoginPageView(newWindow)

        # =======================frames==========================
        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=5)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        middle_frame = LabelFrame(self.root, padx=5, pady=2, bg=bg2_color, height=30, width=1600)
        middle_frame.pack(pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, pady=20, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=50)

        # labels headers
        header1_title = Label(top_frame, 
            text='SHALELE PLACE', 
            font=('arial', 35, 'bold'),
            fg=title_color, 
            bg=bg1_color)
        header1_title.pack(side=TOP)
        header2_title = Label(top_frame, 
            text='Hospitality & Investment Ltd', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()
        header3_title = Label(top_frame, 
            text='No. 12 Kano Road, Beside Federal Goverment Secretarial. Kastsina.', 
            font=('arial', 12,), 
            fg=green_color, 
            bg=bg1_color)
        header3_title.pack()

        about_btn = Button(middle_frame, 
            text="About",  
            bg='grey',  
            fg='white',
            relief='flat',
            width=14,
            bd=1,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14),
            command=self.about_message)
        about_btn.grid(row=0, column=0, padx=4)

        exit_btn = Button(middle_frame, 
            text="Exit",  
            bg=chocolate_color, 
            fg=white_color,
            relief='flat',
            width=14,
            bd=1,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14),
            command=back_page_view)
        exit_btn.grid(row=0, column=1, padx=4)


        booking_btn = Button(bottom_frame,
            text='Bookings',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_booking_page)
        booking_btn.grid(row=0, column=0, pady=20, padx=30)  

        customer_btn = Button(bottom_frame,
            text='Customers',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_customer_page)
        customer_btn.grid(row=0, column=1, pady=20, padx=30)  

        order_btn = Button(bottom_frame,
            text='Orders',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_order_page)
        order_btn.grid(row=0, column=2, pady=20, padx=30) 

        def get_clock_time():
            timeVar = time.strftime("%I:%M:%S %p") 
            clock_lab.config(text=timeVar)
            clock_lab.after(100, get_clock_time)
            # time_zone = time.strftime("%Z")

        # clock time label
        clock_lab = Label(bottom_frame, 
            font=('arial', 20), 
            fg=chocolate_color, 
            bg=white_color,)
        clock_lab.grid(row=1, column=0, columnspan=3, pady=20, padx=5) 

        # date 
        today = date.today()
        date_format = today.strftime("%A - %B %d, %Y")

        date_lab = Label(bottom_frame, 
            text=date_format, 
            font=('arial', 14), 
            fg=blue_color, 
            bg=white_color)
        date_lab.grid(row=2, column=0, columnspan=3, pady=20, padx=5)


        get_clock_time()


# 
class HomePageView(object):
    def get_room_page(self):
        self.newWindow = Toplevel()
        self.app = RoomPageView(self.newWindow)

    def get_food_page(self):
        self.newWindow = Toplevel()
        self.app = FoodPageView(self.newWindow)

    def get_drink_page(self):
        self.newWindow = Toplevel()
        self.app = DrinkPageView(self.newWindow)

    def get_customer_page(self):
        self.newWindow = Toplevel()
        self.app = CustomerPageView(self.newWindow)

    def get_booking_page(self):
        self.newWindow = Toplevel()
        self.app = BookingPageView(self.newWindow)

    def get_order_page(self):
        self.newWindow = Toplevel()
        self.app = OrderPageView(self.newWindow)

    def get_booking_activity(self):
        self.newWindow = Toplevel()
        self.app = BookingActivityView(self.newWindow)

    def get_food_activity(self):
        self.newWindow = Toplevel()
        self.app = FoodActivityView(self.newWindow)

    def get_drink_activity(self):
        self.newWindow = Toplevel()
        self.app = DrinkActivityView(self.newWindow)

    def get_daily_income(self):
        self.newWindow = Toplevel()
        self.app = DailyIncomePageView(self.newWindow) 

    def get_account_page(self):
        self.newWindow = Toplevel()
        self.app = AccountPageView(self.newWindow)

    def get_inventory_page(self):
        self.newWindow = Toplevel()
        self.app = InventoryPageView(self.newWindow)

    def get_login_history_page(self):
        self.newWindow = Toplevel()
        self.app = LoginHistoryPage(self.newWindow)

    def about_message(self):
        msg = """
        Owner: SHALELE PLACE\n
        App Type: Hotel Management System\n
        Built Date: September 2021\n
        Vesion: 1.0\n
        Developer: Denamse Angono Derkos Tirel\n
        Email: tirelangono@gmail.com\n"""
        messagebox.showinfo("About System", msg)


    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry('1350x700+0+0')
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.state('zoomed')

        def back_page():
            root.withdraw()
            newWindow = Toplevel()
            app = LoginPageView(newWindow)


        # =======================frames==========================
        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=5)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        middle_frame = LabelFrame(self.root, padx=5, pady=2, bg=bg2_color, height=30, width=1600)
        middle_frame.pack(pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, pady=20, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header1_title = Label(top_frame, 
            text='SHALELE PLACE', 
            font=('arial', 35, 'bold'), 
            fg=title_color, 
            bg=bg1_color)
        header1_title.pack(side=TOP)
        header2_title = Label(top_frame, 
            text='Hospitality & Investment Ltd', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()
        header3_title = Label(top_frame, 
            text='No. 12 Kano Road, Beside Federal Goverment Secretarial. Kastsina.', 
            font=('arial', 12,), 
            fg=green_color, 
            bg=bg1_color)
        header3_title.pack()

        inventory_btn = Button(middle_frame, 
            text="Inventory",  
            bg='grey', 
            fg='white',
            relief='flat',
            width=12,
            bd=1,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14),
            command=self.get_inventory_page)
        inventory_btn.grid(row=0, column=0, padx=4)

        user_btn = Button(middle_frame, 
            text="Account",  
            bg=blue_color, 
            fg=white_color,
            relief='flat',
            width=14,
            bd=1,
            activeforeground=white_color,
            activebackground=chocolate_color,
            font=('arial',14),
            command=self.get_account_page)
        user_btn.grid(row=0, column=1, padx=4)

        income_summary_btn = Button(middle_frame, 
            text="Daily Income", 
            bg='#076',
            fg=white_color,
            relief='flat', 
            width=14, 
            bd=1, 
            activeforeground=white_color,
            activebackground='#4b8598',
            font=('arial',14),
            command=self.get_daily_income)
        income_summary_btn.grid(row=0, column=2, padx=4)

        bk_activity_btn = Button(middle_frame, 
            text="Bookings History",  
            bg='#076',
            fg=white_color,
            relief='flat', 
            width=14, 
            bd=1, 
            activeforeground=white_color,
            activebackground='#4b8598',
            font=('arial',14),
            command=self.get_booking_activity)
        bk_activity_btn.grid(row=0, column=3, padx=4)

        fd_activity_btn = Button(middle_frame, 
            text="Foods History",  
            bg='#076',
            fg=white_color,
            relief='flat', 
            width=14, 
            bd=1, 
            activeforeground=white_color,
            activebackground='#4b8598',
            font=('arial',14),
            command=self.get_food_activity)
        fd_activity_btn.grid(row=0, column=4, padx=4)

        dk_activity_btn = Button(middle_frame, 
            text="Drinks History",  
            bg='#076',
            fg=white_color, 
            relief='flat',
            width=14, 
            bd=1, 
            activeforeground=white_color,
            activebackground='#4b8598',
            font=('arial',14),
            command=self.get_drink_activity)
        dk_activity_btn.grid(row=0, column=5, padx=4)

        login_history_btn = Button(middle_frame, 
            text="Login History",  
            bg=blue_color, 
            fg=white_color,
            relief='flat',
            width=14,
            bd=1,
            activeforeground=white_color,
            activebackground=chocolate_color,
            font=('arial',14),
            command=self.get_login_history_page)
        login_history_btn.grid(row=0, column=6, padx=4)

        about_btn = Button(middle_frame, 
            text="About",  
            bg='grey', 
            fg='white',
            relief='flat',
            width=12,
            bd=1,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14),
            command=self.about_message)
        about_btn.grid(row=0, column=7, padx=4)

        # exit button from admin side
        exit_btn = Button(self.root, 
            text="Exit", 
            bg=chocolate_color, 
            fg=white_color,
            relief='flat',
            width=12,
            bd=1,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14),
            command=back_page)
        exit_btn.place(x=613, y=600)


        room_btn = Button(bottom_frame,
            text='Rooms',
            width=20,
            height=6,
            bg='grey', 
            fg='white',
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14),
            command=self.get_room_page)
        room_btn.grid(row=0, column=0, pady=20, padx=30) 

        food_btn = Button(bottom_frame,
            text='Foods',
            width=20,
            height=6,
            bg='grey', 
            fg='white',
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_food_page)
        food_btn.grid(row=0, column=1, pady=20, padx=30)

        drinking_btn = Button(bottom_frame,
            text='Drinks',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground='white',
            activebackground='#4b8598',
            font=('arial',14), 
            command=self.get_drink_page)
        drinking_btn.grid(row=0, column=2, pady=20, padx=30) 

        booking_btn = Button(bottom_frame,
            text='Bookings',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_booking_page)
        booking_btn.grid(row=1, column=0, pady=20, padx=30)  

        customer_btn = Button(bottom_frame,
            text='Customers',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_customer_page)
        customer_btn.grid(row=1, column=1, pady=20, padx=30)  

        order_btn = Button(bottom_frame,
            text='Orders',
            width=20,
            height=6,
            bg=grey_color, 
            fg=white_color,
            activeforeground=white_color,
            activebackground=blue_color,
            font=('arial',14), 
            command=self.get_order_page)
        order_btn.grid(row=1, column=2, pady=20, padx=30) 




class DailyIncomePageView(object):
    """docstring for DailyIncomePageView"""
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("600x240+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, relief='flat', padx=5, bg=white_color, width=1600)
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Daily Income Details', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=10, 
            relief='flat',
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        def get_booking_income():
            for row in db.daily_booking():
                print(row)
                booking_income.config(text=f'Daily Bookings Income: ${row}')

        def get_food_income():
            for row in db.daily_food_order():
                print(row)
                food_income.config(text=f'Daily Foods Income: ${row}')

        def get_drink_income():
            for row in db.daily_drink_order():
                print(row)
                drink_income.config(text=f'Daily Drinks Income: ${row}')

        # mobile
        booking_income = Label(bottom_frame, 
            padx=2, 
            pady=2, 
            font=('arial', 16), 
            fg='grey', 
            bg=white_color)
        booking_income.grid(row=1, column=0, sticky='w', pady=10)
        get_booking_income()


        food_income = Label(bottom_frame, 
            padx=2, 
            pady=2, 
            font=('arial', 16), 
            fg='grey', 
            bg=white_color)
        food_income.grid(row=2, column=0, sticky='w', pady=10)
        get_food_income()

        drink_income = Label(bottom_frame, 
            padx=2, 
            pady=2, 
            font=('arial', 16), 
            fg='grey', 
            bg=white_color)
        drink_income.grid(row=3, column=0, sticky='w', pady=10)
        get_drink_income()




# new page  
class AccountPageView(object):
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("850x360+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        username = StringVar()
        mobile = StringVar()
        dob = StringVar()
        password = StringVar()
        designation = StringVar()


        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            username.set(row[1])
            mobile.set(row[2])
            dob.set(row[3])
            password.set(row[4])
            designation.set(row[5])

        def add_account_data():
            if entry_username.get()=="" or entry_mobile.get()=="" or entry_dob.get()=="" or entry_password.get()=="" or entry_designation.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return 
            db.insert_account(entry_username.get(), entry_mobile.get(), entry_dob.get(), entry_password.get(), entry_designation.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved", parent=root)
            clearAll() 
            displayAll()

        def update_account_data():
            if entry_username.get()=="" or entry_mobile.get()=="" or entry_dob.get()=="" or entry_password.get()=="" or entry_designation.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return 
            db.update_account(row[0], entry_username.get(), entry_mobile.get(), entry_dob.get(), entry_password.get(), entry_designation.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated", parent=root)
            clearAll() 
            displayAll()

        def delete_account_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
            db.remove_account(row[0])
            clearAll() 
            displayAll()

        def clearAll():
            username.set('')
            mobile.set('')
            dob.set('')
            password.set('')
            designation.set('')
            displayAll() 

        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_account():
                tv.insert("", END, values=row)

        def search_account_data():
            tv.delete(*tv.get_children()) 
            if entry_username.get() or entry_mobile.get() or entry_dob.get() or entry_password.get() or entry_designation.get():
                for row in db.search_account(entry_username.get(), entry_mobile.get(), entry_dob.get(), entry_password.get(), entry_designation.get(),):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","No Such Information Found", parent=root)
                displayAll() 


        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Account Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()


        # rooms items
        items_fields_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        items_fields_frame.pack(side='left', pady=1, fill='y', expand='false')

        # rooms items
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=24, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Username", 
            "Mobile",
            "D.O.B", 
            "Password",  
            "Designation")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Username", width=200, anchor='center')
        tv.column("Mobile", width=200, anchor='center')
        tv.column("D.O.B", width=200, anchor='center')
        tv.column("Password", width=200, anchor='center')
        tv.column("Designation", width=200, anchor='center')

        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('Username', text="Username",)
        tv.heading('Mobile', text="Mobile",)
        tv.heading('D.O.B', text="D.O.B",)
        tv.heading('Password', text="Password",)
        tv.heading('Designation', text="Designation",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 
        for record in db.fetch_account():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('oddrow',))
              # increment counter 
            count +=1


        # add staff label
        txt_title = Label(items_fields_frame, 
          text='Add New Account', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # username
        lab_username = Label(items_fields_frame, 
          text='Username: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_username.grid(row=1, column=0,sticky='w')
        entry_username = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=username)
        entry_username.grid(row=1, column=1) 

        # mobile
        lab_mobile = Label(items_fields_frame, 
          text='Mobile: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_mobile.grid(row=2, column=0, sticky='w')
        entry_mobile = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=mobile)
        entry_mobile.grid(row=2, column=1)  

        # dob
        lab_dob = Label(items_fields_frame, 
          text='D.O.B (dd/mm/yyyy): ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_dob.grid(row=3, column=0,sticky='w')
        entry_dob = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=dob)
        entry_dob.grid(row=3, column=1) 

        # password
        lab_password = Label(items_fields_frame, 
          text='Password: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_password.grid(row=4, column=0, sticky='w')
        entry_password = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=password)
        entry_password.grid(row=4, column=1)  

        # designation
        lab_designation = Label(items_fields_frame, 
          text='Designation: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_designation.grid(row=5, column=0, sticky='w')
        entry_designation = ttk.Combobox(items_fields_frame, 
          width=19, 
          font=('arial',14), 
          state='readonly', 
          textvariable=designation)
        entry_designation['values'] = ('admin', 'staff')
        entry_designation.grid(row=5, column=1) 

        # btn frame
        btn_frame = Frame(items_fields_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white',
          relief='flat', 
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_account_data)
        add_btn.grid(row=0, column=0, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_account_data)
        update_btn.grid(row=0, column=1, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clearAll)
        clear_btn.grid(row=0, column=2, pady=5, padx=1)

        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_account_data)
        delete_btn.grid(row=0, column=3, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_account_data)
        search_btn.grid(row=0, column=4, pady=5, padx=1)      

        # exit btn
        exit_btn = Button(btn_frame, 
          text='Exit', 
          bg='#72404d', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=root.destroy)
        exit_btn.grid(row=0, column=5, pady=5, padx=1)      



class DrinkActivityView(object):
    """docstring for FoodActivityView"""
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("1000x400+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        drink_name = StringVar()
        quantity = StringVar()
        total_cost = StringVar()
        created_date = StringVar()
        created_time = StringVar()
        
        global row

        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            drink_name.set(row[1])
            quantity.set(row[2])
            total_cost.set(row[3])
            created_date.set(row[4])
            created_time.set(row[5])


        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_drink_activity():
                tv.insert("", END, values=row)

        def get_activity_search():
            tv.delete(*tv.get_children()) 
            if  entry_drink_type.get() or entry_quantity.get() or entry_total_cost.get() or entry_created_date.get() or entry_created_time.get(): 
                for row in db.search_drink_activity(entry_drink_type.get(), entry_quantity.get(), entry_total_cost.get(), entry_created_date.get(), entry_created_time.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()

        def get_delete_activity():
            if row:
                messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
                db.remove_drink_activity(row[0])
            get_clearAll()
            displayAll()

        def get_delete_all_activity():
            messagebox.showinfo("Delete All", "Are you sure you want to delete all these data?", parent=root)
            db.remove_all_drink_activity()
            get_clearAll()
            displayAll()

        def get_clearAll():
            drink_name.set('')
            quantity.set('')
            total_cost.set('')
            created_date.set('')
            created_time.set('')
            displayAll()

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Drinks History Details', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=6, 
            relief='flat',
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        # items frame
        booking_fields = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        booking_fields.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack(pady=5)

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=34, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Drink Name",
            "Quantity",
            "Total Cost",
            "Created Date",
            "Created Time")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Drink Name", width=200, anchor='center')
        tv.column("Quantity", width=100, anchor='center')
        tv.column("Total Cost", width=200, anchor='center')
        tv.column("Created Date", width=250, anchor='center')
        tv.column("Created Time", width=250, anchor='center')
        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('Drink Name', text="Drink Name",)
        tv.heading('Quantity', text="Quantity",)
        tv.heading('Total Cost', text="Total Cost",)
        tv.heading('Created Date', text="Created Date",)
        tv.heading('Created Time', text="Created Time",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')
        

        # add staff label
        txt_title = Label(booking_fields, 
          text='Search Drinks History', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        def get_sum_items():
            for row in db.sum_drink_activity():
                print(row)
                sum_items.config(text=f'${row}')

        sum_items = Label(booking_fields,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        sum_items.place(x=270, y=10)
        
        get_sum_items()

        # mobile
        lab_drink_type = Label(booking_fields, 
          text='Drink Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_drink_type.grid(row=1, column=0, sticky='w')
        entry_drink_type = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=drink_name)
        entry_drink_type.grid(row=1, column=1) 

        # quantity
        lab_quantity = Label(booking_fields, 
          text='Quantity: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_quantity.grid(row=2, column=0, sticky='w')
        entry_quantity = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          state='normal', 
          textvariable=quantity)
        entry_quantity.grid(row=2, column=1)  
        
        # total_cost
        lab_total_cost = Label(booking_fields, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_total_cost.grid(row=3, column=0, sticky='w')
        entry_total_cost = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=total_cost)
        entry_total_cost.grid(row=3, column=1)

        # created_date
        lab_created_date = Label(booking_fields, 
          text='Created Date: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_created_date.grid(row=4, column=0, sticky='w')
        entry_created_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=created_date)
        entry_created_date.grid(row=4, column=1)

        # created_time
        lab_created_time = Label(booking_fields, 
          text='Created Time: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_created_time.grid(row=5, column=0, sticky='w')
        entry_created_time = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=created_time)
        entry_created_time.grid(row=5, column=1)

        # btn frame
        btn_frame = Frame(booking_fields, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=10, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=get_activity_search)
        search_btn.grid(row=0, column=0, pady=5, padx=1)   
        
        # clear_btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          width=10, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_clearAll)
        clear_btn.grid(row=0, column=1, pady=5, padx=1)

        # delete_one_btn
        delete_one_btn = Button(btn_frame, 
          text='Delete One', 
          bg='gray', 
          fg='white',
          width=10, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_delete_activity)
        delete_one_btn.grid(row=0, column=2, pady=5, padx=1)   

        # delete btn
        delete_all_btn = Button(btn_frame, 
          text='Delete All', 
          bg='red', 
          relief='flat',
          fg='white',
          width=10, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=get_delete_all_activity)
        delete_all_btn.grid(row=0, column=3, pady=5, padx=1)       
        
        displayAll()



# food activity
class FoodActivityView(object):
    """docstring for FoodActivityView"""
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("1000x400+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)
        

        food_name = StringVar()
        quantity = StringVar()
        total_cost = StringVar()
        created_date = StringVar()
        created_time = StringVar()
        
        global row

        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            food_name.set(row[1])
            quantity.set(row[2])
            total_cost.set(row[3])
            created_date.set(row[4])
            created_time.set(row[5])


        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_food_activity():
                tv.insert("", END, values=row)

        def get_activity_search():
            tv.delete(*tv.get_children()) 
            if  entry_food_type.get() or entry_quantity.get() or entry_total_cost.get() or entry_created_date.get() or entry_created_time.get(): 
                for row in db.search_food_activity(entry_food_type.get(), entry_quantity.get(), entry_total_cost.get(), entry_created_date.get(), entry_created_time.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()

        def get_delete_activity():
            if row:
                messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
                db.remove_food_activity(row[0])
            get_clearAll()
            displayAll()

        def get_delete_all_activity():
            messagebox.showinfo("Delete All", "Are you sure you want to delete all these data?", parent=root)
            db.remove_all_food_activity()
            get_clearAll()
            displayAll()

        def get_clearAll():
            food_name.set('')
            quantity.set('')
            total_cost.set('')
            created_date.set('')
            created_time.set('')
            displayAll()

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Foods History Details', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=6, 
            height=1, 
            relief='flat',
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        # items frame
        booking_fields = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        booking_fields.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack(pady=5)

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=34, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Food Name",
            "Quantity",
            "Total Cost",
            "Created Date",
            "Created Time")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Food Name", width=200, anchor='center')
        tv.column("Quantity", width=100, anchor='center')
        tv.column("Total Cost", width=200, anchor='center')
        tv.column("Created Date", width=250, anchor='center')
        tv.column("Created Time", width=250, anchor='center')
        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('Food Name', text="Food Name",)
        tv.heading('Quantity', text="Quantity",)
        tv.heading('Total Cost', text="Total Cost",)
        tv.heading('Created Date', text="Created Date",)
        tv.heading('Created Time', text="Created Time",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')
        

        # add staff label
        txt_title = Label(booking_fields, 
          text='Search Foods History', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        def get_sum_items():
            for row in db.sum_food_activity():
                print(row)
                sum_items.config(text=f'${row}')

        sum_items = Label(booking_fields,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        sum_items.place(x=270, y=10)
        
        get_sum_items()

        # mobile
        lab_food_type = Label(booking_fields, 
          text='Food Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_food_type.grid(row=1, column=0, sticky='w')
        entry_food_type = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=food_name)
        entry_food_type.grid(row=1, column=1) 

        # quantity
        lab_quantity = Label(booking_fields, 
          text='Quantity: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_quantity.grid(row=2, column=0, sticky='w')
        entry_quantity = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          state='normal', 
          textvariable=quantity)
        entry_quantity.grid(row=2, column=1)  
        
        # total_cost
        lab_total_cost = Label(booking_fields, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_total_cost.grid(row=3, column=0, sticky='w')
        entry_total_cost = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=total_cost)
        entry_total_cost.grid(row=3, column=1)

        # created_date
        lab_created_date = Label(booking_fields, 
          text='Created Date: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_created_date.grid(row=4, column=0, sticky='w')
        entry_created_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=created_date)
        entry_created_date.grid(row=4, column=1)

        # created_time
        lab_created_time = Label(booking_fields, 
          text='Created Time: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_created_time.grid(row=5, column=0, sticky='w')
        entry_created_time = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=created_time)
        entry_created_time.grid(row=5, column=1)

        # btn frame
        btn_frame = Frame(booking_fields, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=10, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=get_activity_search)
        search_btn.grid(row=0, column=0, pady=5, padx=1)   
        
        # clear_btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=10, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_clearAll)
        clear_btn.grid(row=0, column=1, pady=5, padx=1)

        # delete_one_btn
        delete_one_btn = Button(btn_frame, 
          text='Delete One', 
          bg='gray', 
          fg='white',
          width=10, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_delete_activity)
        delete_one_btn.grid(row=0, column=2, pady=5, padx=1)   

        # delete btn
        delete_all_btn = Button(btn_frame, 
          text='Delete All', 
          bg='red', 
          fg='white',
          relief='flat',
          width=10, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=get_delete_all_activity)
        delete_all_btn.grid(row=0, column=3, pady=5, padx=1)       

        displayAll()

        
class BookingActivityView(object):
    """docstring for BookingActivityView"""
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("1200x480+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)
        
        mobile = StringVar()
        room_number = StringVar()
        room_price = StringVar() 
        check_in_date = StringVar()
        check_out_date = StringVar()
        discount = StringVar() 
        total_cost = StringVar()
        created_date = StringVar()
        created_time = StringVar()

        bill_ref = StringVar()
        search_info = StringVar()
        
        global row

        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            mobile.set(row[1])
            room_number.set(row[2])
            room_price.set(row[3])
            check_in_date.set(row[4])
            check_out_date.set(row[5])
            discount.set(row[6])
            total_cost.set(row[7])
            created_date.set(row[8])
            created_time.set(row[9])

        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_booking_activity():
                tv.insert("", END, values=row)

        def get_activity_search():
            tv.delete(*tv.get_children()) 
            if  entry_mobile.get() or entry_room_number.get() or entry_room_price.get() or entry_check_in_date.get() or entry_check_out_date.get() or entry_total_cost.get() or entry_created_date.get() or entry_created_time.get(): 
                for row in db.search_booking_activity(entry_mobile.get(), entry_room_number.get(), entry_room_price.get(), entry_check_in_date.get(), entry_check_out_date.get(), entry_total_cost.get(), entry_created_date.get(), entry_created_time.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()

        def get_delete_activity():
            if row:
                messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
                db.remove_booking_activity(row[0])
            get_clearAll()
            displayAll()

        def get_delete_all_activity():
            messagebox.showinfo("Delete All", "Are you sure you want to delete all these data?", parent=root)
            db.remove_all_booking_activity()
            get_clearAll()
            displayAll()

        def get_clearAll():
            mobile.set('')
            room_number.set('')
            room_price.set('')
            check_in_date.set('')
            check_out_date.set('')
            discount.set('')
            total_cost.set('')
            created_date.set('')
            created_time.set('')
            displayAll()

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Bookings History Details', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=6, 
            relief='flat',
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        # items frame
        booking_fields = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        booking_fields.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')


        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack(pady=5)

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=34, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6,7,8,9,10))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Mobile",
            "Room Number",
            "Room Price",
            "Check In Date",
            "Check Out Date",
            "Discount (%)",
            "Total Cost",
            "Created Date",
            "Created Time")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Mobile", width=200, anchor='center')
        tv.column("Room Number", width=100, anchor='center')
        tv.column("Room Price", width=200, anchor='center')
        tv.column("Check In Date", width=200, anchor='center')
        tv.column("Check Out Date", width=200, anchor='center')
        tv.column("Discount (%)", width=100, anchor='center')
        tv.column("Total Cost", width=200, anchor='center')
        tv.column("Created Date", width=250, anchor='center')
        tv.column("Created Time", width=250, anchor='center')
        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('Mobile', text="Mobile",)
        tv.heading('Room Number', text="Room Number",)
        tv.heading('Room Price', text="Room Price",)
        tv.heading('Check In Date', text="Check In Date",)
        tv.heading('Check Out Date', text="Check Out Date",)
        tv.heading('Discount (%)', text="Discount (%)",)
        tv.heading('Total Cost', text="Total Cost",)
        tv.heading('Created Date', text="Created Date",)
        tv.heading('Created Time', text="Created Time",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')
        

        # add staff label
        txt_title = Label(booking_fields, 
          text='Search Booking History', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w') 

        def get_sum_items():
            for row in db.sum_booking_activity():
                print(row)
                sum_items.config(text=f'${row}')

        sum_items = Label(booking_fields,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        sum_items.place(x=270, y=10)
        
        get_sum_items()

        # mobile
        lab_mobile = Label(booking_fields, 
          text='Mobile: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_mobile.grid(row=1, column=0, sticky='w')
        entry_mobile = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=mobile)
        entry_mobile.grid(row=1, column=1) 

        # room_number
        lab_room_number = Label(booking_fields, 
          text='Room Number: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_room_number.grid(row=2, column=0, sticky='w')
        entry_room_number = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          state='normal', 
          textvariable=room_number)
        entry_room_number.grid(row=2, column=1)  

        # room_amount
        lab_room_price = Label(booking_fields, 
          text='Room Price: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_room_price.grid(row=3, column=0, sticky='w')
        entry_room_price = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=room_price)
        entry_room_price.grid(row=3, column=1)  

        # check_in_date
        lab_check_in_date = Label(booking_fields, 
          text='Check in (dd/mm/yyyy): ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_check_in_date.grid(row=4, column=0, sticky='w')
        entry_check_in_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          state='normal',
          textvariable=check_in_date)
        entry_check_in_date.grid(row=4, column=1) 

        # check_out_date
        lab_check_out_date = Label(booking_fields, 
          text='Check out (dd/mm/yyyy): ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_check_out_date.grid(row=5, column=0, sticky='w')
        entry_check_out_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=check_out_date)
        entry_check_out_date.grid(row=5, column=1) 

        # discount
        lab_discount = Label(booking_fields, 
          text='Discount (%): ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_discount.grid(row=6, column=0, sticky='w')
        entry_discount = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=discount)
        entry_discount.grid(row=6, column=1)

        # total_cost
        lab_total_cost = Label(booking_fields, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_total_cost.grid(row=7, column=0, sticky='w')
        entry_total_cost = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=total_cost)
        entry_total_cost.grid(row=7, column=1)

        # created_date
        lab_created_date = Label(booking_fields, 
          text='Created Date: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_created_date.grid(row=8, column=0, sticky='w')
        entry_created_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=created_date)
        entry_created_date.grid(row=8, column=1)

        # created_time
        lab_created_time = Label(booking_fields, 
          text='Created Time: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_created_time.grid(row=9, column=0, sticky='w')
        entry_created_time = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=created_time)
        entry_created_time.grid(row=9, column=1)

        # btn frame
        btn_frame = Frame(booking_fields, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=10, column=0, columnspan=2, pady=20)

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=10, 
          height=1, 
          relief='flat',
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=get_activity_search)
        search_btn.grid(row=0, column=0, pady=5, padx=1)   
        
        # clear_btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=10, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_clearAll)
        clear_btn.grid(row=0, column=1, pady=5, padx=1)

        # delete_one_btn
        delete_one_btn = Button(btn_frame, 
          text='Delete One', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=10, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_delete_activity)
        delete_one_btn.grid(row=0, column=2, pady=5, padx=1)   

        # delete btn
        delete_all_btn = Button(btn_frame, 
          text='Delete All', 
          bg='red', 
          fg='white',
          width=10, 
          height=1,
          relief='flat',
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=get_delete_all_activity)
        delete_all_btn.grid(row=0, column=3, pady=5, padx=1)       
        

        displayAll()




# new page  
class RoomPageView(object):
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("850x340+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        room_number = StringVar()
        room_type = StringVar()
        room_price = StringVar()


        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            room_number.set(row[1])
            room_type.set(row[2])
            room_price.set(row[3])

        def add_room_data():
            if entry_room_number.get()=="" or entry_room_type.get()=="" or entry_room_price.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return 
            db.insert_room(entry_room_number.get(), entry_room_type.get(), entry_room_price.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved", parent=root)
            clearAll() 
            displayAll()

        def update_room_data():
            if entry_room_number.get()=="" or entry_room_type.get()=="" or entry_room_price.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return 
            db.update_room(row[0], entry_room_number.get(), entry_room_type.get(), entry_room_price.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated", parent=root)
            clearAll() 
            displayAll()

        def delete_room_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
            db.remove_room(row[0])
            clearAll() 
            displayAll()

        def clearAll():
            room_number.set('')
            room_type.set('')
            room_price.set('')
            displayAll() 

        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_room():
                tv.insert("", END, values=row)

        def search_room_data():
            tv.delete(*tv.get_children()) 
            if entry_room_number.get() or entry_room_type.get() or entry_room_price.get():
                for row in db.search_room(entry_room_number.get(), entry_room_type.get(), entry_room_price.get(),):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","No Such Information Found", parent=root)
                displayAll() 


        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Rooms Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        def get_count():
            for row in db.count_rooms():
                print(row)
                count_items.config(text=f'Rooms: {row}')

        count_items = Label(top_frame,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        count_items.place(x=20, y=5)

        get_count()

        # rooms items
        items_fields_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        items_fields_frame.pack(side='left', pady=1, fill='y', expand='false')

        # rooms items
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=22, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Room Number", 
            "Room Type", 
            "Room Price")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Room Number", width=160, anchor='center')
        tv.column("Room Type", width=200, anchor='center')
        tv.column("Room Price", width=200, anchor='center')

        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('Room Number', text="Room No",)
        tv.heading('Room Type', text="Room Type",)
        tv.heading('Room Price', text="Room Price",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 
        for record in db.fetch_room():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3]), tags=('oddrow',))
              # increment counter 
            count +=1


        # add staff label
        txt_title = Label(items_fields_frame, 
          text='Add New Room', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # room number
        lab_room_number = Label(items_fields_frame, 
          text='Room No: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_room_number.grid(row=1, column=0,sticky='w')
        entry_room_number = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=room_number)
        entry_room_number.grid(row=1, column=1) 

        # room type
        lab_room_type = Label(items_fields_frame, 
          text='Room Type: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_room_type.grid(row=2, column=0, sticky='w')
        entry_room_type = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=room_type)
        entry_room_type.grid(row=2, column=1) 

        # room price
        lab_room_price = Label(items_fields_frame, 
          text='Room Price: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_room_price.grid(row=3, column=0, sticky='w')
        entry_room_price = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=room_price)
        entry_room_price.grid(row=3, column=1) 

        # btn frame
        btn_frame = Frame(items_fields_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white', 
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_room_data)
        add_btn.grid(row=0, column=0, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_room_data)
        update_btn.grid(row=0, column=1, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clearAll)
        clear_btn.grid(row=0, column=2, pady=5, padx=1)

        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_room_data)
        delete_btn.grid(row=0, column=3, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_room_data)
        search_btn.grid(row=0, column=4, pady=5, padx=1)      

        # exit btn
        exit_btn = Button(btn_frame, 
          text='Exit', 
          bg='#72404d', 
          fg='white',
          width=6, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=root.destroy)
        exit_btn.grid(row=0, column=5, pady=5, padx=1)      



# new page  
class FoodPageView(object):
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("750x300+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        food_name = StringVar()
        unit_cost = StringVar()

        def getFoodData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            food_name.set(row[1])
            unit_cost.set(row[2])

        def add_food_data():
            if entry_food_type.get()=="" or entry_unit_cost.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.insert_food(entry_food_type.get(), entry_unit_cost.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved",parent=root)
            clear_food_All() 
            display_food_All()

        def update_food_data():
            if entry_food_type.get()=="" or entry_unit_cost.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.update_food(row[0], entry_food_type.get(), entry_unit_cost.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated",parent=root)
            clear_food_All() 
            display_food_All()

        def delete_food_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?",parent=root)
            db.remove_food(row[0])
            clear_food_All() 
            display_food_All()

        def clear_food_All():
            food_name.set('')
            unit_cost.set('')
            display_food_All()

        def display_food_All():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_food():
                tv.insert("", END, values=row)

        def search_food_data():
            tv.delete(*tv.get_children()) 
            if entry_food_type.get() or entry_unit_cost.get():
                for row in db.search_food(entry_food_type.get(), entry_unit_cost.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","No Such Information Found", parent=root)
                display_food_All()


        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Food Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        def get_count():
            for row in db.count_foods():
                print(row)
                count_items.config(text=f'Foods: {row}')

        count_items = Label(top_frame,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        count_items.place(x=20, y=5)
        
        get_count()

        # rooms items
        items_fields_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        items_fields_frame.pack(side='left', pady=1, fill='y', expand='false')

        # rooms items
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')


        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=20, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Food Name", 
            "Unit Cost")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Food Name", width=150, anchor='center')
        tv.column("Unit Cost", width=150, anchor='center')

        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading("Food Name", text="Food Name",)
        tv.heading("Unit Cost", text="Unit Cost")
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getFoodData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 
        for record in db.fetch_food():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2]), tags=('oddrow',))
              # increment counter 
            count +=1

        # add staff label
        txt_title = Label(items_fields_frame, 
          text='Add New Food', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Food Name
        lab_food_type = Label(items_fields_frame, 
          text='Food Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_food_type.grid(row=1, column=0,sticky='w')
        entry_food_type = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=food_name)
        entry_food_type.grid(row=1, column=1) 

        # Unit Cost
        lab_unit_cost = Label(items_fields_frame, 
          text='Unit Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_unit_cost.grid(row=2, column=0, sticky='w')
        entry_unit_cost = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=unit_cost)
        entry_unit_cost.grid(row=2, column=1)

        # btn frame
        btn_frame = Frame(items_fields_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          relief='flat',
          fg='white', 
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_food_data)
        add_btn.grid(row=0, column=0, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          relief='flat',
          fg='white', 
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_food_data)
        update_btn.grid(row=0, column=1, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          relief='flat',
          fg='white',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clear_food_All)
        clear_btn.grid(row=0, column=2, pady=5, padx=1)

        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_food_data)
        delete_btn.grid(row=0, column=3, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_food_data)
        search_btn.grid(row=0, column=4, pady=5, padx=1)      

        # exit btn
        exit_btn = Button(btn_frame, 
          text='Exit', 
          bg='#72404d', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=root.destroy)
        exit_btn.grid(row=0, column=5, pady=5, padx=1)      




# new page
class DrinkPageView(object):
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("750x300+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        drink_name = StringVar()
        unit_cost = StringVar()

        def getDrinkData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            drink_name.set(row[1])
            unit_cost.set(row[2])

        def display_drink_All():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_drink():
                tv.insert("", END, values=row)

        def add_drink_data():
            if entry_drink_type.get()=="" or entry_unit_cost.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.insert_drink(entry_drink_type.get(), entry_unit_cost.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved",parent=root)
            clear_drink_All() 
            display_drink_All()

        def update_drink_data():
            if entry_drink_type.get()=="" or entry_unit_cost.get()=="":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.update_drink(row[0], entry_drink_type.get(), entry_unit_cost.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated",parent=root)
            clear_drink_All() 
            display_drink_All()

        def delete_drink_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?",parent=root)
            db.remove_drink(row[0])
            clear_drink_All() 
            display_drink_All()

        def clear_drink_All():
            drink_name.set('')
            unit_cost.set('')
            display_drink_All()

        def search_drink_data():
            tv.delete(*tv.get_children()) 
            if entry_drink_type.get() or entry_unit_cost.get():
                for row in db.search_drink(entry_drink_type.get(), entry_unit_cost.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","No Such Information Found",parent=root)
                display_drink_All()

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Drink Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        def get_count():
            for row in db.count_drinks():
                print(row)
                count_items.config(text=f'Drinks: {row}')

        count_items = Label(top_frame,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        count_items.place(x=20, y=5)

        get_count()

        # rooms items
        items_fields_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        items_fields_frame.pack(side='left', pady=1, fill='y', expand='false')

        # rooms items
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')


        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=20, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Drink Name", 
            "Unit Cost")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Drink Name", width=150, anchor='center')
        tv.column("Unit Cost", width=150, anchor='center')

        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading("Drink Name", text="Drink Name",)
        tv.heading("Unit Cost", text="Unit Cost")
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getDrinkData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 
        for record in db.fetch_drink():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2]), tags=('oddrow',))
              # increment counter 
            count +=1


        # add staff label
        txt_title = Label(items_fields_frame, 
          text='Add New Drink', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Food Name
        lab_drink_type = Label(items_fields_frame, 
          text='Drink Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_drink_type.grid(row=1, column=0,sticky='w')
        entry_drink_type = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=drink_name)
        entry_drink_type.grid(row=1, column=1) 

        # Unit Cost
        lab_unit_cost = Label(items_fields_frame, 
          text='Unit Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_unit_cost.grid(row=2, column=0, sticky='w')
        entry_unit_cost = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=unit_cost)
        entry_unit_cost.grid(row=2, column=1)

        # btn frame
        btn_frame = Frame(items_fields_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_drink_data)
        add_btn.grid(row=0, column=0, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_drink_data)
        update_btn.grid(row=0, column=1, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          relief='flat',
          fg='white',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clear_drink_All)
        clear_btn.grid(row=0, column=2, pady=5, padx=1)

        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          width=6, 
          height=1,
          relief='flat',
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_drink_data)
        delete_btn.grid(row=0, column=3, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=6, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_drink_data)
        search_btn.grid(row=0, column=4, pady=5, padx=1)      

        # exit btn
        exit_btn = Button(btn_frame, 
          text='Exit', 
          bg='#72404d', 
          fg='white',
          width=6, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=root.destroy)
        exit_btn.grid(row=0, column=5, pady=5, padx=1)      



# new page  
class CustomerPageView(object):
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("950x340+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        fname = StringVar()
        lname = StringVar()
        mobile = StringVar()
        email = StringVar()

        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            fname.set(row[1])
            lname.set(row[2])
            mobile.set(row[3])
            email.set(row[4])
        
        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_customer():
                tv.insert("", END, values=row)

        def add_customer_data():
            if entry_first_name.get() == "" or entry_last_name.get() == "" or entry_mobile.get() == "" or entry_email.get() == "":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.insert_customer(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_email.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved",parent=root)
            clearAll() 
            displayAll()

        def update_customer_data():
            if entry_first_name.get()=="" or entry_last_name.get() == "" or entry_mobile.get() == "" or entry_email.get() == "":
                messagebox.showerror("Error in Inputs", "No Data Found to Update",parent=root) 
                return 
            db.update_customer(row[0], entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_email.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated",parent=root)
            clearAll() 
            displayAll()

        def delete_customer_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?",parent=root)
            db.remove_customer(row[0])
            clearAll() 
            displayAll()

        def clearAll():
            fname.set('')
            lname.set('')
            mobile.set('')
            email.set('')
            displayAll()

        def search_customer_data(): 
            tv.delete(*tv.get_children()) 
            if entry_first_name.get() or entry_last_name.get() or entry_mobile.get() or entry_email.get():
                for row in db.search_customer(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_email.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Customer Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        def get_count():
            for row in db.count_customers():
                print(row)
                count_items.config(text=f'Customer: {row}')

        count_items = Label(top_frame,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        count_items.place(x=20, y=5)

        get_count()

        # items frame
        items_fields_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        items_fields_frame.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=22, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "First Name", 
            "Surname", 
            "Mobile",
            "Email")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("First Name", width=200, anchor='center')
        tv.column("Surname", width=200, anchor='center')
        tv.column("Mobile", width=180, anchor='center')
        tv.column("Email", width=250, anchor='center')

        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('First Name', text="First Name",)
        tv.heading('Surname', text="Surname",)
        tv.heading('Mobile', text="Phone no",)
        tv.heading('Email', text="Email",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 
        for record in db.fetch_customer():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('oddrow',))
              # increment counter 
            count +=1

        # add staff label
        txt_title = Label(items_fields_frame, 
          text='Add New Customer', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # fname
        lab_first_name = Label(items_fields_frame, 
          text='First Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_first_name.grid(row=1, column=0,sticky='w')
        entry_first_name = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=fname)
        entry_first_name.grid(row=1, column=1) 

        # lname
        lab_last_name = Label(items_fields_frame, 
          text='Surname: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_last_name.grid(row=2, column=0, sticky='w')
        entry_last_name = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=lname)
        entry_last_name.grid(row=2, column=1)  

        # mobile
        lab_mobile = Label(items_fields_frame, 
          text='Phone no: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_mobile.grid(row=3, column=0, sticky='w')
        entry_mobile = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=mobile)
        entry_mobile.grid(row=3, column=1) 

        # email
        lab_email = Label(items_fields_frame, 
          text='Email: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_email.grid(row=4, column=0, sticky='w')
        entry_email = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=email)
        entry_email.grid(row=4, column=1) 

        # btn frame
        btn_frame = Frame(items_fields_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white', 
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_customer_data)
        add_btn.grid(row=0, column=0, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_customer_data)
        update_btn.grid(row=0, column=1, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clearAll)
        clear_btn.grid(row=0, column=2, pady=5, padx=1)

        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          relief='flat',
          fg='white',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_customer_data)
        delete_btn.grid(row=0, column=3, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=6, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_customer_data)
        search_btn.grid(row=0, column=4, pady=5, padx=1)      

        # exit btn
        exit_btn = Button(btn_frame, 
          text='Exit', 
          bg='#72404d', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=root.destroy)
        exit_btn.grid(row=0, column=5, pady=5, padx=1)      



# new page  
class BookingPageView(object):

    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("1200x640+20+10")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        fname = StringVar()
        lname = StringVar()
        mobile = StringVar()
        room_number = StringVar()
        room_type = StringVar()
        room_price = StringVar() 
        check_in_date = StringVar()
        check_out_date = StringVar()
        discount = StringVar() 
        total_cost = StringVar()

        address = StringVar()
        email = StringVar()
        car_reg_no = StringVar()
        means_of_id = StringVar()
        traveling_from = StringVar()
        traveling_to = StringVar()
        party = StringVar()

        bill_ref = StringVar()
        search_customer_info = StringVar()

        global row 
        global textarea 

        def get_receipt_page_view():
            newWindow = Toplevel()
            newWindow.title("Shalele PLAE Hotel")
            # newWindow.geometry("600x460+100+80")
            newWindow.config(bd=0, bg=white_color, relief='flat')
            newWindow.resizable(0, 0)

            global textarea

            top_frame = LabelFrame(newWindow, relief='raised', bg=bg1_color, height=80, pady=10)
            top_frame.pack(side='top', pady=1, fill='x', expand='false')
            bottom_frame = LabelFrame(newWindow, padx=5, bg=white_color, width=1600, relief='flat')
            bottom_frame.pack(pady=1)

            # labels headers
            header2_title = Label(top_frame, 
                text='Receipt Page View', 
                font=('arial', 14, 'bold'), 
                fg=green_color, 
                bg=bg1_color)
            header2_title.pack() 


            # receipt_btn
            save_btn = Button(top_frame, 
                text='Print or Save File', 
                bg='#4b8598', 
                fg='white',
                width=14, 
                height=1, 
                font=('arial',12), 
                bd=1, 
                relief='flat',
                activeforeground='white',
                activebackground='#72404d',
                command=get_receipt_file)
            save_btn.pack(pady=5)


            scrol = Scrollbar(bottom_frame, orient='vertical')
            scrol.pack(fill='y', side='right')

            textarea = Text(bottom_frame, 
                font=('arial',12),
                state='normal',
                pady=10,
                height=20, 
                width=60)
            textarea.focus()
            textarea.pack(anchor='center',)
            scrol.config(command=textarea.yview)

            textarea.get(1.0, END)
            textarea.insert('end', f"SHALELE HOSPITALITY & INVESTMENT Ltd\n")
            textarea.insert('end', f"\nNo. 12 Kano Road, Beside Federal Secretariat. Katsina.\n")
            textarea.insert('end', '\nDate: '+str(time.strftime("%d/%m/%y")))
            textarea.insert('end', '\nBill Ref: '+str(entry_bill_ref.get())) 
            textarea.insert('end', '\n')
            if entry_first_name.get():
                textarea.insert('end', '\nFirst name: '+entry_first_name.get())
            if entry_last_name.get():
                textarea.insert('end', '\nSurname: '+entry_last_name.get())
            if entry_mobile.get():
                textarea.insert('end', '\nPhone no: '+entry_mobile.get())
            if entry_address.get():
                textarea.insert('end', '\nAddress: '+entry_address.get())
            if entry_email.get():
                textarea.insert('end', '\nEmail: '+entry_email.get())
            if entry_car_reg_no.get():
                textarea.insert('end', '\nCar Reg no: '+entry_car_reg_no.get())
            if entry_means_of_id.get():
                textarea.insert('end', '\nMeans of ID: '+entry_means_of_id.get())
            if entry_traveling_from.get():
                textarea.insert('end', '\nTraveling from: '+entry_traveling_from.get())
            if entry_traveling_to.get():
                textarea.insert('end', '\nTraveling To: '+entry_traveling_to.get())
            if entry_room_number.get():
                textarea.insert('end', '\nRoom No: '+entry_room_number.get())
            if entry_room_type.get():
                textarea.insert('end', '\nRoom Type: '+entry_room_type.get())
            if entry_room_price.get():
                textarea.insert('end', '\nRoom Price: ₦'+entry_room_price.get())
            if entry_check_in_date.get():
                textarea.insert('end', '\nDate of Arrival: '+entry_check_in_date.get())
            if entry_check_out_date.get():
                textarea.insert('end', '\nDate of Departure: '+entry_check_out_date.get())
            if entry_party.get():
                textarea.insert('end', '\nParty (No of person): '+entry_party.get())
            if entry_discount.get():
                textarea.insert('end', '\nDiscount (%): '+entry_discount.get())
            if entry_total_cost.get():
                textarea.insert('end', '\nTotal Cost: ₦'+entry_total_cost.get())
            textarea.insert('end', '\n\n')
            textarea.get(END, 1.0)


        def get_receipt_file():
            q = textarea.get("1.0", "end-1c")
            filename = tempfile.mktemp(f"{entry_last_name.get()}.doc")
            open (filename, "w", encoding="utf-8").write(q)
            os.startfile(filename, 'print')
            # Bellow is call to print text from your_widget_name textbox
            # win32api.ShellExecute(0,"print", filename, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)


        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            fname.set(row[1])
            lname.set(row[2])
            mobile.set(row[3])
            address.set(row[4])
            email.set(row[5])
            car_reg_no.set(row[6])
            means_of_id.set(row[7])
            traveling_from.set(row[8])
            traveling_to.set(row[9])
            room_number.set(row[10])
            room_type.set(row[11])
            room_price.set(row[12])
            check_in_date.set(row[13])
            check_out_date.set(row[14])
            party.set(row[15])
            discount.set(row[16])
            total_cost.set(row[17])
            bill_ref.set(row[18])


        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_booking():
                tv.insert("", END, values=row)

        options = [] 
        for item in db.get_all_available_rooms():
            if item not in db.get_occupied_booking_rooms():
                options.append(item)
            # print('Free rooms are: ', options)

        def get_rooms_detail_data(event):
            opts = entry_room_number.get()
            option_id = opts.split("-")[0]
            for x in db.get_rooms_detail(option_id):
                room_type.set(str(x[2]))
                room_price.set(x[3])

        # date 
        today = date.today()
        created_date = today.strftime("%B %d, %Y")
        created_time = str(time.strftime("%I:%M:%S %p"))

    # entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_address.get(), entry_email.get(), entry_car_reg_no.get(), entry_means_of_id.get(), entry_traveling_from.get(), entry_traveling_to.get(), entry_room_number.get(), entry_room_type.get(), entry_room_price.get(), entry_check_in_date.get(), entry_check_out_date.get(), entry_party.get(), entry_discount.get(), entry_total_cost.get()
        
        def add_booking_data():
            if entry_first_name.get()=='' or entry_last_name.get()=='' or entry_mobile.get()=='' or entry_address.get()=='' or entry_email.get()=='' or entry_means_of_id.get()=='' or entry_traveling_from.get()=='' or entry_traveling_to.get()=='' or entry_room_number.get()=='' or entry_room_type.get()=='' or entry_room_price.get()=='' or entry_check_in_date.get()=='' or entry_check_out_date.get()=='' or entry_total_cost.get()=='' or entry_bill_ref.get()=='':
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return 
            db.insert_booking(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_address.get(), entry_email.get(), entry_car_reg_no.get(), entry_means_of_id.get(), entry_traveling_from.get(), entry_traveling_to.get(), entry_room_number.get(), entry_room_type.get(), entry_room_price.get(), entry_check_in_date.get(), entry_check_out_date.get(), entry_party.get(), entry_discount.get(), entry_total_cost.get(), entry_bill_ref.get())
            db.insert_customer(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), 'NA')
            db.insert_booking_activity(entry_mobile.get(), entry_room_number.get(), entry_room_price.get(), entry_check_in_date.get(), entry_check_out_date.get(), entry_discount.get(), entry_total_cost.get(), created_date, created_time)
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved", parent=root)
            clearAll() 
            displayAll()


        def update_booking_data(): 
            if entry_first_name.get()=='' or entry_last_name.get()=='' or entry_mobile.get()=='' or entry_address.get()=='' or entry_email.get()=='' or entry_means_of_id.get()=='' or entry_traveling_from.get()=='' or entry_traveling_to.get()=='' or entry_room_number.get()=='' or entry_room_type.get()=='' or entry_room_price.get()=='' or entry_check_in_date.get()=='' or entry_check_out_date.get()=='' or entry_total_cost.get()=='' or entry_bill_ref.get()=='':
                messagebox.showerror("Error in Inputs", "No Data Found to Update",parent=root) 
                return 
            db.update_booking(row[0], entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_address.get(), entry_email.get(), entry_car_reg_no.get(), entry_means_of_id.get(), entry_traveling_from.get(), entry_traveling_to.get(), entry_room_number.get(), entry_room_type.get(), entry_room_price.get(), entry_check_in_date.get(), entry_check_out_date.get(), entry_party.get(), entry_discount.get(), entry_total_cost.get(), entry_bill_ref.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated",parent=root)
            clearAll() 
            displayAll()

        def search_booking_data():
            tv.delete(*tv.get_children()) 
            if  entry_first_name.get() or entry_last_name.get() or entry_mobile.get() or entry_address.get() or entry_email.get() or entry_car_reg_no.get() or entry_means_of_id.get() or entry_traveling_from.get() or entry_traveling_to.get() or entry_room_number.get() or entry_room_type.get() or entry_room_price.get() or entry_check_in_date.get() or entry_check_out_date.get() or entry_party.get() or entry_discount.get() or entry_total_cost.get() or entry_bill_ref.get(): 
                for row in db.search_booking(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_address.get(), entry_email.get(), entry_car_reg_no.get(), entry_means_of_id.get(), entry_traveling_from.get(), entry_traveling_to.get(), entry_room_number.get(), entry_room_type.get(), entry_room_price.get(), entry_check_in_date.get(), entry_check_out_date.get(), entry_party.get(), entry_discount.get(), entry_total_cost.get(), entry_bill_ref.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()


        def delete_booking_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
            db.remove_booking(row[0])
            clearAll() 
            displayAll()

        def clearAll():
            fname.set('')
            lname.set('')
            mobile.set('')
            address.set('')
            email.set('')
            car_reg_no.set('')
            means_of_id.set('')
            traveling_from.set('')
            traveling_to.set('')
            room_number.set('')
            room_type.set('')
            room_price.set('')
            check_in_date.set('')
            check_out_date.set('')
            party.set('')
            discount.set('')
            total_cost.set('')
            displayAll()

        def get_total_cost_data():
            try:
                # computing the total price
                inDate = entry_check_in_date.get()
                outDate = entry_check_out_date.get()
                checkin = datetime.strptime(inDate, "%d/%m/%Y")
                checkout = datetime.strptime(outDate, "%d/%m/%Y")
                days_number = (abs(checkout - checkin).days)

                room_cost = entry_room_price.get()
                total_amount = float(room_cost) * float(days_number)
                total_cost.set(total_amount) 
                # computing the discount
                discount_cost = entry_discount.get()
                total_discount_cost = (float(discount_cost) * float(total_amount))/100
                final_cost = total_amount - total_discount_cost
                total_cost.set(final_cost)
            except:
                messagebox.showinfo("Info","Nothing to calculate", parent=root)


        def get_customer_info():
            if entry_search.get() == "":
                messagebox.showerror("Error","Please Type Something", parent=root)
            else:
                row = db.search_customer_for_booking(entry_search.get(), entry_search.get(), entry_search.get(), entry_search.get()) 
                print(row)
                if row==None:
                    messagebox.showinfo("Result","Nothing Found", parent=root)
                else:
                    for x in row:
                        fname.set(x[1])
                        lname.set(x[2])
                        mobile.set(x[3])
                        email.set(x[4])
                        search_fname2.config(text=x[1])
                        search_lname2.config(text=x[2])
                        search_customer_mobile2.config(text=x[3])
        

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Booking Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        def get_count():
            for row in db.count_bookings():
                print(row)
                count_items.config(text=f'Bookings: {row}')

        count_items = Label(top_frame,
            font=('arial', 14, 'bold'),
            fg=green_color, 
            bg=bg1_color)
        count_items.place(x=140, y=5)

        get_count()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=10, 
            relief='flat',
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        # items frame
        booking_fields = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        booking_fields.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        '''

        ##############customer info###############

        '''

        customer_detail_frame = LabelFrame(list_frame, bg=white_color, width=300)
        customer_detail_frame.pack(side='top', anchor='w',  fill='x')

        # search entry
        entry_search = Entry(customer_detail_frame, 
            bg=white_color, 
            width=20, 
            font=('arial',14), 
            bd=2, 
            textvariable=search_customer_info)
        entry_search.grid(row=0, column=0, padx=2) 

        # add btn
        search_btn = Button(customer_detail_frame, 
            text='Search Customer', 
            bg='gray',
            fg=white_color, 
            activeforeground='white',
            activebackground='#4b8598',
            height=1,
            font=('arial',12), 
            bd=2,
            command=get_customer_info)
        search_btn.grid(row=0, column=1, padx=3)

        # right card_frame
        card_frame = Frame(customer_detail_frame, bg=white_color, height=300)
        card_frame.grid(row=1, column=0, sticky='w', pady=2)

        # title
        title_frame0 = Label(card_frame, 
            text="Search to View Customer Details", 
            font=('arial', 12, 'bold'),
            fg='#4b8598', 
            bg=white_color)
        title_frame0.grid(row=0, column=0, sticky='w', columnspan=2)

        # first name
        search_fname1 = Label(card_frame, 
            text="First Name: ", 
            font=('arial', 14), 
            fg='grey', 
            bg=white_color)
        search_fname1.grid(row=1, column=0, sticky='w')

        search_fname2 = Label(card_frame, 
            text="", 
            font=('arial', 14), 
            fg='#4f234f', 
            bg=white_color)
        search_fname2.grid(row=1, column=1, sticky='w')

        # last name
        search_lname1 = Label(card_frame, 
            text='Surname: ', 
            font=('arial', 14), 
            fg='grey', 
            bg=white_color)
        search_lname1.grid(row=2, column=0, sticky='w')

        search_lname2 = Label(card_frame, 
            text="", 
            font=('arial', 14), 
            fg='#4f234f', 
            bg=white_color)
        search_lname2.grid(row=2, column=1, sticky='w')

        # mobile
        search_customer_mobile1 = Label(card_frame, 
            text='Phone no: ', 
            font=('arial', 14), 
            fg='grey', 
            bg=white_color)
        search_customer_mobile1.grid(row=3, column=0, sticky='w')
        search_customer_mobile2 = Label(card_frame, 
            text="", 
            font=('arial', 14), 
            fg='#4f234f', 
            bg=white_color)
        search_customer_mobile2.grid(row=3, column=1, sticky='w')

        '''
        ################frames#################

        '''
        get_bill_ref = random.randint(100000, 99999999)
        bill_ref.set(get_bill_ref)

        # right card_frame
        bill_ref_frame = LabelFrame(customer_detail_frame, bg=white_color, height=300)
        bill_ref_frame.grid(row=1, column=2,  rowspan=2, sticky='w', pady=2, padx=20)

        # ref_number
        lab_bill_ref = Label(bill_ref_frame, 
            text='Bill Ref: ', 
            font=('arial', 14), 
            fg='red', 
            bg=white_color)
        lab_bill_ref.grid(row=0, column=0, sticky='w')

        # ref_number
        entry_bill_ref = Entry(bill_ref_frame, 
            bg='white', 
            width=20, 
            font=('arial',14), 
            bd=2, 
            textvariable=bill_ref)
        entry_bill_ref.grid(row=1, column=0, sticky='w')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack(pady=10)

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=32, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "FirstName",
            "Surname",
            "PhoneNo",
            "Address",
            "Email",
            "CarRegNo",
            "MeansOfID",
            "TravelingFrom",
            "TravelingTo",
            "RoomNumber",
            "RoomType",
            "RoomPrice",
            "CheckInDate",
            "CheckOutDate",
            "Party",
            "Discount (%)",
            "Total Cost",
            "Bill Ref")

        # format our columns
        tv.column("ID", width=90, anchor='center')
        tv.column("FirstName", width=200, anchor='center')
        tv.column("Surname", width=200, anchor='center')
        tv.column("PhoneNo", width=200, anchor='center')
        tv.column("Address", width=240, anchor='center')
        tv.column("Email", width=200, anchor='center')
        tv.column("CarRegNo", width=200, anchor='center')
        tv.column("MeansOfID", width=200, anchor='center')
        tv.column("TravelingFrom", width=200, anchor='center')
        tv.column("TravelingTo", width=200, anchor='center')
        tv.column("RoomNumber", width=200, anchor='center')
        tv.column("RoomType", width=200, anchor='center')
        tv.column("RoomPrice", width=200, anchor='center')
        tv.column("CheckInDate", width=200, anchor='center')
        tv.column("CheckOutDate", width=200, anchor='center')
        tv.column("Party", width=200, anchor='center')
        tv.column("Discount (%)", width=200, anchor='center')
        tv.column("Total Cost", width=200, anchor='center')
        tv.column("Bill Ref", width=200, anchor='center')
        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('FirstName', text="First Name",)
        tv.heading('Surname', text="Surname",)
        tv.heading('PhoneNo', text="Phone no",)
        tv.heading('Address', text="Address",)
        tv.heading('Email', text="Email",)
        tv.heading('CarRegNo', text="Car Reg No",)
        tv.heading('MeansOfID', text="Means of ID",)
        tv.heading('TravelingFrom', text="Traveling From",)
        tv.heading('TravelingTo', text="Traveling To",)
        tv.heading('RoomNumber', text="Room no",)
        tv.heading('RoomType', text="Room Type",)
        tv.heading('RoomPrice', text="Room Price",)
        tv.heading('CheckInDate', text="Date of Arrival",)
        tv.heading('CheckOutDate', text="Date of Departure",)
        tv.heading('Party', text="Party (No of person)",)
        tv.heading('Discount (%)', text="Discount (%)",)
        tv.heading('Total Cost', text="Total Cost",)
        tv.heading('Bill Ref', text="Bill Ref",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 

        for record in db.fetch_booking():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18]), tags=('oddrow',))
            # increment counter 
            count +=1 

        # receipt_btn
        receipt_btn = Button(booking_fields, 
            text='View Receipt', 
            bg='#4b8598', 
            fg='white',
            width=12, 
            height=1, 
            font=('arial',12), 
            bd=1, 
            relief='flat',
            activeforeground='white',
            activebackground='#72404d',
            command=get_receipt_page_view)
        receipt_btn.place(x=300, y=2)

        # add staff label
        txt_title = Label(booking_fields, 
          text='Add New Booking', 
          font=('arial', 16,'bold'), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # fname
        lab_first_name = Label(booking_fields, 
          text='First Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_first_name.grid(row=1, column=0,sticky='w')
        entry_first_name = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial', 12, 'bold'),
          bd=2,
          textvariable=fname)
        entry_first_name.grid(row=1, column=1) 

        # lname
        lab_last_name = Label(booking_fields, 
          text='Surname: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_last_name.grid(row=2, column=0, sticky='w')
        entry_last_name = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2,
          textvariable=lname)
        entry_last_name.grid(row=2, column=1)  

        # mobile
        lab_mobile = Label(booking_fields, 
          text='Phone no: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_mobile.grid(row=3, column=0, sticky='w')
        entry_mobile = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2, 
          textvariable=mobile)
        entry_mobile.grid(row=3, column=1) 

        # address
        lab_address = Label(booking_fields, 
          text='Address: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_address.grid(row=4, column=0,sticky='w')
        entry_address = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2,
          textvariable=address)
        entry_address.grid(row=4, column=1) 

        # email
        lab_email = Label(booking_fields, 
          text='Email: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_email.grid(row=5, column=0, sticky='w')
        entry_email = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2,
          textvariable=email)
        entry_email.grid(row=5, column=1)  

        # car_reg_no
        lab_car_reg_no = Label(booking_fields, 
          text='Car Reg No: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_car_reg_no.grid(row=6, column=0, sticky='w')
        entry_car_reg_no = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2, 
          textvariable=car_reg_no)
        entry_car_reg_no.grid(row=6, column=1) 

        # means_of_id
        lab_means_of_id = Label(booking_fields, 
          text='Means of ID: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_means_of_id.grid(row=7, column=0,sticky='w')
        entry_means_of_id = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2,
          textvariable=means_of_id)
        entry_means_of_id.grid(row=7, column=1) 

        # traveling_from
        lab_traveling_from = Label(booking_fields, 
          text='Traveling From: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_traveling_from.grid(row=8, column=0, sticky='w')
        entry_traveling_from = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2,
          textvariable=traveling_from)
        entry_traveling_from.grid(row=8, column=1)  

        # traveling_to
        lab_traveling_to = Label(booking_fields, 
          text='Traveling To: ', 
          padx=2, 
          pady=2, 
          font=('arial', 12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_traveling_to.grid(row=9, column=0, sticky='w')
        entry_traveling_to = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12, 'bold'), 
          bd=2, 
          textvariable=traveling_to)
        entry_traveling_to.grid(row=9, column=1) 

        # room_number
        lab_room_number = Label(booking_fields, 
          text='Room no: ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_room_number.grid(row=10, column=0, sticky='w')
        entry_room_number = ttk.Combobox(booking_fields, 
          width=19, 
          font=('arial',12,'bold'), 
          state='readonly',
          textvariable=room_number) 
        entry_room_number['values'] = options
        entry_room_number.bind("<<ComboboxSelected>>", get_rooms_detail_data)
        entry_room_number.grid(row=10, column=1) 

        # room_type
        lab_room_type = Label(booking_fields, 
          text='Room Type: ', 
          padx=2, 
          pady=2, 
          font=('arial',12, 'bold'), 
          fg='grey', 
          bg=white_color)
        lab_room_type.grid(row=11, column=0, sticky='w')
        entry_room_type = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          state='readonly',
          textvariable=room_type)
        entry_room_type.grid(row=11, column=1) 

        # room_amount
        lab_room_price = Label(booking_fields, 
          text='Room Price: ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_room_price.grid(row=12, column=0, sticky='w')
        entry_room_price = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          state='readonly',
          textvariable=room_price)
        entry_room_price.grid(row=12, column=1)  

        # check_in_date
        lab_check_in_date = Label(booking_fields, 
          text='Date of Arrival (dd/mm/yyyy): ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_check_in_date.grid(row=13, column=0, sticky='w')
        entry_check_in_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          state='normal', 
          textvariable=check_in_date)
        entry_check_in_date.grid(row=13, column=1) 

        # check_out_date
        lab_check_out_date = Label(booking_fields, 
          text='Date of departure (dd/mm/yyyy): ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_check_out_date.grid(row=14, column=0, sticky='w')
        entry_check_out_date = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          state='normal', 
          textvariable=check_out_date)
        entry_check_out_date.grid(row=14, column=1) 

        # party
        lab_party = Label(booking_fields, 
          text='Party (No of person): ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_party.grid(row=15, column=0, sticky='w')
        entry_party = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          textvariable=party)
        entry_party.grid(row=15, column=1)

        # discount
        lab_discount = Label(booking_fields, 
          text='Discount (%): ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_discount.grid(row=16, column=0, sticky='w')
        entry_discount = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          textvariable=discount)
        entry_discount.grid(row=16, column=1)

        # total_cost
        lab_total_cost = Label(booking_fields, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial',12,'bold'), 
          fg='grey', 
          bg=white_color)
        lab_total_cost.grid(row=17, column=0, sticky='w')
        entry_total_cost = Entry(booking_fields, 
          bg='white', 
          width=20, 
          font=('arial',12,'bold'), 
          bd=2, 
          textvariable=total_cost)
        entry_total_cost.grid(row=17, column=1)


        # btn frame
        btn_frame = Frame(booking_fields, padx=5, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=18, column=0, columnspan=2, pady=5)

        # total btn
        total_btn = Button(btn_frame, 
          text='Total', 
          bg='#076',
          fg='white', 
          width=6, 
          height=1,
          relief='flat',
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=get_total_cost_data)
        total_btn.grid(row=0, column=0, pady=5, padx=1)   

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_booking_data)
        add_btn.grid(row=0, column=1, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          width=6, 
          height=1,
          relief='flat',
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_booking_data)
        update_btn.grid(row=0, column=2, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clearAll)
        clear_btn.grid(row=0, column=3, pady=5, padx=1)   


        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          width=6, 
          height=1,
          relief='flat',
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_booking_data)
        delete_btn.grid(row=0, column=4, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=6, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_booking_data)
        search_btn.grid(row=0, column=5, pady=5, padx=1)      



# new page  
class OrderPageView(object):
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("1260x590+20+20")
        self.root.config(bd=0, bg=white_color, relief='flat')
        # self.root.resizable(0, 0)

        food_name = StringVar()
        fd_unit_cost = StringVar()
        fd_quantity = StringVar()
        fd_total = StringVar()

        drink_name = StringVar()
        dk_unit_cost = StringVar()
        dk_quantity = StringVar()
        dk_total = StringVar() 

        fname = StringVar()
        lname = StringVar()
        mobile = StringVar() 

        # date 
        today = date.today()
        created_date = today.strftime("%B %d, %Y")
        created_time = str(time.strftime("%I:%M:%S %p"))

        global row 
        global textarea 

        get_bill_ref = random.randint(100000, 99999999)

        def get_receipt_page_view():
            newWindow = Toplevel()
            newWindow.title("SHALELE PLACE")
            # newWindow.geometry("810x500+200+100")
            newWindow.config(bd=0, bg=white_color, relief='flat')
            newWindow.resizable(0, 0)

            global textarea

            top_frame = LabelFrame(newWindow, relief='raised', bg=bg1_color, height=80, pady=10)
            top_frame.pack(side='top', pady=1, fill='x', expand='false')
            bottom_frame = LabelFrame(newWindow, padx=5, bg=white_color, width=1600, relief='flat')
            bottom_frame.pack(pady=1)

            # labels headers
            header2_title = Label(top_frame, 
                text='Receipt Page View', 
                font=('arial', 14, 'bold'), 
                fg=green_color, 
                bg=bg1_color)
            header2_title.pack() 

            # receipt_btn
            save_btn = Button(top_frame, 
                text='Print or Save File', 
                bg='#4b8598', 
                fg='white',
                width=14, 
                height=1, 
                font=('arial',12), 
                bd=1, 
                relief='flat',
                activeforeground='white',
                activebackground='#72404d',
                command=get_receipt_file)
            save_btn.pack(pady=5)

            scrol = Scrollbar(bottom_frame, orient='vertical')
            scrol.pack(fill='y', side='right')

            textarea = Text(bottom_frame, 
                font=('arial',12),
                state='normal', 
                pady=10,
                height=20, 
                width=60)
            textarea.focus()
            textarea.pack()
            scrol.config(command=textarea.yview)

            # calculating the foods and drinks totals 
            if entry_dk_total.get():
                get_grand_sum = (entry_dk_total.get())
            if entry_fd_total.get():
                get_grand_sum = (entry_fd_total.get()) 
            if entry_dk_total.get() and entry_fd_total.get():
                get_grand_sum = (float(entry_dk_total.get())+float(entry_fd_total.get()))

            
            textarea.get(1.0, END)
            textarea.insert('end', f"\nSHALELE HOSPITALITY & INVESTMENT Ltd\n")
            textarea.insert('end', f"\nNo. 12 Kano Road, Beside Federal Secretariat. Katsina.\n")
            textarea.insert('end', '\nDate: '+str(time.strftime("%d/%m/%y")))
            textarea.insert('end', '\nBill Ref: '+str(get_bill_ref)+'\n')
            if entry_food_type.get():
                textarea.insert('end', '\nORDER FOOD(s)')
                textarea.insert('end', '\nFood Name: '+entry_food_type.get())
            if entry_fd_unit_cost.get():
                textarea.insert('end', '\nUnit Cost:  ₦'+entry_fd_unit_cost.get())
            if entry_fd_quantity.get():
                textarea.insert('end', '\nQuantity:   '+entry_fd_quantity.get())
            if entry_fd_total.get():
                textarea.insert('end', '\nSub Total:  ₦'+entry_fd_total.get())
                textarea.insert('end', '\n')
            if entry_drink_type.get():
                textarea.insert('end', '\nORDER DRINK(s)')
                textarea.insert('end', '\nDrink Name: '+entry_drink_type.get())
            if entry_dk_unit_cost.get():
                textarea.insert('end', '\nUnit Cost:  ₦'+entry_dk_unit_cost.get())
            if entry_dk_quantity.get():
                textarea.insert('end', '\nQuantity:   '+entry_dk_quantity.get())
            if entry_dk_total.get():
                textarea.insert('end', '\nSub Total:  ₦'+entry_dk_total.get())
                textarea.insert('end', '\n')
            if entry_first_name.get():
                textarea.insert('end', '\nTotal Cost: ₦'+str(get_grand_sum))
                textarea.insert('end', '\nFirst Name: '+entry_first_name.get())
            if entry_last_name.get():
                textarea.insert('end', '\nSurname:  '+entry_last_name.get())
            if entry_mobile.get():
                textarea.insert('end', '\nPhone no: '+entry_mobile.get())
            textarea.insert('end', '\n\n')
            textarea.get(END, 1.0)


        def get_receipt_file():
            q = textarea.get(1.0, "end-1c")
            filename = tempfile.mktemp(f"{entry_last_name.get()}.doc")
            open (filename, "w", encoding="utf-8").write(q)
            os.startfile(filename, 'print')


        def getFoodData(event): 
            selected_row = tv_food.focus()
            data = tv_food.item(selected_row) 
            global row 
            row = data["values"] 
            fname.set(row[1])
            lname.set(row[2])
            mobile.set(row[3])
            food_name.set(row[4])
            fd_unit_cost.set(row[5])
            fd_quantity.set(row[6])
            fd_total.set(row[7])


        def display_all_foods():
            tv_food.delete(*tv_food.get_children()) 
            for row in db.fetch_order_food():
                tv_food.insert("", END, values=row)

        def add_food_order_data():
            if entry_first_name.get()=="" or entry_last_name.get()=="" or entry_mobile.get()=="" or entry_food_type.get()=="" or entry_fd_unit_cost.get()=="" or entry_fd_quantity.get()=="" or entry_fd_total.get()=="": 
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return
            db.insert_order_food(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_food_type.get(), entry_fd_unit_cost.get(), entry_fd_quantity.get(), entry_fd_total.get())
            db.insert_food_activity(entry_food_type.get(), entry_fd_quantity.get(), entry_fd_total.get(), created_date, created_time)
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved", parent=root)
            clear_food_order_All()
            display_all_foods()

        def update_food_order_data():
            if entry_first_name.get()=="" or entry_last_name.get()=="" or entry_mobile.get()=="" or entry_food_type.get()=="" or entry_fd_unit_cost.get()=="" or entry_fd_quantity.get()=="" or entry_fd_total.get()=="": 
                messagebox.showerror("Error in Inputs", "No Data Found to Update", parent=root) 
                return 
            db.update_order_food(row[0], entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_food_type.get(), entry_fd_unit_cost.get(), entry_fd_quantity.get(), entry_fd_total.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated", parent=root)
            clear_food_order_All()
            display_all_foods() 

        def delete_food_order_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
            db.remove_order_food(row[0])
            clear_food_order_All()
            display_all_foods() 

        def clear_food_order_All():
            fname.set('')
            lname.set('')
            mobile.set('')
            food_name.set('')
            fd_unit_cost.set('')
            fd_quantity.set('')
            fd_total.set('')
            display_all_foods()

        def search_food_order_data():
            tv_food.delete(*tv_food.get_children()) 
            if  entry_first_name.get() or entry_last_name.get() or entry_mobile.get() or entry_food_type.get() or entry_fd_unit_cost.get() or entry_fd_quantity.get() or entry_fd_total.get(): 
                for row in db.search_order_food(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_food_type.get(), entry_fd_unit_cost.get(), entry_fd_quantity.get(), entry_fd_total.get()):
                    tv_food.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                display_all_foods()

        food_options_list = []
        for row in db.get_foods_option():
            food_options_list.append(row[1])

        def get_foods_details_data(event):
            opts = entry_food_type.get()
            option_id = opts.split("-")[0]
            for x in db.get_foods_details(option_id):
                fd_unit_cost.set(x[2])


        def getDrinkData(event): 
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"] 
            fname.set(row[1])
            lname.set(row[2])
            mobile.set(row[3])
            drink_name.set(row[4])
            dk_unit_cost.set(row[5])
            dk_quantity.set(row[6])
            dk_total.set(row[7])

        def display_all_drinks():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_order_drink():
                tv.insert("", END, values=row)

        def add_drink_order_data():
            if entry_first_name.get()=="" or entry_last_name.get()=="" or entry_mobile.get()=="" or entry_drink_type.get()=="" or entry_dk_unit_cost.get()=="" or entry_dk_quantity.get()=="" or entry_dk_total.get()=="": 
                messagebox.showerror("Error in Inputs", "Please Fill All the Details", parent=root) 
                return
            db.insert_order_drink(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_drink_type.get(), entry_dk_unit_cost.get(), entry_dk_quantity.get(), entry_dk_total.get())
            db.insert_drink_activity(entry_drink_type.get(), entry_dk_quantity.get(), entry_dk_total.get(), created_date, created_time)
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved", parent=root)
            clear_drink_order_All()
            display_all_drinks()

        def update_drink_order_data():
            if entry_first_name.get()=="" or entry_last_name.get()=="" or entry_mobile.get()=="" or entry_drink_type.get()=="" or entry_dk_unit_cost.get()=="" or entry_dk_quantity.get()=="" or entry_dk_total.get()=="": 
                messagebox.showerror("Error in Inputs", "No Data Found to Update", parent=root) 
                return 
            db.update_order_drink(row[0], entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_drink_type.get(), entry_dk_unit_cost.get(), entry_dk_quantity.get(), entry_dk_total.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated", parent=root)
            clear_drink_order_All()
            display_all_drinks() 

        def delete_drink_order_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
            db.remove_order_drink(row[0])
            clear_drink_order_All()
            display_all_drinks() 

        def clear_drink_order_All():
            fname.set('')
            lname.set('')
            mobile.set('')
            drink_name.set('')
            dk_unit_cost.set('')
            dk_quantity.set('')
            dk_total.set('')
            display_all_drinks()

        def search_food_order_data():
            tv.delete(*tv.get_children()) 
            if entry_first_name.get() or entry_last_name.get() or entry_mobile.get() or entry_drink_type.get() or entry_dk_unit_cost.get() or entry_dk_quantity.get() or entry_dk_total.get(): 
                for row in db.search_order_drink(entry_first_name.get(), entry_last_name.get(), entry_mobile.get(), entry_drink_type.get(), entry_dk_unit_cost.get(), entry_dk_quantity.get(), entry_dk_total.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                display_all_drinks()

        drink_options_list = []
        for row in db.get_drink_option():
            drink_options_list.append(row[1])

        def get_drink_details_data(event):
            opts = entry_drink_type.get()
            option_id = opts.split("-")[0]
            for x in db.get_drink_details(option_id):
                dk_unit_cost.set(str(x[2]))


        def get_customer_info_for_order():
            row = db.search_customer_for_order(entry_first_name.get(), entry_last_name.get(), entry_last_name.get()) 
            print(row)
            if row==None:
                messagebox.showinfo("Result","Nothing Found", parent=root)
            else:
                for x in row:
                    fname.set(x[1])
                    lname.set(x[2])
                    mobile.set(x[3])


        def get_total_foods():
            try:
                food_qty = entry_fd_quantity.get()
                food_price = entry_fd_unit_cost.get()
                fdtotal = float(food_qty)*float(food_price)
                fd_total.set(str(fdtotal))
            except:
                messagebox.showinfo("Info","Nothing to calculate", parent=root)
            

        def get_total_drinks():
            try:
                drink_qty = entry_dk_quantity.get()
                drink_price = entry_dk_unit_cost.get()
                dktotal = float(drink_qty)*float(drink_price)
                dk_total.set(str(dktotal))
            except:
                messagebox.showinfo("Info","Nothing to calculate", parent=root)


        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        middle_frame = LabelFrame(self.root, relief='flat', bg=white_color, height=40)
        middle_frame.pack(fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        end_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        end_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Order Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=10, 
            relief='flat',
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        # save_btn
        save_btn = Button(top_frame, 
            text='View Receipt', 
            bg='#4b8598', 
            fg='white',
            relief='flat',
            width=14, 
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#72404d',
            command=get_receipt_page_view)
        save_btn.place(x=120, y=2)

        # fname
        lab_first_name = Label(middle_frame, 
          text='First Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_first_name.grid(row=0, column=0, padx=4)
        entry_first_name = Entry(middle_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=fname)
        entry_first_name.grid(row=0, column=1) 

        # lname
        lab_last_name = Label(middle_frame, 
          text='Surname: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_last_name.grid(row=0, column=2, padx=4)
        entry_last_name = Entry(middle_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=lname)
        entry_last_name.grid(row=0, column=3)  

        # mobile
        lab_mobile = Label(middle_frame, 
          text='Phone no: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_mobile.grid(row=0, column=4, padx=4)
        entry_mobile = Entry(middle_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=mobile)
        entry_mobile.grid(row=0, column=5) 

        # add btn
        search_btn = Button(middle_frame, 
            text='Search Customer', 
            bg='gray',
            fg=white_color, 
            activeforeground='white',
            activebackground='#4b8598',
            height=1,
            font=('arial',12), 
            bd=2,
            command=get_customer_info_for_order)
        search_btn.grid(row=0, column=6, padx=10)


        # items frame
        food_fields = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        food_fields.pack(side='left', pady=1, fill='x', expand='false')

        # items frame
        food_list = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        food_list.pack(side='right', pady=1, fill='x', expand='false')

        '''
        ###############for foods##############
        '''

        # add staff label
        txt_title = Label(food_fields, 
          text='Order Food', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Food Name
        lab_food_type = Label(food_fields, 
          text='Food Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_food_type.grid(row=1, column=0,sticky='w')
        entry_food_type = ttk.Combobox(food_fields, 
          width=19, 
          font=('arial',14), 
          state='readonly', 
          textvariable=food_name)
        entry_food_type["values"]=food_options_list
        entry_food_type.bind("<<ComboboxSelected>>", get_foods_details_data)
        entry_food_type.grid(row=1, column=1) 

        # Unit Cost
        lab_fd_unit_cost = Label(food_fields, 
          text='Unit Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_fd_unit_cost.grid(row=2, column=0, sticky='w')
        entry_fd_unit_cost = Entry(food_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=fd_unit_cost)
        entry_fd_unit_cost.grid(row=2, column=1)

        # Quantity
        lab_fd_quantity= Label(food_fields, 
          text='Quantity: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_fd_quantity.grid(row=3, column=0, sticky='w')
        entry_fd_quantity = Entry(food_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=fd_quantity)
        entry_fd_quantity.grid(row=3, column=1)

        # total cost
        lab_fd_total= Label(food_fields, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_fd_total.grid(row=4, column=0, sticky='w')
        entry_fd_total = Entry(food_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=fd_total)
        entry_fd_total.grid(row=4, column=1)

        # btn frame
        btn_frame = Frame(food_fields, padx=10, relief='flat', bg=white_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        # total btn
        total_btn = Button(btn_frame, 
          text='Total', 
          bg='#076',
          fg='white', 
          width=6, 
          relief='flat',
          height=1,
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=get_total_foods)
        total_btn.grid(row=0, column=0, pady=5, padx=1) 

        # add btn
        add_fd_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          relief='flat',
          fg='white', 
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_food_order_data)
        add_fd_btn.grid(row=0, column=1, pady=5, padx=1)

        # update btn
        update_fd_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_food_order_data)
        update_fd_btn.grid(row=0, column=2, pady=5, padx=1)

        # clear btn
        clear_fd_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clear_food_order_All)
        clear_fd_btn.grid(row=0, column=3, pady=5, padx=1)

        # delete btn
        delete_fd_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          width=6, 
          height=1,
          relief='flat',
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_food_order_data)
        delete_fd_btn.grid(row=0, column=4, pady=5, padx=1)       

        # search btn
        search_fd_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_food_order_data)
        search_fd_btn.grid(row=0, column=5, pady=5, padx=1)

        # list frame
        tree_frame = Frame(food_list, bg=white_color, width=500,)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=20, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv_food = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6,7,8))
        tv_food.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv_food.yview) 
        tree_scroll_horizontal.config(command=tv_food.xview) 

        # columns 
        tv_food['columns'] = (
            "ID", 
            "First Name", 
            "Surname",
            "Mobile",
            "Food Name", 
            "Unit Cost",
            "Quantity",
            "Total Cost")

        # format our columns
        tv_food.column("ID", width=80, anchor='center')
        tv_food.column("First Name", width=200, anchor='center')
        tv_food.column("Surname", width=200, anchor='center')
        tv_food.column("Mobile", width=200, anchor='center')
        tv_food.column("Food Name", width=150, anchor='center')
        tv_food.column("Unit Cost", width=150, anchor='center')
        tv_food.column("Quantity", width=100, anchor='center')
        tv_food.column("Total Cost", width=150, anchor='center')

        # create headings 
        tv_food.heading('ID', text="ID",)
        tv_food.heading('First Name', text="First Name",)
        tv_food.heading('Surname', text="Surname",)
        tv_food.heading('Mobile', text="Mobile",)
        tv_food.heading("Food Name", text="Food Name",)
        tv_food.heading("Unit Cost", text="Unit Cost")
        tv_food.heading("Quantity", text="Quantity")
        tv_food.heading("Total Cost", text="Total Cost")
        tv_food['show'] = 'headings'
        tv_food.bind("<ButtonRelease-1>", getFoodData)
        tv_food.pack(fill='x')

        # create Striped Row Tags 
        tv_food.tag_configure('oddrow', background='white', foreground='black')
        tv_food.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count_item 
        count_item = 0 
        for record in db.fetch_order_food():
            if count_item%2 == 0:
                tv_food.insert(parent='', index='end', iid=count_item, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]), tags=('evenrow',))
            else: 
                tv_food.insert(parent='', index='end', iid=count_item, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]), tags=('oddrow',))
            count_item +=1

        '''
        ###############for drinks##############
        '''

        # items frame
        drink_fields = LabelFrame(end_frame, pady=5, padx=10, bg=white_color, width=500,)
        drink_fields.pack(side='left', pady=1, fill='x', expand='false')

        # items frame
        drink_list = LabelFrame(end_frame, pady=5, padx=10, bg=white_color, width=500,)
        drink_list.pack(side='right', pady=1, fill='x', expand='false')

        # add staff label
        txt_title = Label(drink_fields, 
          text='Order Drink', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Food Name
        lab_drink_type = Label(drink_fields, 
          text='Drink Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_drink_type.grid(row=1, column=0,sticky='w')
        entry_drink_type = ttk.Combobox(drink_fields, 
          width=19, 
          font=('arial',14), 
          state='readonly', 
          textvariable=drink_name)
        entry_drink_type["values"]= drink_options_list
        entry_drink_type.bind("<<ComboboxSelected>>", get_drink_details_data)
        entry_drink_type.grid(row=1, column=1) 

        # Unit Cost
        lab_dk_unit_cost = Label(drink_fields, 
          text='Unit Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_dk_unit_cost.grid(row=2, column=0, sticky='w')
        entry_dk_unit_cost = Entry(drink_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=dk_unit_cost)
        entry_dk_unit_cost.grid(row=2, column=1)

        # Quantity
        lab_dk_quantity= Label(drink_fields, 
          text='Quantity: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_dk_quantity.grid(row=3, column=0, sticky='w')
        entry_dk_quantity = Entry(drink_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=dk_quantity)
        entry_dk_quantity.grid(row=3, column=1)

        # total cost
        lab_dk_total= Label(drink_fields, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_dk_total.grid(row=4, column=0, sticky='w')
        entry_dk_total = Entry(drink_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=dk_total)
        entry_dk_total.grid(row=4, column=1)


        # btn frame
        btn_frame = Frame(drink_fields, padx=10, relief='flat', bg=white_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        # total btn
        total_btn = Button(btn_frame, 
          text='Total', 
          bg='#076',
          fg='white', 
          width=6, 
          height=1,
          relief='flat',
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=get_total_drinks)
        total_btn.grid(row=0, column=0, pady=5, padx=1)

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_drink_order_data)
        add_btn.grid(row=0, column=1, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_drink_order_data)
        update_btn.grid(row=0, column=2, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clear_drink_order_All)
        clear_btn.grid(row=0, column=3, pady=5, padx=1)

        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          relief='flat',
          bg='red', 
          fg='white',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_drink_order_data)
        delete_btn.grid(row=0, column=4, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=6, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_food_order_data)
        search_btn.grid(row=0, column=5, pady=5, padx=1) 

        
        # list frame
        tree_frame = Frame(drink_list, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=20, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6,7,8))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "First Name",
            "Last Name",
            "Mobile",
            "Drink Name", 
            "Unit Cost",
            "Quantity",
            "Total Cost")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("First Name", width=200, anchor='center')
        tv.column("Last Name", width=200, anchor='center')
        tv.column("Mobile", width=200, anchor='center')
        tv.column("Drink Name", width=150, anchor='center')
        tv.column("Unit Cost", width=150, anchor='center')
        tv.column("Quantity", width=100, anchor='center')
        tv.column("Total Cost", width=150, anchor='center')

        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('First Name', text="First Name",)
        tv.heading('Last Name', text="Last Name",)
        tv.heading('Mobile', text="Mobile",)
        tv.heading("Drink Name", text="Drink Name",)
        tv.heading("Unit Cost", text="Unit Cost")
        tv.heading("Quantity", text="Quantity")
        tv.heading("Total Cost", text="Total Cost")
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getDrinkData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global countid 

        countid = 0 
        for record in db.fetch_order_drink():
            if countid%2 == 0:
                tv.insert(parent='', index='end', iid=countid, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=countid, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]), tags=('oddrow',))
            countid +=1




class InventoryPageView(object): 
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("1100x630+20+20")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        name = StringVar()
        quantity = StringVar()
        unit = StringVar()
        unit_cost = StringVar()
        total_cost = StringVar()

        item_name = StringVar()
        used_qty = StringVar()
        remain_qty = StringVar()
        created_date = StringVar()

        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            name.set(row[1])
            quantity.set(row[2])
            unit.set(row[3])
            unit_cost.set(row[4])
            total_cost.set(row[5])
        
        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_store():
                tv.insert("", END, values=row)


        def add_store_data():
            if entry_name.get() == "" or entry_quantity.get() == "" or entry_unit.get() == "" or entry_unit_cost.get() == "" or entry_total_cost.get() == "":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.insert_store(entry_name.get(), entry_quantity.get(), entry_unit.get(), entry_unit_cost.get(), entry_total_cost.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved",parent=root)
            clearAll() 
            displayAll()

        def update_store_data():
            if entry_name.get() == "" or entry_quantity.get() == "" or entry_unit.get() == "" or entry_unit_cost.get() == "" or entry_total_cost.get() == "":
                messagebox.showerror("Error in Inputs", "No Data Found to Update",parent=root) 
                return 
            db.update_store(row[0], entry_name.get(), entry_quantity.get(), entry_unit.get(), entry_unit_cost.get(), entry_total_cost.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated",parent=root)
            clearAll() 
            displayAll()

        def delete_store_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?",parent=root)
            db.remove_store(row[0])
            clearAll() 
            displayAll()

        def clearAll():
            name.set('')
            quantity.set('')
            unit.set('')
            unit_cost.set('')
            total_cost.set('')
            displayAll()

        def search_store_data(): 
            tv.delete(*tv.get_children()) 
            if entry_name.get() or entry_quantity.get() or entry_unit.get() or entry_unit_cost.get() or entry_total_cost.get():
                for row in db.search_store(entry_name.get(), entry_quantity.get(), entry_unit.get(), entry_unit_cost.get(), entry_total_cost.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()


        def get_total_store():
            try:
                item_qty = entry_quantity.get()
                unit_price = entry_unit_cost.get()
                total_items = float(item_qty)*float(unit_price)
                total_cost.set(str(total_items))
            except:
                messagebox.showinfo("Info","Nothing to calculate. Please enter some quantity and unit cost.", parent=root)


        def getStoreData(event):          
            selected_row = tvlist.focus()
            data = tvlist.item(selected_row) 
            global row 
            row = data["values"]
            item_name.set(row[1])
            used_qty.set(row[2])
            remain_qty.set(row[3]) 
            created_date.set(row[4])

        today = date.today()
        created_item_date = today.strftime("%B %d, %Y")

        created_date.set(str(created_item_date))

        def get_displayAll():
            tvlist.delete(*tvlist.get_children()) 
            for row in db.fetch_store_usage():
                tvlist.insert("", END, values=row)

        def get_add_data():
            if entry_item_name.get() == "" or entry_used_qty.get() == "" or entry_remain_qty.get() == "":
                messagebox.showerror("Error in Inputs", "Please Fill All the Details",parent=root) 
                return 
            db.insert_store_usage(entry_item_name.get(), entry_used_qty.get(), entry_remain_qty.get(), created_item_date)
            messagebox.showinfo("Success!", "Record Has Been Successfully Saved",parent=root)
            get_clearAll() 
            get_displayAll()
        
        def get_update_data():
            if entry_item_name.get() == "" or entry_used_qty.get() == "" or entry_remain_qty.get() == "" or entry_created_date.get()=="":
                messagebox.showerror("Error in Inputs", "No Data Found to Update",parent=root) 
                return 
            db.update_store_usage(row[0], entry_item_name.get(), entry_used_qty.get(), entry_remain_qty.get(), entry_created_date.get())
            messagebox.showinfo("Success!", "Record Has Been Successfully Updated",parent=root)
            get_clearAll() 
            get_displayAll()

        def get_delete_data():
            messagebox.showinfo("Delete", "Are you sure you want to delete these data?",parent=root)
            db.remove_store_usage(row[0])
            get_clearAll() 
            get_displayAll()

        def get_clearAll():
            item_name.set('')
            used_qty.set('')
            remain_qty.set('')
            get_displayAll()

        def get_search_data(): 
            tvlist.delete(*tvlist.get_children()) 
            if entry_item_name.get() or entry_used_qty.get() or entry_remain_qty.get() or entry_created_date.get():
                for row in db.search_store_usage(entry_item_name.get(), entry_used_qty.get(), entry_remain_qty.get(), entry_created_date.get()):
                    tvlist.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                get_displayAll()

        options = [] 
        for item in db.get_store_items():
            options.append(item[1])

        def get_remaining_qty():
            try:
                opts = entry_item_name.get()
                option_id = opts.split("-")[0]
                for x in db.get_store_details(option_id):
                    old_qty = x[2]

                current_qty = entry_used_qty.get()

                total_qty = float(old_qty)-float(current_qty)
                db.update_store_qty(row[0], total_qty)
                remain_qty.set(str(total_qty)) 
                messagebox.showinfo("Info", f"The item remains only {total_qty} in store.", parent=root)
            except:
                messagebox.showinfo("Info", "Something went wrong. Check first the remaining quantity in your store.", parent=root)


        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)
        invent_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        invent_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Inventory Page View', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
          text='Exit', 
          bg='#72404d', 
          fg='white',
          relief='flat',
          width=10, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=root.destroy)
        exit_btn.place(x=10, y=1) 

        items_fields_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        items_fields_frame.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=22, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5,6))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "Name", 
            "Quantity", 
            "Unit",
            "Unit Cost",
            "Total Cost",)

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("Name", width=250, anchor='center')
        tv.column("Quantity", width=200, anchor='center')
        tv.column("Unit", width=180, anchor='center')
        tv.column("Unit Cost", width=200, anchor='center')
        tv.column("Total Cost", width=200, anchor='center')
        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('Name', text="Name",)
        tv.heading('Quantity', text="Quantity",)
        tv.heading('Unit', text="Unit",)
        tv.heading('Unit Cost', text="Unit Cost",)
        tv.heading('Total Cost', text="Total Cost",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global count 
        count = 0 
        for record in db.fetch_store():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4],record[5]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4],record[5]), tags=('oddrow',))
              # increment counter 
            count +=1

        # add staff label
        txt_title = Label(items_fields_frame, 
          text='Add Item In Store', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # fname
        lab_name = Label(items_fields_frame, 
          text='Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_name.grid(row=1, column=0,sticky='w')
        entry_name = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=name)
        entry_name.grid(row=1, column=1) 

        # lname
        lab_quantity = Label(items_fields_frame, 
          text='Quantity: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_quantity.grid(row=2, column=0, sticky='w')
        entry_quantity = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=quantity)
        entry_quantity.grid(row=2, column=1)  

        # mobile
        lab_unit = Label(items_fields_frame, 
          text='Unit: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_unit.grid(row=3, column=0, sticky='w')
        entry_unit = ttk.Combobox(items_fields_frame, 
          width=19, 
          font=('arial',14), 
          state='readonly', 
          textvariable=unit)
        entry_unit["values"]= ['Kilo','Litre','Metre','Not Available']
        entry_unit.grid(row=3, column=1) 
        
        # email
        lab_unit_cost = Label(items_fields_frame, 
          text='Unit Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_unit_cost.grid(row=4, column=0, sticky='w')
        entry_unit_cost = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=unit_cost)
        entry_unit_cost.grid(row=4, column=1) 
        
        lab_total_cost = Label(items_fields_frame, 
          text='Total Cost: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_total_cost.grid(row=5, column=0, sticky='w')
        entry_total_cost = Entry(items_fields_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          textvariable=total_cost)
        entry_total_cost.grid(row=5, column=1) 

        # btn frame
        btn_frame = Frame(items_fields_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)

        # total btn
        total_btn = Button(btn_frame, 
          text='Total', 
          bg='#076',
          fg='white', 
          width=6, 
          relief='flat',
          height=1,
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=get_total_store)
        total_btn.grid(row=0, column=0, pady=5, padx=1)   

        # add btn
        add_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          fg='white', 
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=add_store_data)
        add_btn.grid(row=0, column=1, pady=5, padx=1)

        # update btn
        update_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=update_store_data)
        update_btn.grid(row=0, column=2, pady=5, padx=1)

        # clear btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=clearAll)
        clear_btn.grid(row=0, column=3, pady=5, padx=1)   


        # delete btn
        delete_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=delete_store_data)
        delete_btn.grid(row=0, column=4, pady=5, padx=1)       

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=search_store_data)
        search_btn.grid(row=0, column=5, pady=5, padx=1)

        textarea_frame = LabelFrame(invent_frame, pady=5, padx=10, bg=white_color, width=500,)
        textarea_frame.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        item_list_frame = LabelFrame(invent_frame, pady=5, padx=10, bg=white_color, width=500,)
        item_list_frame.pack(side='right', pady=1, fill='y', expand='false') 

        # list frame
        tree_frame = Frame(item_list_frame, bg=white_color)
        tree_frame.pack()

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=22, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tvlist = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4,5))
        tvlist.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tvlist.yview) 
        tree_scroll_horizontal.config(command=tvlist.xview) 

        # columns 
        tvlist['columns'] = (
            "ID", 
            "Name", 
            "Used Quantity", 
            "Remaining Quantity",
            "Created Date")

        # format our columns
        tvlist.column("ID", width=80, anchor='center')
        tvlist.column("Name", width=250, anchor='center')
        tvlist.column("Used Quantity", width=200, anchor='center')
        tvlist.column("Remaining Quantity", width=200, anchor='center')
        tvlist.column("Created Date", width=200, anchor='center')
        # create headings 
        tvlist.heading('ID', text="ID",)
        tvlist.heading('Name', text="Name",)
        tvlist.heading('Used Quantity', text="Used Quantity",)
        tvlist.heading('Remaining Quantity', text="Remaining Quantity",)
        tvlist.heading('Created Date', text="Created Date",)
        tvlist['show'] = 'headings'
        tvlist.bind("<ButtonRelease-1>", getStoreData)
        tvlist.pack(fill='x')

        # create Striped Row Tags 
        tvlist.tag_configure('oddrow', background='white', foreground='black')
        tvlist.tag_configure('evenrow', background='lightblue', foreground='black')

        # add our data to the screen 
        global countItem 
        countItem = 0 
        for record in db.fetch_store_usage():
            if countItem%2 == 0:
                tvlist.insert(parent='', index='end', iid=countItem, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('evenrow',))
            else: 
                tvlist.insert(parent='', index='end', iid=countItem, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('oddrow',))
              # increment counter 
            countItem +=1

        # add staff label
        txts_title = Label(textarea_frame, 
          text='Use Items From Store', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txts_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # fname
        lab_item_name = Label(textarea_frame, 
          text='Name: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_item_name.grid(row=1, column=0,sticky='w')
        entry_item_name = ttk.Combobox(textarea_frame, 
          width=19, 
          font=('arial',14), 
          state='readonly', 
          textvariable=item_name)
        entry_item_name["values"]= options
        entry_item_name.grid(row=1, column=1) 

        # lname
        lab_used_qty = Label(textarea_frame, 
          text='Qty To use: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_used_qty.grid(row=2, column=0, sticky='w')
        entry_used_qty = Entry(textarea_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=used_qty)
        entry_used_qty.grid(row=2, column=1)  

        # lname
        lab_remain_qty = Label(textarea_frame, 
          text='Qty Remain: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_remain_qty.grid(row=3, column=0, sticky='w')
        entry_remain_qty = Entry(textarea_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=remain_qty)
        entry_remain_qty.grid(row=3, column=1)  

        # lname
        lab_created_date = Label(textarea_frame, 
          text='Created Date: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_created_date.grid(row=4, column=0, sticky='w')
        entry_created_date = Entry(textarea_frame, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          textvariable=created_date)
        entry_created_date.grid(row=4, column=1)  

        # btn frame
        btn_frame = Frame(textarea_frame, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

        # total btn
        remain_btn = Button(btn_frame, 
          text='Qty Remain', 
          bg='#076',
          fg='white', 
          # width=6,
          relief='flat', 
          height=1,
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#4b8598',
          command=get_remaining_qty)
        remain_btn.grid(row=0, column=0, pady=5, padx=1)   

        # add btn
        adds_btn = Button(btn_frame, 
          text='Add', 
          bg='gray',
          relief='flat',
          fg='white', 
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_add_data)
        adds_btn.grid(row=0, column=1, pady=5, padx=1)

        # update btn
        updates_btn = Button(btn_frame, 
          text='Update', 
          bg='gray',
          fg='white', 
          relief='flat',
          width=6, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_update_data)
        updates_btn.grid(row=0, column=2, pady=5, padx=1)

        # clear btn
        clears_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          width=6, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_clearAll)
        clears_btn.grid(row=0, column=3, pady=5, padx=1)   


        # delete btn
        deletes_btn = Button(btn_frame, 
          text='Delete', 
          bg='red', 
          fg='white',
          width=6, 
          height=1,
          relief='flat',
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=get_delete_data)
        deletes_btn.grid(row=0, column=4, pady=5, padx=1)       

        # search btn
        searchs_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          relief='flat',
          width=6, 
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=get_search_data)
        searchs_btn.grid(row=0, column=5, pady=5, padx=1) 

        displayAll()
        get_displayAll()



class LoginHistoryPage(object):
    """docstring for LoginHistoryPage"""
    def __init__(self, root):
        self.root = root
        self.root.title("SHALELE PLACE")
        self.root.geometry("900x400+20+80")
        self.root.config(bd=0, bg=white_color, relief='flat')
        self.root.resizable(0, 0)

        login_user = StringVar()
        login_date = StringVar()
        login_time = StringVar()
        
        def getData(event):
            selected_row = tv.focus()
            data = tv.item(selected_row) 
            global row 
            row = data["values"]
            login_user.set(row[1])
            login_date.set(row[2])
            login_time.set(row[3])

        def displayAll():
            tv.delete(*tv.get_children()) 
            for row in db.fetch_login_history():
                tv.insert("", END, values=row)

        def get_search():
            tv.delete(*tv.get_children()) 
            if  entry_login_user.get() or entry_login_date.get() or entry_login_time.get(): 
                for row in db.search_login_history(entry_login_user.get(), entry_login_date.get(), entry_login_time.get()):
                    tv.insert("", END, values=row)
            else:
                messagebox.showerror("Error","Nothing Found", parent=root)
                displayAll()

        def get_delete():
            if row:
                messagebox.showinfo("Delete", "Are you sure you want to delete these data?", parent=root)
                db.remove_login_history(row[0])
            get_clearAll()
            displayAll()

        def get_delete_all():
            messagebox.showinfo("Delete All", "Are you sure you want to delete all these data?", parent=root)
            db.remove_all_login_history()
            get_clearAll()
            displayAll()

        def get_clearAll():
            login_user.set('')
            login_date.set('')
            login_time.set('')
            displayAll()

        top_frame = LabelFrame(self.root, relief='raised', bg=bg1_color, height=80, pady=10)
        top_frame.pack(side='top', pady=1, fill='x', expand='false')
        bottom_frame = LabelFrame(self.root, padx=5, bg=white_color, width=1600, relief='flat')
        bottom_frame.pack(pady=1)

        # labels headers
        header2_title = Label(top_frame, 
            text='Login History Details', 
            font=('arial', 14, 'bold'), 
            fg=green_color, 
            bg=bg1_color)
        header2_title.pack()

        # exit btn
        exit_btn = Button(top_frame, 
            text='Exit', 
            bg='#72404d', 
            fg='white',
            width=6, 
            relief='flat',
            height=1, 
            font=('arial',12), 
            bd=1, 
            activeforeground='white',
            activebackground='#4b8598',
            command=root.destroy)
        exit_btn.place(x=10, y=2)

        # items frame
        history_fields = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        history_fields.pack(side='left', pady=1, fill='y', expand='false')

        # items frame
        list_frame = LabelFrame(bottom_frame, pady=5, padx=10, bg=white_color, width=500,)
        list_frame.pack(side='right', pady=1, fill='y', expand='false')

        # list frame
        tree_frame = Frame(list_frame, bg=white_color)
        tree_frame.pack(pady=5)

        # styling
        style = ttk.Style(root)
        style.theme_use('default')
        style.configure("Treeview", 
            background="silver", 
            foreground="#4f234f", 
            rowheight=34, 
            fieldbackground="silver", 
            font=('arial', 14))
        style.map('Treeview', background=[('selected', '#4b8598')], foreground=[('selected', 'white')])

        # list scroll bar
        tree_scroll_vertical = Scrollbar(tree_frame, orient='vertical')
        tree_scroll_vertical.pack(side=RIGHT, fill='y') 
        tree_scroll_horizontal = Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_horizontal.pack(side=BOTTOM, fill='x') 

        # create the Treeview 
        tv = ttk.Treeview(tree_frame, 
            yscrollcommand=tree_scroll_vertical.set,
            xscrollcommand=tree_scroll_horizontal.set,  
            selectmode="extended",
            columns=(1,2,3,4))
        tv.pack()

        # configure the Scrollbar 
        tree_scroll_vertical.config(command=tv.yview) 
        tree_scroll_horizontal.config(command=tv.xview) 

        # columns 
        tv['columns'] = (
            "ID", 
            "LoginUser",
            "LoginDate",
            "LoginTime")

        # format our columns
        tv.column("ID", width=80, anchor='center')
        tv.column("LoginUser", width=250, anchor='center')
        tv.column("LoginDate", width=250, anchor='center')
        tv.column("LoginTime", width=250, anchor='center')
        
        # create headings 
        tv.heading('ID', text="ID",)
        tv.heading('LoginUser', text="Login User",)
        tv.heading('LoginDate', text="Login Date",)
        tv.heading('LoginTime', text="Login Time",)
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill='x')

        # create Striped Row Tags 
        tv.tag_configure('oddrow', background='white', foreground='black')
        tv.tag_configure('evenrow', background='lightblue', foreground='black')

        global count 
        count = 0 
        for record in db.fetch_login_history():
            if count%2 == 0:
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
            else: 
                tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
            count +=1
        

        # add staff label
        txt_title = Label(history_fields, 
          text='Search Login History', 
          font=('arial', 18), 
          fg='#4b8598', 
          bg=white_color)
        txt_title.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        
        # entry_login_user
        lab_login_user = Label(history_fields, 
          text='Login User: ', 
          padx=2, 
          pady=2, 
          font=('arial', 14), 
          fg='grey', 
          bg=white_color)
        lab_login_user.grid(row=1, column=0, sticky='w')
        entry_login_user = Entry(history_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=login_user)
        entry_login_user.grid(row=1, column=1) 

        # login_date
        lab_login_date = Label(history_fields, 
          text='Login Date: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_login_date.grid(row=2, column=0, sticky='w')
        entry_login_date = Entry(history_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2,
          state='normal', 
          textvariable=login_date)
        entry_login_date.grid(row=2, column=1)  
        
        # login_time
        lab_login_time = Label(history_fields, 
          text='Login Time: ', 
          padx=2, 
          pady=2, 
          font=('arial',14), 
          fg='grey', 
          bg=white_color)
        lab_login_time.grid(row=3, column=0, sticky='w')
        entry_login_time = Entry(history_fields, 
          bg='white', 
          width=20, 
          font=('arial',14), 
          bd=2, 
          state='normal',
          textvariable=login_time)
        entry_login_time.grid(row=3, column=1)


        # btn frame
        btn_frame = Frame(history_fields, padx=10, pady=4, relief='flat', bg=white_color)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        # search btn
        search_btn = Button(btn_frame, 
          text='Search', 
          bg='#4b8598', 
          fg='white',
          width=10, 
          relief='flat',
          height=1, 
          font=('arial',12), 
          bd=2, 
          activeforeground='white',
          activebackground='#72404d',
          command=get_search)
        search_btn.grid(row=0, column=0, pady=5, padx=1)   
        
        # clear_btn
        clear_btn = Button(btn_frame, 
          text='Clear', 
          bg='gray', 
          fg='white',
          width=10, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_clearAll)
        clear_btn.grid(row=0, column=1, pady=5, padx=1)

        # delete_one_btn
        delete_one_btn = Button(btn_frame, 
          text='Delete One', 
          bg='gray', 
          fg='white',
          width=10, 
          relief='flat',
          height=1,
          activeforeground='white',
          activebackground='#4b8598',
          font=('arial',12), 
          bd=2, 
          command=get_delete)
        delete_one_btn.grid(row=0, column=2, pady=5, padx=1)   

        # delete btn
        delete_all_btn = Button(btn_frame, 
          text='Delete All', 
          bg='red', 
          relief='flat',
          fg='white',
          width=10, 
          height=1,
          activeforeground='white',
          activebackground='#4b8598', 
          font=('arial',12), 
          bd=2, 
          command=get_delete_all)
        delete_all_btn.grid(row=0, column=3, pady=5, padx=1)       
        
        displayAll()



def close_app(event):
    root.quit()
    exit()


LoginPageView(root)
# StaffHomePageView(root)
# HomePageView(root)

root.bind('<Escape>', close_app)

root.mainloop()



# pyinstaller --onefile -w -i logo.ico --add-data "db.py;." app.py





