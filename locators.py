from selenium.webdriver.common.by import By

class TestLocators:
# Локаторы на странице Регистрации аккаунта
# локатор для поля Имя
    name_field = By.XPATH, ".//label[text()='Имя']/following-sibling::input"
# локатор для поля Email
    email_field = By.XPATH, ".//label[text()='Email']/following-sibling::input"
# локатор для поля Пароль
    password_field = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"
# локатор для кнопки регистрации
    registration_button = By.XPATH, ".//button[text()='Зарегистрироваться']"
# локатор линка Войти на форме регистрации
    login_link_registration_form = By.XPATH, ".//a[text()='Войти']"
# локатор при некорректном пароле
    invalid_password_error = By.XPATH, ".//p[text()='Некорректный пароль']"

# Локаторы на Главной странице
# локатор кнопки Войти в аккаунт
    login_button_main_page = By.XPATH, ".//button[text()='Войти в аккаунт']"
# локатор перехода в Личный кабинет
    link_personal_account = By.XPATH, ".//p[text()='Личный Кабинет']"
# локатор кнопки Оформить заказ
    button_checkout_order = By.XPATH, ".//button[text()='Оформить заказ']"
# локатор кнопки Конструктор
    link_constructor = By.XPATH, ".//p[text()='Конструктор']"
# раздел Булки
    section_buns = By.XPATH, ".//span[text()='Булки']"
# раздел Соусы
    section_sauces = By.XPATH, ".//span[text()='Соусы']"
# раздел Начинки
    section_toppings = By.XPATH, ".//span[text()='Начинки']"
# Селектор, который помечает раздел как активный
    active_section = By.XPATH,".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"

# Локаторы личного кабинета
# локатор кнопки Выход
    logout_button = By.XPATH, ".//button[text()='Выход']"
# Локатор линка Профиль
    profile_link = By.XPATH, ".//a[text()='Профиль']"
# локатор лого
    header_logo = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"

# Локаторы формы Восстановления пароля
# локатор линка Войти
    login_link_recovery_form = By.XPATH, ".//a[@href='/login']"
# локатор кнопки Восстановления пароля
    button_password_recovery = By.XPATH, ".//a[text()='Восстановить пароль']"

# Локаторы формы Войти/аутентификация
# локатор поля email
    aut_email_field = By.XPATH, ".//label[text()='Email']/following-sibling::input"
# локатор поля пароль
    aut_password_field = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"
# локатор кнопки вход
    aut_login_button = (By.XPATH, '//button[text()="Войти"]')
# локатор линка регистрации
    aut_registration_link = By.XPATH, ".//a[text()='Зарегистрироваться']"
# локатор линка восстановления пароля
    aut_recovery_password = By.XPATH, ".//a[text()='Восстановить пароль']"