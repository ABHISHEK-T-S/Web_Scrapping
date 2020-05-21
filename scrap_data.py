from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlreq

myurl = "https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uclient = urlreq(myurl)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html,"html.parser")

page_soup.body.p #gives you the p value

filename = "products.csv"
f = open(filename,"w")
headers ="name, price, rating \n"
f.write(headers)

names = page_soup.find_all("div",{"class":"_3wU53n"}) # grabs all  names using class
price = page_soup.find_all("div",{"class":"_1vC4OE _2rQ-NK"}) # grabs all price using class
rating = page_soup.find_all("div",{"class":"hGSR34"}) # grabs all ratings using class
for x in range(0 , 23):
    product_name = names[x].text
    product_price = price[x].text
    product_rating = rating[x].text

    print("name :"+ product_name)
    print("price :"+ product_price)
    print("rating :"+ product_rating)

    f.write(product_name + "," +product_price.replace("₹"," ").replace(",","") +"," +product_rating + "\n")

f.close()
