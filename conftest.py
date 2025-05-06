#Conftest file to install and required browser, start automation and end automation using pytest fixtures

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#pytest fixture to start and stop automation, with default scope="function"
@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()