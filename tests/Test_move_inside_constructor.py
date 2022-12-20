from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import TestLocators

#тест 11 - прокрутить до соусов
def test_move_inside_constructor_scroll_sauce(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.MAKE_BURGER)))
    sauce = driver.find_element(*TestLocators.SAUCE_BUTTON)
    driver.execute_script("arguments[0].scrollIntoView();", sauce)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.SPICYX_SAUCE)))
    assert driver.find_element(*TestLocators.SPICYX_SAUCE).text == 'Соус Spicy-X'


# тест 12 - прокрутить до начинки
def test_move_inside_constructor_scroll_filling(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.MAKE_BURGER)))
    filling = driver.find_element(*TestLocators.FILLING_BUTTON)
    driver.execute_script("arguments[0].scrollIntoView();", filling)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.FILLING_PROTOSTOMIA)))
    assert driver.find_element(*TestLocators.FILLING_PROTOSTOMIA).text == 'Мясо бессмертных моллюсков Protostomia'



# тест 13 - прокрутить до булки
def test_move_inside_constructor_scroll_buns(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.MAKE_BURGER)))
    buns = driver.find_element(*TestLocators.BREAD_BUTTON)
    driver.execute_script("arguments[0].scrollIntoView();", buns)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.FLOUR_BREAD_BUTTON)))
    assert driver.find_element(*TestLocators.FLOUR_BREAD_BUTTON).text == 'Флюоресцентная булка R2-D3'


# тест 14 - кликнуть на раздел Соусы в верхнем горизонтальном меню
def test_move_inside_constructor_click_sauce(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.MAKE_BURGER)))
    driver.find_element(*TestLocators.SAUCE_HORIZONTAL_MENU).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.SPICYX_SAUCE)))
    assert driver.find_element(*TestLocators.SPICYX_SAUCE).text == 'Соус Spicy-X'

# тест 15 -кликнуть на раздел Начинки в верхнем горизонтальном меню
def test_move_inside_constructor_click_filling(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.MAKE_BURGER)))
    driver.find_element(*TestLocators.FILLING_HORIZONTAL_MENU).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.FILLING_PROTOSTOMIA)))
    assert driver.find_element(*TestLocators.FILLING_PROTOSTOMIA).text == 'Мясо бессмертных моллюсков Protostomia'

# тест 16 - кликнуть на раздел Булки в верхнем горизонтальном меню
def test_move_inside_constructor_click_buns(driver):
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.MAKE_BURGER)))
    driver.find_element(*TestLocators.BREAD_HORIZONTAL_MENU).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((TestLocators.FLOUR_BREAD_BUTTON)))
    assert driver.find_element(*TestLocators.FLOUR_BREAD_BUTTON).text == 'Флюоресцентная булка R2-D3'

