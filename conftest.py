import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password, valid_number, valid_login, valid_account
from selenium import webdriver


# фикстура для запуска тестов
@pytest.fixture
def driver():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.maximize_window()

    yield driver

    driver.quit()