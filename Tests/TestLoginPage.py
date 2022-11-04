import time

import pytest
import config.data as credential
from utilities.loginPage_utilities import LoginPageUtilities
import locators.LoginPageLocators as Lpu
lpu = LoginPageUtilities()


@pytest.mark.usefixtures('initiate_driver')
class TestLoginPage:
    @pytest.mark.validCredentail
    def test_login_page_with_valid_credential_version2(self):
        lpu.perform_login(credential.valid_mobile_num)

        assert lpu.verify_presence_of_order_button(), 'Logout button not found'

    @pytest.mark.invalidCredentail
    @pytest.mark.parametrize("mobile_num", [(123466), (8975642), (78945632)])
    def test_login_page_with_wrong_credential(self, mobile_num):
        lpu.click_element(Lpu.account_button)
        lpu.click_element(Lpu.login_button)
        lpu.fill_mobile_no(mobile_num)

        assert 1==1, "Mobile number is not correct"



