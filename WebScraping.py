      #find_all with Pandas
import pandas
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("a",{"class":"title"})
product=[]
for i in names:
    product.append(i.text)
# print(product)
prices=soup.find_all("h4",class_="float-end price card-title pull-right") 
price=[]
for i in prices:
    price.append(i.text)
# print(price)
description_lst=soup.find_all("p",class_="description card-text")
decs=[]
for i in description_lst:
    decs.append(i.text)

# print(decs)

data_rate=soup.find_all("p",class_="float-end review-count")
rate=[]
for i in data_rate:
    rate.append(i.text)
# print(rate)

df=pandas.DataFrame({"Product Names":product,"Prices":price,"Description":decs,"Reviews":rate})
# print(df)
# df.to_csv("Product_Details.csv")
df.to_excel("Product_Details.xlsx")


