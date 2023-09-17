from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REG_FORM = (By.XPATH, '//form[@id="register_form"]')

class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_NAME_MATCH = (By.XPATH, '//div[@class="alertinner "]/strong')
    ADD_TO_CART_BUTTON = (By.XPATH,"//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_PRICE_MATCH = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_CART_FROM_MAIN_PAGE = (By.XPATH, '//span[@class="btn-group"]/a[@href="/ru/basket/"]')
    OPEN_CART_FROM_PRODUCT_PAGE = (By.XPATH, '//span[@class="btn-group"]/a[@class="btn btn-default"]')
    PRODUCT_PRESENCE_IN_CART = (By.XPATH, '//div[@class="basket-title hidden-xs"]')
    EMPTY_CART_TEXT = (By.XPATH, '//div[@id="content_inner"]/p')