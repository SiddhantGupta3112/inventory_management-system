import mysql.connector
from datetime import datetime, timedelta
import random


def demodata():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Inventory"
    )

    cursor = connection.cursor()

    productData = [
        ("P-0001", "Onion", 10, 100),
        ("P-0002", "Potato", 10, 100),
        ("P-0003", "Tomato", 10, 100),
        ("P-0004", "Brinjal", 10, 100),
        ("P-0005", "Green Chilli", 10, 100),
        ("P-0006", "Cauliflower", 10, 100),
        ("P-0007", "Lady Finger", 10, 100),
        ("P-0008", "Cabbage", 10, 100),
        ("P-0009", "Cucumber", 10, 100),
        ("P-0010", "Bitter Gourd", 10, 100),
        ("P-0011", "Carrot", 10, 100),
        ("P-0012", "Pumpkin", 10, 100),
        ("P-0013", "Bottle Gourd", 10, 100),
        ("P-0014", "Radish", 10, 100),
        ("P-0015", "Ginger", 10, 100),
        ("P-0016", "Lemon", 10, 100),
        ("P-0017", "Capsicum", 10, 100),
        ("P-0018", "Banana Green", 10, 100),
        ("P-0019", "Spinach", 10, 100),
        ("P-0020", "Colocasia", 10, 100),
        ("P-0021", "Ridge Gourd", 10, 100),
        ("P-0022", "Peas", 10, 100),
        ("P-0023", "Tinda", 10, 100),
        ("P-0024", "Coriander", 10, 100),
        ("P-0025", "Guar", 10, 100),
        ("P-0026", "Pointed Gourd", 10, 100),
        ("P-0027", "Sweet Potato", 10, 100),
        ("P-0028", "Drumstick", 10, 100),
        ("P-0029", "Sponge Gourd", 10, 100),
        ("P-0030", "Beetroot", 10, 100),
        ("P-0031", "Methi", 10, 100),
        ("P-0032", "French Beans", 10, 100),
        ("P-0033", "Ashgourd", 10, 100),
        ("P-0034", "Peas Cod", 10, 100),
        ("P-0035", "Little Gourd", 10, 100),
        ("P-0036", "Snake Gourd", 10, 100),
        ("P-0037", "Turnip", 10, 100),
        ("P-0038", "Field Pea", 10, 100),
        ("P-0039", "Amaranthus", 10, 100),
        ("P-0040", "Banana", 10, 100),
        ("P-0041", "Apple", 10, 100),
        ("P-0042", "Mango", 10, 100),
        ("P-0043", "Watermelon", 10, 100),
        ("P-0044", "Pomegranate", 10, 100),
        ("P-0045", "Grapes", 10, 100),
        ("P-0046", "Orange", 10, 100),
        ("P-0047", "Papaya", 10, 100),
        ("P-0048", "Kharbuja", 10, 100),
        ("P-0049", "Mousambi", 10, 100),
        ("P-0050", "Guava", 10, 100),
        ("G-0001", "Arhar Dal", 23, 100),
        ("G-0002", "Moong Dal", 21, 100),
        ("G-0003", "Masur Dal", 15, 100),
        ("G-0004", "Chana Dal", 32, 100),
        ("G-0005", "Lobia", 28, 100),
        ("G-0006", "Chole", 49, 100),
        ("G-0007", "Coconut oil", 299, 100),
        ("G-0008", "Hair oil", 304, 100),
        ("G-0009", "Toothpaste", 350, 100),
        ("G-0010", "Mustard oil", 237, 100),
        ("G-0011", "Peanut butter", 350, 100),
        ("G-0012", "Chocolate Drink", 350, 100),
        ("G-0013", "Tea", 285, 100),
        ("G-0014", "Corn Flakes", 310, 100),
        ("G-0015", "Oats", 207, 100),
        ("G-0016", "Honey", 300, 100),
        ("G-0017", "Chocolate Syrup", 220, 100),
        ("G-0018", "Washing Detergent", 1225, 100),
        ("G-0019", "Floor Cleaner", 385, 100),
        ("G-0020", "Hand Wash", 209, 100),
        ("G-0021", "Mosquito Repellant", 450, 100),
        ("G-0022", "Dish Soap", 350, 100),
        ("G-0023", "Toilet Cleaner", 369, 100),
        ("G-0024", "Refined oil", 137, 100),
        ("G-0025", "Potato Chips", 20, 100),
        ("G-0026", "Cold Drinks", 40, 100),
        ("D-0001", "Milk", 10, 100),
        ("D-0002", "Butter", 150, 100),
        ("D-0003", "Curd", 75, 100),
        ("D-0004", "Buttermilk", 20, 100),
        ("D-0005", "Bread", 25, 100),
    ]

    # Insert product data into the 'Product' table with try-except for existing data
    try:
        cmd_product = '''
            INSERT INTO Product (ProductID, ProductName, ProductCost, Quantity)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.executemany(cmd_product, productData)
        connection.commit()
    except mysql.connector.Error as err:
        print("Data Exists")
        connection.rollback()

    # Sample products with their IDs
    products = [
        "D-0001", "D-0002", "D-0003", "D-0004", "D-0005",
        "G-0001", "G-0002", "G-0003", "G-0004", "G-0005",
        "G-0006", "G-0007", "G-0008", "G-0009", "G-0010",
        "G-0011", "G-0012", "G-0013", "G-0014", "G-0015",
        "G-0016", "G-0017", "G-0018", "G-0019", "G-0020",
        "G-0021", "G-0022", "G-0023", "G-0024", "G-0025",
        "G-0026", "P-0001", "P-0002", "P-0003", "P-0004",
        "P-0005", "P-0006", "P-0007", "P-0008", "P-0009",
        "P-0010", "P-0011", "P-0012", "P-0013", "P-0014",
        "P-0015", "P-0016", "P-0017", "P-0018", "P-0019",
        "P-0020", "P-0021", "P-0022", "P-0023", "P-0024"
    ]

    # Generate random demo data
    demo_data = []

    for _ in range(50):
        product_id = random.choice(products)
        sale_amount = random.randint(1, 50)
        sale_date = datetime.now() - timedelta(days=1)
        demo_data.append((product_id, sale_amount, sale_date))

    # Insert demo data into the 'sale' table with try-except for existing data
    try:
        cmd_sales = '''
            INSERT INTO Sale (productID, saleAmount, saleDate)
            VALUES (%s, %s, %s)
        '''
        cursor.executemany(cmd_sales, demo_data)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()

    # Insert data into the 'Member' table with try-except for existing data
    try:
        value = [
           ('siddhant', 'Siddhant', 1234),
           ('john', 'John', 1224),
           ('bob', 'Bob', 1345),
           ('a', 'A', 1678)
        ]
        cmd_member = '''
            INSERT INTO Member (name, username, password)
            VALUES (%s, %s, %s)
        '''
        cursor.execute(cmd_member, )
        connection.commit()
    except mysql.connector.Error as err:
        print("Member Data Exists")
        connection.rollback()








    # Close the connection
    connection.close()


# Call the function to generate demo data
#demodata()


