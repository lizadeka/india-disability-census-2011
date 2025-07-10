# # scraper_selenium.py

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import os

# URL = "https://censusindia.gov.in/census.website/data/census-tables"
# OUTPUT_DIR = "india_census_project\saved data"
# OUTPUT_FILE = os.path.join(OUTPUT_DIR, "download_links.csv")
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# options = Options()
# options.add_argument('--headless')  # Run Chrome in background
# options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(options=options)
# driver.get(URL)

# time.sleep(5)  # Wait for the page to fully load JavaScript

# soup = BeautifulSoup(driver.page_source, "html.parser")
# driver.quit()

# all_links = []

# tables = soup.find_all("table")
# for table in tables:
#     rows = table.find_all("tr")
#     for row in rows:
#         cols = row.find_all("td")
#         if len(cols) >= 2:
#             description = cols[0].get_text(strip=True)
#             link_tag = cols[-1].find("a", href=True)
#             if link_tag:
#                 download_url = link_tag["href"]
#                 all_links.append({
#                     "Description": description,
#                     "Download_Link": download_url
#                 })

# df = pd.DataFrame(all_links)
# df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
# print(f"✅ Scraped {len(df)} download links and saved to {OUTPUT_FILE}")



# scraper_selenium.py

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# import requests
# import time
# import os
# from urllib.parse import urljoin, unquote

# # Constants
# BASE_URL = "https://censusindia.gov.in"
# START_URL = "https://censusindia.gov.in/census.website/data/census-tables"
# OUTPUT_DIR = "india_census_project/saved data"
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Set up headless browser
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(options=options)
# driver.get(START_URL)
# time.sleep(5)  # Wait for JS to load

# # Parse the page
# soup = BeautifulSoup(driver.page_source, "html.parser")
# driver.quit()

# # Find and clean download links
# all_links = []

# tables = soup.find_all("table")
# for table in tables:
#     rows = table.find_all("tr")
#     for row in rows:
#         cols = row.find_all("td")
#         if len(cols) >= 2:
#             description = cols[0].get_text(strip=True)
#             link_tag = cols[-1].find("a", href=True)
#             if link_tag:
#                 relative_url = link_tag["href"]
#                 full_url = urljoin(BASE_URL, relative_url)
#                 all_links.append({
#                     "Description": description,
#                     "Download_Link": full_url
#                 })

# # Save list of links to CSV
# df = pd.DataFrame(all_links)
# df.to_csv(os.path.join(OUTPUT_DIR, "download_links.csv"), index=False, encoding="utf-8")
# print(f"✅ Scraped {len(df)} download links.")

# # ✅ Now download each file
# print("⬇️ Downloading files...")
# for row in all_links:
#     url = row["Download_Link"]
#     filename = os.path.basename(unquote(url))  # Clean filename
#     filepath = os.path.join(OUTPUT_DIR, filename)

#     try:
#         response = requests.get(url)
#         with open(filepath, 'wb') as f:
#             f.write(response.content)
#         print(f"✅ Saved: {filename}")
#     except Exception as e:
#         print(f"❌ Failed to download {url}: {e}")


# ------------------------------------------------------------------------------------------------------------

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL containing the download links
BASE_URL = "https://censusindia.gov.in/nada/index.php/catalog/43434"

# 🔸 Custom Save Directory (use raw string to handle spaces and backslashes)
save_dir = r"C:\Users\MY PC\Downloads\Data analyst\Python\india_census_project\saved data"
os.makedirs(save_dir, exist_ok=True)

# Step 1: Fetch and parse the page
print("📥 Fetching page...")
print("🔎 Extracting download links...")

# Fetch and parse page
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

download_links = []

for link in soup.find_all("a", href=True):
    href = link['href']
    text = link.text.strip()
    if "download" in href and (href.endswith(".xls") or href.endswith(".xlsx")):
        full_url = href if href.startswith("http") else "https://censusindia.gov.in" + href
        filename = full_url.split("/")[-1]
        filepath = os.path.join(save_dir, filename)

        try:
            print(f"⬇️ Downloading {filename}...")
            file_response = requests.get(full_url)
            with open(filepath, 'wb') as f:
                f.write(file_response.content)
            print(f"✅ Saved to {filepath}")
            download_links.append((text, full_url))
        except Exception as e:
            print(f"❌ Failed to download {filename}: {e}")


