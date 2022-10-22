from selenium.webdriver.common.by import By

medium_size_button = (By.XPATH, '//div[@id="app"]//button[contains(text(), "L")]')
add_to_bag = (By.CSS_SELECTOR, '#pdp-bottom-cta-container')
cart_button = (By.XPATH, '//div[@id="app"]//div[contains(text(), "Cart")]')
frame = (By.CSS_SELECTOR, '//iframe[@title = "Nykaa Fashion Cart"]')
product_to_buy_button = (By.CSS_SELECTOR, 'button[data-at="continue-to-checkout"]')
wishlist_button = (By.CSS_SELECTOR, 'button[data-at="move-to-wishlist"]')
