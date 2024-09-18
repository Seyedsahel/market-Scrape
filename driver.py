import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_product_info(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")


    driver = webdriver.Chrome(options=chrome_options)


    driver.get(url)
    wait = WebDriverWait(driver, 50)
    print(f"Scraping: {driver.title}")
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extracting information
    out_put = {}
    
    title = soup.find("h1", class_="text-h4 text-neutral-900 mb-2 pointer-events-none")
    if title:
        product_name = title.text
        out_put["title"] = product_name.strip()
    else:
        print("Product name tag not found")

    price = soup.find("div", class_="flex justify-start mr-auto text-h4 pr-4")
    if price:
        real = price.find("span", class_="text-h4 ml-1 text-neutral-800")
        if real:
            out_put["price"] = real.text
        else:
            print("Price span not found")
    else:
        print("Price div not found")

    cat = soup.find("div", class_="flex items-center w-full px-5 lg:px-0")
    if cat:
        real = cat.find("nav", class_="flex items-center")
        if real:
            out_put["cat"] = real.text
        else:
            print("Category nav not found")
    else:
        print("Category div not found")


    driver.quit()

    
    # ذخیره‌سازی به فایل CSV
    with open('output2.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(out_put.keys())  # نوشتن هدر
        writer.writerow(out_put.values())  # نوشتن مقادیر


# Example usage
urls = [
    "https://www.digikala.com/product/dkp-1161734/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA-%DA%AF%D9%86%D8%AF%D9%85-%DA%A9%D8%A7%D9%85%D9%84-%D8%B3%D8%A7%D9%82%D9%87-%D8%B7%D9%84%D8%A7%DB%8C%DB%8C-%D9%85%DB%8C%D9%86%D9%88-200-%DA%AF%D8%B1%D9%85/",
    "https://www.digikala.com/product/dkp-5709642/%D8%AF%D9%81%D8%AA%D8%B1-%D9%85%D8%B4%D9%82-%D9%85%D8%AF%D9%84-%D8%A7%DB%8C%D9%81%D9%84-%D8%A8%D8%B3%D8%AA%D9%87-5-%D8%B9%D8%AF%D8%AF%DB%8C/",
    "https://www.digikala.com/product/dkp-15284218/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D9%85%D8%AF%D9%84-ultra/",
    "https://www.digikala.com/product/dkp-15445767/%D8%AF%D8%B3%D8%AA%DB%8C%DA%AF%DB%8C%D8%B1%D9%87-%D8%B4%DB%8C%D8%B4%D9%87-%D8%A8%D8%A7%D9%84%D8%A7%D8%A8%D8%B1-%D8%B3%D9%87%DB%8C%D9%84-%DB%8C%D8%AF%DA%A9-%D9%85%D8%AF%D9%84-s-01-%D9%85%D9%86%D8%A7%D8%B3%D8%A8-%D8%A8%D8%B1%D8%A7%DB%8C-%D9%BE%D8%B1%D8%A7%DB%8C%D8%AF-%D9%85%D8%AC%D9%85%D9%88%D8%B9%D9%87-2-%D8%B9%D8%AF%D8%AF%DB%8C/",
   "https://www.digikala.com/product/dkp-14139839/%D8%B1%DB%8C%D9%86%DA%AF-%D9%84%D8%A7%DB%8C%D8%AA-%D9%85%D8%AF%D9%84-%D8%B9%D8%B1%D9%88%D8%B3%DA%A9%DB%8C-%DA%A9%D8%AF-c3/"
]
for url in urls:
    scrape_product_info(url)
