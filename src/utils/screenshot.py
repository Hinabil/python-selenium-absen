from selenium.webdriver.chrome.webdriver import WebDriver
import time

def take_screenshot(driver: WebDriver, filename: str):
    """Capture a screenshot of the current browser window."""
    try:
        driver.save_screenshot(filename)
        print(f"Screenshot saved as: {filename}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")