import pytest
from POMFiles.login_page import LoginPage
from POMFiles.home_page import HomePage
from POMFiles.shopping_cart import ShoppingCart

"""This test case tests the complete checkout flow after placing an item in the cart"""

@pytest.mark.usefixtures("setup")
class TestFinishCheckoutFlow:
    def test_checkout_flow(self):
        loginpg = LoginPage(self.driver)
        loginpg.load_login_page()
        loginpg.login_to_application()
        homepg = HomePage(self.driver)
        homepg.select_item_from_page("Sauce Labs Backpack")
        homepg.add_item_to_cart()
        homepg.navigate_to_cart()
        shpcart = ShoppingCart(self.driver)
        shpcart.verify_item_added_to_cart("Sauce Labs Backpack")
        shpcart.click_checkout()
        shpcart.fill_checkout_information("abc", "xyz", "123")
        shpcart.click_continue()
        shpcart.verify_item_added_to_cart("Sauce Labs Backpack")
        shpcart.click_finish()
        homepg.logout()
