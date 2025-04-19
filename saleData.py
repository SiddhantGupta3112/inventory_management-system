import mysql.connector as sql
from tabulate import tabulate
from datetime import date

def order_function():
    connection = sql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Inventory"
    )
    cursor = connection.cursor()

    def display_menu():
        cursor.execute('SELECT productName from product')
        menu = cursor.fetchall()
        print("AVAILABLE ITEMS")
        table = []
        for ele in menu:
            for items in ele:
                table.append([items])
        print(tabulate(table, headers=["Product Name"]))

    print("Type /m to display the menu")
    order = []

    while True:
        product = input("Enter product for purchase: ")

        if product.lower() == '/m':
            display_menu()
            continue

        cmd = '''
        SELECT productID FROM product
        WHERE productName = %s
        '''
        cursor.execute(cmd, (product,))
        productID = cursor.fetchall()

        if len(productID) > 0:
            print("*Note: Quantity for produce must be in kg, while quantity for dairy and grocery must be in units to be bought")
            quantity = int(input("Enter quantity for purchase: "))

            cmd2 = '''
            SELECT quantity FROM product 
            WHERE productID = %s
            '''
            cursor.execute(cmd2, (productID[0][0],))
            stock = int(cursor.fetchall()[0][0])

            if stock >= quantity:
                cmd3 = '''
                UPDATE product
                SET quantity = quantity - %s
                WHERE productID = %s
                '''
                parameter3 = (quantity, productID[0][0])
                cursor.execute(cmd3, parameter3)
                connection.commit()

                cmd4 = '''
                SELECT productCost FROM product
                WHERE productID = %s
                '''
                cursor.execute(cmd4, (productID[0][0],))
                price = int(cursor.fetchall()[0][0])

                total = int(price) * int(quantity)

                cmd5 = '''
                INSERT INTO sale (productID, saleAmount, saleDate)
                VALUES (%s, %s, %s)
                '''
                saleDate = date.today()
                cursor.execute(cmd5, (productID[0][0], total, saleDate))
                connection.commit()

                order.append((product, quantity, price, total))

            else:
                print("Unfortunately, we don't have enough. We only have {} units of {}. Please enter another amount.".format(stock, product))
                continue

            response = input("Would you like to purchase another item? (Type '/y' to purchase or '/n' to move to transaction): ")
            if response.lower() == '/n':
                print("YOUR BILL IS: ")
                print(tabulate(order, headers=["Item", "Quantity", "Price", "Subtotal"]))

                grand_total = sum(ele[3] for ele in order)
                print("Your Grand Total is " + str(grand_total))
                break

        else:
            print("Product not found. Please try again.")

    cursor.close()
    connection.close()

# Uncomment the following line if you want to test this file individually
#order_function()