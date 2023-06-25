import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dbms"
)

cursor = mydb.cursor()
mydb.autocommit=True


def partner_menu():
    while True:
        print("1. Update Delivery Status")
        print("2. Logout")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            update_status()
        elif choice == '2':
            break
        else:
            print("Invalid Choice")
            partner_menu()

def update_status():
    ord_id = input("Enter Order id: ")
    print("Choose option to update the status of Delivery")
    print("1. Delivered")
    print("2. In Transit")
    print("3. Pending")
    d=str("Delivered")
    i=str("In Transit")
    p=str("Pending")
    choice=input("Choice: ")
    if choice =="1": 
        cursor.execute("UPDATE delivery SET Tracking_Status = %s WHERE Order_id =%s", (d,ord_id))
        mydb.commit()
        print("Order status changed to DELIVERED")
    elif choice =="2": 
        cursor.execute("UPDATE delivery SET Tracking_Status = %s WHERE Order_id =%s", (i,ord_id))
        mydb.commit()
        print("Order status changed to IN TRANSIT")
    elif choice =="3": 
        cursor.execute("UPDATE delivery SET Tracking_Status = %s WHERE Order_id =%s", (p,ord_id))
        mydb.commit()
        print("Order status changed to PENDING")


    