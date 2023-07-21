from selenium.webdriver.common.by import By
from urllib.parse import urlparse


# создаем конструктор
class BaseForm(object):
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        # неявное ожидание 5 с.
        self.driver.implicitly_wait(timeout)

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname


class AuthForm(BaseForm):
    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id' \
              '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type' \
              '=code&scope=openid&state=d0a2a0b6-eeae-40ba-821b-166a75fbe8c3&theme&auth_type'

        driver.get(url)

        self.username = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.auth_btn = driver.find_element(By.ID, "kc-login")
        self.forgot = driver.find_element(By.ID, "forgot_password")
        self.register = driver.find_element(By.ID, 'kc-register')
        self.placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
        self.agree = driver.find_element(By.ID, "rt-footer-agreement-link")
        self.vk_btn = driver.find_element(By.ID, "oidc_vk")
        self.ok_btn = driver.find_element(By.ID, 'oidc_ok')
        self.mail_ru_btn = driver.find_element(By.ID, 'oidc_mail')
        self.yandex_btn = driver.find_element(By.ID, 'oidc_ya')

    def btn_click(self):
        self.auth_btn.click()

# создаем метод для поиска одного элемента
    def find_element(self, by, location):
        return self.driver.find_element(by, location)

    def get_current_url(self):
        url = urlparse(self.driver.current_url)
        return url.path


class CodeForm(BaseForm):
    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=' \
              'openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%' \
              '252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22F32A8722-D786-4D10-94F1-0340566C7440%22%7D'

        driver.get(url)

        self.address = driver.find_element(By.ID, "address")
        self.code_btn = driver.find_element(By.ID, "otp_get_code")

    def get_click(self):
        self.code_btn.click()