from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

print("="*50)
print('''Bem vindo ao Billy \nDesenvolvido por Davi "yotta" Almeida ''')
print("="*50)

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Dev\chromedriver.exe")

driver.get("https://google.com.br")

elem = driver.find_element_by_name("q")
elem.click()
elem.send_keys("Curso em Video" + Keys.RETURN)

elem = driver.find_element_by_css_selector("h3.LC20lb DKV0Md")
elem.click()
