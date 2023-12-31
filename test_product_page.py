import pytest

from .pages.product_page import ProductCart
from .pages.login_page import LoginPage
from .pages.basket_page import BasePage
import time

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    links = f"{link}"
    page = ProductCart(browser, links)
    page.open()
    page.click_add_to_cart_button()

@pytest.mark.parametrize('link',['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    links = f"{link}"
    page = ProductCart(browser, links)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.parametrize('link',['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'])
def test_guest_cant_see_success_message(browser, link):
    links = f"{link}"
    page = ProductCart(browser,links)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.parametrize('link',['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    links = f"{link}"
    page = ProductCart(browser, links)
    page.open()
    page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductCart(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductCart(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductCart(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened_from_product_page()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductCart(browser, url)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
        page = ProductCart(browser, url)
        page.open()
        page.click_add_to_cart_button()