from .Pages.product_page import ProductPage
import time
import pytest

# @pytest.mark.parametrize('link', ["okay_link",
#                                   pytest.param("bugged_link", marks=pytest.mark.xfail),
#                                   "okay_link"])
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
def test_guest_can_add_product_to_basket(browser):
    link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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



