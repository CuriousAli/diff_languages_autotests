from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_parametrs_via_cmd(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

