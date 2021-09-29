import requests
from bs4 import BeautifulSoup
import csv

links = []

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text)
    books_category = soup.find ("ul",{"class" : "nav nav-list"}).find_all("li")

    for li in books_category:
       a = li.find("a")
       link = a["href"]
       links.append("http://books.toscrape.com/" + link)
    

with open("urls.txt", "w") as file:
    for link in links:
      file.write(link + '\n')

with open("urls.txt", "r") as file:
    for row in file:
      print(row)

links_books = []

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)   
if response.ok:
   soup = BeautifulSoup(response.text)
   books = soup.find ("div",{"class" : "col-sm-8 col-md-9"}).find_all("h3")

   for h3 in books:
     a = h3.find("a")
     link_books = a["href"]
     links_books.append("http://books.toscrape.com/catalogue/category/books/travel_2/index.html" + 
                        link_books)


with open("urls_books.txt", "w") as file:
      for link_books in links_books:
         file.write(link_books + '\n')

with open("urls_books.txt", "r") as file:
     for row in file:
         print(row)

url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text)

product_page_url = url
colonne = soup.find ("table", {"class" : "table table-striped"}).find_all("td") 
universal_product_code = colonne[0]
title = soup.find("h1")
price_including_tax = colonne[3]
price_excluding_tax = colonne[2]
number_available = colonne[5]
product_description = soup.find ("article",{"class" : "product_page"}).find_all("p")[3]
category = soup.find ("ul",{"class" : "breadcrumb"}).find_all("a")[2]
review_rating = colonne[6]
images = soup.find("div", class_='item active').find_all("img")
for image_url in images:
   image_url = (image_url.get('src'))

print("Url de la page : " + url + ", titre : " + title.text + 
  ", Upc : " + universal_product_code.text +
  ", Prix avec taxe : " + price_including_tax.text +
  ", Prix sans taxe : " + price_excluding_tax.text +
  ", Disponibilité : " + number_available.text + 
  ", Desciption : " + product_description.text +
  ", Catégorie : " + category.text +
  ", Nombre d'avis : " + review_rating.text +
  ", Url de l'image : " + image_url)