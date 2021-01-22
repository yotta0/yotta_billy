# Os imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# apresentação 

print("="*50)
print('''Bem vindo ao Billy \nDesenvolvido por Davi "yotta" Almeida ''')
print("="*50)
driver = webdriver.Chrome(executable_path=r"C:\Program Files\Dev\chromedriver.exe")


# Login
name_login = "uabb-lf-name"
passw_login = "uabb-lf-password"  

login = "davicastroti@hotmail.com"
passw = "senha"

driver.get("https://www.cursoemvideo.com/login/")

input_login = driver.find_element_by_name(name_login)
input_passw = driver.find_element_by_name(passw_login)
input_login.send_keys(login)
input_passw.send_keys(passw + Keys.RETURN)

sleep(2)

def test():

    driver.get("https://www.cursoemvideo.com/course/html5/")
    sleep(5)
    driver.get("https://www.cursoemvideo.com/minha-conta/")
    sleep(5)
    driver.get("https://www.cursoemvideo.com/course/html5/")




while True:
    test()