from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Dev\chromedriver.exe")

driver.get("https://google.com.br")
