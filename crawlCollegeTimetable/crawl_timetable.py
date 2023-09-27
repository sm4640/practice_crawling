import requests
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp'
driver.get(url)
driver.implicitly_wait(5)

driver.find_element(  # 글로벌 선택
    By.XPATH, '/html/body/div/form/div[1]/table[1]/tbody/tr/td[3]/label[2]').click()


driver.implicitly_wait(5)

f = open("major.txt", 'w', encoding='utf-8')
driver.find_element(  # 전공/부전공
    By.XPATH, '/html/body/div/form/div[1]/table[2]/tbody/tr[1]/th/div[1]/label').click()

driver.implicitly_wait(5)

dropdown1 = Select(driver.find_element(By.XPATH, '//*[@id="ag_crs_strct_cd"]'))
select1 = driver.find_element(By.XPATH, '//*[@id="ag_crs_strct_cd"]')
options1 = select1.find_elements(By.TAG_NAME, 'option')

for i in range(len(options1)):
    dropdown1.select_by_index(i)
    driver.find_element(By.XPATH, '/html/body/div/form/div[2]/button').click()

    driver.implicitly_wait(5)

    table = driver.find_element(By.XPATH, '//*[@id="lssnTable"]')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    print(options1[i].text)
    # f.write(options1[i].text + '\n')
    time.sleep(2)
    for i in range(1, len(tbody.find_elements(By.TAG_NAME, 'tr'))+1):
        txt = tbody.find_element(
            By.XPATH, f'//*[@id="lssnlist"]/tr[{i}]/td[14]').text
        print(txt)
        f.write(txt + "\n")
    print('\n')
    f.write("\n\n")
    time.sleep(2)

f.close()
######################################################################

f = open("culture.txt", 'w', encoding='utf-8')
driver.find_element(  # 실용외국어/교양과목
    By.XPATH, '/html/body/div/form/div[1]/table[2]/tbody/tr[1]/th/div[2]/label').click()

dropdown2 = Select(driver.find_element(By.XPATH, '//*[@id="ag_compt_fld_cd"]'))
select2 = driver.find_element(By.XPATH, '//*[@id="ag_compt_fld_cd"]')
options2 = select2.find_elements(By.TAG_NAME, 'option')

for i in range(len(options2)):
    dropdown2.select_by_index(i)
    driver.find_element(By.XPATH, '/html/body/div/form/div[2]/button').click()

    driver.implicitly_wait(5)

    table = driver.find_element(By.XPATH, '//*[@id="lssnTable"]')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    print(options2[i].text)
    # f.write(options2[i].text + '\n')
    time.sleep(2)
    for i in range(1, len(tbody.find_elements(By.TAG_NAME, 'tr'))+1):
        txt = tbody.find_element(
            By.XPATH, f'//*[@id="lssnlist"]/tr[{i}]/td[14]').text
        print(txt)
        f.write(txt + "\n")
    print('\n')
    f.write("\n\n")
    time.sleep(2)

f.close()


while True:
    pass
