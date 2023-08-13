from .Pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)

    name1 = page.get_product_in_basket_name()
    name2 = page.get_product_name()
    # assert - "The product name in the cart doesn't match the selected one"
    page.product_should_be_in_basket(name1, name2)

    price1 = page.get_product_in_basket_price()
    price2 = page.get_product_price()
    # assert - "Basket price doesn't match product price"
    page.price_should_be_in_basket(price1, price2)



