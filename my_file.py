import requests
from bs4 import BeautifulSoup
url="https://quotes.toscrape.com/"
r=requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

#gives the visual representation of the parse tree created from the raw HTML content
'''print(soup.prettify())'''

#To access title
'''print(soup.title.string)'''

#To access particular text:
# result=soup.find(class_="col-md-8")
# # text=result.find("div",class_="quote")
quotes=[]
# main_text=result.find_all("span",class_="text")
# for i in main_text:
#     print(i)
quote_txt=soup.find_all('span',class_="text")
for i in quote_txt:
    result=i.text
    #print(result)
    quotes.append(result)
print(quotes)



authors=[]
auth=soup.find_all('small',class_="author")
for i in auth:
    data=i.text
    authors.append(data)
print(authors) 