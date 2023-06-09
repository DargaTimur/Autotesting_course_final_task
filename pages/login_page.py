from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.browser.current_url, "Login URL link is not presented"

    def should_be_login_form(self):
        # проверка формы входа на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "LOGIN FORM is not presented"

    def should_be_register_form(self):
        # проверка формы регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "REGISTER FORM link is not presented"
