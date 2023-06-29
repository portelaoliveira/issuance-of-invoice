from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

path = os.getcwd()
archive = path + r"\login.html"
driver = webdriver.Chrome()
driver.get(archive)

login = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
login.send_keys("testewebscraping@gmail.com")
password = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
password.send_keys("123456")

login_click = driver.find_element(By.XPATH, "/html/body/div/form/button")
login_click.click()

name = driver.find_element(By.NAME, "nome")
name.send_keys("Web Scraping Automation - Nome")

address = driver.find_element(By.NAME, "endereco")
address.send_keys("Street 54, Block 59, Home 67 - Endereço")

neighborhood = driver.find_element(By.NAME, "bairro")
neighborhood.send_keys("Web Scraping - Bairro")

county = driver.find_element(By.NAME, "municipio")
county.send_keys("Web Scraping - Município")

cep = driver.find_element(By.NAME, "cep")
cep.send_keys("12345678")

uf = driver.find_element(By.TAG_NAME, 'select')
uf_select = Select(uf)
uf_select.select_by_visible_text("DF")

cnpj_or_cpf = driver.find_element(By.NAME, "cnpj")
cnpj_or_cpf.send_keys("03040590049")

state_registration = driver.find_element(By.NAME, "inscricao")
state_registration.send_keys("Web Scraping - Inscrição estadual")

service_description = driver.find_element(By.NAME, "descricao")
service_description.send_keys("Web Scraping - Descrição do produto/serviço")

quantity = driver.find_element(By.NAME, "quantidade")
quantity.send_keys("27")

unitary_value = driver.find_element(By.NAME, "valor_unitario")
unitary_value.send_keys("2,6")

total_value = driver.find_element(By.NAME, "total")
total_value.send_keys("250,68")

sleep(10)
