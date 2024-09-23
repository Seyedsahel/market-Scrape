
▎Product Information Scraper

This Python script uses Selenium and BeautifulSoup to scrape product information from specified URLs on the Digikala website. It extracts the product title, price, and category, then saves this information to a CSV file.

▎Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your version of Chrome)

▎Required Python Packages

You will need to install the following packages:

pip install selenium beautifulsoup4


▎Setup

1. Download ChromeDriver: 
   - Ensure that you download the ChromeDriver version that matches your installed version of Google Chrome. Place the chromedriver executable in a directory included in your system's PATH or specify its path in the script.

2. Clone or Download the Script:
   - Clone this repository or download the script file.

3. Modify the URLs:
   - Update the urls list in the script with the product URLs you want to scrape.

▎Running the Script

1. Open a terminal (or command prompt).
2. Navigate to the directory where the script is located.
3. Run the script using Python:

python your_script_name.py


Replace your_script_name.py with the actual name of your Python file.

▎Output

The scraped product information will be saved to a CSV file named output2.csv in the same directory as the script. The CSV file will contain headers for title, price, and cat, along with their corresponding values for each product.

▎Notes

- The script runs in headless mode by default, meaning it won't open a browser window during execution. If you want to see the browser actions, you can remove or comment out the line that adds the --headless argument in the chrome_options.
- Ensure that you comply with the website's terms of service when scraping data.

download chrome driver : https://developer.chrome.com/docs/chromedriver/downloads