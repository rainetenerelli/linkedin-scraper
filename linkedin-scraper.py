#Import Libraries
from selenium import webdriver
from parsel import Selector
import parameters

driver = webdriver.Chrome('chromedriver')
profile_link="https://www.linkedin.com/in/christinelam320/"
driver.get(profile_link)

raw_input("Press enter when you're logged in.")
driver.get(profile_link)

#assign web page source code
sel = Selector(text=driver.page_source)

#will print these values to a csv
file_name = 'profiles.csv'

#gets the name of the connection
name = sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
name = name.strip()

job = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal")]/text()').extract_first()
job = job.strip()

recentExp = sel.xpath('//*[starts-with(@class, "t-16 t-black t-bold")]/text()').extract_first()
recentExp = recentExp.strip()

