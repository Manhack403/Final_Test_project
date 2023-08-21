from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login = self.browser.find_element(By.XPATH, "//a[@id='login_link']")
        login.click()
        assert "login" in self.browser.current_url, "Browser don't open login form"

    def should_be_login_form(self):
        login = self.browser.find_element(By.XPATH, "//a[@id='login_link']")
        login.click()
        assert self.is_element_present(By.XPATH, "//form[@id='login_form']"), "There is no login form"


    def should_be_register_form(self):
        login = self.browser.find_element(By.XPATH, "//a[@id='login_link']")
        login.click()
        assert self.is_element_present(By.XPATH, '//form[@id="register_form"]'), "There is no registration form"

