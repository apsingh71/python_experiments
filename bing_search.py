import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ff_profile_dir= "C:/Documents and Settings/ted/Application Data/Mozilla/Firefox/Profiles/3guaoeq2.default"

ff_profile = webdriver.FirefoxProfile(ff_profile_dir)


browser=webdriver.Firefox(firefox_profile=ff_profile)

browser.get('http://www.bing.com')

text="What day is today"

for i in range(0, 15):
    rnd=chr(random.randint(32, 122))
    text += " " + rnd
    print(text)


    search_box = browser.find_element_by_name("q")
    search_box.clear()


    search_box.send_keys(text)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)    





browser.close()



''' import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()

browser.get('http://www.bing.com')

search_box = browser.find_element_by_name("q")

search_box.send_keys("Hello World")
search_box.send_keys(Keys.RETURN)



search_box = browser.find_element_by_name("q")
search_box.clear()



browser.close()

'''

