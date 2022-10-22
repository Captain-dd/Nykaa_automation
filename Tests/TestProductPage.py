import pytest
import time
from utilities.loginPage_utilities import LoginPageUtilities
from utilities.searchPage_utilities import ProductPageUtilities
from selenium.webdriver.common.by import By
import locators.ProductPageLocators as Ppl

lpu = LoginPageUtilities()
ppu = ProductPageUtilities()


@pytest.mark.usefixtures('initiate_driver')
class TestProductPage:

    @pytest.mark.parametrize("product_name", [('Mens Kurta'), ('Mens Tshirt'), ('mens jins')])
    def test_buy_a_product(self, product_name):
        ppu.search_product(product_name)
        ppu.click_a_product()
        ppu.switch_to_product_window()
        ppu.select_size()
        ppu.click_add_to_bag_button()
        ppu.click_cart_button()
        ppu.click_proceed_to_buy()

        assert 1 == 5, "proceed to buy button not working"

    @pytest.mark.parametrize("product_name", [('Mens Kurta'), ('Mens Tshirt'), ('mens jins')])
    def test_wishlist_a_product(self, product_name):
        ppu.search_product(product_name)
        ppu.click_a_product()
        ppu.switch_to_product_window()
        ppu.select_size()
        ppu.click_add_to_bag_button()
        ppu.click_cart_button()
        ppu.click_add_to_wishlist_button()

        assert 1 == 5, "wish to list button not working"

    def test_switch_to_frame(self):

        back_to_shop_button = (By.XPATH, "//button[contains(text(), 'Back to shopping')]")

        ppu.click_element(Ppl.cart_button)
        ppu.switch_to_frame()
        time.sleep(5)
        ppu.click_element(back_to_shop_button)
        # ppu.click_element()
        time.sleep(10)
