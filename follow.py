#!/usr/bin/python3
import sys
import time
import numpy as np
from random import randint
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class Follow:
 
    def __init__(self, headless):
        opt = Options()
        if headless:
            opt.add_argument('--headless')
        self.driver = webdriver.Firefox(options=opt)
        print('selenium running..')
    
    def __del__(self):
        ##TODO: remove time.sleep when it is working
        time.sleep(0)
        self.driver.close()
        print("selenium stopped")
    
    def get_instagram(self):
        self.driver.get('https://www.instgram.com/')
    
    def send_username(self, _username):
        u = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'))).send_keys(_username)

    def send_password(self, _password):
        p = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'))).send_keys(_password) 
    
    def login(self):
        l = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div'))).click()
    
    def save_login_info(self):
        k = '/html/body/div[1]/section/main/div/div/div/div/button'
        n = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,k))).click()
    
    def turn_off_notif(self):
        not_now = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)'))).click()

    def search_bar(self, followers):
        search = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'))).send_keys(followers)
        go = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a'))).click()
   
    def follower_amount(self):
        ret = 0
        followers = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'))).click()
        followers_text =  WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'))).text
        followers_text = str(followers_text)
        small = True
        #if they have over 100k followers
        if len(followers_text) == 14:
            ret = int(followers_text[0:3])*100000
            small = False
        #if they have something like 14.6k followers, we lose the hundreds place but still decent
        #and if not, they have something like 1344, then we leave alone and iter that amount
        if len(followers_text) == 15:
            for i in followers_text:
                if i == '.':
                    print(type(int(followers_text[0:2])))
                    ret = int(followers_text[0:2])*1000
                    small = False
            if small:
                ret = int(followers_text[0:4])
        return ret

    def close_follower_box(self):
        close = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div/div[1]/div/div[2]/button'))).click()
    
    def set_topics(*argv):
        li = [arg for arg in argv]
        return li
    
    def check_topic(substring, name):
        ret = False
        if len(str(name)) <  0:
            return ret
        for substring in name:
            if substring in name or substring+'_' in name or '_'+substring in name:
                ret = True
        return ret
    
    def element_present(self,text):
        ttext = WebDriverWait(self.driver, 5).until(ec.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, text)))
        if ttext:
            return True
        else: 
            return False
    
    def setup(self, _username=None, _password=None, acc=None, topics=None):
        self.get_instagram()
        self.send_username(_username)
        self.send_password(_password)
        self.login()
        self.save_login_info()
        self.turn_off_notif()
        parent_account = self.search_bar(acc)

    def search_follow_public_only(self, followers):
        ##TODO: if by random we get three accounts that are private in a row,
        ## the system will break. as of now program works for about 5 account bounces.
        ## GOAL is to go for the duration of 0..followers.
        ig_usernames = np.array([0], dtype=np.int32)
        i, j, k, private = 0,1,1,0
        rand_account = lambda _: ig_usernames[randint(1,len(ig_usernames))]

        while followers > i:
            i += 1
            time.sleep(3)
            
            try:
                followers_href = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'li.Y8-fY:nth-child(2) > a:nth-child(1)'))).click()
                usr = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a')
                usr_text = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a').text
                ig_usernames = np.append(ig_usernames, usr_text) 
                print(ig_usernames)
            
            except Exception as NoSuchElement:
                self.search_bar(rand_account(''))

            if i == 10:
                i = 1
                print(i,'i ==10 block  -------')
                close = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div/div[1]/div/div[2]/button'))).click()
                self.search_bar(ig_usernames[j])
                time.sleep(3)
                j += 1
                
                try:
                    followers_href.click()
            
                except Exception as TimeoutException:
                    print("the user {} is private".format(ig_usernames[j]))
                    j += 1
                    private = True
                
                if private == True:
                    try:
                        p = 'This Account is Private'
                        private_text = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(By.XPATH, '/html/body/div[1]/section/main/div/div/article/div[1]/div/h2')).text
                        
                        if str(private_text)[0:3] == p[0:3]:
                            self.search_bar(rand_account(''))
                    
                    except Exception as TimeoutException:
                        try:
                            self.driver.find_element_by_xpath("//div[@class='vIsJD' and text()='\
                                Follow to see their photos and videos.']")
                        except Exception as NoSuchElement:
                             self.search_bar(rand_account(''))
                    
                    private = False
                   
        return ig_usernames

    def follow_by_scroll(self, followers):
        ##TODO: when i == 12, the dialogue box seems to not load properly
        ig_usernames = np.array([0], dtype=np.int32)
        followers_href = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'li.Y8-fY:nth-child(2) > a:nth-child(1)'))).click()
        for i, k in enumerate(range(1, followers)):
            i += 1
            time.sleep(3)
            usr = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable(By.XPATH,'/html/body/div[6]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a'))
            usr_text = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a').text
            ig_usernames = np.append(ig_usernames, usr_text)
            if k > 6:
                time.sleep(3)
                usr_text.location_once_scrolled_into_view
            print(ig_usernames)
    
def main():    
    username=input()
    password=input()
    account= input()
    f = Follow(0)
    tt = f.setup(username, password, account, topics=None)
    fg = f.search_follow_public_only(1000)
    #gg = f.follow_by_scroll(1000)
if __name__ == '__main__':
    main()
