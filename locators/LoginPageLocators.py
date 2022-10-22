from selenium.webdriver.common.by import By

account_button = (By.XPATH, "//div[@id='app']//div[contains(text(), 'Account')]")
login_button = (By.XPATH, '//div[@id="app"]//button[@class = "sub-menu__login "]')
mobile_input_field = (By.CSS_SELECTOR, "input[name = 'mobileInput']")
submit_button_to_get_otp = (By.XPATH, '//div[@id="portal-root"]//button[@type="submit"]')
verify_otp_button = (By.XPATH, '//div[@id="portal-root"]//button[@type="submit" and contains(text(), "Verify OTP")]')

order_button = (By.CSS_SELECTOR, 'button[class="sub-menu__menu-item border-bottom border-top"]')
