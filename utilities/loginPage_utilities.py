import time

from utilities.common_utilities import CommonUtilities
import locators.LoginPageLocators as Lpl


class LoginPageUtilities(CommonUtilities):

    def fill_mobile_no(self, mobile_number):
        self.send_text(element_locator=Lpl.mobile_input_field, text=mobile_number)

    def verify_presence_of_order_button(self):
        # account button is reused here
        self.click_element(Lpl.account_button)

        return self.verify_presence_of_an_button(element_locator=Lpl.order_button)

    def perform_login(self, mobile_number):
        self.click_element(Lpl.account_button)
        self.click_element(Lpl.login_button)
        self.fill_mobile_no(mobile_number=mobile_number)
        self.click_element(Lpl.submit_button_to_get_otp)
        time.sleep(20)
        self.click_element(Lpl.verify_otp_button)
