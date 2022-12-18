from selenium.webdriver.common.by import By

class TestLocators:
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]" # кнопка "Войти в аккаунт"
    LOCATOR_ENTER_H2 = By.XPATH, "//h2[contains(text(),'Вход')]" # название страницы "Вход"
    REGISTRATION_TEXT = By.XPATH, "//a[contains(text(),'Зарегистрироваться')]" # текст "Зарегистрироваться"
    LOCATOR_REGISTRATION_H2 = By.XPATH, "//h2[contains(text(),'Регистрация')]" # название страницы "Регистрация"
    REG_FIELD_NAME = By.XPATH, "(.//input[@name='name'])[1]"  #локатор поля "Имя"
    REG_FIELD_EMAIL = By.XPATH, "(.//input[@name='name'])[2]" #локатор поля "Email"
    REG_FIELD_PASSWORD = By.XPATH, ".//input[@type='password']" #локатор поля "Пароль"
    REGISTRATION_BUTTON = By.XPATH, "//button[contains(text(),'Зарегистрироваться')]" #локатор кнопки "Зарегистрироваться"
    REGISTRATION_ERROR_MESSAGE = By.XPATH, "//p[contains(text(),'Некорректный пароль')]" #локатор сообщения об ошибке при регистрации
    AUTH_FIELD_EMAIL = By.XPATH, ".//input[@name='name']" # поле Email на странице "Вход" и при входе по кнопке "Войти" и "Личный кабинет"
    AUTH_FIELD_PASSWORD = By.XPATH, ".//input[@type='password']"  # поле Пароль на странице "Вход"
    AUTH_LOGIN_BUTTON = By.XPATH, "// button[contains(text(), 'Войти')]" # кнопка "Войти" на странице "Вход"
    PERSONAL_CABINET = By.XPATH, "//p[contains(text(),'Личный Кабинет')]" # кнопка "Личный кабинет"
    LOGIN_TEXT_REGISTRATION_FORM = By.XPATH, "//a[contains(text(),'Войти')]" # "Войти" на странице "Регистрация"
    RESTORE_PASSWORD_TEXT = By.XPATH,"//a[contains(text(),'Восстановить пароль')]"  # гипертекст "Восстановить пароль"
    LOGIN_TEXT_RESTORE_PASSWORD = By.XPATH, "//a[contains(text(),'Войти')]" # "Войти" на странице "Восстановление пароля"
    PROFILE_BUTTON = By.XPATH, "//a[contains(text(),'Профиль')]" # кнопка "Профиль" (в личном кабинете)
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(),'Конструктор')]" # кнопка "Конструктор"
    MAKE_BURGER = By.XPATH, "//h1[contains(text(),'Соберите бургер')]" # надпись "Соберите бургер" на главной странице
    LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']" # логотип Stellar Burgers
    EXIT_BUTTON = By.XPATH, "//button[contains(text(),'Выход')]" # кнопка "Выйти" (в личном кабинете)
    SAUCE_BUTTON = By.XPATH, "//h2[contains(text(),'Соусы')]" # кнопка "Соусы"
    SPICYX_SAUCE = By.XPATH, "//p[contains(text(),'Соус Spicy-X')]" # пример соуса 'Соус Spicy-X'
    FILLING_BUTTON = By.XPATH, "//h2[contains(text(),'Начинки')]" # кнопка "Начинки"
    FILLING_PROTOSTOMIA = By.XPATH, "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]" # пример начинки 'Мясо бессмертных моллюсков Protostomia'
    BREAD_BUTTON = By.XPATH, "//h2[contains(text(),'Булки')]" # кнопка "Булки"
    FLOUR_BREAD_BUTTON = By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]" # пример булки 'Флюоресцентная булка R2-D3'
    SAUCE_HORIZONTAL_MENU = By.XPATH, "//span[contains(text(),'Соусы')]" # раздел Соусы в верхнем горизонтальном меню
    FILLING_HORIZONTAL_MENU = By.XPATH, "//span[contains(text(),'Начинки')]" # раздел Начинки в верхнем горизонтальном меню
    BREAD_HORIZONTAL_MENU = By.XPATH, "//h2[contains(text(),'Булки')]" #раздел Булки в верхнем горизонтальном меню
