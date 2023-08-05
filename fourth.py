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


driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(0.5)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/a').click() #CAPS wiki Link
time.sleep(0.5)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/div/ul/li[4]/a').click() #CAPS wiki Link
time.sleep(0.5)

print("회장 : ", end="")
print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[1]/li').text) # name info get
print("정보 : ")
driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[1]/li/a[2]').click() #Document input
time.sleep(1)
print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text) #Document text get
print()
driver.back()

print("------------------------------------------------------------")
print("부회장 : ", end="")
print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[2]/li').text)
print("정보 : ")
driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[2]/li/a[2]').click() 
time.sleep(1)
print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
print()
driver.back()

print("------------------------------------------------------------")
print("학술부 : ")
ls = driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul[3]/li') #get list value of page wiki list
j = 1
for i in ls: #loop
    print(j)
    print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[3]/li['+ str(j) +']/a[2]').text, end = ", ")
    print("정보 : ")
    driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[3]/li['+ str(j) +']/a[2]').click() 
    time.sleep(1)
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
    print()
    driver.back()
    j+=1
    

print("------------------------------------------------------------")
print("기획부 : ")
ls = driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul[4]/li')
j = 1
for i in ls:
    print(j)
    print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[4]/li['+ str(j) +']/a[2]').text, end = ", ")
    print("정보 : ")
    driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[4]/li['+ str(j) +']/a[2]').click() 
    time.sleep(1)
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
    print()
    driver.back()
    j+=1

print("------------------------------------------------------------")
print("관리부 : ")
ls = driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul[5]/li')
j = 1
for i in ls:
    print(j)
    print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[5]/li['+ str(j) +']/a[2]').text, end = ", ")
    print("정보 : ")
    driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[5]/li['+ str(j) +']/a[2]').click() 
    time.sleep(1)
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
    print()
    driver.back()
    j+=1

print("------------------------------------------------------------")
print("총무부 : ")
ls = driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul[6]/li')
j = 1
for i in ls:
    print(j)
    print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[6]/li['+ str(j) +']/a[2]').text, end = ", ")
    print("정보 : ")
    driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[6]/li['+ str(j) +']/a[2]').click() 
    time.sleep(1)
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
    print()
    driver.back()
    j+=1

print("------------------------------------------------------------")
print("홈페이지관리부 : ")
ls = driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul[7]/li')
j = 1
for i in ls:
    print(j)
    print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[7]/li['+ str(j) +']/a[2]').text, end = ", ")
    print("정보 : ")
    driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[7]/li['+ str(j) +']/a[2]').click() 
    time.sleep(1)
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
    print()
    driver.back()
    j+=1

print("------------------------------------------------------------")
print("편집부 : ")
ls = driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul[8]/li')
j = 1
for i in ls:
    print(j)
    print(driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[8]/li['+ str(j) +']/a[2]').text, end = ", ")
    print("정보 : ")
    driver.find_element(By.XPATH, '/html/body/section[2]/div/ul[8]/li['+ str(j) +']/a[2]').click() 
    time.sleep(1)
    print(driver.find_element(By.XPATH, '/html/body/section[3]/div').text)
    print()
    driver.back()
    j+=1
