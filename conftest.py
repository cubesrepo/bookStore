import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest

import test_data


@pytest.fixture(scope="session")
def driver(request):
    # retrieve the value from the command line
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        if headless:
            opt = ChromeOptions()
            opt.add_argument("--headless")
            opt.add_argument("--window-size=1920, 1080")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=opt)
        else:
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        if headless:
            opt = EdgeOptions()
            opt.add_argument("--headless")
            opt.add_argument("--window-size=1920, 1080")
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=opt)
        else:
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
    elif browser == "firefox":
        if headless:
            opt = FirefoxOptions()
            opt.add_argument("--headless")
            opt.add_argument("--window-size=1920, 1080")
            service = GeckoService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=opt)
        else:
            service = GeckoService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser {browser}")
    driver.maximize_window()
    driver.get(test_data.BASE_URL)
    yield driver
    time.sleep(3)
    driver.quit()

#pytest addoption allows you create custom command line
# with below code you can specify which browser to run EX. pytest --browser=edge
# also with the --headless you can run your test with headless using pytest --headless
# if we combine that example when we want to run edge in headless with html report pytest --html=report.html --browser=edge --headless
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify browser")
    parser.addoption("--headless", action="store_true", default=False, help="headless mode")
