# #FLipkart Data Scrapin- Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


image_name=[]
cost=[]
rating=[]
image_link=[]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(1,20):
    url="https://www.flipkart.com/all/~cs-srqvl071ka/pr?sid=all&collection-tab-name=++Indoor+Games&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkluZG9vciBUb3lzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=11.productCard.PMU_V2_5&page="+str(i)
    driver.get(url)
    print("Page title:", driver.title)


    main_box=driver.find_element(By.CLASS_NAME,"DOjaWF")

    img_name=main_box.find_elements(By.CLASS_NAME,"wjcEIp")    
    for name in img_name:
        img_name=name.text
        image_name.append(img_name)
    print(len(image_name))

    price=main_box.find_elements(By.CLASS_NAME,"Nx9bqj")
    for money in price:
        price=money.text
        cost.append(price)    
    print(len(cost))


    stars=main_box.find_elements(By.CLASS_NAME,"XQDdHH")
    for reviews in stars:
        stars=reviews.text
        rating.append(stars)    
    print(len(rating))


    img_lnk=main_box.find_elements(By.CLASS_NAME, "DByuf4")
    for lnk in img_lnk:
        img_lnk=lnk.get_attribute("src")
        image_link.append(img_lnk)
        print(image_link)
    print(len(image_link))


max_length = max(len(image_name), len(cost), len(rating), len(image_link))
 
# Extend lists with "NA" if they are empty
image_name.extend(["NA"] * (max_length - len(image_name)))
cost.extend(["NA"] * (max_length - len(cost)))
rating.extend(["NA"] * (max_length - len(rating)))
image_link.extend(["NA"] * (max_length - len(image_link)))
 
data=pd.DataFrame({
    
    "Image Name":image_name,
    "Price":cost,
    "Ratings":rating,
    "Image Links":image_link
})

data.to_csv('flipkart_data.csv',index_label="S.No.")


driver.quit()






########
# Flipkart Data Scraping - Selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import pandas as pd

# # Setup WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.flipkart.com/all/~cs-srqvl071ka/pr?sid=all&collection-tab-name=++Indoor+Games&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkluZG9vciBUb3lzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=11.productCard.PMU_V2_5&page=1")

# print("Page title:", driver.title)

# # Lists to store data
# image_name, cost, rating, image_link = [], [], [], []

# # Find all product boxes
# product_boxes = driver.find_element(By.CLASS_NAME, "DOjaWF")

# for product in product_boxes:
#     # Image Name
#     name = product.find_elements(By.CLASS_NAME, "wjcEIp")
#     image=name.text
#     image_name.apend(image)

#     # # Price
    # price = product.find_elements(By.CLASS_NAME, "Nx9bqj")
    # # cost.append(price.text)

    # # Ratings
    # stars = product.find_elements(By.CLASS_NAME, "XQDdHH")
    # rating.append(stars[0].text if stars else "NA")

    # # Image Link
    # img = product.find_elements(By.CLASS_NAME, "DByuf4")
    # # image_link.append(img.text)

# # Create DataFrame
# data = pd.DataFrame({
#     "Image Name": image_name,
#     "Price": cost,
#     "Ratings": rating,
#     "Image Links": image_link
# })

# # Save to CSV
# data.to_csv('flipkart_data3.csv', index_label="S.No.")
# print("✅ Data saved to 'flipkart_data.csv'")

# driver.quit()








###TRY3# Flipkart Data Scraping - Selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import pandas as pd

# # Setup WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.flipkart.com/all/~cs-srqvl071ka/pr?sid=all&collection-tab-name=++Indoor+Games&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkluZG9vciBUb3lzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=11.productCard.PMU_V2_5&page=1")

# print("Page title:", driver.title)

# # Lists to store data
# image_name, cost, rating, image_link = [], [], [], []

# # Find all product boxes
# product_boxes = driver.find_elements(By.CLASS_NAME, "DOjaWF")

# for product in product_boxes:
#     # Image Name
#     name_elem = product.find_elements(By.CLASS_NAME, "wjcEIp")
#     image_name.append(name_elem[0].text if name_elem else "NA")

#     # Price
#     price_elem = product.find_elements(By.CLASS_NAME, "Nx9bqj")
#     cost.append(price_elem[0].text if price_elem else "NA")

#     # Ratings (Insert "NA" if missing)
#     rating_elem = product.find_elements(By.CLASS_NAME, "XQDdHH")
#     rating.append(rating_elem[0].text if rating_elem else "NA")

#     # Image Link
#     img_elem = product.find_elements(By.CLASS_NAME, "DByuf4")
#     image_link.append(img_elem[0].get_attribute("src") if img_elem else "NA")

# # ✅ All lists now have the same length and proper alignment

# # Create DataFrame
# data = pd.DataFrame({
#     "Image Name": image_name,
#     "Price": cost,
#     "Ratings": rating,
#     "Image Links": image_link
# })

# # Save to CSV
# data.to_csv('flipkart_data0.csv', index_label="S.No.")
# print("✅ Data saved to 'flipkart_data.csv'")

# driver.quit()



