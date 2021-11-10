import sqlite3
import time
from time import strftime
from datetime import datetime, date, timedelta 

 # date 
today = date.today()
created_on = today.strftime("%B %d, %Y")

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db) 
        self.cur = self.con.cursor()

        account_sql = """
            CREATE TABLE IF NOT EXISTS account(
                id integer PRIMARY KEY AUTOINCREMENT,
                username char,
                mobile char,
                dob char,
                password char,
                designation char

            )
        """
        self.cur.execute(account_sql)
        self.con.commit()

        room_sql = """
            CREATE TABLE IF NOT EXISTS rooms(
                id integer PRIMARY KEY AUTOINCREMENT,
                room_number char,
                room_type char,
                room_price text
            )
        """
        self.cur.execute(room_sql)
        self.con.commit()

        food_sql = """
            CREATE TABLE IF NOT EXISTS foods(
                id integer PRIMARY KEY AUTOINCREMENT, 
                name char, 
                unit_cost real
            )
        """
        self.cur.execute(food_sql) 
        self.con.commit()

        drink_sql = """
            CREATE TABLE IF NOT EXISTS drinks(
                id integer PRIMARY KEY AUTOINCREMENT, 
                name char, 
                unit_cost real
            )
        """
        self.cur.execute(drink_sql) 
        self.con.commit()

        customer_sql = """
            CREATE TABLE IF NOT EXISTS customers(
                id integer PRIMARY KEY, 
                fname char(50),
                lname char(50), 
                mobile char(50), 
                email char(50) NULL
            )
        """
        self.cur.execute(customer_sql)
        self.con.commit()

        booking_sql = """
            CREATE TABLE IF NOT EXISTS bookings(
                id integer PRIMARY KEY AUTOINCREMENT, 
                fname char(50),
                lname char(50), 
                mobile char(50),
                address char(50),
                email char(50),
                car_reg_no char(50),
                means_of_id char(50),
                traveling_from char(50),
                traveling_to char(50),
                room_number integer,
                room_type char(20),
                room_price real,
                check_in_date text,
                check_out_date text,
                party char(50),
                discount real,
                total_cost real, 
                bill_ref text
            )
        """
        self.cur.execute(booking_sql)
        self.con.commit()

        order_food_sql = """
            CREATE TABLE IF NOT EXISTS order_food(
                id integer PRIMARY KEY AUTOINCREMENT, 
                fname char(50),
                lname char(50), 
                mobile char(50),
                food_name text, 
                unit_cost real,
                quantity text,
                total_cost text
            )
        """
        self.cur.execute(order_food_sql) 
        self.con.commit()

        order_drink_sql = """
            CREATE TABLE IF NOT EXISTS order_drink(
                id integer PRIMARY KEY AUTOINCREMENT, 
                fname char(50),
                lname char(50), 
                mobile char(50),
                drink_name text, 
                unit_cost real,
                quantity text,
                total_cost text 
            )
        """
        self.cur.execute(order_drink_sql) 
        self.con.commit()


        booking_activity_sql = """
            CREATE TABLE IF NOT EXISTS booking_activity(
                id integer PRIMARY KEY AUTOINCREMENT, 
                mobile text,
                room_number char,
                room_price char,
                check_in_date text,
                check_out_date text,
                discount char,
                total_cost real,
                created_date text,
                created_time text
            )
        """
        self.cur.execute(booking_activity_sql) 
        self.con.commit()

        order_food_activity_sql = """
            CREATE TABLE IF NOT EXISTS order_food_activity(
                id integer PRIMARY KEY AUTOINCREMENT, 
                food_name text, 
                quantity text,
                total_cost text, 
                created_date text,
                created_time text
            )
        """
        self.cur.execute(order_food_activity_sql) 
        self.con.commit()

        order_drink_activity_sql = """
            CREATE TABLE IF NOT EXISTS order_drink_activity(
                id integer PRIMARY KEY AUTOINCREMENT, 
                drink_name text, 
                quantity text,
                total_cost text, 
                created_date text,
                created_time text
            )
        """
        self.cur.execute(order_drink_activity_sql) 
        self.con.commit()

        store_sql = """
            CREATE TABLE IF NOT EXISTS store(
                id integer PRIMARY KEY AUTOINCREMENT, 
                name text, 
                quantity text,
                unit text,
                unit_cost real,
                total_cost text
            )
        """
        self.cur.execute(store_sql) 
        self.con.commit()


        store_usage_sql = """
            CREATE TABLE IF NOT EXISTS store_usage(
                id integer PRIMARY KEY AUTOINCREMENT, 
                name text, 
                qty_use text,
                qty_remain text, 
                created_date text
            )
        """
        self.cur.execute(store_usage_sql) 
        self.con.commit()

        login_history_sql = """
            CREATE TABLE IF NOT EXISTS login_history(
                id integer PRIMARY KEY, 
                login_user text, 
                login_date text, 
                login_time text
            )
        """ 
        self.cur.execute(login_history_sql)
        self.con.commit()


    # login history 
    def insert_login_history(self, login_user, login_date, login_time):
        self.cur.execute("INSERT INTO login_history VALUES(NULL,?,?,?)",
            (login_user, login_date, login_time))
        self.con.commit()

    def fetch_login_history(self):
        self.cur.execute("SELECT * FROM login_history ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def search_login_history(self, login_user, login_date, login_time):
        self.cur.execute("SELECT * FROM login_history WHERE login_user=? OR login_date=? OR login_time=?", 
            (login_user, login_date, login_time))
        rows = self.cur.fetchall()
        return rows 

    def remove_login_history(self, id):
        self.cur.execute("DELETE FROM login_history WHERE id=?", (id,)) 
        self.con.commit()

    def remove_all_login_history(self):
        self.cur.execute("DELETE FROM login_history") 
        self.con.commit()


    # store_usage 
    def insert_store_usage(self, name, qty_use, qty_remain, created_date):
        self.cur.execute("INSERT INTO store_usage VALUES(NULL,?,?,?,?)",
            (name, qty_use, qty_remain, created_date))
        self.con.commit()

    def update_store_usage(self, id, name, qty_use, qty_remain, created_date):
        self.cur.execute("UPDATE store_usage SET name=?, qty_use=?, qty_remain=?, created_date=? WHERE id=?", 
            (name, qty_use, qty_remain, created_date, id,))
        self.con.commit()

    def fetch_store_usage(self):
        self.cur.execute("SELECT * FROM store_usage ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def search_store_usage(self, name, qty_use, qty_remain, created_date):
        self.cur.execute("SELECT * FROM store_usage WHERE name=? OR qty_use=? OR qty_remain=? OR created_date=?", 
            (name, qty_use, qty_remain, created_date))
        rows = self.cur.fetchall()
        return rows 

    def remove_store_usage(self, id):
        self.cur.execute("DELETE FROM store_usage WHERE id=?", (id,)) 
        self.con.commit()


    # store 
    def insert_store(self, name, quantity, unit, unit_cost, total_cost):
        self.cur.execute("INSERT INTO store VALUES(NULL,?,?,?,?,?)",
            (name, quantity, unit, unit_cost, total_cost))
        self.con.commit()

    def update_store(self, id, name, quantity, unit, unit_cost, total_cost):
        self.cur.execute("UPDATE store SET name=?, quantity=?, unit=?, unit_cost=?, total_cost=? WHERE id=?", 
            (name, quantity, unit, unit_cost,total_cost, id,))
        self.con.commit()

    def update_store_qty(self, id, quantity):
        self.cur.execute("UPDATE store SET quantity=? WHERE id=?", 
            (quantity, id,))
        self.con.commit()

    def fetch_store(self):
        self.cur.execute("SELECT * FROM store ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def search_store(self, name, quantity, unit, unit_cost, total_cost):
        self.cur.execute("SELECT * FROM store WHERE name=? OR quantity=? OR unit=? OR unit_cost=? OR total_cost=?", 
            (name, quantity, unit, unit_cost, total_cost))
        rows = self.cur.fetchall()
        return rows 

    def get_store_items(self):
        self.cur.execute("SELECT id, name FROM store") 
        rows = self.cur.fetchall()
        return rows

    def get_store_details(self, name):
        self.cur.execute("SELECT * FROM store WHERE name=?", (name,))
        rows = self.cur.fetchall()
        return rows

    def remove_store(self, id):
        self.cur.execute("DELETE FROM store WHERE id=?", (id,)) 
        self.con.commit()


    # account
    def insert_account(self, username, mobile, dob, password, designation):
        self.cur.execute("INSERT INTO account VALUES (NULL, ?, ?, ?, ?, ?)", 
            (username, mobile, dob, password, designation))
        self.con.commit() 

    def fetch_account(self):
        self.cur.execute("SELECT * FROM account")
        rows = self.cur.fetchall()
        return rows 

    def search_account(self, username, mobile, dob, password, designation):
        self.cur.execute("SELECT * FROM account WHERE username=? OR mobile=? OR dob=? OR password=? OR designation=?", 
            (username, mobile, dob, password, designation))
        rows = self.cur.fetchall()
        return rows 

    def login_account(self, username, password, designation):
        self.cur.execute("SELECT username, password, designation FROM account WHERE username=? AND  password=? AND designation=?", 
            (username, password, designation))
        rows = self.cur.fetchone()
        return rows 

    def remove_account(self, id):
        self.cur.execute("DELETE FROM account WHERE id=?", (id,)) 
        self.con.commit()

    def update_account(self, id, username, mobile, dob, password, designation):
        self.cur.execute("UPDATE account SET username=?, mobile=?, dob=?, password=?, designation=? WHERE id=?", 
            (username, mobile, dob, password, designation, id,))
        self.con.commit()


    # order_drink_activity 
    def insert_drink_activity(self, drink_name, quantity, total_cost, created_date, created_time):
        self.cur.execute("INSERT INTO order_drink_activity VALUES(NULL,?,?,?,?,?)",
            (drink_name, quantity, total_cost, created_date, created_time))
        self.con.commit()

    def fetch_drink_activity(self):
        self.cur.execute("SELECT * FROM order_drink_activity ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def search_drink_activity(self, drink_name, quantity, total_cost, created_date, created_time):
        self.cur.execute("SELECT * FROM order_drink_activity WHERE drink_name=? OR quantity=? OR total_cost=? OR created_date=? OR created_time=?", 
            (drink_name, quantity, total_cost, created_date, created_time))
        rows = self.cur.fetchall()
        return rows 

    def remove_drink_activity(self, id):
        self.cur.execute("DELETE FROM order_drink_activity WHERE id=?", (id,)) 
        self.con.commit()

    def remove_all_drink_activity(self):
        self.cur.execute("DELETE FROM order_drink_activity") 
        self.con.commit()

    def sum_drink_activity(self):
        self.cur.execute("SELECT SUM(total_cost) FROM order_drink_activity")
        rows = self.cur.fetchall()
        return rows 

    def daily_drink_order(self):
        self.cur.execute(f"SELECT SUM(total_cost) FROM order_drink_activity WHERE created_date='{created_on}'")
        rows = self.cur.fetchall()
        return rows

    # order_food_activity 
    def insert_food_activity(self, food_name, quantity, total_cost, created_date, created_time):
        self.cur.execute("INSERT INTO order_food_activity VALUES(NULL,?,?,?,?,?)",
            (food_name, quantity, total_cost, created_date, created_time))
        self.con.commit()

    def fetch_food_activity(self):
        self.cur.execute("SELECT * FROM order_food_activity ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def search_food_activity(self, food_name, quantity, total_cost, created_date, created_time):
        self.cur.execute("SELECT * FROM order_food_activity WHERE food_name=? OR quantity=? OR total_cost=? OR created_date=? OR created_time=?", 
            (food_name, quantity, total_cost, created_date, created_time))
        rows = self.cur.fetchall()
        return rows 

    def remove_food_activity(self, id):
        self.cur.execute("DELETE FROM order_food_activity WHERE id=?", (id,)) 
        self.con.commit()

    def remove_all_food_activity(self):
        self.cur.execute("DELETE FROM order_food_activity") 
        self.con.commit()

    def sum_food_activity(self):
        self.cur.execute("SELECT SUM(total_cost) FROM order_food_activity")
        rows = self.cur.fetchall()
        return rows 

    def daily_food_order(self):
        self.cur.execute(f"SELECT SUM(total_cost) FROM order_food_activity WHERE created_date='{created_on}'")
        rows = self.cur.fetchall()
        return rows


    # booking_activity 
    def insert_booking_activity(self, mobile, room_number, room_price, check_in_date, check_out_date, discount, total_cost, created_date, created_time):
        self.cur.execute("INSERT INTO booking_activity VALUES(NULL,?,?,?,?,?,?,?,?,?)",
            (mobile, room_number, room_price, check_in_date, check_out_date, discount, total_cost, created_date, created_time))
        self.con.commit()

    def fetch_booking_activity(self):
        self.cur.execute("SELECT * FROM booking_activity ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def search_booking_activity(self, mobile, room_number, room_price, check_in_date, check_out_date, total_cost, created_date, created_time):
        self.cur.execute("SELECT * FROM booking_activity WHERE mobile=? OR room_number=? OR room_price=? OR check_in_date=? OR check_out_date=? OR total_cost=? OR created_date=? OR created_time=?", 
            (mobile, room_number, room_price, check_in_date, check_out_date, total_cost, created_date, created_time))
        rows = self.cur.fetchall()
        return rows 

    def remove_booking_activity(self, id):
        self.cur.execute("DELETE FROM booking_activity WHERE id=?", (id,)) 
        self.con.commit()

    def remove_all_booking_activity(self):
        self.cur.execute("DELETE FROM booking_activity") 
        self.con.commit() 

    def sum_booking_activity(self):
        self.cur.execute("SELECT SUM(total_cost) FROM booking_activity")
        rows = self.cur.fetchall()
        return rows 

    def daily_booking(self):
        self.cur.execute(f"SELECT SUM(total_cost) FROM booking_activity WHERE created_date='{created_on}'")
        rows = self.cur.fetchall()
        return rows


    # rooms table
    def fetch_room(self):
        self.cur.execute("SELECT * FROM rooms ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows 

    def count_rooms(self):
        self.cur.execute("SELECT COUNT (*) FROM rooms")
        rows = self.cur.fetchall()
        return rows 

    def search_room(self, room_number, room_type, room_price):
        self.cur.execute("SELECT * FROM rooms WHERE room_number=? OR room_type=? OR room_price=?", 
            (room_number, room_type, room_price))
        rows = self.cur.fetchall()
        return rows 

    def insert_room(self, room_number, room_type, room_price):
        self.cur.execute("INSERT INTO rooms VALUES(NULL, ?, ?, ?)", 
            (room_number, room_type, room_price))
        self.con.commit()

    def update_room(self, id, room_number, room_type, room_price):
        self.cur.execute("UPDATE rooms SET room_number=?, room_type=?, room_price=? WHERE id=?", 
            (room_number, room_type, room_price, id,))
        self.con.commit()

    def remove_room(self, id):
        self.cur.execute("DELETE FROM rooms WHERE id=?", (id,))
        self.con.commit()

    def get_rooms_option(self):
        self.cur.execute("SELECT id, room_number FROM rooms")
        rows = self.cur.fetchall()
        return rows 

    def get_all_available_rooms(self):
        self.cur.execute("SELECT room_number FROM rooms") 
        rows = self.cur.fetchall()
        return rows

    def get_rooms_detail(self, room_number):
        self.cur.execute("SELECT * FROM rooms WHERE room_number=?", (room_number,))
        rows = self.cur.fetchall()
        return rows 


    # foods table
    def insert_food(self, name, unit_cost):
        self.cur.execute("INSERT INTO foods VALUES(NULL, ?, ?)", (name, unit_cost))
        self.con.commit()

    def fetch_food(self):
        self.cur.execute("SELECT * FROM foods ORDER BY id DESC")
        rows = self.cur.fetchall()
        return rows 

    def count_foods(self):
        self.cur.execute("SELECT COUNT (*) FROM foods")
        rows = self.cur.fetchall()
        return rows

    def search_food(self, name, unit_cost):
        self.cur.execute("SELECT * FROM foods WHERE name=? OR unit_cost=?", (name, unit_cost)) 
        rows = self.cur.fetchall()
        return rows 

    def remove_food(self, id):
        self.cur.execute("DELETE FROM foods WHERE id=?", (id,)) 
        self.con.commit()

    def update_food(self, id, name, unit_cost):
        self.cur.execute("UPDATE foods SET name=?, unit_cost=? WHERE id=?", (name, unit_cost, id,))
        self.con.commit() 

    def get_foods_option(self):
        self.cur.execute("SELECT id, name FROM foods")
        rows = self.cur.fetchall()
        return rows 

    def get_foods_details(self, name):
        self.cur.execute("SELECT * FROM foods WHERE name=?", (name,))
        rows = self.cur.fetchall()
        return rows 


    # drinks table
    def insert_drink(self, name, unit_cost):
        self.cur.execute("INSERT INTO drinks VALUES(NULL, ?, ?)", (name, unit_cost))
        self.con.commit()

    def fetch_drink(self):
        self.cur.execute("SELECT * FROM drinks ORDER BY id DESC")
        rows = self.cur.fetchall()
        return rows 

    def count_drinks(self):
        self.cur.execute("SELECT COUNT (*) FROM drinks")
        rows = self.cur.fetchall()
        return rows

    def search_drink(self, name, unit_cost):
        self.cur.execute("SELECT * FROM drinks WHERE name=? OR unit_cost=?", (name, unit_cost)) 
        rows = self.cur.fetchall()
        return rows 

    def remove_drink(self, id):
        self.cur.execute("DELETE FROM drinks WHERE id=?", (id,)) 
        self.con.commit()

    def update_drink(self, id, name, unit_cost):
        self.cur.execute("UPDATE drinks SET name=?, unit_cost=? WHERE id=?", (name, unit_cost, id,))
        self.con.commit()

    def get_drink_option(self):
        self.cur.execute("SELECT id, name FROM drinks")
        rows = self.cur.fetchall()
        return rows 

    def get_drink_details(self, name):
        self.cur.execute("SELECT * FROM drinks WHERE name=?", (name,))
        rows = self.cur.fetchall()
        return rows 


    # customers table
    def insert_customer(self, fname, lname, mobile, email):
        self.cur.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?, ?)", 
            (fname, lname, mobile, email))
        self.con.commit() 

    def fetch_customer(self):
        self.cur.execute("SELECT * FROM customers ORDER BY id DESC")
        rows = self.cur.fetchall()
        return rows

    def count_customers(self):
        self.cur.execute("SELECT COUNT (*) FROM customers")
        rows = self.cur.fetchall()
        return rows

    def search_customer(self, fname, lname, mobile, email):
        self.cur.execute("SELECT * FROM customers WHERE fname=? OR lname=? OR mobile=? OR email=?", 
            (fname, lname, mobile, email))
        rows = self.cur.fetchall()
        return rows 

    def search_customer_for_booking(self, fname, lname, mobile, email):
        self.cur.execute("SELECT * FROM customers WHERE fname=? OR lname=? OR mobile=? OR email=?", 
            (fname, lname, mobile, email))
        rows = self.cur.fetchmany()
        return rows


    def search_customer_for_order(self, fname, lname, mobile):
        self.cur.execute("SELECT * FROM customers WHERE fname=? OR lname=? OR mobile=?", 
            (fname, lname, mobile))
        rows = self.cur.fetchmany()
        return rows

    def remove_customer(self, id):
        self.cur.execute("DELETE FROM customers WHERE id=?", (id,)) 
        self.con.commit()
    
    def update_customer(self, id, fname, lname, mobile, email):
        self.cur.execute("UPDATE customers SET fname=?, lname=?, mobile=?, email=? WHERE id=?", 
             (fname, lname, mobile, email, id,))
        self.con.commit()

# fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref

     # bookings table
    def insert_booking(self, fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref):
        self.cur.execute("INSERT INTO bookings VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
            (fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref))
        self.con.commit() 

    def fetch_booking(self):
        self.cur.execute("SELECT * FROM bookings ORDER BY id DESC") 
        rows = self.cur.fetchall()
        return rows

    def count_bookings(self):
        self.cur.execute("SELECT COUNT (*) FROM bookings")
        rows = self.cur.fetchall()
        return rows

    def search_booking(self, fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref):
        self.cur.execute("SELECT * FROM bookings WHERE fname=? OR lname=? OR mobile=? OR address=? OR email=? OR car_reg_no=? OR means_of_id=? OR traveling_from=? OR traveling_to=? OR room_number=? OR room_type=? OR room_price=? OR check_in_date=? OR check_out_date=? OR party=? OR discount=? OR total_cost=? OR bill_ref=?", 
            (fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref))
        rows = self.cur.fetchall()
        return rows 

    def get_occupied_booking_rooms(self):
        self.cur.execute("SELECT room_number FROM bookings") 
        rows = self.cur.fetchall()
        return rows

    def remove_booking(self, id):
        self.cur.execute("DELETE FROM bookings WHERE id=?", (id,))
        self.con.commit()

    def update_booking(self, id, fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref):
        self.cur.execute("UPDATE bookings SET fname=?, lname=?, mobile=?, address=?, email=?, car_reg_no=?, means_of_id=?, traveling_from=?, traveling_to=?, room_number=?, room_type=?, room_price=?, check_in_date=?, check_out_date=?, party=?, discount=?, total_cost=?, bill_ref=? WHERE id=?", 
            (fname, lname, mobile, address, email, car_reg_no, means_of_id, traveling_from, traveling_to, room_number, room_type, room_price, check_in_date, check_out_date, party, discount, total_cost, bill_ref, id,))
        self.con.commit()


    # order_food table
    def insert_order_food(self, fname, lname, mobile, food_name, unit_cost, quantity, total_cost):
        self.cur.execute("INSERT INTO order_food VALUES(NULL,  ?, ?, ?, ?, ?, ?, ?)", (fname, lname, mobile, food_name, unit_cost, quantity, total_cost))
        self.con.commit()

    def fetch_order_food(self):
        self.cur.execute("SELECT * FROM order_food ORDER BY id DESC")
        rows = self.cur.fetchall()
        return rows 

    def search_order_food(self, fname, lname, mobile, food_name, unit_cost, quantity, total_cost):
        self.cur.execute("SELECT * FROM order_food WHERE fname=? OR lname=? OR mobile=? OR food_name=? OR unit_cost=? OR quantity=? OR total_cost=?", (fname, lname, mobile, food_name, unit_cost, quantity, total_cost)) 
        rows = self.cur.fetchall()
        return rows 

    def remove_order_food(self, id):
        self.cur.execute("DELETE FROM order_food WHERE id=?", (id,)) 
        self.con.commit()

    def update_order_food(self, id, fname, lname, mobile, food_name, unit_cost, quantity, total_cost):
        self.cur.execute("UPDATE order_food SET fname=?, lname=?, mobile=?, food_name=?, unit_cost=?, quantity=?, total_cost=? WHERE id=?", (fname, lname, mobile, food_name, unit_cost, quantity, total_cost, id,))
        self.con.commit()


    # order_drink table
    def insert_order_drink(self, fname, lname, mobile, drink_name, unit_cost, quantity, total_cost):
        self.cur.execute("INSERT INTO order_drink VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", (fname, lname, mobile, drink_name, unit_cost, quantity, total_cost))
        self.con.commit()

    def fetch_order_drink(self):
        self.cur.execute("SELECT * FROM order_drink ORDER BY id DESC")
        rows = self.cur.fetchall()
        return rows 

    def search_order_drink(self, fname, lname, mobile, drink_name, unit_cost, quantity, total_cost):
        self.cur.execute("SELECT * FROM order_drink WHERE fname=? OR lname=? OR mobile=? OR drink_name=? OR unit_cost=? OR quantity=? OR total_cost=?", (fname, lname, mobile, drink_name, unit_cost, quantity, total_cost)) 
        rows = self.cur.fetchall()
        return rows 

    def remove_order_drink(self, id):
        self.cur.execute("DELETE FROM order_drink WHERE id=?", (id,)) 
        self.con.commit()

    def update_order_drink(self, id, fname, lname, mobile, drink_name, unit_cost, quantity, total_cost):
        self.cur.execute("UPDATE order_drink SET fname=?, lname=?, mobile=?, drink_name=?, unit_cost=?, quantity=?, total_cost=? WHERE id=?", (fname, lname, mobile, drink_name, unit_cost, quantity, total_cost, id,))
        self.con.commit()



    
result = Database("shalele_hotel_db.db")
print(result)


