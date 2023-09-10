from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductCart(BasePage):
    def click_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(*LoginPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        BasePage.solve_quiz_and_get_code(self)
        time.sleep(3)

        product_name = self.browser.find_element(*LoginPageLocators.PRODUCT_NAME).text
        product_name_match = self.browser.find_element(*LoginPageLocators.PRODUCT_NAME_MATCH).text
        print(product_name, product_name_match)
        assert product_name ==  product_name_match, "Product name doesn't match"

        price = self.browser.find_element(*LoginPageLocators.PRODUCT_PRICE).text
        price_match = self.browser.find_element(*LoginPageLocators.PRODUCT_PRICE_MATCH).text
        print(price, price_match)
        assert price == price_match, "Price in cart doesn't match"