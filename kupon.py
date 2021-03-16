import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver import ActionChains


def reg():
    global browser
    browser = webdriver.Chrome("C:\CH\chromedriver.exe")
    browser.set_window_size(1200, 720)
    browser.get('https://uc.zone/login/')
    textlogin = browser.find_element_by_name('login')
    textlogin.send_keys('***')
    textpass = browser.find_element_by_name('password')
    textpass.send_keys('***')
    textbutton = browser.find_element_by_xpath('//*[@id="top"]/div[3]/div/div/div[2]/div/div/div/form/div[1]/dl/dd/div/div[2]/button')
    textbutton.send_keys(Keys.ENTER) #Конец регистрации

def findpromo():
    time.sleep(1)
    global promo
    textpromo = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div[1]')
    promo = str(textpromo.text)
    print("Latest:", promo)
    browser.refresh()
    global promo2
    textpromo2 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div[1]')
    promo2 = str(textpromo2.text)
    while promo2 == promo:
        textpromo2 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div[1]')
        promo2 = str(textpromo2.text)
        #browser.refresh()

    if promo2 != promo:
        browser.get('https://uc.zone/account/promocode')
        inputpromo = browser.find_element_by_name('promocode')
        inputpromo.send_keys(promo2)
        print("New:", promo2)
        #inputpromo.send_keys(Keys.ENTER)


reg()
findpromo()

