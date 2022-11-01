from selenium.webdriver.common.by import By

medium_size_button = (By.XPATH, '//div[@id="app"]//button[contains(text(), "L")]')
add_to_bag = (By.CSS_SELECTOR, '#pdp-bottom-cta-container')
cart_button = (By.XPATH, '//div[@id="app"]//div[contains(text(), "Cart")]')
frame_locator = (By.XPATH, '//iframe[@title = "Nykaa Fashion Cart"]')
product_to_buy_button = (By.CSS_SELECTOR, 'button[data-at="continue-to-checkout"]')
add_to_wishlist = (By.CSS_SELECTOR, 'button[data-at="move-to-wishlist"]')
got_it_button_iframe = (By.XPATH, '//div[@id="portal-root"]//button[contains(text(),"Got it")]')
wishlist = (By.XPATH, '//div[@id="app"]//div[text()="Wishlist"]')

back_button_of_iframe = (By.XPATH, '//div[@id="app"]//a[@data-at="cart-backbtn"]')