import mysql.connector
from register import *
from login import *

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)



# MAIN MENU
# /////////////////////////////////////////////////////////////
def main():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid")

main()


# # //////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////////