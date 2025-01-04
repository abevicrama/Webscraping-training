from bs4 import BeautifulSoup
import requests
import json

url = 'https://quotes.toscrape.com'

html_text = requests.get('https://www.sarasavi.lk/product-category/nawakatha')

soup = BeautifulSoup(html_text.text, 'lxml')
#print(html_text.text)
#with open("mess.html", "w",encoding="utf-8") as file1:
#        file1.write(html_text.text)





script = soup.find('script', id='__NEXT_DATA__')

#next_li = next_ul.find('li', class_='next')
#next_a = next_li.find('a')


if script and script.string:
    # Parse the JSON content
    data = json.loads(script.string)  # Use json.loads to parse JSON content
    # Access the desired data
    page_count = data['props']['pageProps']['iniData']['last_page']
    select_data = data['props']['pageProps']['iniData']
   

    for i in range(0,40):
        data = select_data['data']
        next_page = select_data['last_page_url']
        book_data = data[i]
        book_name = book_data['name']
        author = book_data['author']['name']
        publisher = book_data['publisher']['name']
       
        print(f"Name: {book_name}")
        print(f"Author: {author}")
        print(f"Publisher: {publisher}")
        print("\n")






else:
    print("Script with id '__NEXT_DATA__' not found or has no content.")
