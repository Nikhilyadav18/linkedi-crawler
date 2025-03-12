import os
import json
import requests
import pandas as pd

# ✅ Gemini API URL & Key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
API_KEY = "AIzaSyCkEocS3TsWnc-6FlLePsb-IELNaHWcWOA"  # .env file me API key honi chahiye

# ✅ Excel File Path (Change if needed)
EXCEL_FILE = "Internship_Dummy_Data.xlsx"

# ✅ Output Excel File
OUTPUT_EXCEL_FILE = "classified_internship_data.xlsx"

def send_to_gemini(about_us_text):
    # ✅ Request Body
    prompt = f"""
    Analyze the following internship details from the "About Us" paragraph and classify into the below JSON format:
    
    "about_us": "{about_us_text}"
    
    Respond in JSON format like this:
    {{
      "internship_stipend": "Paid (10000)" or "Unpaid",
      "degree_required": "B.Tech / MCA / Any",
      "location": "City Name / Remote",
      "tech_stack_required": {{
        "difficulty": "Easy / Medium / Hard",
        "technologies": "React, Node.js, MongoDB"
      }}
    }}
    """

    request_data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(
            f"{API_URL}?key={API_KEY}",
            headers={'Content-Type': 'application/json'},
            json=request_data
        )
        response.raise_for_status()

        # ✅ Parse text content from Gemini Response
        text_content = response.json()['candidates'][0]['content']['parts'][0]['text']
        
        # ✅ Clean and parse JSON
        cleaned_text = text_content.strip().replace("```json", "").replace("```", "")
        parsed_json = json.loads(cleaned_text)

        return parsed_json

    except Exception as e:
        print("❌ Error communicating with Gemini API:", e)
        return None

def process_excel_file(file_path):
    df = pd.read_excel(file_path)
    
    # ✅ List to store processed data
    processed_rows = []

    for index, row in df.iterrows():
        internship_role = row.get('Internship Role', '')
        company_name = row.get('Company Name', '')
        about_us = row.get('About Us', '')

        print(f"🔎 Processing row {index+1}: {internship_role} at {company_name}")

        gemini_response = send_to_gemini(about_us)

        if gemini_response:
            # Flatten the tech_stack_required for Excel columns
            difficulty = gemini_response['tech_stack_required']['difficulty']
            technologies = gemini_response['tech_stack_required']['technologies']

            # ✅ Create a new row dictionary
            new_row = {
                "Internship Role": internship_role,
                "Company Name": company_name,
                "Internship Stipend": gemini_response['internship_stipend'],
                "Degree Required": gemini_response['degree_required'],
                "Location": gemini_response['location'],
                "Tech Stack Difficulty": difficulty,
                "Technologies": technologies
            }

            processed_rows.append(new_row)

    # ✅ Convert processed data to DataFrame
    output_df = pd.DataFrame(processed_rows)

    # ✅ Save DataFrame to Excel
    output_df.to_excel(OUTPUT_EXCEL_FILE, index=False)
    
    print(f"\n✅ Classified data saved to Excel: {OUTPUT_EXCEL_FILE}")

if __name__ == "__main__":
    if not API_KEY:
        print("❌ GOOGLE_API_KEY not found in environment variables!")
    else:
        process_excel_file(EXCEL_FILE)
