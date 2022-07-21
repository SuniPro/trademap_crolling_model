from lib2to3.pgen2 import driver
from xml.dom.minidom import Element
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from openpyxl import workbook
import pandas as pd
import requests

# Create python excel / for excel analysis model
wb = workbook()
ws = wb.active
ws.title = "abrams"
wb.save('abrams hscode integration.xlsx')
wb.close()

# read_excel / import pycxel part 20x20
idmethod = pd.read_excel('C:/Users/수니/Desktop/pymodel/example.xlsx', sheet_name = 'hscodesetting 1', usecols=[2], skiprows=[2])
passmethod = pd.read_excel('C:/Users/수니/Desktop/pymodel/example.xlsx', sheet_name = 'hscodesetting 1', usecols=[2], skiprows=[3])


# login method model
idmethod = input('이메일 : ')
passmethod = input('비밀번호 : ')
class_txt = input('HS CODE 입력: ')
selectimports = input('수입은 입, 수출은 출을 입력하세요 :')




path = "C:/Users/수니/Desktop/pymodel/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.trademap.org/')
time.sleep(8)

# id 입력 메소드
driver.find_element_by_id("ctl00_MenuControl_Label_Login").click()
idelement = driver.find_element_by_id("Username")
idelement.send_keys(idmethod)
time.sleep(1)

# password 입력 메소드

driver.find_element_by_id("Password").click()
passelement = driver.find_element_by_id("Password")
passelement.send_keys(passmethod)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/form/fieldset/div[4]/div/button').click()

# login process complate

# visual input model 

''' 가상 입력 모델 작성 (임시) '''

selectimports = input('수입은 입, 수출은 출을 입력하세요 :')
# importsproductcode = input('HSCODE:')
importsproductcode = "090111"


if selectimports == "입":

    # 수입 HSCODE 입력
    driver.find_element_by_id("ctl00_PageContent_label_RadioButton_TradeType_Import").click() # 수입 클릭
    time.sleep(4)
    # driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product").click() # productcode div 클릭
    driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product_Input").click() # productcode inputbox 클릭
    importelement1 = driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product_Input")
    importelement1.send_keys(importsproductcode)
    time.sleep(3)
    driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product_c0").click() # 하단 드롭메뉴 첫번째 productcode 클릭
    
    # 수입국가
    importscontry = input('수입국가를 입력하세요: ') # Korea, Republic of
    driver.find_element_by_id("ctl00_PageContent_RadComboBox_Country_Input").click()
    importelementcontry = driver.find_element_by_id("ctl00_PageContent_RadComboBox_Country_Input")
    importelementcontry.send_keys(importscontry)
    time.sleep(3)
    driver.find_element_by_id("ctl00_PageContent_RadComboBox_Country_c0").click() # 하단 드롭메뉴 첫번째 국가 선택
    
    
    # 대상국가
    importspartner = input('대상국가를 입력하세요: ') # France
    driver.find_element_by_id("ctl00_PageContent_RadComboBox_Partner_Input").click()
    importelementpartner = driver.find_element_by_id("ctl00_PageContent_RadComboBox_Partner_Input")
    importelementpartner.send_keys(importspartner)
    time.sleep(3)
    driver.find_element_by_id("ctl00_PageContent_RadComboBox_Partner_c0").click()
    time.sleep(100)
    
else: selectimports == "출"
    
    
# 수출 HSCODE 입력
driver.find_element_by_id("ctl00_PageContent_label_RadioButton_TradeType_Export").click() # 수출 클릭
time.sleep(4)
# driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product").click() # productcode div 클릭
driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product_Input").click() # productcode inputbox 클릭
importelement1 = driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product_Input")
importelement1.send_keys(importsproductcode)
time.sleep(3)
driver.find_element_by_id("ctl00_PageContent_RadComboBox_Product_c0").click() # 하단 드롭메뉴 첫번째 productcode 클릭
    
    # 수입국가
importscontry = input('수입국가를 입력하세요: ') # Korea, Republic of
driver.find_element_by_id("ctl00_PageContent_RadComboBox_Country_Input").click()
importelementcontry = driver.find_element_by_id("ctl00_PageContent_RadComboBox_Country_Input")
importelementcontry.send_keys(importscontry)
time.sleep(3)
driver.find_element_by_id("ctl00_PageContent_RadComboBox_Country_c0").click() # 하단 드롭메뉴 첫번째 국가 선택
    
    
    # 대상국가
importspartner = input('대상국가를 입력하세요: ') # France
driver.find_element_by_id("ctl00_PageContent_RadComboBox_Partner_Input").click()
importelementpartner = driver.find_element_by_id("ctl00_PageContent_RadComboBox_Partner_Input")
importelementpartner.send_keys(importspartner)
time.sleep(3)
driver.find_element_by_id("ctl00_PageContent_RadComboBox_Partner_c0").click()
time.sleep(100)
# form class name find and input search in tag neme

# Table select method

selecttable = input('데이터테이블을 선택? :') # Trade indicators 등 데이터 테이블 선택 메소드

if selecttable == "무역지표": # 무역지표 선택

    driver.find_element_by_id("ctl00_PageContent_Button_TradeIndicators").click()
    table = driver.find_element_by_id("ctl00_PageContent_MyGridView1")
    req = requests.get()

elif selecttable == "연간시계열": # 연간시계열 지표 선택

    driver.find_element_by_id("ctl00_PageContent_Button_TradeIndicators").click()
# searchd element / class txt(hscode)

elif selecttable == "분기별시계열":

    driver.find_element_by_id("ctl00_PageContent_Button_TimeSeries_Q").click()

elif selecttable == "월별시계열":

    driver.find_element_by_id("ctl00_PageContent_Button_TimeSeries_M").click()

else: selecttable == "회사"
    
driver.find_element_by_id("ctl00_PageContent_Button_TimeSeries_M").click()

time.sleep(100)