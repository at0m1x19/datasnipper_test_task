import os

import pytest
from playwright.sync_api import sync_playwright

from src.swapi_client import SwapiClient


@pytest.fixture(scope="session")
def swapi_client():
    """
    Returns an instance of SwapiClient.
    """
    return SwapiClient()


@pytest.fixture(scope="session")
def base_host():
    """
    Returns the base host, e.g. https://www.datasnipper.com
    Could be read from an env variable or config file.
    """
    return os.environ.get("DATASNIPPER_HOST", "https://www.datasnipper.com")


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
