from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_WAIT_TIME_SECONDS = 30


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        element = WebDriverWait(driver, DEFAULT_WAIT_TIME_SECONDS).until(
            EC.presence_of_element_located(self.locator))
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        return WebDriverWait(driver, DEFAULT_WAIT_TIME_SECONDS).until(
            EC.presence_of_element_located(self.locator))