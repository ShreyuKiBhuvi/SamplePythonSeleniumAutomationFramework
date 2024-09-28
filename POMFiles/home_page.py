from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from POMFiles.common_page_methods import CommonPageMethods
from POMFiles.element_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC
from POMFiles.element_locators import CommonLocators

"""This files serves as a repository for all methods related to home page"""

class HomePage(CommonPageMethods):

    def select_item_from_page(self, item_name, timeout=10):
        """This method is used to select item listed on home page catalog"""
        try:
           elements = WebDriverWait(self.driver, timeout).until(
           EC.presence_of_all_elements_located((self.get_element_locator_type(HomePageLocators.INVENTORY_NAME_LABEL["type"]), HomePageLocators.INVENTORY_NAME_LABEL["locator"]))
           )
           for element in elements:
            if element.text == item_name:
               element.click()
               print(f"Clicked on the element with text: '{item_name}'")
            return
        except NoSuchElementException:
            raise Exception(f"No elements found using locator: {HomePageLocators.INVENTORY_NAME_LABEL["locator"]} and type: {HomePageLocators.INVENTORY_NAME_LABEL["type"]}")

    def add_item_to_cart(self):
        """This method clicks the Add to cart button"""
        add_to_cart_button = self.wait_for_element(HomePageLocators.ADD_TO_CART_BUTTON["locator"], HomePageLocators.ADD_TO_CART_BUTTON["type"])
        add_to_cart_button.click()
        self.verify_element_exists(HomePageLocators.REMOVE_FROM_CART_BUTTON["locator"], HomePageLocators.REMOVE_FROM_CART_BUTTON["type"])

    def navigate_to_cart(self):
        """This method navigates the user to Cart page"""
        cartlink = self.wait_for_element(HomePageLocators.SHOPPING_CART_LINK["locator"], HomePageLocators.SHOPPING_CART_LINK["type"])
        cartlink.click()
        self.validate_page_title("Your Cart")

    def click_hamburger_menu(self):
        """This method clicks on the hamburger menu"""
        hamburg_button = self.wait_for_element(HomePageLocators.HAMBURGER_MENU_BUTTON["locator"],
                                         HomePageLocators.HAMBURGER_MENU_BUTTON["type"])
        hamburg_button.click()
        self.verify_element_exists(self.wait_for_element(HomePageLocators.HAMBURGER_MENU_CLOSE_BUTTON["locator"],
                                         HomePageLocators.HAMBURGER_MENU_CLOSE_BUTTON["type"]))

    def click_hamburger_menu_about(self):
        """This method clicks on the About link in the hamburger menu"""
        hamburg_about_button = self.wait_for_element(HomePageLocators.HAMBURGER_MENU_ABOUT_LINK["locator"],
                                               HomePageLocators.HAMBURGER_MENU_ABOUT_LINK["type"])
        hamburg_about_button.click()
        self.verify_element_exists(self.wait_for_element(HomePageLocators.ABOUT_PAGE_TITLE["locator"],
                                                         HomePageLocators.ABOUT_PAGE_TITLE["type"]))

    def logout(self):
        """This method clicks on the Logout link in hamburger menu"""
        self.click_hamburger_menu()
        logout_button = self.wait_for_element(HomePageLocators.LOGOUT_BUTTON["locator"],
                                                     HomePageLocators.LOGOUT_BUTTON["type"])
        logout_button.click()
        self.verify_element_exists(CommonLocators.LOGIN_LOGO["locator"], CommonLocators.LOGIN_LOGO["type"])







