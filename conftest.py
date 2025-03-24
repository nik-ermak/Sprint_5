import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_data import UserData
from locators import TestLocators
from test_url import main_site

# фикстура для веб-драйвера
@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


# фикстура аутентификации
@pytest.fixture
def authentication(driver):
    driver.find_element(*TestLocators.login_button_main_page).click()
    driver.find_element(*TestLocators.aut_email_field).send_keys(UserData.EMAIL)
    driver.find_element(*TestLocators.aut_password_field).send_keys(UserData.PASSWORD)
    driver.find_element(*TestLocators.aut_login_button).click()