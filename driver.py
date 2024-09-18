import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

out_put = {}
url = "https://www.digikala.com/product/dkp-7066205/%D8%B3%D9%87-%D9%BE%D8%A7%DB%8C%D9%87-%D8%AF%D9%88%D8%B1%D8%A8%DB%8C%D9%86-%D9%85%D8%AF%D9%84-lw215/"
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 50)
print(driver.title)
page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')

# استخراج اطلاعات
title = soup.find("h1", class_="text-h4 text-neutral-900 mb-2 pointer-events-none")
if title:
    product_name = title.text
    out_put["title"] = product_name.strip()
else:
    print("product name tag not found")

price = soup.find("div", class_="flex justify-start mr-auto text-h4 pr-4")
if price:
    real = price.find("span", class_="text-h4 ml-1 text-neutral-800")
    if real:
        out_put["price"] = real.text
    else:
        print("span no")
else:
    print("div no")

cat = soup.find("div", class_="flex items-center w-full px-5 lg:px-0")
if cat:
    real = cat.find("nav", class_="flex items-center")
    if real:
        out_put["cat"] = real.text
    else:
        print("span no")
else:
    print("div no")

driver.quit()

# ذخیره‌سازی به فایل CSV
with open('output.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(out_put.keys())  # نوشتن هدر
    writer.writerow(out_put.values())  # نوشتن مقادیر

print(out_put)
