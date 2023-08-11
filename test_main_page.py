from .Pages.main_page import MainPage


def test_guest_should_see_login_link(browser):          # присутствует кнопка "логин"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


# После того, как проинициализирован новый объект Page (ф-я go_to_login_page)
# в тесте нам не нужно думать про инициализацию страницы,
# она уже создана. Сохранив возвращаемое значение в переменную,
# мы можем использовать методы новой страницы в тесте:
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()





