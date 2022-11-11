from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# тест 10 - выход из аккаунта
def test_exit_cabinet(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('aygulshafigullina_4_789@ya.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
    driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"