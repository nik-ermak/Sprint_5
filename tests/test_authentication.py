from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver
from test_data import UserData


class TestAuthentication:
    # Главная страница. Вход по кнопке "Войти в аккаунт"
    def test_authentication_aut_login_button_success(self, driver):
        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))

        driver.find_element(*TestLocators.aut_email_field).send_keys(UserData.email)
        driver.find_element(*TestLocators.aut_password_field).send_keys(UserData.password)
        driver.find_element(*TestLocators.aut_login_button).click()

        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        assert driver.find_element(*TestLocators.button_checkout_order).is_displayed()

    # Главная страница. Вход через Личный кабинет
    def test_authentication_link_personal_account_success(self, driver):
        driver.find_element(*TestLocators.link_personal_account).click()
        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        driver.find_element(*TestLocators.aut_email_field).send_keys(UserData.email)
        driver.find_element(*TestLocators.aut_password_field).send_keys(UserData.password)
        driver.find_element(*TestLocators.aut_login_button).click()

        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        assert driver.find_element(*TestLocators.button_checkout_order).is_displayed()

    # Главная страница. Вход через форму регистрации
    def test_authentication_aut_registration_link_success(self,driver):
        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))

        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_link_registration_form))

        driver.find_element(*TestLocators.login_link_registration_form).click()
        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))

        driver.find_element(*TestLocators.aut_email_field).send_keys(UserData.email)
        driver.find_element(*TestLocators.aut_password_field).send_keys(UserData.password)
        driver.find_element(*TestLocators.aut_login_button).click()

        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        assert driver.find_element(*TestLocators.button_checkout_order).is_displayed()

    # Главная страница. Вход через восстановление пароля
    def test_authentication_aut_recovery_password_success(self, driver):
        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_recovery_password))

        driver.find_element(*TestLocators.aut_recovery_password).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.login_link_recovery_form))

        driver.find_element(*TestLocators.login_link_recovery_form).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        driver.find_element(*TestLocators.aut_email_field).send_keys(UserData.email)
        driver.find_element(*TestLocators.aut_password_field).send_keys(UserData.password)
        driver.find_element(*TestLocators.aut_login_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.button_checkout_order))
        assert driver.find_element(*TestLocators.button_checkout_order).is_displayed()

