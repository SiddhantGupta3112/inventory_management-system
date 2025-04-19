import urllib.request
from bs4 import BeautifulSoup
import mysql.connector as sql

def pricechange():
    connection = sql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Inventory"
    )

    cursor = connection.cursor()
    cursor.execute('USE Inventory')

    cmd = '''
    SELECT ProductName FROM Product
    WHERE productID LIKE 'P%'
    '''
    cursor.execute(cmd)
    product = cursor.fetchall()

    for ele in product:
        for commodity in ele:
            def currentPrice(commodity):
                link = "https://www.commodityinsightsx.com/commodities/mandi-prices/" + commodity.replace(" ", "-") + "-market-price"
                url = link

                try:
                    req = urllib.request.Request(url)
                    response = urllib.request.urlopen(req)
                    html_content = response.read().decode()
                    soup = BeautifulSoup(html_content, 'html.parser')

                    paragraphs = soup.find_all('p', {'class': 'page-info'})

                    target_text = "The average price is"
                    desired_paragraph = None

                    for paragraph in paragraphs:
                        if target_text in paragraph.get_text():
                            desired_paragraph = paragraph
                            break

                    paragraph_text = desired_paragraph.get_text()
                    return paragraph_text, link
                except urllib.error.HTTPError:
                    return None, link

            priceData, link = currentPrice(commodity)
            if priceData is not None:
                priceData = priceData.split(".")

                for ele in priceData:
                    if "average" in ele.split():
                        for ele in ele.split():
                            try:
                                int(ele)
                                price = int(int(ele) / 100)
                                break
                            except:
                                continue

                cmd2 = '''
                SELECT purchaseCost FROM Product
                WHERE productName = %s
                '''
                parameter = (commodity,)
                cursor.execute(cmd2, parameter)
                old_price = cursor.fetchone()[0]

                cmd3 = '''
                UPDATE Product
                SET purchaseCost = %s
                WHERE productName = %s
                '''
                parameter = (price, commodity)
                cursor.execute(cmd3, parameter)

                cmd4 = '''
                UPDATE product
                SET productCost = %s
                WHERE productName = %s
                '''
                parameter = (int(price * 1.50), commodity)
                cursor.execute(cmd4, parameter)

                connection.commit()

                print(f"Price changed for {commodity}: {old_price} -> {price}")

    print("Price change complete")
#pricechange()