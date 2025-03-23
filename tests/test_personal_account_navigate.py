from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from conftest import driver, authentication

class TestPersonalAccountNav:
    # Переход в личный кабинет
    def test_navigate_personal_account_success(self,driver,authentication):
        driver.find_element(*TestLocators.link_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.profile_link))

        assert driver.find_element(*TestLocators.profile_link).is_displayed()
