import pytest
from POMFiles.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginFlow:
    def test_authenticated_flow(self):
        login_page = LoginPage(self.driver)
        login_page.load_login_page()
        login_page.login_to_application()