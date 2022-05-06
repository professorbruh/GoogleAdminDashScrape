import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import json

driver = webdriver.Chrome(ChromeDriverManager().install())
login_details = {}
with open('login_details.json') as json_file:
    login_details = json.load(json_file)



def login():
    driver.get("https://admin.google.com/")
    time.sleep(5)
    email = driver.find_element_by_id("identifierId")
    email.send_keys(login_details["email"])
    next_button = driver.find_element_by_class_name("VfPpkd-vQzf8d")
    next_button.click();
    time.sleep(5)
    password = driver.find_element_by_name("password")
    password.send_keys(login_details["password"])
    next_button = driver.find_element_by_class_name("VfPpkd-vQzf8d")
    next_button.click()
    time.sleep(5)


login()