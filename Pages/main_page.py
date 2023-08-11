from .base_page import BasePage
from .login_page import LoginPage   # Для перехода между страницами, возвращая нужный Page Object
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # Для перехода между страницами, возвращая нужный Page Object. В методе,
        # который осуществляет переход к странице логина, проинициализировать новый
        # объект Page и вернуть его:
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        # При создании объекта мы обязательно передаем ему тот же самый объект
        # драйвера для работы с браузером, а в качестве url передаем текущий адрес.

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #символ * указывает, что передали именно пару, и этот кортеж нужно распаковать
