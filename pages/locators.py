from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REG_FORM = (By.XPATH, '//form[@id="register_form"]')
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_NAME_MATCH = (By.XPATH, '//div[@class="alertinner "]/strong')
    ADD_TO_CART_BUTTON = (By.XPATH,"//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_PRICE_MATCH = (By.XPATH, '//div[@class="alertinner "]/p/strong')