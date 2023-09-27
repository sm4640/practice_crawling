# 페이지 크롤링

# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.naver.com/'
# # url = 'https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
# response = requests.get(url, headers=headers)


# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# print(html)

###############################################################

# tbody = soup.select('#premier1 > div > table > tbody')
# trs = tbody.select('tr')
# print(html)
# print(tbody)
# for tr in trs:
#    print(tr)

# premier1 > div > table > tbody > tr:nth-child(2) > td:nth-child(15)
# print(tbody)

############################ 존나 성장한 후의 크롤링(23.07.06)###############################
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver = webdriver.Chrome('c:\\chromedriver.exe')
driver.implicitly_wait(5)

url = 'https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do'
driver.get(url)
driver.implicitly_wait(5)

#################### 여기까지 기본 세팅 ######################

selupjong = ['외식', '도소매', '서비스']

selindus1 = ['한식', '분식', '중식', '일식', '서양식', '기타 외국식', '패스트푸드',
             '치킨', '피자', '제과제빵', '아이스크림/빙수', '커피', '음료 (커피 외)', '주점', '기타 외식']
selindus2 = ['편의점', '의류 / 패션', '화장품', '농수산물', '(건강)식품', '종합소매점', '기타도소매']
selindus3 = ['교육 (교과)', '교육 (외국어)', '기타 교육', '유아 관련 (교육 외)', '부동산 중개', '임대', '숙박', '유아관련', '스포츠 관련', '이미용', '자동차 관련',
             'PC방', '오락', '배달', '안경', '세탁', '이사', '운송', '반려동물 관련', '약국', '인력 파견', '기타 서비스']
f = open("service.txt", 'w')
dropdown1 = Select(driver.find_element(By.XPATH, '//*[@id="searchCondition"]'))
dropdown1.select_by_value("3")

dropdown2 = Select(driver.find_element(By.XPATH, '//*[@id="selUpjong"]'))
dropdown2.select_by_visible_text(selupjong[2])
for i in selindus3:
    dropdown3 = Select(driver.find_element(By.XPATH, '//*[@id="selIndus"]'))
    dropdown3.select_by_visible_text(i)
    driver.implicitly_wait(5)

    driver.find_element(
        By.XPATH, '//*[@id="frm"]/div[4]/input[2]').click()

    driver.implicitly_wait(5)

    driver.find_element(
        By.XPATH, '//*[@id = "content"]/div[4]/table/thead/tr/th[5]/div/a[2]').click()

    driver.implicitly_wait(5)
    print('\n' + i + '\n')
    f.write('\n' + i + '\n\n')
    table = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/table')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    for tr in tbody.find_elements(By.TAG_NAME, 'tr')[1:]:
        txt = tr.find_element(By.TAG_NAME, 'td').text
        print(txt)
        f.write(txt + "\n")

f.close()

while True:
    pass
