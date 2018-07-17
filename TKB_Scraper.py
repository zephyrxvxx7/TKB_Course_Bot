from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from time import sleep
from info import username, password, className, year, month, day, branch, time, grabbed


mainUrl = "http://bookseat.tkblearning.com.tw/book-seat/student/login/toLogin"


chrome_options = webdriver.ChromeOptions()

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()


def login():
    browser.get(mainUrl)

    loginCode = browser.find_element_by_xpath('//*[@id="LoginCode"]').text
    loginCodelist = loginCode.split(' ')
    loginCode = ''.join(loginCodelist)

    browser.find_element_by_xpath('//*[@id="id"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="pwd"]').send_keys(password)
    browser.find_element_by_xpath(
        '//*[@id="logininputcode"]').send_keys(loginCode)

    browser.find_element_by_xpath(
        '/html/body/form/div/div/div/table/tbody/tr[6]/td[2]/div[1]/a').click()

    print('登入成功')


def grab():
    global className

    select = Select(browser.find_element_by_xpath('//*[@id="class_selector"]'))
    for op in select.options:
        if(op.text[:len(className)] == className):
            className = op.text
    select.select_by_visible_text(className)
    sleep(0.5)

    select = Select(browser.find_element_by_xpath('//*[@id="date_selector"]'))
    select.select_by_value(
        '{year}-{month:0>2s}-{day:0>2s}'.format(year=year, month=month, day=day))
    sleep(0.5)

    select = Select(browser.find_element_by_xpath(
        '//*[@id="branch_selector"]'))
    select.select_by_visible_text(branch + '數位學堂')
    sleep(0.5)

    browser.find_element_by_xpath(
        '//*[@id="session_time_div"]/input[{0}]'.format(time)).click()

    userinputCode = browser.find_element_by_xpath('//*[@id="code"]').text
    userinputCodelist = userinputCode.split(' ')
    userinputCode = ''.join(userinputCodelist)

    browser.find_element_by_xpath(
        '//*[@id="userinputcode"]').send_keys(userinputCode)

    if grabbed:
        browser.find_element_by_xpath(
            '/html/body/div[3]/div[3]/div/div[2]/section/article/table/tbody/tr[8]/td[2]/div[1]/a').click()
        alert = browser.switch_to_alert()
        print(alert.text)
        alert.accept()
        alert = browser.switch_to_alert()
        alert.accept()
        print('選課成功')

    sleep(5)


if __name__ == "__main__":
    login()
    grab()
    browser.close()
