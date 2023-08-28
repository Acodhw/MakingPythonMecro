from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
from urllib import request

# first work

print("Your Keyword : ", end="")
keyword = input()

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?sca_esv=559959589&hl=ko&sxsrf=AB5stBhJnmcyaFp8JUOzhEwj-zfq2gCSXQ:1692969712364&q='+keyword+'&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjao8jS8_eAAxVGbPUHHaWrCpQQ0pQJegQIDBAB&biw=1082&bih=747&dpr=1.25') #search to google
time.sleep(1)
el = driver.find_element(
    By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
el_url = el.get_attribute('src') 
print(el_url)
request.urlretrieve(el_url, keyword+".jpg") 
driver.close()

# Second work

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/joonggonara/1005170350?q=%ED%82%AC%EB%A7%81%EC%BA%A0%ED%94%84+%EC%A4%91%EA%B3%A0%EB%82%98%EB%9D%BC&rc=&art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtdHJhZGUtYXJ0aWNsZQ.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6Impvb25nZ29uYXJhIiwiYXJ0aWNsZUlkIjoxMDA1MTcwMzUwLCJpc3N1ZWRBdCI6MTY5MTQxNDQ3NjAxOX0.gSGhRLrM1zVCRagPK4EukuURQKFQYxUqcWgPG2C-aDI') #link get
time.sleep(3)

iframe = driver.find_element(By.XPATH, '//*[@id="cafe_main"]') #Get iframe
driver.switch_to.frame(iframe)

el = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/img')
el_url = el.get_attribute('src') 
print(el_url)
request.urlretrieve(el_url, "iframe.jpg") ;