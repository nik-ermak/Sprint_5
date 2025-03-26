from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver, authentication

class TestConstructorNav:
    # Навигация из личного кабинета в конструктор
    def test_navigate_constructor_header_success(self, driver, authentication):
        driver.find_element(*TestLocators.link_personal_account).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.profile_link))

        driver.find_element(*TestLocators.link_constructor).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))

        assert driver.find_element(*TestLocators.button_checkout_order).is_displayed()

    # Навигация из личного кабинета в конструктор через логотип
    def test_navigate_constructor_logo_success(self, driver, authentication):
        driver.find_element(*TestLocators.link_personal_account).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.profile_link))

        driver.find_element(*TestLocators.header_logo).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))

        assert driver.find_element(*TestLocators.button_checkout_order).is_displayed()