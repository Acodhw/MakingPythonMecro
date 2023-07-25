from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

urlLs = []

for i in range(1, 21): # i has integar in range 1 ~ 20
    driver.get("http://wikidocs.net/" + str(i)) # link open
    dic = {"Url" : driver.current_url, "Title" : driver.title} # make dictonary
    urlLs.append(dic) # append dictonary to list
    time.sleep(1)

print(urlLs) # print urls
driver.quit()