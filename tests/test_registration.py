import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver
from test_data import UserData
from gen_date import create_random_email, create_random_password

class TestRegistration:
    # Регистрация с валидными данными
    def test_registration_valid_data_success(self, driver):
        random_email = create_random_email()
        random_password = create_random_password()

        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))
        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.registration_button))

        driver.find_element(*TestLocators.name_field).send_keys(UserData.USERNAME)
        driver.find_element(*TestLocators.email_field).send_keys(random_email)
        driver.find_element(*TestLocators.password_field).send_keys(random_password)
        driver.find_element(*TestLocators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        assert driver.find_element(*TestLocators.aut_login_button).is_displayed()

    # Попытка регистрации с пустым полем Имя
    def test_registration_empty_name_field_failed(self, driver):
        random_email = create_random_email()
        random_password = create_random_password()

        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))
        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.registration_button))

        current_url = driver.current_url

        driver.find_element(*TestLocators.name_field).send_keys('')
        driver.find_element(*TestLocators.email_field).send_keys(random_email)
        driver.find_element(*TestLocators.password_field).send_keys(random_password)
        driver.find_element(*TestLocators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        current_url_after_click = driver.current_url

        assert current_url_after_click == current_url

    # Попытка регистрации с пустым полем Email
    def test_registration_empty_email_field_failed(self, driver):
        random_password = create_random_password()

        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))
        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.registration_button))

        current_url = driver.current_url

        driver.find_element(*TestLocators.name_field).send_keys(UserData.USERNAME)
        driver.find_element(*TestLocators.email_field).send_keys('')
        driver.find_element(*TestLocators.password_field).send_keys(random_password)
        driver.find_element(*TestLocators.registration_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        current_url_after_click = driver.current_url

        assert current_url_after_click == current_url

    # Попытка регистрации с пустым полем пароль
    def test_registration_empty_password_field_failed(self, driver):
        random_email = create_random_email()

        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))
        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.registration_button))

        current_url = driver.current_url

        driver.find_element(*TestLocators.name_field).send_keys(UserData.USERNAME)
        driver.find_element(*TestLocators.email_field).send_keys(random_email)
        driver.find_element(*TestLocators.password_field).send_keys('')
        driver.find_element(*TestLocators.registration_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        current_url_after_click = driver.current_url

        assert current_url_after_click == current_url

    # Проверка получения ошибки "Некорректный пароль". Длина пароля меньше 6 символов
    @pytest.mark.parametrize('invalid_password', ['12345', '1234', '1'])
    def test_registration_invalid_password_error(self, driver, invalid_password):
        random_email = create_random_email()

        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))
        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.registration_button))

        driver.find_element(*TestLocators.name_field).send_keys(UserData.USERNAME)
        driver.find_element(*TestLocators.email_field).send_keys(random_email)
        driver.find_element(*TestLocators.password_field).send_keys(invalid_password)
        driver.find_element(*TestLocators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.invalid_password_error))

        assert driver.find_element(*TestLocators.invalid_password_error).is_displayed()

    # Проверка ввода длинного пароля
    @pytest.mark.parametrize('long_valid_password', ['1234567', '123456789', '9999999999999999'])
    def test_registration_valid_long_password(self, driver, long_valid_password):
        random_email = create_random_email()

        driver.find_element(*TestLocators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_registration_link))
        driver.find_element(*TestLocators.aut_registration_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.registration_button))

        driver.find_element(*TestLocators.name_field).send_keys(UserData.USERNAME)
        driver.find_element(*TestLocators.email_field).send_keys(random_email)
        driver.find_element(*TestLocators.password_field).send_keys(long_valid_password)
        driver.find_element(*TestLocators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.aut_login_button))

        assert driver.find_element(*TestLocators.aut_login_button).is_displayed()