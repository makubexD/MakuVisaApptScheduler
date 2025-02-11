from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import SHOW_GUI
from fake_useragent import UserAgent

_driver = None

def get_driver():
    global _driver
    if _driver is None:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        if SHOW_GUI == 'False':
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument("--window-size=1920, 1200")
            options.add_argument("enable-automation")
            options.add_argument("--disable-infobars")
            options.add_argument('--disable-dev-shm-usage')
            ua = UserAgent()
            user_agent = ua.random
            options.add_argument(f'user-agent={user_agent}')
        _driver = webdriver.Chrome(service=service, options=options)
    return _driver