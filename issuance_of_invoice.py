from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pandas as pd

table = pd.read_excel("NotasEmitir.xlsx")

path = os.getcwd()
archive = path + r"\login.html"

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": path + r"\invoices",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
driver.get(archive)

login = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
login.clear()
login.send_keys("testewebscraping@gmail.com")
password = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
password.clear()
password.send_keys("123456")
login_click = driver.find_element(By.XPATH, "/html/body/div/form/button")
login_click.click()

for line in table.index:
    name = driver.find_element(By.NAME, "nome")
    name.clear()
    name.send_keys(table.loc[line, "Cliente"])

    address = driver.find_element(By.NAME, "endereco")
    address.clear()
    address.send_keys(table.loc[line, "Endereço"])

    neighborhood = driver.find_element(By.NAME, "bairro")
    neighborhood.clear()
    neighborhood.send_keys(table.loc[line, "Bairro"])

    county = driver.find_element(By.NAME, "municipio")
    county.clear()
    county.send_keys(table.loc[line, "Municipio"])

    cep = driver.find_element(By.NAME, "cep")
    cep.clear()
    cep.send_keys(str(table.loc[line, "CEP"]))

    uf = driver.find_element(By.TAG_NAME, 'select')
    uf_select = Select(uf)
    uf_select.select_by_visible_text(table.loc[line, "UF"])

    cnpj_or_cpf = driver.find_element(By.NAME, "cnpj")
    cnpj_or_cpf.clear()
    cnpj_or_cpf.send_keys(str(table.loc[line, "CPF/CNPJ"]))

    state_registration = driver.find_element(By.NAME, "inscricao")
    state_registration.clear()
    state_registration.send_keys(str(table.loc[line, "Inscricao Estadual"]))

    service_description = driver.find_element(By.NAME, "descricao")
    service_description.clear()
    service_description.send_keys(table.loc[line, "Descrição"])

    quantity = driver.find_element(By.NAME, "quantidade")
    quantity.clear()
    quantity.send_keys(str(table.loc[line, "Quantidade"]))

    unitary_value = driver.find_element(By.NAME, "valor_unitario")
    unitary_value.clear()
    unitary_value.send_keys(str(table.loc[line, "Valor Unitario"]))

    total_value = driver.find_element(By.NAME, "total")
    total_value.clear()
    total_value.send_keys(str(table.loc[line, "Valor Total"]))

    dowload_invoice = driver.find_element(By.XPATH, '//*[@id="formulario"]/button')
    dowload_invoice.click()

    driver.refresh()

sleep(20)
