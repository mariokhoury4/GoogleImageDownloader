from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os


URL = "https://www.google.com/search?q=1000+memes&rlz=1C1GCEU_enLB918LB918&hl=en&sxsrf=ALeKk00tRlApvFwfyzOctv-pYD5xXpyxPQ:1608463048109&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjyiPfkt9ztAhXsTxUIHcydBRQQ_AUoAXoECBQQAw&biw=767&bih=744"
driver = webdriver.Chrome(executable_path="D:/python project/chromedriver.exe")
driver.get(URL)

i = 0
while i < 7 :
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    try:
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(5)
    i+=1

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()
img_tags = soup.find_all("img", class_="rg_i")
count = 0
for i in img_tags:
    try:
        urllib.request.urlretrieve(i['src'], str(count)+".jpg")
        count+=1
        print("Number of images downloaded = "+str(count),end='\r')
    except Exception as e:
        pass
