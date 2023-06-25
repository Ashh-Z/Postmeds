import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)

cursor = mydb.cursor()
mydb.autocommit=True

def register():
    print("1. Register as Vendor")
    print("2. Reister as User")
    print("3. Register as Delivery Partner")
    print("4. Back")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        register_vendor()
    elif choice == "2":
        register_user()
    elif choice == "3":
        register_del_part()
    elif choice == "4":
        print("Returning...")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        register()

def register_vendor():
    print("Please enter the following details:")
    vendor_username = input("Vendor Username: ")
    vendor_number = input("Vendor Phone Number: ")
    vendor_password = input("Vendor Password: ")

    #new vendor_id for new vendor
    query = f"INSERT INTO VENDOR (Vendor_username, Vendor_number, Vendor_password) VALUES ('{vendor_username}', '{vendor_number}', '{vendor_password}')"
    cursor.execute(query)
    print("Vendor registered successfully!")

def register_user():
    print("Please enter the following details:")
    customer_name = input("Customer Name: ")
    customer_number = input("Customer Phone Number: ")
    customer_password = input("Customer Password: ")
    customer_address = input("Customer Address: ")
    is_premium_subscriber = input("Is Premium Subscriber (yes/no): ")
    if is_premium_subscriber=="yes":
        cock = 1
    else:
        cock = 0
    age = int(input("Age: "))
    

    cursor.execute("SELECT MAX(Customer_id) FROM USER")
    result = cursor.fetchone()
    Customer_id = result[0]+1

    #unique customer ID
    query = f"INSERT INTO USER (Customer_id, Customer_name, Customer_password, Customer_number, Customer_address, isPremium_subscriber, Age) VALUES ('{Customer_id}' ,  '{customer_name}', '{customer_password}', '{customer_number}', '{customer_address}', '{cock}', {age})"
    cursor.execute(query)
    print("User registered successfully!")


def register_del_part():
    print("Please enter the following details:")
    del_username = input("Delivery Partner Username: ")
    del_number = input("Delivery Partner Phone Number: ")
    del_password = input("Delivery Partner Password: ")
    cursor.execute("SELECT MAX(Partner_id) FROM Delivery_Partner")
    result = cursor.fetchone()
    Partner_id = result[0]+1
    query = f"INSERT INTO Delivery_Partner (Partner_id,Partner_username, Partner_number, Partner_password) VALUES ('{Partner_id}' ,  '{del_username}', '{del_number}', '{del_password}')"
    cursor.execute(query)
    print("Partner registered successfully!")
    