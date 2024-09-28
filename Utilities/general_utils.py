from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class GeneralUtils:
    @staticmethod
    def get_webdriver(browser_name: str):
        if browser_name.lower() == "chrome":
            driver = webdriver.Chrome(service=ChromeService())
        elif browser_name.lower() == "firefox":
            driver = webdriver.Firefox(service=FirefoxService())
        elif browser_name.lower() == "edge":
            driver = webdriver.Edge(service=EdgeService())
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        return driver