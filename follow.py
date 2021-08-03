import os
import sys
import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

#username, password, person to search for follower list
username, password, ll  = str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])
options = Options()
resized = options.add_argument('window-size=1400,600')
driver = webdriver.Chrome(chrome_options=options, executable_path=os.getcwd()+'/chromedriver')
wait = WebDriverWait(driver, 5)
landing = driver.get('https://www.instagram.com/')
u = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(username)
p = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys(password)
log_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))).click()
ret = '#react-root > section > main > div > div > div > div > button'
save_login_info = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,ret))).click()
notifications = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'button.aOOlW.HoLwm'))).click()
search_input = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'div.LWmhU._0aCwM > input'))).send_keys(ll)
#click followers #href
element0  = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div'
uu = wait.until(ec.element_to_be_clickable((By.XPATH, element0))).click()
followers = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
#css selector sequence
"""
select1 = 'body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(2) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button'
select2 ='body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(3) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button'
select3 ='body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(4) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button'
select9='body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(5) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button'
select10='body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(6) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button'
"""
#xpath elements sequence
"""
one = /html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button
two = /html/body/div[5]/div/div/div[2]/ul/div/li[2]/div/div[3]/button
three = /html/body/div[5]/div/div/div[2]/ul/div/li[3]/div/div[3]/button
four = /html/body/div[5]/div/div/div[2]/ul/div/li[4]/div/div[3]/button
"""
#xpath elements sequence after scroll
"""
scoll0 = /html/body/div[5]/div/div/div[2]/ul/div/li[9]
scroll1 = /html/body/div[5]/div/div/div[2]/ul/div/li[9]/div/div[2]/button
"""
##TODO: swap sleep with better way and optimize
for i in range(1, 1000000000000000):
    time.sleep(5)
    path = '/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button'
    el = driver.find_element_by_xpath(path).click()
    if i % 6 == 0: 
        try:
            scroll = ActionsChains(driver)
            scroll.move_to_element(el).perform()
            sel = driver.find_element_by_xpath(path).click()
        except NoSuchElementException as exception:
            time.sleep(3) 
        wait.until(ec.element_to_be_clickable((By.XPATH,path))).click() 
