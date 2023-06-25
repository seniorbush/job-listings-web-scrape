import requests                 # http requests
from bs4 import BeautifulSoup   # web-scraper
import pandas as pd             # dataframes


url = "https://www.mcsgroup.jobs/jobs/?keyword=developer&location=belfast&radius=20&sector=it+%26+digital"

response = requests.get(url, allow_redirects=False, timeout=4)
html = response.text

soup = BeautifulSoup(html, "html.parser") # web-scraper
results = soup.findAll("div", { "class" : "card job MCS" })

jobs = {}


for result in results:
    

    job_listing_details = result.findAll("div", {"class" : "col"})

    job_date_posted = job_listing_details[0].find("span").text[7:]
    job_title = job_listing_details[2].find("h4").text
    job_link = f'https://www.mcsgroup.jobs{job_listing_details[2].find("a")["href"]}'
    job_salary = job_listing_details[3].find("strong").text
    job_location = job_listing_details[4].find("strong").text
    job_type = job_listing_details[5].find("strong").text


    jobs[job_title] = {
        "salary" : job_salary, 
        "location" : job_location,
        "type" : job_type,
        "date" : job_date_posted,
        "link" : job_link
        }

print(jobs)
        
    
