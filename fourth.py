# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#first Work

print("Find name ", end=">> ")
name = input()

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[5]/a').click() #CAPS wiki Link
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[5]/div/ul/li[3]/a').click() #CAPS wiki Link
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="search"]').send_keys(name) # input 
driver.find_element(
    By.XPATH, '/html/body/section[2]/div[1]/form/button').click()  # click search button
time.sleep(2)

if not driver.find_element(By.XPATH, '/html/body/section[3]/div/p').text == "해당 문서가 없습니다.":
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
else:
    print("Not Founded.")


#Second Work

