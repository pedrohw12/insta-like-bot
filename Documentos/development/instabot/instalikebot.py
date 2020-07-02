from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = ""
password = ""

getdriver = ("https://www.instagram.com/accounts/login/")
global driver

driver = webdriver.Chrome()
driver.get(getdriver)

time.sleep(1)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Entrar')]").click()

def first_picture(): 
	
	# finds the first picture 
	pic = driver.find_element_by_class_name("_9AhH0") 
	pic.click() # clicks on the first picture 

def like_pic(): 
	time.sleep(4) 
	like = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span') 

	# you can find the like button using class name too 
	time.sleep(2) 
	like.click() # clicking the like button 

first_picture()
like_pic()
