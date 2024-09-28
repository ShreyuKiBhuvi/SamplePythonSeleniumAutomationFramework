from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from POMFiles.common_page_methods import CommonPageMethods
from POMFiles.element_locators import ShoppingCartLocators
from selenium.webdriver.support import expected_conditions as EC

"""This files serves as a repository for all methods related to cart and checkout page"""

class ShoppingCart(CommonPageMethods):

    def verify_item_added_to_cart(self, element_name):
        """This methods verifies whether an item has been added to the card"""
        try:
            locator = (ShoppingCartLocators.ITEMS_IN_CART["type"], ShoppingCartLocators.ITEMS_IN_CART["locator"])

            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
            for item in elements:
                if item.text == element_name:
                    print(f"Item {element_name} is present in the cart")
                return
        except NoSuchElementException:
            raise Exception(f"No elements found using locator: {ShoppingCartLocators.ITEMS_IN_CART["locator"]} and type: {ShoppingCartLocators.ITEMS_IN_CART["type"]}")

    def click_checkout(self):
        """This method clicks on the checkout button"""
        checkout_button = self.wait_for_element(ShoppingCartLocators.CHECKOUT_BUTTON["locator"], ShoppingCartLocators.CHECKOUT_BUTTON["type"])
        checkout_button.click()
        self.validate_page_title("Checkout: Your Information")

    def fill_checkout_information(self, first_name, last_name, zip):
        """This method fills the checkout information"""
        self.enter_text(ShoppingCartLocators.CHECKOUT_FIRST_NAME["locator"], first_name,
                        ShoppingCartLocators.CHECKOUT_FIRST_NAME["type"])
        self.enter_text(ShoppingCartLocators.CHECKOUT_LAST_NAME["locator"], last_name,
                        ShoppingCartLocators.CHECKOUT_LAST_NAME["type"])
        self.enter_text(ShoppingCartLocators.CHECKOUT_ZIP_CODE["locator"], zip,
                        ShoppingCartLocators.CHECKOUT_ZIP_CODE["type"])

    def click_continue(self):
        """This method clicks on the Continue button"""
        continue_button = self.wait_for_element(ShoppingCartLocators.CHECKOUT_CONTINUE["locator"],
                                                ShoppingCartLocators.CHECKOUT_CONTINUE["type"])
        continue_button.click()
        self.validate_page_title("Checkout: Overview")


    def click_finish(self):
        """This method clicks on the Finish button"""
        finish_button = self.wait_for_element(ShoppingCartLocators.CHECKOUT_FINISH["locator"],
                                                ShoppingCartLocators.CHECKOUT_FINISH["type"])
        finish_button.click()
        self.validate_page_title("Checkout: Complete!")



