import undetected_chromedriver as uc

from loguru import logger
from typing import Union

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Browser:
    def __init__(self):
        self.driver = uc.Chrome()
        self.wait = WebDriverWait(self.driver, 15)
        self.url = 'https://ya.ru'

    def get_page(self) -> None:
        """ Открыть стартовую страницу ya.ru """
        self.driver.get(url=self.url)
        logger.info('Перешли на ya.ru')

    def is_captcha(self) -> None:
        """ Проверка наличия капчи """
        try:
            captcha = self.wait.until(EC.visibility_of_element_located((By.ID, 'js-button')))
            captcha.click()
            logger.info('Появилось окно капчи')
        except TimeoutException:
            logger.info('Без капчи')

    def is_suggest_area(self) -> bool:
        """ Проверка окна подсказок в поиске """
        try:
            search = self.wait.until(EC.presence_of_element_located((By.ID, 'text')))
            search.send_keys('Тензор')
            self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'mini-suggest__overlay.mini-suggest__overlay_visible')))
            logger.success('Появилась таблица с подсказками (suggest)')
            search.send_keys(Keys.ENTER)
            return True
        except TimeoutException:
            logger.error('Окно с подсказками не появилось')
            return False

    def is_search_result(self) -> bool:
        """ Проверка появления поисковой выдачи """
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.ID, 'search-result')))
            logger.success('Появилась страница результатов поиска')
            return True
        except TimeoutException:
            logger.info('Не вижу результаты поиска')
            return False

    def get_first_element(self, url: str) -> bool:
        """ Проверка корректности ссылки """
        all_result = self.driver.find_elements(By.CSS_SELECTOR, '.serp-item.serp-item_card')
        first_elem = all_result[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
        if first_elem == url:
            logger.success('Ссылка ведет на корректный сайт')
            return True
        logger.error('Некорректная ссылка')
        return False

    def show_menu_list(self) -> None:
        """ Вызов меню сервисов """
        try:
            search = self.wait.until(EC.presence_of_element_located((By.ID, 'text')))
            search.click()
            logger.success('Кликнул по строке поиска')
        except TimeoutException:
            logger.error('Не смог кликнуть по строке поиска')

    def menu_list(self) -> bool:
        """ Проверка видимости меню сервисов """
        try:
            self.driver.find_elements(
                By.CSS_SELECTOR, 'mini-suggest__overlay.mini-suggest__overlay_visible')
            logger.success('Меню сервисов на месте')
            return True
        except NoSuchElementException:
            logger.error(f'Меню серсивов не обнаружено')
            return False
        except Exception as e:
            logger.error(e)
            return False

    def open_menu(self) -> None:
        """ Переход окно выбора сервисов """
        try:
            services = self.driver.find_element(By.CSS_SELECTOR, '[title="Все сервисы"]')
            services.click()
            logger.success('Выбрал все категории')
        except NoSuchElementException:
            logger.error(f'Кнопка "Все сервисы" не обнаружена')
        except Exception as e:
            logger.error(e)

    def images_url(self) -> None:
        """ Выбор категории Картинки """
        try:
            images_page = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Картинки"]')
            images_page.click()
            logger.success('Выбрал категорию картинки')
        except NoSuchElementException:
            logger.error(f'Кнопка "Картинки" не обнаружена')
        except Exception as e:
            logger.error(e)

    def switch_tab(self) -> None:
        """ Переключение на новую вкладку """
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.success('Переключился на другую вкладку')
        except Exception as e:
            logger.error(e)

    def get_image_page_url(self, url: str) -> bool:
        """ Проверка корректности ссылки с категорией """
        try:
            image_url = self.driver.current_url
            logger.info(f'Текущая ссылка {image_url}')
            if image_url in url:
                logger.success('Корректный адрес Яндекс.Картинки')
                return True
            logger.error('Не корректная ссылка с картинками')
            return False
        except Exception as e:
            logger.error(e)
            return False

    def first_category(self) -> None:
        """ Выбор первой категории в картинках """
        try:
            category = self.driver.find_elements(By.CSS_SELECTOR, '[data-grid-name="im"]')
            category[0].click()
            logger.success('Выбрал первую категорию')
        except NoSuchElementException:
            logger.error('Не обнаружил элемент с первой категорией картинок')
        except Exception as e:
            logger.error(e)

    def get_category_mane_in_search(self) -> bool:
        """ Проверка наличия названия категории в строке поиска """
        try:
            search_area = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.input__control')))
            category_name = search_area.get_attribute('value')
            logger.info(category_name)
            if category_name:
                return True
            logger.error('Название категории отстуствует')
            return False
        except TimeoutException:
            logger.error('Не загрузилось полее строки ввода')
            return False
        except Exception as e:
            logger.error(e)
            return False

    def open_first_image(self) -> None:
        """ Открыть первую картинку """
        try:
            images = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'serp-item')))
            images[0].click()
            logger.info('Открыл первую картинку')
        except TimeoutException:
            logger.error('Не обнаружен элемент с первой картинкой')
        except Exception as e:
            logger.error(e)

    def get_image_url(self) -> Union[str, bool]:
        """ Проверка загрузки картинки (получить ссылку на картинку) """
        try:
            image_elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MMImage-Origin')))
            image_link = image_elem.get_attribute('src')
            logger.info(image_link)
            return image_link
        except TimeoutException:
            logger.error('Не загрузился элемент со ссылкой на картинку')
            return False
        except Exception as e:
            logger.error(e)
            return False

    def next_image(self) -> None:
        """ Переход на новую картинку """
        try:
            next_elems = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'CircleButton')))
            next_elems[-1].click()
            logger.success('Перешли к следующей картинке')
        except NoSuchElementException:
            logger.error('Не смогли перейти к следующей картинке')
        except Exception as e:
            logger.error(e)

    @staticmethod
    def compare_images(img1: str, img2: str) -> bool:
        """ Сравнение двух картинок """
        if img1 == img2:
            logger.info('Картинки совпадают')
            return True
        else:
            logger.info('Картинки разные')
            return False

    def previous_image(self) -> None:
        """ Переход к предыдущей картинке """
        try:
            next_elems = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'CircleButton')))
            next_elems[0].click()
            logger.success('Перешли к прошлой картинке')
        except NoSuchElementException:
            logger.error('Не смогли перейти к предыдущей картинке')
        except Exception as e:
            logger.error(e)
