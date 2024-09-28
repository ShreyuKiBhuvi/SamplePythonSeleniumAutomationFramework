from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utilities.general_utils import GeneralUtils

"""This files serves as a repository for all common methods"""

class CommonPageMethods:
    def __init__(self, driver):
        self.driver = driver


    def get_element_locator_type(self, locator_type):
        """Retrieve the locator type so that it can be used as parameter value"""
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            raise ValueError(f"Locator type {locator_type} not supported")

    def wait_for_element(self, locator, locator_type="xpath", timeout=10):
        """Wait until the element is present on the page."""
        locator_type = self.get_element_locator_type(locator_type)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator))
        )

    def verify_element_exists(self, locator, locator_type="xpath", timeout=10):
        """Verify if an element exists on the page."""
        try:
            locator_type = self.get_element_locator_type(locator_type)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator))
            )
            return True
        except:
            return False

    def validate_page_title(self, expected_title, timeout=10):
        """Validate if the Page title of any page is accurate"""
        try:
            title_element = self.wait_for_element('//*[@data-test="title"]', locator_type='xpath', timeout=timeout)
            actual_title = title_element.text.strip()  # Get the text and remove any leading/trailing whitespace

            assert actual_title == expected_title, f"Expected title: '{expected_title}', but got: '{actual_title}'"
        except AssertionError as e:
            print(f"Title validation failed: {e}")
            raise
        except Exception as e:
            print(f"An error occurred while validating the title: {e}")
            raise

    def click(self, locator, locator_type="xpath"):
        """Click on an element found by the given locator."""
        element = self.wait_for_element(locator, locator_type)
        element.click()

    def enter_text(self, locator, text, locator_type="xpath"):
        """Send text to an input field."""
        element = self.wait_for_element(locator, locator_type)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown(self, locator, select_by="visible_text", value=None, locator_type="xpath", timeout=10):
        """Select an element from dropdown"""
        try:
            # Wait for the dropdown to be present on the page
            dropdown_element = self.wait_for_element(locator, locator_type, timeout)

            # Initialize the Select class on the found dropdown element
            select = Select(dropdown_element)

            # Select based on the provided strategy
            if select_by == "visible_text":
                select.select_by_visible_text(value)
            elif select_by == "value":
                select.select_by_value(value)
            elif select_by == "index":
                select.select_by_index(int(value))
            else:
                raise ValueError(f"Unsupported selection method: {select_by}")
        except NoSuchElementException:
            raise Exception(f"Dropdown element not found using {locator_type}: {locator}")

    def click_browser_back_button(self):
        """Navigate back to the previous page in the browser's history."""
        try:
            self.driver.back()  # Simulates a click on the browser's back button
            print("Navigated back to the previous page.")
        except Exception as e:
            print(f"An error occurred while trying to go back: {e}")


