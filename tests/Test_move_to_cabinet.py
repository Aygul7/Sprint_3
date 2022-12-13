from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.Locators import TestLocators

# тест 7 - Переход в личный кабинет (после авторизации)
def test_move_to_cabinet(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_BUTTON)))
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_ENTER_H2)))
    driver.find_element(*TestLocators.AUTH_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.AUTH_FIELD_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'