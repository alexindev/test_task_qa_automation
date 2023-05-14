from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_presence_located(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_visibility_located(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_presence_of_all_located(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
