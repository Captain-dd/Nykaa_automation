import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import config.data as cd
driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.fixture()
def initiate_driver():

    driver.get('https://www.nykaafashion.com/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    driver.quit()

# comment added by palak

