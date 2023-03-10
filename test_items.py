import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestCatalogePage():
    def test_page_contains_button_to_add_a_product_to_the_basket(self, browser):
        browser.get(link)
        time.sleep(5)
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "The page is missing a button to add" \
                                                                                 " a product to the basket"