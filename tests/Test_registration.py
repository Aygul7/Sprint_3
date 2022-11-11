from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# тест 1 - успешная регистрация с именем "Aygul", email "aygulshafigullina_4_789@ya.ru", паролем "123456"
def test_registration(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('Aygul')
    driver.find_element(By.XPATH,
                            "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
            'aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'


# тест 2 - ошибка для некорректного пароля "1234"
def test_registration_error(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
    # assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('Aygul')
    driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
        'aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('1234')
    driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
    assert driver.find_elements(By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
