import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)

cursor = mydb.cursor()
mydb.autocommit=True

def user_menu(customer_id):
    print("Welcome to the user menu!\n")
    while True:
        print("Please choose an option:")
        print("1. View products")
        print("2. View cart")
        print("3. Add item to cart")
        print("4. Remove item from cart")
        print("5. Place order")
        print("6. View orders")
        print("7. Rate product")
        print("8. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_products()
        elif choice == "2":
            view_cart(customer_id)
        elif choice == "3":
            add_to_cart(customer_id)
        elif choice == "4":
            remove_from_cart(customer_id)
        elif choice == "5":
            place_order(customer_id)
        elif choice == "6":
            view_orders(customer_id)
        elif choice == "7":
            rate_product(customer_id)
        elif choice == "8":
            print("Logging Out...")
            break
        else:
            print("Invalid choice. Please try again.\n")

def view_products():
    # Execute SQL query to retrieve all products
    cursor.execute("SELECT * FROM PRODUCT")
    products = cursor.fetchall()
    
    # Print the product details
    print("Available products:")
    for product in products:
        print(f"Product ID: {product[0]}, Name: {product[1]}, Type: {product[2]}, Price: {product[3]}, Expiry Date: {product[4]}, Rating: {product[5]}, Quantity: {product[6]}")
    print()


def add_to_cart(customer_id):
    # Execute SQL query to check if the customer already has the product in their cart
    product_id = int(input("Enter the Product ID: "))
    quantity = int(input("Enter the Quantity: "))
    
    cursor.execute(f"SELECT * FROM CART WHERE Customer_id = '{customer_id}' AND Product_id = '{product_id}'")
    cart_item = cursor.fetchone()
    
    # If the customer already has the product in their cart, update the quantity
    if cart_item:
        new_quantity = cart_item[2] + quantity
        cursor.execute(f"UPDATE CART SET Product_quantity = '{new_quantity}' WHERE Customer_id = '{customer_id}' AND Product_id = '{product_id}'")
        print(f"{quantity} {product_id}(s) added to cart")
    # Otherwise, add a new cart item
    else:
        cursor.execute(f"INSERT INTO CART (Customer_id, Product_id, Product_quantity) VALUES ('{customer_id}', '{product_id}', '{quantity}')")
        print(f"{quantity} {product_id}(s) added to cart")
    print()
    
def checkout(customer_id):
    cursor.execute(f"SELECT * FROM CART WHERE Customer_id = {customer_id}")
    cart_items = cursor.fetchall()
    if not cart_items:
        print("Your cart is empty.")
    else:
        print("Checking Out....")
        total=0
        for item in cart_items:
            cursor.execute(f"SELECT * FROM product WHERE Product_id = {item[1]}")
            prod=cursor.fetchone()
            if(prod[6]<item[2]):
                print(f"Sorry we only have {prod[6]} {prod[1]} in stock!!!\n")
                print("Going Back Can't Coplete the order")
                return
        for item in cart_items:
            cursor.execute(f"SELECT * FROM product WHERE Product_id = {item[1]}")
            prod=cursor.fetchone()
            cursor.execute(f"UPDATE product set Product_quantity={prod[6]-item[2]} WHERE Product_id = {item[1]}")
            total+=item[2]*prod[3]
        anss = [False, 0]
        inp = input("Do you want to apply coupon(yes/no): ")
        if(inp=="yes"):
            anss = apply_coupon(customer_id, total)
            
        if(anss[0]):
            total = anss[1]
        print(f"Total Order Value: {total}\nTaking you to the payment portal.....\n")
        cursor.execute(f"Insert into ORDERS(Order_value, Customer_id) VALUES({total}, {customer_id})")
        print("Thanks for the purchase.....")
        cursor.execute(f"DELETE FROM CART WHERE Customer_id = {customer_id}")
    cursor.execute(f"SELECT Partner_id FROM delivery_partner")
    partners = cursor.fetchall()
    part = random.choice(partners)[0]
    cursor.execute(f"SELECT max(Order_id) FROM orders")
    order_id = cursor.fetchone()[0]
    cursor.execute(f"Insert into delivery(Order_id, Customer_id, Partner_id, Tracking_Status) VALUES({order_id}, {customer_id}, {part}, 'Pending')")
    

def view_cart(customer_id):
    # Get the cart items for the given customer ID
    cursor.execute(f"SELECT * FROM CART WHERE Customer_id = {customer_id}")
    cart_items = cursor.fetchall()
    if not cart_items:
        print("Your cart is empty.")
    else:
        print("Here are the items in your cart:")
        print("Product | Quantity | Price")
        for item in cart_items:
            cursor.execute(f"SELECT * FROM product WHERE Product_id = {item[1]}")
            prod=cursor.fetchone()
            name=prod[1]
            price = prod[3]
            print(f"Product Name: {name}     Quantity: {item[2]}     Toatl Price: {item[2]*price}")

    # Ask user if they want to checkout or continue shopping
    while True:
        checkout_choice = input("Enter 'c' to checkout or 's' to continue shopping: ")
        if checkout_choice.lower() == "c":
            checkout(customer_id)
            break
        elif checkout_choice.lower() == "s":
            user_menu(customer_id)
            break
        else:
            print("Invalid choice. Please enter 'c' to checkout or 's' to continue shopping.")


def remove_from_cart(customer_id):
    product_id = input("Enter the product ID you want to remove from cart: ")
    cursor.execute(f" DELETE FROM Cart WHERE Customer_id={customer_id} AND Product_id={product_id}")
    print("Product removed from cart successfully!")

def place_order(customer_id):
    checkout(customer_id)

def view_orders(customer_id):
    cursor.execute(f"SELECT * FROM ORDERS WHERE Customer_id={customer_id}")
    orders = cursor.fetchall()
    
    cursor.execute(f"SELECT * FROM USER WHERE Customer_id={customer_id}")
    cus = cursor.fetchone()
    
    
    if not orders:
        print("No orders found!")
        return
    
    for order in orders:
        cursor.execute(f"SELECT * FROM delivery WHERE Order_id={order[0]}")
        delivery = cursor.fetchone()
        print("Order ID: ", order[0])
        print("Delivery Address: ", cus[4])
        print("Order Price: ", order[1])
        print("Delivery Partner ID: ", delivery[2])
        print("Order Status: ", delivery[3])
        print()
        
        
def apply_coupon(customer_id, ord_val):
    totp=0
    cursor.execute(f"SELECT * FROM COUPONS WHERE Customer_id = '{customer_id}'")
    coupons = cursor.fetchall()
    if not coupons:
        print("Sorry you don't have any coupons available!!")
        return [False, 0]
        
    else:
        for i in coupons:
            print(f"Coupon ID:{i[0]}    Coupon Discount: {i[1]}    Coupon Expiry: {i[2]}    Coupon Minimum Order Value: {i[3]}")
            
    coupon_code = input("Enter coupon code: ")
    cursor.execute(f"SELECT * FROM COUPONS WHERE Coupon_id = '{coupon_code}'")
    coupon = cursor.fetchone()
    if not coupon:
        print("Invalid coupon code.")
        apply_coupon(customer_id)
    if(ord_val<coupon[3]):
        print("Sorry you can't apply this coupon as your order value is not enough!!")
        return [False, 0]
    cursor.execute(f"DELETE FROM COUPONS WHERE Coupon_id = '{coupon_code}'")
    
    cursor.execute(f"SELECT * FROM CART WHERE Customer_id = {customer_id}")
    cart_items = cursor.fetchall()

    # Apply the discount to each cart item
    for item in cart_items:
        cursor.execute(f"SELECT * FROM product WHERE Product_id = {item[1]}")
        prod=cursor.fetchone()
        price = prod[3]
        
        new_price = price * (1 - coupon[1] / 100)
        

        totp+=new_price*item[2]

    print("Coupon applied successfully.")
    return [True, totp]

def rate_product(customer_id):
    product_id = int(input("Enter the Product ID: "))
    rating = int(input("Enter the rating (1-10): "))

    cursor.execute(f"SELECT * FROM product WHERE Product_id = {product_id}")
    product = cursor.fetchone()

    if not product:
        print("Invalid product ID.")
        rate_product(customer_id)

    if rating < 1 or rating > 10:
        print("Invalid rating. Please enter a number between 1 and 10.")
        rate_product(customer_id)
    cursor.execute(f"SELECT COUNT(Product_id) FROM rates WHERE Product_id = {product_id}")
    num=cursor.fetchone()
    newrating = (product[5]*num[0] + rating)/(num[0]+1)
    # Insert the rating into the RATES table
    cursor.execute(f"INSERT INTO RATES (Customer_id, Product_id) VALUES ({customer_id}, {product_id})")
    cursor.execute(f"UPDATE PRODUCT SET Rating={round(newrating, 2)} WHERE Product_id = {product_id}")
    print("Thank you for rating this product!")