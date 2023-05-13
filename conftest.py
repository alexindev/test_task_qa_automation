import pytest
from browser_methods import Browser

@pytest.fixture()
def browser():
    browser = Browser()
    yield browser
    browser.driver.quit()
