from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config.control import explicit_wait_time
from conftest import driver
from pyautogui import press

import locators.HomePageLocators as hpl


class CommonUtilities:

    def click_element(self, element_locator):
        # wait for element to load
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(EC.presence_of_element_located(element_locator))
        # click element
        driver.find_element(by=element_locator[0], value=element_locator[1]).click()

    def send_text(self, element_locator, text):
        # wait for element to load
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(EC.presence_of_element_located(element_locator))
        # send text data to element
        driver.find_element(by=element_locator[0], value=element_locator[1]).send_keys(text)

    def get_text(self, element_locator):
        # wait for element to load
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(EC.presence_of_element_located(element_locator))
        # return text from element
        return driver.find_element(by=element_locator[0], value=element_locator[1]).text

    def get_current_url(self):
        return driver.current_url

    def verify_presence_of_an_button(self, element_locator):
        try:
            WebDriverWait(driver=driver, timeout=explicit_wait_time).until(
                EC.presence_of_element_located(element_locator))
            return True
        except:
            return False

    def get_multiple_element(self, element_locator):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(
            EC.presence_of_element_located(element_locator))

        return driver.find_elements(by=element_locator[0], value=element_locator[1])

    def press_enter_key(self):
        press('enter')

    def search_product(self, product_name):

        self.send_text(element_locator=hpl.search_bar, text=product_name)
        self.press_enter_key()

    def switch_to_frame(self, frame_locator):

        driver.switch_to.frame(driver.find_element(by=frame_locator[0], value=frame_locator[1]))

