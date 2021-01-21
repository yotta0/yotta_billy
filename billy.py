from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Dev\chromedriver.exe")
print("="*50)
print('''Bem vindo ao Billy \nDesenvolvido por Davi "yotta" Almeida ''')
print("="*50)

def login():
    name_login = "uabb-lf-name"
    passw_login = ""



driver.get("https://www.cursoemvideo.com/login/")

