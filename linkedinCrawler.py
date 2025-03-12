import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ==== CONFIGURATION ====
csv_file = "linkedin_links.csv"   # CSV input file
excel_output_file = "Internship_Dummy_Data.xlsx"  # Excel output file

# ==== CHROME OPTIONS ====
options = Options()
options.add_argument("user-data-dir=C:/Users/Bharat/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Default")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# ==== DRIVER SETUP ====
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ==== READ LINKS FROM CSV ====
try:
    df_links = pd.read_csv(csv_file)
    print(f"✅ Loaded {len(df_links)} links from CSV!")
except Exception as e:
    print(f"❌ Error loading CSV file: {e}")
    driver.quit()
    exit()

# ==== LIST TO STORE SCRAPED DATA ====
all_job_details = []

# ==== LOOP THROUGH EACH LINK ====
for index, row in df_links.iterrows():
    linkedin_job_url = row['Link']
    print(f"\n🔗 Processing ({index+1}/{len(df_links)}): {linkedin_job_url}")

    try:
        driver.get(linkedin_job_url)
        wait = WebDriverWait(driver, 20)

        # ==== EXTRACT COMPANY NAME ====
        try:
            company_element = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "job-details-jobs-unified-top-card__company-name")
            ))
            company_name = company_element.text.strip()
            print(f"✅ Company Name: {company_name}")
        except Exception as e:
            print(f"❌ Company name not found: {e}")
            company_name = "Not Found"

        # ==== EXTRACT JOB TITLE ====
        try:
            job_title_element = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "job-details-jobs-unified-top-card__job-title")
            ))
            job_title = job_title_element.text.strip()
            print(f"✅ Job Title: {job_title}")
        except Exception as e:
            print(f"❌ Job title not found: {e}")
            job_title = "Not Found"

        # ==== EXTRACT JOB DESCRIPTION ====
        try:
            description_container = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "jobs-description__container")
            ))
            description_text = description_container.text.strip()
            print(f"✅ Job Description Found!")
        except Exception as e:
            print(f"❌ Job description not found: {e}")
            description_text = "Not Found"

        # ==== ADD DATA TO LIST ====
        job_details = {
            "Index": index + 1,
            "Job Link": linkedin_job_url,
            "Company Name": company_name,
            "Job Title": job_title,
            "Job Description": description_text
        }

        all_job_details.append(job_details)

        # OPTIONAL DELAY (to avoid detection)
        time.sleep(2)

    except Exception as e:
        print(f"❌ Failed to process link {linkedin_job_url}: {e}")
        continue

# ==== SAVE ALL DATA TO EXCEL ====
try:
    df_output = pd.DataFrame(all_job_details)
    df_output.to_excel(excel_output_file, index=False)
    print(f"\n✅ All job details saved successfully to '{excel_output_file}'!")
except Exception as e:
    print(f"❌ Error saving Excel file: {e}")

finally:
    driver.quit()
