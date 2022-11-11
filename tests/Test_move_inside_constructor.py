from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#тест 11 - прокрутить до соусов
def test_move_inside_constructor_scroll_sauce(driver):
    sauce = driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]")
    driver.execute_script("arguments[0].scrollIntoView();", sauce)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Соус Spicy-X')]")))
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Соус Spicy-X')]").text == 'Соус Spicy-X'


# тест 12 - прокрутить до начинки
def test_move_inside_constructor_scroll_filling(driver):
    filling = driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]")
    driver.execute_script("arguments[0].scrollIntoView();", filling)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]")))
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]").text == 'Мясо бессмертных моллюсков Protostomia'


# тест 13 - прокрутить до булки
def test_move_inside_constructor_scroll_buns(driver):
    buns = driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]")
    driver.execute_script("arguments[0].scrollIntoView();", buns)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")))
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]").text == 'Флюоресцентная булка R2-D3'


# тест 14 - кликнуть на раздел Соусы в верхнем горизонтальном меню
def test_move_inside_constructor_click_sauce(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Соус Spicy-X')]")))
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Соус Spicy-X')]").text == 'Соус Spicy-X'

# тест 15 -кликнуть на раздел Начинки в верхнем горизонтальном меню
def test_move_inside_constructor_click_filling(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]")))
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]").text == 'Мясо бессмертных моллюсков Protostomia'

# тест 16 - кликнуть на раздел Булки в верхнем горизонтальном меню
def test_move_inside_constructor_click_buns(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")))
    driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").click()
    assert driver.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]").text == 'Флюоресцентная булка R2-D3'