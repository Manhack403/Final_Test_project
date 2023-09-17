from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        BasePage.open_product_basket_from_main_page(self)
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_PRESENCE_IN_CART), \
            "Product shouldnt be in a cart"
        assert self.is_element_present(*BasePageLocators.EMPTY_CART_TEXT), \
            "Cart is not empty"


    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        BasePage.open_product_basket_from_product_page(self)
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_PRESENCE_IN_CART), \
            "Product shouldnt be in a cart"
        assert self.is_element_present(*BasePageLocators.EMPTY_CART_TEXT), \
            "Cart is not empty"

