import calendar
import time
from datetime import datetime

from config import LOGIN, PASSWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

curent_date = datetime.now()
month_days = calendar.monthrange(curent_date.year, curent_date.month)



url = {'main_page' : 'https://crm.soller-mts.com/login' ,
       'dispatcher_page' : 'https://crm.soller-mts.com/zgloszenia/lista/dyspozytor',
       }

browser = webdriver.Firefox(executable_path='//home/venia_ventis/PycharmProjects/pythonProject/firefoxdriver/geckodriver')

try:
    browser.get(url=url['main_page'])
    time.sleep(5)
    email_input = browser.find_element_by_name("_username")
    email_input.clear
    email_input.send_keys(LOGIN)
    time.sleep(2)

    password_input = browser.find_element_by_name("_password")
    password_input.clear
    password_input.send_keys(PASSWORD)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    browser.get(url=url['dispatcher_page'])

    first_date_input = browser.find_element_by_id("issue_filter_dispatcher_createdAtFrom")
    time.sleep(1)
    first_date_input.send_keys('{}-{}-{}'.format(curent_date.year,curent_date.month,month_days[0]))

    time.sleep(1)

    last_date_input = browser.find_element_by_id("issue_filter_dispatcher_createdAtTo")
    time.sleep(1)
    last_date_input.send_keys('{}-{}-{}'.format(curent_date.year,curent_date.month,month_days[1]))

    time.sleep(2)

    dispatcher_name = browser.find_element("xpath",
                                           "/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/form/div[3]/div[3]/div/span/span[1]/span/span[2]").click()
    dispatcher_name_input = browser.find_element("xpath", "/html/body/span/span/span[1]/input")
    dispatcher_name_input.send_keys("Daniel Ventsis")


    time.sleep(4)

    order_status = browser.find_element_by_class_name("btn-group").click()
    order_completed = browser.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/form/div[1]/div[4]/div/span/div/ul/li[5]").click()
    new_order = browser.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/form/div[1]/div[4]/div/span/div/ul/li[2]/a/label/input").click()
    order_in_progress = browser.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/form/div[1]/div[4]/div/span/div/ul/li[4]/a/label/input").click()

    time.sleep(2)

    allow_click = browser.find_element("xpath", "html/body/div[1]/div/div[3]/div/div[3]/div/div/div[2]/form/div[7]/div/button").click()

    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()