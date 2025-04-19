import sys
import mysql.connector
from tabulate import tabulate
from datetime import date
from saleData import order_function 
from bs4 import BeautifulSoup
from database import sqlSetup
from demodata import demodata
from autoorder import autoorder
from priceChange import pricechange

try:
    sqlSetup()
    demodata()
finally:
    print("Database and tables created. Programme ready to be used")

def login():
    def check_login_credentials(username, password):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="inventory"
            )
            cursor = conn.cursor()

            query = "SELECT * FROM members WHERE Username = %s AND Password = %s"
            user_data = (username, password)
            cursor.execute(query, user_data)

            if cursor.fetchone():
                return True, user_data
            else:
                return False, None

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()
            conn.close()

    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")

    success, result = check_login_credentials(username, password)

    if success:
        print("Hello")
        return True, result
    else:
        print("Invalid Input. Please Try Again")
        return login()

def signup():
    name = input("Please enter Your Name: ")
    username = input("Please Create Your Username: ")
    password = input("Please Enter Your Password: ")
    passwordCheck = input("Please re-enter your password: ")

    if password == passwordCheck:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="inventory"
            )
            cursor = conn.cursor()

            # Insert user details into the table with auto-incremented memberID
            insert_query = "INSERT INTO members (name, Username, Password) VALUES (%s, %s, %s)"
            user_data = (name, username, password)
            cursor.execute(insert_query, user_data)

            conn.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()
            conn.close()
    else:
        print("Invalid Input")
        signup()

def get_user_status(username):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="inventory"
        )
        cursor = conn.cursor()

        query = "SELECT status FROM members WHERE Username = %s"
        cursor.execute(query, (username,))

        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()

print("Welcome User")
answer = input("Please type '/S' to sign-in or type '/L' to login: ")

if answer.lower() == '/l':
    status, user_data = login()
    
elif answer.lower() == '/s':
    signup()
    print("Signup Complete. Please Login to Continue")
    status, user_data = login()
else:
    sys.exit("Invalid Input. Please Try Again")

if get_user_status(user_data[0]) == 'user':
    print("Welcome user")
    order_function()  
else:
    print("Welcome Executive")
    print("Please press 1 to reorder")
    print("Please press 2 to change prices")
    response = input("Please press 1 or 2: ")

    if response == '1':
        autoorder()
    elif response == '2':
        pricechange()
    else:
        sys.exit("Invalid Input. Please try again")