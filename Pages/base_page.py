from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):    #метод is_element_present, в котором будем перехватывать
        try:                                     # исключение. В него будем передавать два аргумента:
            self.browser.find_element(how, what)  # как искать (css, id, xpath и тд) и что искать
        except (NoSuchElementException):            # (строку-селектор).
            return False
        return True





