from bs4 import BeautifulSoup
import requests
import openpyxl
from openpyxl import Workbook


html_text = requests.get('https://books.toscrape.com/catalogue/page-4.html')


soup = BeautifulSoup(html_text.text, 'lxml')
with open("books.html", "w",encoding="utf-8") as file1:
    file1.write(html_text.text)

div1=soup.find('ol', class_='row')
div2 = div1.find_all('li' , class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

file = "hello.xlsx"
wb = openpyxl.Workbook(file)
ws = wb.active
wb.save("hello.xlsx")


for book in div2:
    N_data = []
    file = "hello.xlsx"
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    div3 = book.find('article', class_='product_pod')
    n_head = div3.find('h3')
    b_price = div3.find('div', class_='product_price')
    b_price_t = b_price.find('p', class_='price_color')
    #print(n_head.text)
    N_data.append(n_head.text)
    #print(b_price_t.text)
    N_data.append(b_price_t.text)
    ws.append(N_data)
    wb.save("hello.xlsx")
