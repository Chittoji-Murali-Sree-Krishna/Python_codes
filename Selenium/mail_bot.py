from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome()
browser.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1597037588&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d5e47432a-faef-5cf1-95bd-fb0b77ee31f9&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
search = browser.find_element_by_name("loginfmt")
search.send_keys("Your email")
search.send_keys(Keys.RETURN)
sleep(2)
passwd = browser.find_element_by_name("passwd")
passwd.send_keys("Your password")
sleep(2)
passwd.send_keys(Keys.RETURN)
sleep(2)
new = browser.find_element_by_id("id__3")
new.click()
sleep(5)
mail = browser.find_element_by_class_name("ms-BasePicker-input.pickerInput_34694d2a")
mail.send_keys("Recievers email")
mail.send_keys(Keys.TAB)
sleep(1)
sub = browser.find_element_by_id("TextField531")
sub.send_keys("hi this is selenium")
sub.send_keys(Keys.TAB)
sleep(1)
msg = browser.find_element_by_class_name("_4utP_vaqQ3UQZH0GEBVQe.B1QSRkzQCtvCtutReyNZ._3BPbKk5i3nczB3IlZG0FaR._17ghdPL1NLKYjRvmoJgpoK.yfRvh-CU21dFu_j7B1j_j")
msg.send_keys("hello warlord, this is message from your selenium bot")
msg.send_keys(Keys.TAB)
sleep(2)
send = browser.find_element_by_id("id__535")
send.click()
