import time
from utilities.common_utilities import CommonUtilities
import locators.SearchPageLocators as spl
import locators.ProductPageLocators as ppl
from conftest import driver

from selenium.webdriver.common.by import By
class ProductPageUtilities(CommonUtilities):

    # def verify_all_product_name_appeard_after_search(self, product_name, keyword):
    #
    #     self.search_product(product_name=product_name)
    #
    #     product_lst = driver.find_elements(by=spl.name_of_product[0], value=spl.name_of_product[1])
    #     product_name_lst = []
    #     for i in product_lst:
    #         product_name_lst.append(i.text)
    #
    #     counter = 0
    #
    #     for i in product_name_lst:
    #
    #         if keyword in i:
    #             counter = counter + 1
    #
    #     percent_product_appeared_correct = (counter*100)/len(product_name_lst)
    #
    #     if percent_product_appeared_correct > 50:
    #         return True
    #
    #     else:
    #         return False

    # def click_add_to_bag_button(self):
    #     self.click_element(ppl.add_to_bag)
    #
    # def click_cart_button(self):
    #     self.click_element(ppl.cart_button)
    #
    # def click_proceed_to_buy(self):
    #     self.click_element(ppl.product_to_buy_button)
    #
    # def click_add_to_wishlist_button(self):
    #     self.click_element(ppl.add_to_wishlist)
    #
    # def click_a_product(self):
    #     self.click_element(spl.name_of_product)

    def switch_to_product_window(self):
        tabs = driver.window_handles

        driver.switch_to.window(tabs[1])

    # def select_size(self):
    #     self.click_element(ppl.medium_size_button)

