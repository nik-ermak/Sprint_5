from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver, authentication


class TestLogout:
    # Выход из аккаунта через личный кабинет
    def test_logout_personal_account_success(self,driver, authentication):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))

        driver.find_element(*TestLocators.link_personal_account).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.logout_button))

        driver.find_element(*TestLocators.logout_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        assert driver.find_element(*TestLocators.aut_login_button).is_displayed()
