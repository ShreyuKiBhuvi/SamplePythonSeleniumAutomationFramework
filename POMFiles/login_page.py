from POMFiles.common_page_methods import CommonPageMethods
from POMFiles.element_locators import CommonLocators, LoginPageLocators, HomePageLocators

class LoginPage(CommonPageMethods):

    def load_login_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.wait_for_element(CommonLocators.LOGIN_LOGO['locator'], CommonLocators.LOGIN_LOGO['type'])

    def login_to_application(self):
        """Search for a product by entering its name into the search box."""
        self.enter_text(LoginPageLocators.USERNAME_INPUT["locator"], "standard_user", LoginPageLocators.USERNAME_INPUT["type"])
        self.enter_text(LoginPageLocators.PASSWORD_INPUT["locator"], "secret_sauce", LoginPageLocators.PASSWORD_INPUT["type"])
        self.click(LoginPageLocators.LOGIN_BUTTON["locator"], LoginPageLocators.LOGIN_BUTTON["type"])
        self.validate_page_title(HomePageLocators.expected_title)


