from selenium.webdriver.common.by import By


class Locators:
    CAPTCHA_BUTTON = (By.ID, 'js-button')
    SEARCH_AREA = (By.ID, 'text')
    SUGGEST = (By.CLASS_NAME, 'mini-suggest__overlay.mini-suggest__overlay_visible')
    SEARCH_RESULT = (By.ID, 'search-result')
    SEARCH_ITEMS = (By.CSS_SELECTOR, '.serp-item.serp-item_card')
    URL_TAG = (By.TAG_NAME, 'a')
    MENU_SERVICES = (By.CSS_SELECTOR, '[title="Все сервисы"]')
    MENU_IMAGES = (By.CSS_SELECTOR, '[aria-label="Картинки"]')
    IMAGE_CATEGORIES = (By.CSS_SELECTOR, '[data-grid-name="im"]')
    IMAGE_SEARCH_AREA = (By.CSS_SELECTOR, '.input__control')
    IMAGES = (By.CLASS_NAME, 'serp-item')
    IMAGE_URL = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    IMAGE_LOCATE_BUTTONS = (By.CLASS_NAME, 'CircleButton')

