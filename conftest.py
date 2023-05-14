import pytest
import undetected_chromedriver as uc

from pages.actions_page import ActionsPage


@pytest.fixture(scope='session')
def browser():
    driver = uc.Chrome()
    page = ActionsPage(driver, 'https://ya.ru')
    yield page
    driver.quit()
