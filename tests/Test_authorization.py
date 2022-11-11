from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# тест 3 - войти с правильным email и паролем по кнопке "Войти"
def test_auth_login(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    # assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

# тест 4 - вход через кнопку «Личный кабинет»
def test_auth_cabinet_button(driver):
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    # assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


# тест 5 - вход по тексту "Войти" на странице регистрации
def test_auth_enter(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
    # assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


# тест 6 - вход по кнопке "Войти" в форме "Восстановить пароль"
def test_auth_forgot_password(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]").click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/forgot-password"

