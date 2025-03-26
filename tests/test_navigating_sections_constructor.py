from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver, authentication


class TestNavigatingSectionsLogin:
    # Переход от раздела Булки в раздел Соусы. Авторизация есть
    def test_navigate_buns_to_sauces_login_success(self, driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        driver.find_element(*TestLocators.section_sauces).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'

    # Переход от раздела Булки в раздел Начинки. Авторизация есть
    def test_navigate_buns_to_toppings_login_success(self, driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        driver.find_element(*TestLocators.section_toppings).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'

    # Переход от раздела Соусы к разделу Булки. Авторизация есть
    def test_navigate_sauces_to_buns_login_success(self, driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        driver.find_element(*TestLocators.section_sauces).click()
        driver.find_element(*TestLocators.section_buns).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Булки'

    # Переход от раздела Соусы к разделу Начинки. Авторизация есть
    def test_navigate_sauces_to_toppings_login_success(self, driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        driver.find_element(*TestLocators.section_sauces).click()
        driver.find_element(*TestLocators.section_toppings).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'

    # Переход от раздела Начинки к разделу Булки. Авторизация есть
    def test_navigate_toppings_to_buns_login_success(self, driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        driver.find_element(*TestLocators.section_toppings).click()
        driver.find_element(*TestLocators.section_buns).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Булки'

    # Переход от раздела Начинки к разделу Соусы. Авторизация есть
    def test_navigate_toppings_to_sauces_login_success(self, driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        driver.find_element(*TestLocators.section_toppings).click()
        driver.find_element(*TestLocators.section_sauces).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'


class TestNavigatingSectionsNoLogin:
    # Переход от раздела Булки в раздел Соусы. Авторизации нет
    def test_navigate_buns_to_sauces_no_login_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_button_main_page))
        driver.find_element(*TestLocators.section_sauces).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'

    # Переход от раздела Булки в раздел Начинки. Авторизации нет
    def test_navigate_buns_to_toppings_no_login_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_button_main_page))
        driver.find_element(*TestLocators.section_toppings).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'

    # Переход от раздела Соусы к разделу Булки. Авторизации нет
    def test_navigate_sauces_to_buns_no_login_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_button_main_page))
        driver.find_element(*TestLocators.section_sauces).click()
        driver.find_element(*TestLocators.section_buns).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Булки'

    # Переход от раздела Соусы к разделу Начинки. Авторизации нет
    def test_navigate_sauces_to_toppings_no_login_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_button_main_page))
        driver.find_element(*TestLocators.section_sauces).click()
        driver.find_element(*TestLocators.section_toppings).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'

    # Переход от раздела Начинки к разделу Булки. Авторизации нет
    def test_navigate_toppings_to_buns_no_login_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_button_main_page))
        driver.find_element(*TestLocators.section_toppings).click()
        driver.find_element(*TestLocators.section_buns).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Булки'

    # Переход от раздела Начинки к разделу Соусы. Авторизации нет
    def test_navigate_toppings_to_sauces_no_login_success(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_button_main_page))
        driver.find_element(*TestLocators.section_toppings).click()
        driver.find_element(*TestLocators.section_sauces).click()

        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'