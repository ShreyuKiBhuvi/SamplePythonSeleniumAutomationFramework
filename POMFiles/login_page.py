from POMFiles.common_page_methods import CommonPageMethods
from POMFiles.element_locators import CommonLocators, LoginPageLocators, HomePageLocators

"""This files serves as a repository for all methods related to login page"""

class LoginPage(CommonPageMethods):

    def load_login_page(self):
        """This method loads the application URL"""
        self.driver.get(CommonLocators.APP_URL)
        self.wait_for_element(CommonLocators.LOGIN_LOGO['locator'], CommonLocators.LOGIN_LOGO['type'])

    def login_to_application(self):
        """This method signs into the application"""
        self.enter_text(LoginPageLocators.USERNAME_INPUT["locator"], LoginPageLocators.USERNAME, LoginPageLocators.USERNAME_INPUT["type"])
        self.enter_text(LoginPageLocators.PASSWORD_INPUT["locator"], LoginPageLocators.PASSWORD, LoginPageLocators.PASSWORD_INPUT["type"])
        self.click(LoginPageLocators.LOGIN_BUTTON["locator"], LoginPageLocators.LOGIN_BUTTON["type"])
        self.validate_page_title(HomePageLocators.expected_title)


