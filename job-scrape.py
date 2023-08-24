import requests                 # http requests
from bs4 import BeautifulSoup   # web-scraper
import pandas as pd             # dataframes

jobs = {}
page_number = 1

term = input("Input job search keyword: \n")

page = f"https://www.mcsgroup.jobs/jobs/?keyword={term}&page={page_number}"


for page in range(1, 4):
   
    page = f"https://www.mcsgroup.jobs/jobs/?keyword={term}&page={page_number}"

    response = requests.get(page, allow_redirects=False, timeout=8)
    html = response.text

    soup = BeautifulSoup(html, "html.parser") # web-scraper
    results = soup.findAll("div", { "class" : "card job MCS" }) # accessing outer html element

    for result in results:
        
        
        job_listing_details = result.findAll("div", {"class" : "col"}) # columns with data required

        # collect targeted job information
        job_listing_date = job_listing_details[0].find("span").text[7:]
        job_title = job_listing_details[2].find("h4").text
        job_link = f'https://www.mcsgroup.jobs{job_listing_details[2].find("a")["href"]}'
        job_salary = job_listing_details[3].find("strong").text
        job_location = job_listing_details[4].find("strong").text
        job_type = job_listing_details[5].find("strong").text


        jobs[job_title] = {
            "Min Salary" : job_salary[:6], 
            "Location" : job_location,
            "Type" : job_type,
            "Listed" : job_listing_date,
            "Link" : job_link
            }

    page_number = page_number+1

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)


df = pd.DataFrame.from_dict(jobs).transpose() # transpose swaps rows to columns


if df.empty:
    print('No results found!')
else:
    print(df)

