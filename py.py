from operator import index
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
start_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(start_URL)
time.sleep(10)
scraped_data=[]

def scrape():
    headers=["Star_name", "Distance", "Mass", "Radius", "Luminosity"]
    planet_data=[]
    for i in range(0,400):
        soupe = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soupe.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:

                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            
        browser.find_element(By.XPATH,value='//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open("scraper.csv","w") as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planet_data)
scrape()        

    
