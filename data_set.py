#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://localhost:8888/?token=839f30ff7cbc19115d78218c73cfa17ace39a73751a509cc")
driver.get("http://localhost:8888/notebooks/dataset%20preparation.ipynb")
time.sleep(10)
driver.execute_script("document.body.style.zoom='150%'")
time.sleep(10)
elements = driver.find_elements(By.XPATH, '//td')
i=982
for element in elements:
    element.location_once_scrolled_into_view
    element.screenshot("images/" + str(i) + '.png')
    with open('texts/' +str(i)+ '.txt', 'w', encoding = 'utf-8') as file:
        file.write(element.text)
    i+=1
driver.close()


# In[ ]:




