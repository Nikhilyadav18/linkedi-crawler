from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# ==== CONFIGURATION ====
chrome_driver_path = 'chromedriver.exe'  # Path to your ChromeDriver
search_query = 'site:linkedin.com/in OR site:linkedin.com/jobs "Full Stack Developer Internship" AND India AND "Apply Now" OR "Hiring" OR "Internship Openings" 2025'
max_links = 100  # Number of links you want to collect
output_file = 'linkedin_links.csv'

# ==== CHROME OPTIONS ====
# Enable Chrome DevTools Protocol
options = Options()
options.add_argument("user-data-dir=C:/Users/Bharat/AppData/Local/Google/Chrome/User Data")  # Chrome profile
options.add_argument("--profile-directory=Default")  # Use specific Chrome profile

# ==== DRIVER SETUP ====
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# ==== GOOGLE SEARCH ====
driver.get('https://www.google.com/')
time.sleep(5)

# Accept cookies if needed
try:
    accept_button = driver.find_element(By.XPATH, '//button/div[text()="Accept all"]')
    accept_button.click()
except:
    pass


# Find search box and enter query
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(25)
# ==== SCRAPE LINKS ====
links = []
page = 1

while len(links) < max_links:
    print(f"Scraping Page: {page}")
    time.sleep(5)

    # Get all <a> tags
    search_results = driver.find_elements(By.XPATH, '//a[@href]')
    for result in search_results:
        url = result.get_attribute('href')
        if url and 'linkedin.com' in url and url not in links:
            links.append(url)
            print(f"[{len(links)}] {url}")

        if len(links) >= max_links:
            break

    # Go to next page if available
    try:
        next_button = driver.find_element(By.ID, 'pnnext')
        next_button.click()
        page += 1
    except:
        print("No more pages found.")
        break

# ==== SAVE TO CSV ====
df = pd.DataFrame({
    'Index': range(1, len(links)+1),
    'Link': links
})
df.to_csv(output_file, index=False, encoding='utf-8')
print(f"\n✅ Saved {len(links)} links to '{output_file}'")

# ==== CLOSE DRIVER ====
driver.quit()