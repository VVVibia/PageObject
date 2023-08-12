from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".breadcrumb>.active")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>p>strong")  #Сообщение со стоимостью корзины.
    NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")     #Сообщение о том, что товар добавлен в корзину
