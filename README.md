# linkedi-crawler
# 🚀 **AUTOMATED LINKEDIN CRAWLER**

A powerful **Python-based automation tool** designed to simplify your search for **internships** and **job opportunities** directly from **LinkedIn** search results.
 This project leverages **Google Dorking**, **Web Crawling**, and **Gemini AI** to deliver structured and classified data for job seekers and HR professionals.

------

## 🛠️ **Project Overview**

This is a collection of Python scripts that work in a **three-step pipeline**, starting from extracting **LinkedIn links** using **Google Dorking** to delivering a **classified Excel sheet** of internships and jobs.

------

## 📂 **Workflow Structure**

### 1. **GoogleCrawler.py**

🔍 *Performs Google Dorking to extract relevant LinkedIn URLs.*

- Input

  : A Google Dork query like:

  ```
  bash
  
  
  CopyEdit
  site:linkedin.com/in OR site:linkedin.com/jobs "Full Stack Developer Internship" AND India AND "Apply Now" OR "Hiring" OR "Internship Openings" 2025
  ```

- **Process**:
   Searches Google with the provided query and scrapes LinkedIn job/internship links.

- Output

  :

  Saves the collected links into a CSV file called:

  ```
  CopyEdit
  linkedin_links.csv
  ```

------

### 2. **linkedinCrawler.py**

🕸 *Scrapes job descriptions from the LinkedIn links collected in Step 1.*

- **Input**:
   `linkedin_links.csv`

- Process

  :

  Extracts key details from each LinkedIn job/internship page such as:

  - About Us
  - Company Name
  - Internship Role

- Output

  :

  Structured data in an Excel file called:

  ```
  CopyEdit
  Internship_Dummy_Data.xlsx
  ```

------

### 3. **classifingData.py**

🤖 *Uses Gemini AI to classify and refine the scraped data.*

- **Input**:
   `Internship_Dummy_Data.xlsx`

- Process

  :

  Sends data to 

  Gemini AI

   for classification.

  Classifies details like:

  - Internship Stipend (Paid / Unpaid)
  - Degree Required (B.Tech / MCA / Any)
  - Location (City Name / Remote)
  - Tech Stack (Difficulty and Technologies)

- Output

  :

  Final classified Excel file called:

  ```
  CopyEdit
  classified_internship_data.xlsx
  ```

------

## 🔑 **Tech Stack**

| Tool                                           | Description                                          |
| ---------------------------------------------- | ---------------------------------------------------- |
| **Python**                                     | Core language used for development                   |
| **BeautifulSoup / Selenium**                   | Web scraping & crawling                              |
| **Pandas**                                     | Data processing and Excel file handling              |
| **Gemini AI (Google Generative Language API)** | Data classification and AI processing                |
| **Google Dorking**                             | Advanced search queries for LinkedIn data extraction |

------

## ⚙️ **Requirements**

- Python 3.x

- Required Python libraries (install via 

  ```
  pip install -r requirements.txt
  ```

  ):

  ```
  nginxCopyEditpandas
  requests
  beautifulsoup4
  openpyxl
  selenium
  ```

- **Gemini AI API Key** (must be added to your environment variables or directly in the script for testing purposes)

------

## 📝 **Notes**

- 🔐 **Gemini AI API** is used in this project, and you'll need an active **API Key** to use the classification feature.

- ⚠️ **Data fluctuations** may occur due to scraping limitations and changes in LinkedIn’s site structure.

- 🛠 

  This project is still under development!

   Future updates will include:

  - Error handling improvements
  - More stable crawling mechanisms
  - Support for more job platforms

------

## 🚀 **How to Run the Project**

1. Clone the repository:

   ```
   bashCopyEditgit clone https://github.com/your-repo/automated-linkedin-crawler.git
   cd automated-linkedin-crawler
   ```

2. Install dependencies:

   ```
   nginx
   
   
   CopyEdit
   pip install -r requirements.txt
   ```

3. Add your **Gemini API Key** to the environment variables or directly in the script (for testing).

4. Run the pipeline:

   - Step 1

     :

     ```
     nginx
     
     
     CopyEdit
     python GoogleCrawler.py
     ```

   - Step 2

     :

     ```
     nginx
     
     
     CopyEdit
     python linkedinCrawler.py
     ```

   - Step 3

     :

     ```
     nginx
     
     
     CopyEdit
     python classifingData.py
     ```

   Final output will be saved as:

   ```
   CopyEdit
   classified_internship_data.xlsx
   ```

------

## 🧑‍💻 **Contributing**

Want to contribute? Great!

- Fork the repo
- Create a new branch
- Submit a pull request

------

## 📧 **Contact**

For any queries or suggestions, feel free to reach out!
 📩 **Email**: nikhilmehta76765@gmail.com
 🌐 **GitHub**: nikhilyadav18

------

## ⚠️ **Disclaimer**

- This tool is for educational and personal use only.
- Any misuse for violating LinkedIn’s terms of service is not encouraged or supported by the developers.

------

### ⭐ Don't forget to **star** the repo if you find this helpful!

------

Let me know if you want to add **screenshots**, **flowcharts**, or **GIF demos** to the README!
 Or agar isme koi specific **branding** dalna hai (logo, banner, etc.), toh bata dena.
