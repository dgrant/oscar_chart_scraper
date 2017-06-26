from element import BasePageElement
from locators import EncounterPageLocators, SignInPageLocators, SearchPageLocators

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(locator))


class SignInPage(BasePage):
    username_element = BasePageElement(SignInPageLocators.USER_NAME_FIELD)
    password_element = BasePageElement(SignInPageLocators.PASSWORD_FIELD)
    second_password_element = BasePageElement(SignInPageLocators.SECOND_PASSWORD_FIELD)
    signin_button = BasePageElement(SignInPageLocators.SIGN_IN_BUTTON)

    def __init__(self, url, driver):
        super().__init__(driver)
        driver.get(url)

    def is_loaded(self):
        return self.username_element

    def fill(self, user, password, second_password):
        self.username_element = user
        self.password_element = password
        self.second_password_element = second_password
        self.signin_button.click()

class SearchPage(BasePage):
    search_type = BasePageElement(SearchPageLocators.SELECT_SEARCH_MODE)
    keyword = BasePageElement(SearchPageLocators.KEYWORD_INPUT)
    search_button = BasePageElement(SearchPageLocators.SUBMIT_BUTTON)
    encounter_button = BasePageElement(SearchPageLocators.ENCOUNTER_BUTTON)

    def __init__(self, url, driver):
        super().__init__(driver)
        driver.get(url + '/demographic/search.jsp')

    def search_by_phn_number(self, phn):
        Select(self.search_type).select_by_value('search_hin')
        self.keyword = phn
        self.search_button.click()
        self.encounter_button.click()


class EncounterPage(BasePage):
    print_all_button_element = BasePageElement(EncounterPageLocators.PRINT_ALL_RADIO_BUTTON)
    print_cpp_button_element = BasePageElement(EncounterPageLocators.PRINT_CPP_BUTTON)
    print_go_button_element = BasePageElement(EncounterPageLocators.PRINT_GO_BUTTON)
    print_labs_button_element = BasePageElement(EncounterPageLocators.PRINT_LABS_BUTTON)
    print_rx_button_element = BasePageElement(EncounterPageLocators.PRINT_RX_BUTTON)
    print_button_element = BasePageElement(EncounterPageLocators.PRINT_BUTTON)

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.print_button_element

    def print_all(self):
        self.print_button_element.click()
        self.print_all_button_element.click()
        self.print_cpp_button_element.click()
        self.print_rx_button_element.click()
        self.print_labs_button_element.click()
        self.print_go_button_element.click()