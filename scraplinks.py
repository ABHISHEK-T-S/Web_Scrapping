from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlreq

myurl = "https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
filename = "products.txt"
f = open(filename,"w")
uclient = urlreq(myurl)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html,"html.parser")

page_soup.body.p #gives you the p value

links = page_soup.find_all("div",{"class":"_1UoZlX"}) #grabs all product links

for link in links:
    href = link.a["href"]
    name = link.a.div.div.div.div.img["alt"]
    print(name)
    print( "link: " +href)
    print("\n")
    f.write(name +"\n")
    f.write("link: " +href +"\n\n")
f.close()
   

 

