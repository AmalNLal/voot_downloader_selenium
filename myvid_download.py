#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[12]:


class Myvid():
    def __init__(self,url):
        self.url = url
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",'video/mp4')
        self.bot = webdriver.Firefox(firefox_profile=profile)
    
    def access(self):
        bot = self.bot
        bot.get('https://myvid.download/')
        time.sleep(5)
        ip = bot.find_element_by_id('dlURL')
        ip.send_keys(self.url)
        ip.send_keys(Keys.RETURN)
        time.sleep(15)
    
    def download(self):
        bot = self.bot
        dls = bot.find_elements_by_class_name('text-right')
        dls[3].click()
        


# In[14]:


#my = Myvid()
#my.access()
#my.download()


# In[ ]:




