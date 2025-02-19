from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import csv
# Initialize Chrome WebDriver without download
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/denovo.cfm")


# title=driver.find_element(By.ID,value="topic_page_title").text

# print(title)
# print("Page title:", driver.title)

# links=driver.find_element(By.CLASS_NAME,value="hmenu").text
# print(links)

# para=driver.find_element(By.CLASS_NAME,value="pmn-intro").text
# print(para)

# input_fields = driver.find_elements(By.XPATH, "//table//label")

# data = []
# for label in input_fields:
#     data_text = label.text
#     data.append(data_text)
#     print(data_text)


driver.get("https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm")

extract=driver.find_elements(By.XPATH, "//table[2]/tbody/tr/td")
list=[]
for td in extract:
    data_extract=td.text
    list.append(data_extract)
print(list)

data_extracted=pd.DataFrame(list)

data_extracted.to_csv("data_fda.csv",index=True)
driver.quit()
