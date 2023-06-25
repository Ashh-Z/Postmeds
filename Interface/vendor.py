import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)

cursor = mydb.cursor()
mydb.autocommit=True

# Vendor Menu
def vendor_menu():
    while True:
        print("1. Add Product")
        print("2. Logout")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            print("Logging Out...")
        else:
            print("Invalid Choice")
            vendor_menu()

def add_product():
    cursor.execute("SELECT MAX(Product_id) FROM Product")
    result = cursor.fetchone()
    product_id = result[0]+1
    product_name = input("Enter Product Name: ")
    product_type = input("Enter Product Type: ")
    product_price = float(input("Enter Product Price: "))
    product_expirydate = input("Enter Product Expiry Date (YYYY-DD-MM): ")
    rating = 0.0
    product_quantity = input("Enter Product Quantity: ")
    cursor.execute("INSERT INTO PRODUCT (Product_id,Product_name, Product_type, Product_price, Product_expirydate, Rating, Product_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)", (product_id,product_name, product_type, product_price, product_expirydate, rating, product_quantity))
    print("Product Added Successfully!")
    vendor_menu()
