from bs4 import BeautifulSoup
import requests
import openpyxl
import os  # For file existence check

# Fetch the website content
html_text = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(html_text.text, 'lxml')

# Save HTML locally (optional)
with open("books.html", "w") as file1:
    file1.write(html_text.text)

# Find the book data
div1 = soup.find('ol', class_='row')
div2 = div1.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

# Extract data
N_data = []
P_data = []
for book in div2:
    div3 = book.find('article', class_='product_pod')
    n_head = div3.find('h3')
    b_price = div3.find('div', class_='product_price')
    b_price_t = b_price.find('p', class_='price_color')
    
    # Append data to lists
    N_data.append(n_head.text)
    P_data.append(b_price_t.text)

# File path
file = "hello.xlsx"

# Check if the file exists
if not os.path.exists(file):
    # Create a new workbook if file doesn't exist
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Books"
    # Add headers
    ws.append(["Book Title", "Price"])
else:
    # Load the existing workbook
    wb = openpyxl.load_workbook(file)
    ws = wb.active

# Append data to the sheet
for title, price in zip(N_data, P_data):
    ws.append([title, price])

# Save the workbook
wb.save(file)

# Output to console (optional)
print("\nBook Titles:\n", N_data)
print("\nBook Prices:\n", P_data)
