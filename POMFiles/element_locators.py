"""This files serves as a central repository for all locators and other variables"""

class CommonLocators:
    APP_URL = "https://www.saucedemo.com/"
    LOGIN_LOGO = {"locator": ".//div[@class = 'login_logo' and text()='Swag Labs']",
                "type": "xpath"}
    APP_LOGO = {
        "locator": ".//div[@class = 'app_logo' and text()='Swag Labs']",
        "type": "xpath"}

class LoginPageLocators:
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    USERNAME_INPUT = {"locator": "user-name", "type": "id"}
    PASSWORD_INPUT = {"locator": "password", "type": "id"}
    LOGIN_BUTTON = {"locator": "login-button", "type": "id"}

class HomePageLocators:
    expected_title = "Products"
    HAMBURGER_MENU_BUTTON = {"locator": ".//button[contains(text(), 'Open Menu')]", "type": "xpath"}
    HAMBURGER_MENU_CLOSE_BUTTON = {"locator": ".//button[contains(text(), 'Close Menu')]", "type": "xpath"}
    HAMBURGER_MENU_ABOUT_LINK = {"locator": ".//nav/a[contains(text(), 'About')]", "type": "xpath"}
    SHOPPING_CART_LINK = {"locator": ".//a[contains(@data-test, 'shopping-cart-link')]", "type": "xpath"}
    ADD_TO_CART_BUTTON = {"locator": "add-to-cart", "type": "id"}
    REMOVE_FROM_CART_BUTTON = {"locator": ".//button[text() = 'Remove']", "type": "xpath"}
    PRODUCT_SORT_DROPDOWN = {"locator": ".//*[contains(@data-test, 'product-sort-container')]", "type": "xpath"}
    INVENTORY_NAME_LABEL = {"locator": ".//*[contains(@data-test, 'inventory-item-name')]", "type": "xpath"}
    ABOUT_PAGE_TITLE = {"locator": ".//title[contains(text(), 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing')]", "type": "xpath"}
    LOGOUT_BUTTON = {"locator": ".//a[contains(text(), 'Logout')]", "type": "xpath"}

class ShoppingCartLocators:
    expected_title = "Your Cart"
    ITEMS_IN_CART = {"locator": ".//div[contains(@class, 'cart_item_label')]/a/div", "type": "xpath"}
    CONTINUE_SHOPPING_BUTTON = {"locator": "continue-shopping", "type": "id"}
    CHECKOUT_BUTTON = {"locator": "checkout", "type": "id"}
    CHECKOUT_FIRST_NAME = {"locator": "first-name", "type": "id"}
    CHECKOUT_LAST_NAME = {"locator": "last-name", "type": "id"}
    CHECKOUT_ZIP_CODE = {"locator": "postal-code", "type": "id"}
    CHECKOUT_CONTINUE = {"locator": "continue", "type": "id"}
    CHECKOUT_CANCEL = {"locator": "cancel", "type": "id"}
    CHECKOUT_FINISH = {"locator": "finish", "type": "id"}