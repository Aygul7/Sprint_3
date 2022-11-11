from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# тест 8 - Переход из личного кабинета в конструктор по клику на Конструктор
def test_move_to_constructor_button_constructor(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# тест 9 - Переход из личного кабинета в конструктор по клику на логотип
def test_move_to_constructor_Click_logo(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
    driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'