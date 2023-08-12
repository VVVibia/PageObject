from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()


    def product_should_be_in_basket(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == name_in_basket.text, "The product name in the cart doesn't match the selected one"


    def price_should_be_in_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", product_price)
        assert product_price.text == price_in_basket.text, "Basket price doesn't match product price"