import mysql.connector as sql

def sqlSetup():
    
    # Creating the database
    def createDatabase():
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor = connection.cursor()
        cursor.execute("create database if not exists Inventory")
        connection.close()

    createDatabase()

    # Creating a Table to store all products for purchase
    def createTableProduct():
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Inventory"
        )
        cursor = connection.cursor()
        cursor.execute('Use Inventory')
        cmd = ''' 
        Create table if not exists Product(
            productID Varchar(10) Not Null Primary Key,
            productName Varchar(30) Not Null,
            productCost Decimal(10, 2) Not Null,
            purchaseCost Decimal(10, 2),
            Quantity int Not Null 
        )    
        '''
        cursor.execute(cmd)
        connection.close()

    createTableProduct()

    # Create table Sale
    def createTablesale():
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Inventory"
        )
        cursor = connection.cursor()
        cursor.execute('Use Inventory')
        cmd = ''' 
        Create table if not exists Sale(
            saleID Varchar(10) Not Null Primary Key,
            productID Varchar(10) Not Null,
            saleAmount Decimal(10, 2) Not Null,
            saleDate Date default(current_date()) 
        ) 
        '''
        cursor.execute(cmd)
        connection.close()

    createTablesale()

    # Create table Purchase
    def createTablePurchase():
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Inventory"
        )
        cursor = connection.cursor()
        cursor.execute('Use Inventory')
        cmd = ''' 
        Create table if not exists Purchase(
            purchaseID Varchar(10) Not Null Primary Key,
            productID Varchar(10) Not Null,
            PurchaseCost Decimal(10, 2) Not Null,
            purchaseAmount Decimal(10, 2) Not Null,
            purchaseDate Date default(current_date()) 
        ) 
        '''
        cursor.execute(cmd)
        connection.close()

    createTablePurchase()

    # Create table Member
    def createTableMember():
        connection = sql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Inventory"
        )
        cursor = connection.cursor()
        cursor.execute('Use Inventory')
        cmd = ''' 
        Create table if not exists Members(
            MemberID int Not Null Primary Key,
            name Varchar(45) Not Null,
            username Varchar(100) Not Null,
            password Varchar(100) Not Null,
            status varchar(10) default 'user'
        ) 
        '''
        cursor.execute(cmd)
        connection.close()

    createTableMember()