from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "The substring 'login' isn't present in the current browser URL"
        #assert self.url == self.browser.current_url, "The substring 'login' isn't present in the current browser URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def go_to_login_page(self):            #из main_page дубликат
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()