#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import myvid_download


# In[2]:


class Voot:
    def __init__(self):
        self.bot = webdriver.Firefox()
    
    def access(self):
        bot = self.bot
        bot.get('https://voot.com/shows/bigg-boss/100730')
        time.sleep(5)
        bot.find_element_by_class_name('MuiTypography-root-93.DefaultCard-metatitle-517.MuiTypography-body2-101').click()
        time.sleep(5)
        return str(bot.current_url)


# In[3]:


v = Voot() 
url = v.access()
my = myvid_download.Myvid(url)
my.access()
my.download()


# In[ ]:




