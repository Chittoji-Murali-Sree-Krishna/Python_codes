from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep  # for loading issues
browser = webdriver.Chrome()
browser.get('https://www.amazon.in/')
search = browser.find_element_by_id("twotabsearchtextbox")
search.send_keys('nokia5.3')
sleep(2)
search.send_keys(Keys.RETURN)
sleep(2)
ram = browser.find_element_by_xpath(
    '//*[@id="p_n_feature_seven_browse-bin/8561133031"]/span/a/span')
ram.click()
mobile = browser.find_element_by_xpath(
    '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[1]/div/div/span/a/div/img')
mobile.click()
sleep(10)
addToCart = browser.find_element_by_id('add-to-cart-button')
addToCart.click()
