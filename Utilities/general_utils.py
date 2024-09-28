from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class GeneralUtils:
    @staticmethod
    def get_webdriver(browser_name: str):
        if browser_name.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Run in headless mode
            chrome_options.add_argument("--no-sandbox")  # Overcome limited resource problems
            chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
            chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
            driver = webdriver.Chrome(service=Service(), options=chrome_options)
        elif browser_name.lower() == "firefox":
            driver = webdriver.Firefox(service=FirefoxService())
        elif browser_name.lower() == "edge":
            driver = webdriver.Edge(service=EdgeService())
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        return driver