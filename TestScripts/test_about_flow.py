import pytest
from POMFiles.common_page_methods import CommonPageMethods
from POMFiles.login_page import LoginPage
from POMFiles.home_page import HomePage
from POMFiles.shopping_cart import ShoppingCart

@pytest.mark.usefixtures("setup")
class TestAboutFlow:
    def test_about_link_flow(self):
        loginpg = LoginPage(self.driver)
        loginpg.load_login_page()
        loginpg.login_to_application()
        homepg = HomePage(self.driver)
        homepg.click_hamburger_menu()
        homepg.click_hamburger_menu_about()
        common = CommonPageMethods(self.driver)
        common.click_browser_back_button()
        common.validate_page_title("Products")
        homepg.logout()



