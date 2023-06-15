from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

button = WebDriverWait(driver, 20).until(
    element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg[ng-click="customer()"]')))
button.click()

button = WebDriverWait(driver, 20).until(element_to_be_clickable((By.ID, 'userSelect')))
button.click()

dropdown = driver.find_element(by="id", value="userSelect")
select = Select(dropdown)
select.select_by_visible_text("Neville Longbottom")

new_button = WebDriverWait(driver, 20).until(element_to_be_clickable((By.CSS_SELECTOR,
                                                                      'button.btn.btn-default[type="submit"][ng-show="custId != \'\'"]')))

new_button.click()

welcome_message = WebDriverWait(driver, 20).until(
    visibility_of_element_located((By.CSS_SELECTOR, 'span.fontBig.ng-binding')))
assert welcome_message.text == 'Neville Longbottom', "User login failed"
