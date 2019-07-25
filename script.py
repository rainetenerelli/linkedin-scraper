# imports
from selenium import webdriver
import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector


# defining new variable passing two parameters
#writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
#writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/uas/login')

username = driver.find_element_by_id('username')
username.send_keys(parameters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(0.5)

driver.get('https://www.linkedin.com/in/rainetenerelli/')

sel = Selector(text=driver.page_source)

name = sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
name = name.strip()

job = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal")]/text()').extract_first()
job = job.strip()

currentWorkplace = sel.xpath('//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
currentWorkplace = currentWorkplace.strip()

url = driver.current_url

contact = element = driver.find_element_by_xpath('//*[@id="ember71"]')
contact.click()
sleep(0.5)
sel2 = Selector(text=driver.page_source)


email = sel.xpath("//*[starts-with(@class,'pv-contact-info__contact-type ci-email')]/ul/*/*/a").get()
website = sel2.xpath("//*[starts-with(@class,'pv-contact-info__contact-type ci-websites')]/ul/*/*/a").get()


