import pytest
from Utilities.general_utils import GeneralUtils

@pytest.fixture(scope="class")
def setup(request):
    driver = GeneralUtils.get_webdriver("chrome")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
