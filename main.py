import undetected_chromedriver as uc

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from loguru import logger



class Browser:
    def __init__(self):
        self.driver = uc.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = 'https://ya.ru'

    def get_page(self):
        return self.driver.get(url=self.url)

    def is_captcha(self) -> None:
        try:
            captcha = self.wait.until(EC.visibility_of_element_located((By.ID, 'js-button')))
            captcha.click()
        except TimeoutException:
            logger.info('нет капчи')

    def search_area(self):
        search = self.wait.until(EC.presence_of_element_located((By.ID, 'text')))
        search.send_keys('Тензор')
        if self.is_suggest_area():
            search.send_keys(Keys.ENTER)

    def is_suggest_area(self):
        try:
            self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'mini-suggest__overlay.mini-suggest__overlay_visible')))
            logger.success('вижу')
            return True
        except TimeoutException:
            logger.info('не вижу поля')
            return False

    def is_search_result(self):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.ID, 'search-result')))
            logger.success('вижу результаты')
            return True
        except TimeoutException:
            logger.info('не вижу результаты')
            return False

    def get_first_element(self):
        all_result = self.driver.find_elements(By.CSS_SELECTOR, '.serp-item.serp-item_card')
        first_elem = all_result[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
        return first_elem

    def show_menu_list(self):
        try:
            search = self.wait.until(EC.presence_of_element_located((By.ID, 'text')))
            search.click()
            logger.success('кликнул')
        except TimeoutException:
            logger.error('не смог кликнуть')

    def menu_list(self):
        try:
            menu_list = self.driver.find_elements(By.CSS_SELECTOR, 'mini-suggest__overlay.mini-suggest__overlay_visible')
            logger.success('меню на месте')
            return menu_list
        except Exception as e:
            logger.error(f'нет меню лист {e}')

    def open_menu(self):
        try:
            services = self.driver.find_element(By.CSS_SELECTOR,'[title="Все сервисы"]')
            services.click()
            logger.success('Выбрал все категории')
        except Exception as e:
            logger.error(e)

    def images_url(self):
        try:
            images_page = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Картинки"]')
            images_page.click()
            logger.success('Выбрал категорию картинки')
        except Exception as e:
            logger.error(e)

    def get_image_page_url(self):
        try:
            image_url = self.driver.current_url
            logger.info(image_url)
            return image_url
        except Exception as e:
            logger.error(e)

    def switch_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.success('Переключился на другую вкладку')
        except Exception as e:
            logger.error(e)

    def first_category(self):
        try:
            category = self.driver.find_elements(By.CSS_SELECTOR, '[data-grid-name="im"]')
            category[0].click()
            logger.success('Выбрал категорию')
        except Exception as e:
            logger.error(e)

    def get_category_mane_in_search(self):
        try:
            search_area = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.input__control')))
            category_name = search_area.get_attribute('value')
            logger.info(category_name)
            return category_name
        except Exception as e:
            logger.error(e)

    def open_image(self):
        try:
            images = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'serp-item')))
            images[0].click()
        except Exception as e:
            logger.error(e)

    def is_opened_image(self):
        try:
            global image
            image_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MMImage-Origin')))
            image = image_link.get_attribute('src')
            logger.info(image)
            return image
        except Exception as e:
            logger.error(e)

    def next_image(self):
        try:
            next_elems = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'CircleButton')))
            next_elems[-1].click()
            logger.success('Перешли к новой картинке')
        except Exception as e:
            logger.error(e)

    def compare_images(self):
        try:
            global image
            image_elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MMImage-Origin')))
            new_image = image_elem.get_attribute('src')
            if image != new_image:
                logger.success('Разные картинки')
            else:
                logger.error('Картинки одинаковые')
        except Exception as e:
            logger.error(e)

    def previous_image(self):
        try:
            next_elems = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'CircleButton')))
            next_elems[0].click()
            logger.success('Перешли к прошлой картинке')
        except Exception as e:
            logger.error(e)

    def new_compare_images(self):
        try:
            global image
            image_elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MMImage-Origin')))
            new_image = image_elem.get_attribute('src')
            if image == new_image:
                logger.success('Верная картинка')
            else:
                logger.error('Картинки поменялась')
        except Exception as e:
            logger.error(e)

    def close_driver(self):
        self.driver.quit()
        logger.info('Браузер закрыт')


image = None
driver = Browser()


try:
    driver.get_page()
    driver.is_captcha()
    driver.search_area()
    driver.is_search_result()
    driver.get_first_element()
    driver.get_page()
    driver.show_menu_list()
    driver.menu_list()
    driver.open_menu()
    driver.images_url()
    driver.switch_tab()
    driver.first_category()
    driver.get_category_mane_in_search()
    driver.open_image()
    driver.is_opened_image()
    driver.next_image()
    driver.compare_images()
    driver.previous_image()
    driver.new_compare_images()

finally:
    driver.close_driver()