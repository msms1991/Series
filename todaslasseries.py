from operator import index
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas


PATH = '/Users/maxi_/Desktop/Driver/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.starz.com/ar/es/view-all/blocks/1523514')

time.sleep(5)

seriess = list()

count = 0 
for X in range(1,25):
    for Y in range(1,5):
        xpath = f'/html/body/starz-root/div/div[1]/section/starz-view-all/div/div/div/div/section[1]/virtual-scroller/div[2]/div[{X}]/div[{Y}]/div/starz-content-item/article/div[1]/a[1]/h3'
        series = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        print("Nombre de serie: ",series)
        seriess.append(seriess) 
        
df = pandas.DataFrame({'Series: ' , seriess})

df.to_csv('Probandomil.csv', index = False)