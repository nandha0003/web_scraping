# import csv

# data = [
#     ["Title", "Star Rating", "Price"],
#     ["Hawkeye, Vol. 1: My Life as a Weapon (Hawkeye #1)", 3, 45.24],
#     ["Having the Barbarian's Baby (Ice Planet Barbarians #7.5)", 4, 34.96],
#     ["Giant Days, Vol. 1 (Giant Days #1-4)", 4, 56.76],
#     ["Fruits Basket, Vol. 1 (Fruits Basket #1)", 5, 40.28]
# ]

# # Specify the CSV file name
# csv_file_name = "scrapingoutput.csv"

# # Write data to the CSV file
# with open(csv_file_name, 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(data)

# print(f"Data has been written to {csv_file_name}")



import csv
import requests
from bs4 import BeautifulSoup

# List to store scraped data
data = [["Title", "Star Rating", "Price", "Image URL", "In-stock"]]

for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')

    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        image_url = image['src']
        availability = article.find('p', class_='instock availability').text.strip()
        
        # Append data to the list
        data.append([title, star, price, image_url, availability])

# Specify the CSV file name
csv_file_name = "scrapingoutput.csv"

# Write data to the CSV file
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print(f"Data has been written to {csv_file_name}")

####################################################################################################


