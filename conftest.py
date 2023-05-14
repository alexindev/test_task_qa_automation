import pytest
import undetected_chromedriver as uc

@pytest.fixture()
def browser():
    driver = uc.Chrome()
    yield driver
    driver.quit()
