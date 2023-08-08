#import time
#from selenium import webdriver
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
#from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):          # присутствует кнопка "логин"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):           # можно кликнуть по кнопке "логин"
    link = "http://selenium1py.pythonanywhere.com/"
    #link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр
                                                        # драйвера и url адрес
    page.open()                                         # открываем страницу
    page.go_to_login_page()                             # выполняем метод страницы — переходим на страницу логина


def test_guest_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


