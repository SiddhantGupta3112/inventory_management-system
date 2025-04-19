import mysql.connector as sql
from datetime import date, timedelta

# Function to check products for sale and sort them into their respective categories
def autoorder():
    print("Inside autoorder function")

    def productCheck():
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234",
        )
        cursor = connection.cursor()
        cursor.execute('USE Inventory')
        cursor.execute("SELECT productID FROM Product")
        products = cursor.fetchall()

        produce = []
        dairy = []
        grocery = []

        for i in products:
            if i[0][0] == "P":
                produce.append(i)
            elif i[0][0] == "D":
                dairy.append(i)
            else:
                grocery.append(i)
        connection.close()
        return produce, dairy, grocery

    produce, dairy, grocery = productCheck()

    def reorderCategory(category):
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234",
        )
        cursor = connection.cursor()
        cursor.execute('USE Inventory')

        for ele in category:
            cmd4 = '''
            SELECT productName from product
            WHERE productID = %s
            '''
            parameter4 = (ele[0],)
            cursor.execute(cmd4, parameter4)
            productName = cursor.fetchall()[0][0]

            cmd = '''
            SELECT saleAmount FROM sale
            WHERE productID = %s AND saleDate = %s
            '''
            saleDate = date.today() - timedelta(days=1)
            parameters = (ele[0], saleDate)
            cursor.execute(cmd, parameters)
            result = cursor.fetchall()
            saleAmount = sum(int(sale[0]) for sale in result)

            cmd2 = '''
            SELECT purchaseCost From product
            WHERE productID = %s
            '''
            parameters2 = (ele[0],)
            cursor.execute(cmd2, parameters2)
            price = cursor.fetchall()[0][0]

            quantitySold = saleAmount / int(price)

            cmd3 = '''
            SELECT quantity from product
            where productID = %s
            '''
            parameters3 = (ele[0],)
            cursor.execute(cmd3, parameters3)
            stock = cursor.fetchall()[0][0]

            orderQuantity = 0  # Initialize orderQuantity here

            if quantitySold - stock > 0:
                orderQuantity = (quantitySold - stock) * 1.25
            else:
                print("No order needed")

            costPrice = float(orderQuantity) * float(price)
            print(f"{int(orderQuantity)} units of {productName} are needed to be purchased")
            print("Would you like the order to proceed as is or order a different quantity")
            response = input("Type /p to Proceed or /c to Change the order: ")

            if response.lower() == '/p':
                pass  # No need to modify orderQuantity if proceeding
            elif response.lower() == '/c':
                orderQuantity = int(input("Enter units to be ordered: "))

            orderMessage = f"Ordered {int(orderQuantity)} units of {productName} for cost price {int(costPrice)} @ {price} / unit \n"

            with open("order.txt", "a") as f:
                f.write(orderMessage)

            cmd5 = '''
            UPDATE product
            SET quantity = quantity + %s
            WHERE productID = %s
            '''
            parameter5 = (orderQuantity, ele[0])
            cursor.execute(cmd5, parameter5)
            connection.commit()

            cmd6 = '''
            SELECT purchaseID from Purchase
            '''
            cursor.execute(cmd6)
            purchaseID = int(cursor.fetchall()[-1][0]) + 1

            cmd7 = '''
            INSERT INTO purchase
            VALUES (%s, %s, %s, %s)
            '''
            parameter7 = (purchaseID, ele[0], costPrice, date.today())
            cursor.execute(cmd7, parameter7)
            connection.commit()

    reorderCategory(produce)
    reorderCategory(dairy)
    reorderCategory(grocery)

# Uncomment the line below to test the autoorder function
#autoorder()