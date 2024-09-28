
class CommonLocators:
    LOGIN_LOGO = {"locator": ".//div[@class = 'login_logo' and text()='Swag Labs']",
                "type": "xpath"}
    APP_LOGO = {
        "locator": ".//div[@class = 'app_logo' and text()='Swag Labs']",
        "type": "xpath"}

class LoginPageLocators:
    USERNAME_INPUT = {"locator": "user-name", "type": "id"}
    PASSWORD_INPUT = {"locator": "password", "type": "id"}
    LOGIN_BUTTON = {"locator": "login-button", "type": "id"}

class HomePageLocators:
    expected_title = "Products"
    HAMBURGER_MENU_BUTTON = {"locator": ".//button[contains(text(), 'Open Menu')]", "type": "xpath"}
    SHOPPING_CART_LINK = {"locator": ".//a[contains(@data-test, 'shopping-cart-link')]", "type": "xpath"}
    ADD_TO_CART_BUTTON = {"locator": "add-to-cart-sauce-labs-backpack", "type": "id"}
    PRODUCT_SORT_DROPDOWN = {"locator": "product-sort-container", "type": "data-test"}