import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)

cursor = mydb.cursor()
mydb.autocommit=True


def admin_menu():
    while True:
        print("1. Update product")
        print("2. Delete user")
        print("3. Delete Vendor")
        print("4. Delete Partner")
        print("5 Delete Product")
        print("6. Logout")

        choice = input("Enter Your Choice: ")
        if choice == '1':
            update_product()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            delete_vendor()
        elif choice == "4":
            delete_partner()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Logging Out")
            break
        else:
            print("Invalid Choice")
            admin_menu()


def update_product():
    product_id = input("Enter Product ID: ")
    cursor.execute("SELECT * FROM PRODUCT WHERE Product_id = %s", (product_id,))
    product = cursor.fetchone()
    if product:
        print("1. Update Product Name")
        print("2. Update Product Type")
        print("3. Update Product Price")
        print("4. Update Product Expiry Date")
        print("5. Update Product Rating")
        print("6. Update Product Quantity")
        print("7. Back to Admin Menu")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            product_name = input("Enter New Product Name: ")
            cursor.execute("UPDATE PRODUCT SET Product_name = %s WHERE Product_id = %s", (product_name, product_id))
            mydb.commit()
            print("Product Name Updated Successfully!")
            update_product()
        elif choice == '2':
            product_type = input("Enter New Product Type: ")
            cursor.execute("UPDATE PRODUCT SET Product_type = %s WHERE Product_id = %s", (product_type, product_id))
            mydb.commit()
            print("Product Type Updated Successfully!")
            update_product()
        elif choice == '3':
            product_price = input("Enter New Product Price: ")
            cursor.execute("UPDATE PRODUCT SET Product_price = %s WHERE Product_id = %s", (product_price, product_id))
            mydb.commit()
            print("Product Price Updated Successfully!")
            update_product()
       
        elif choice == '4':
            product_expirydate = input("Enter New expiry date ")
            cursor.execute("UPDATE PRODUCT SET Product_expirydate = %s WHERE Product_id = %s", (product_expirydate, product_id))
            mydb.commit()
            print("Product expiry date Updated Successfully!")
            update_product()

        elif choice == '5':
            product_rating = input("Enter New Product rating: ")
            cursor.execute("UPDATE PRODUCT SET Rating = %s WHERE Product_id = %s", (product_rating, product_id))
            mydb.commit()
            print("Product Price Updated Successfully!")
            update_product()

        elif choice == '6':
            product_price = input("Enter New Product quantity: ")
            cursor.execute("UPDATE PRODUCT SET Product_quantity = %s WHERE Product_id = %s", (product_price, product_id))
            mydb.commit()
            print("Product Price Updated Successfully!")
            update_product()
        elif choice=="7":
            admin_menu()

def delete_user():
    delme=int(input("Enter Customer ID to be deleted: "))
    cursor.execute(f"DELETE FROM Cart WHERE Customer_id={delme}")
    cursor.execute(f"DELETE FROM Rates WHERE Customer_id={delme}")
    cursor.execute(f"DELETE FROM Coupons WHERE Customer_id={delme}")
    cursor.execute(f"DELETE FROM Delivery WHERE Customer_id={delme}")
    cursor.execute(f"DELETE FROM Prescription WHERE Customer_id={delme}")
    cursor.execute(f"DELETE FROM USER WHERE Customer_id={delme}")
    print("User deleted successfully!")


def delete_vendor():
    delme=int(input("Enter Vendor ID to be deleted: "))
    cursor.execute(f"DELETE FROM vendor WHERE Vendor_id={delme}")
    print("Vendor deleted successfully!")

def delete_partner():
    delme=int(input("Enter Partner ID to be deleted: "))
    cursor.execute(f"DELETE FROM Delivery WHERE Partner_id={delme}")
    cursor.execute(f"DELETE FROM Delivery_partner WHERE Partner_id={delme}")
    print("Partner deleted successfully!")

def delete_product():
    delme=int(input("Enter product ID to be deleted: "))
    cursor.execute(f"DELETE FROM Rates WHERE Product_id={delme}")
    cursor.execute(f"DELETE FROM Prescription WHERE Product_id={delme}")
    cursor.execute(f"DELETE FROM Cart WHERE Product_id={delme}")
    cursor.execute(f"DELETE FROM Belongs_to WHERE Product_id={delme}")
    cursor.execute(f"DELETE FROM PRODUCT WHERE Product_id={delme}")
    print("Product deleted successfully!")