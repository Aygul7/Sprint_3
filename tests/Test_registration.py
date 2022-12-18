from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import TestLocators


#тест 1 - успешная регистрация с именем "Aygul", email "aygulshafigullina_4_789@ya.ru", паролем "123456"
def test_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_BUTTON)))
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_ENTER_H2)))
    driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_REGISTRATION_H2)))
    driver.find_element(*TestLocators.REG_FIELD_NAME).send_keys('Aygul')
    driver.find_element(*TestLocators.REG_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.REG_FIELD_PASSWORD).send_keys('123456')
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

#тест 2 - ошибка для некорректного пароля "1234"
def test_registration_error(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_BUTTON)))
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_ENTER_H2)))
    driver.find_element(*TestLocators.REGISTRATION_TEXT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOCATOR_REGISTRATION_H2)))
    driver.find_element(*TestLocators.REG_FIELD_NAME).send_keys('Aygul')
    driver.find_element(*TestLocators.REG_FIELD_EMAIL).send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(*TestLocators.REG_FIELD_PASSWORD).send_keys('1234')
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.find_element(*TestLocators.REGISTRATION_ERROR_MESSAGE).text == "Некорректный пароль"


