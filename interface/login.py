import mysql.connector
from vendor import *
from user import *
from partner import *
from admin import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)

cursor = mydb.cursor()
mydb.autocommit=True

def login():
    print("1. Login as Vendor")
    print("2. Login as User")
    print("3. Login as Delivery Partner")
    print("4. Login as Admin")
    print("5. Back")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        vendor_login()
    elif choice == "2":
        user_login()
    elif choice == "3":
        partner_login()
    elif choice == "4":
        admin_login()
    elif choice == "5":
        print("Returning...")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        login()

def vendor_login():
    vendor_username = input("Enter Vendor Username: ")
    vendor_password = input("Enter Vendor Password: ")
    cursor.execute("SELECT * FROM Vendor WHERE Vendor_username = %s AND Vendor_password = %s", (vendor_username, vendor_password))
    vendor = cursor.fetchone()
    if vendor:
        print("Vendor Logged in Successfully!")
        vendor_menu()
    else:
        print("Invalid Login Credentials")

def user_login():
    user_name=input("Enter user name: ")
    user_password=input("Enter password: ")
    cursor.execute("SELECT customer_id FROM User WHERE customer_name = %s AND customer_password = %s", (user_name,user_password))
    user = cursor.fetchone()
    if user:
        print("User Logged in Successfully!")
        user_menu(user[0])
    else:
        print("Invalid Login Credentials")

def partner_login():
    partner_name=input("Enter user name: ")
    partner_password=input("Enter password: ")
    cursor.execute("SELECT * FROM Delivery_partner WHERE Partner_username = %s AND Partner_password = %s", (partner_name,partner_password))
    user = cursor.fetchone()
    if user:
        print("Delivery Partner Logged in Successfully!")
        partner_menu()
    else:
        print("Invalid Login Credentials")

def admin_login():
    admin_name=input("Enter user name: ")
    admin_password=input("Enter password: ")
    cursor.execute("SELECT * FROM Admin WHERE Admin_username = %s AND Admin_password = %s", (admin_name,admin_password))
    user = cursor.fetchone()
    if user:
        print("Admin Logged in Successfully!")
        admin_menu()
    else:
        print("Invalid Login Credentials")
