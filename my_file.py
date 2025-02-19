import requests
from bs4 import BeautifulSoup
import sqlite3
import csv



url="https://quotes.toscrape.com/"
r=requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')


#connect to database
conn=sqlite3.connect("scrapdata.db")

#cursor:
cursor=conn.cursor()

#Scraping Data:
quotes=[]
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

#creating table:
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS data(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         QUOTES TEXT not NULL,
#         AuthorName text not Null)
# """)

# for quote, author in zip(quotes, authors):
#     cursor.execute("INSERT INTO data (QUOTES, AuthorName) VALUES (?, ?)", (quote, author))



conn.commit()
conn.close()


#Save to CSV file                
with open("scraped_quotes.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Step 2: Write the header row
    writer.writerow(["Sr.No", "Quotes", "Authors"])
    
    # Step 3: Write data rows with Sr.No starting from 1
    for i, (quote, author) in enumerate(zip(quotes, authors), start=1):
        writer.writerow([i, quote, author])

print("Data saved successfully to scraped_quotes.csv!")