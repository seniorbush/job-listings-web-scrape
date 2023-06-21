import requests                 # http requests
from bs4 import BeautifulSoup   # web-scraper
import pandas as pd             # dataframes


url = "https://www.mcsgroup.jobs/jobs/?keyword=developer&location=belfast&radius=20&sector=it+%26+digital"

response = requests.get(url, allow_redirects=False, timeout=4)
html = response.text


soup = BeautifulSoup(html, "html.parser") # web-scraper

# Outer Most Entry Point of HTML:
outer_most_point = soup.find('div',attrs={'class': 'container-rl results-container'})

results = soup.findA("div", { "class" : "card job MCS" })

for result in results:
    
    # jobs = []

    # if (result["class"] == "xs-heading job-title"):
    #     jobs.append(result)
    print(result)
        
    
# print(jobs)