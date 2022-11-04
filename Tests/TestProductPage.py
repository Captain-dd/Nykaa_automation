import pytest
import time
from utilities.loginPage_utilities import LoginPageUtilities
from utilities.searchPage_utilities import ProductPageUtilities
from selenium.webdriver.common.by import By
import locators.ProductPageLocators as Ppl
import locators.SearchPageLocators as Spl

from conftest import driver

lpu = LoginPageUtilities()
ppu = ProductPageUtilities()


@pytest.mark.usefixtures('initiate_driver')
class TestProductPage:

    # @pytest.mark.parametrize("product_name", [('Mens Kurta'), ('Mens Tshirt'), ('mens jins')])
    @pytest.mark.parametrize("product_name, mobile_num", [('Mens Tshirt', 9913300039)])
    def test_buy_a_product(self, product_name, mobile_num):

        lpu.perform_login(mobile_number=9913300039)
        time.sleep(2)
        ppu.search_product(product_name=product_name)
        ppu.press_enter_key()
        time.sleep(2)
        ppu.click_element(element_locator=Spl.name_of_product)
        time.sleep(2)
        ppu.switch_to_product_window()
        ppu.click_element(element_locator=Ppl.medium_size_button)
        ppu.click_element(element_locator=Ppl.add_to_bag)
        ppu.click_element(element_locator=Ppl.cart_button)
        ppu.switch_to_frame(frame_locator=Ppl.frame_locator)
        try:
            ppu.click_element(element_locator=Ppl.got_it_button_iframe)
        except:
            pass

        ppu.click_element(element_locator=Ppl.add_to_wishlist)
        time.sleep(2)
        ppu.click_element(element_locator=Ppl.back_button_of_iframe)
        time.sleep(2)
        ppu.click_element(element_locator=Ppl.wishlist)

        tabs = driver.window_handles
        driver.switch_to.window(tabs[2])

        # element_lst = driver.find_elements(by=By.XPATH, value='')
        #
        # data = []
        #
        # for i in element_lst:
        #
        #     data.append(i.text)

        assert driver.current_url


        assert 'Difference of Opinion' in data, "proceed to buy button not working"

    # @pytest.mark.parametrize("product_name", [('Mens Kurta'), ('Mens Tshirt'), ('mens jins')])
    # def test_wishlist_a_product(self, product_name):
    #     ppu.search_product(product_name)
    #     ppu.click_a_product()
    #     ppu.switch_to_product_window()
    #     ppu.select_size()
    #     ppu.click_add_to_bag_button()
    #     ppu.click_cart_button()
    #     ppu.click_add_to_wishlist_button()

        # assert 1 == 5, "wish to list button not working"

    def test_switch_to_frame(self):

        back_to_shop_button = (By.XPATH, "//button[contains(text(), 'Back to shopping')]")

        ppu.click_element(Ppl.cart_button)
        ppu.switch_to_frame()
        time.sleep(5)
        ppu.click_element(back_to_shop_button)
        # ppu.click_element()
        time.sleep(10)
