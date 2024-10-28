import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(3)

products = driver.find_elements(By.CLASS_NAME, '_Ud0k')

print(products)
parsed_data = []

for product in products:
    try:
       name = product.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
       price = product.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName').text
       link = product.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("svet.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'цена', 'ссылка на товар'])
    writer.writerows(parsed_data)