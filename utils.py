from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:
    def __init__(self, driver = 1):
        self.driver = driver

    def find_element(self, by, value, locator: tuple[str, str] = None):
        if locator == None:
            return self.driver.find_element(by, value)
        return self.find_element(locator[0], locator[1]).find_element(by, value)

    def click_element(self, by, value, locator: tuple[str, str] = None):
        if locator == None:
            self.find_element(by, value).click()
            return
        
        self.find_element(locator[0], locator[1]).find_element(by, value).click()

    def fill_element(self, by, value, text):
        self.find_element(by, value).send_keys(text)

    def wait_until_element_located(self, by, value, timeout = 10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((by, value)))