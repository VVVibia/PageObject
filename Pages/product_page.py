from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()


    # название совпадает
    def get_product_in_basket_name(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        return name_in_basket.text

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def product_should_be_in_basket(self, name1, name2):
        assert name1 == name2, "The product name in the cart doesn't match the selected one"


    # цена совпадает
    def get_product_in_basket_price(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        return price_in_basket.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", product_price)
        return product_price.text

    def price_should_be_in_basket(self, price1, price2):
        assert price1 == price2, "Basket price doesn't match product price"