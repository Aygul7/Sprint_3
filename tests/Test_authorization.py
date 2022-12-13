from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.Locators import TestLocators

# тест 3 - войти с правильным email и паролем по кнопке "Войти"
def test_auth_login(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_BUTTON)))
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_ENTER_H2)))
    driver.find_element(*TestLocators.AUTH_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.AUTH_FIELD_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

# тест 4 - вход через кнопку «Личный кабинет»
def test_auth_cabinet_button(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.AUTH_FIELD_EMAIL)))
    driver.find_element(*TestLocators.AUTH_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.AUTH_FIELD_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


# тест 5 - вход по тексту "Войти" на странице регистрации
def test_auth_enter(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_BUTTON)))
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_REGISTRATION_H2)))
    driver.find_element(*TestLocators.LOGIN_TEXT_REGISTRATION_FORM).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.AUTH_FIELD_EMAIL)))
    driver.find_element(*TestLocators.AUTH_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.AUTH_FIELD_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


# тест 6 - вход по кнопке "Войти" в форме "Восстановить пароль"
def test_auth_forgot_password(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_BUTTON)))
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.RESTORE_PASSWORD_TEXT).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((TestLocators.AUTH_FIELD_EMAIL)))
    driver.find_element(*TestLocators.LOGIN_TEXT_RESTORE_PASSWORD).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_ENTER_H2)))
    driver.find_element(*TestLocators.AUTH_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.AUTH_FIELD_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.AUTH_LOGIN_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

