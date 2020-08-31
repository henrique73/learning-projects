from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import urllib.request

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get("https://www.reddit.com/r/aww/top/?t=day")


linkElem = driver.find_elements_by_css_selector('[alt="Post image"]')
    

for i in linkElem:
    if "external" not in i.get_attribute("src"):
        link = i.get_attribute("src")
        print(link)
        urllib.request.urlretrieve(link, "r/awwImage.png")
        break
        
