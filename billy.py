from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

print("="*50)
print('''Bem vindo ao Billy \nDesenvolvido por Davi "yotta" Almeida ''')
print("="*50)
driver = webdriver.Chrome(executable_path=r"C:\Program Files\Dev\chromedriver.exe")

name_login = "uabb-lf-name"
passw_login = "uabb-lf-password"
name_user = "davicastroti@hotmail.com"
passw_user = "Jdac455247rd1414."

driver.get("https://www.cursoemvideo.com/login/")

element_name = driver.find_element_by_name(name_login)
element_passw = driver.find_element_by_name(passw_user)

element_name.send_keys(name_user)







