from typing import Union
from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from pages.base_page import Base
from locators.element_page_locators import Locators


class ActionsPage(Base):
    def is_captcha(self) -> None:
        """ Проверка наличия капчи """
        try:
            captcha = self.element_visibility_located(Locators.CAPTCHA_BUTTON, 5)
            captcha.click()
            logger.info('Появилось окно капчи')
        except TimeoutException:
            logger.info('Без капчи')

    def is_suggest(self, text: str) -> bool:
        """ Проверка окна подсказок в поиске """
        try:
            search = self.element_presence_located(Locators.SEARCH_AREA, 10)
            search.send_keys(text)
            self.element_presence_located(Locators.SUGGEST, 10)
            logger.success('Появилась таблица с подсказками (suggest)')
            search.send_keys(Keys.ENTER)
            return True
        except TimeoutException:
            logger.error('Окно с подсказками не появилось')
            return False

    def is_search_result(self) -> bool:
        """ Проверка появления поисковой выдачи """
        try:
            self.element_presence_located(Locators.SEARCH_RESULT, 10)
            logger.success('Появилась страница результатов поиска')
            return True
        except TimeoutException:
            logger.info('Не вижу результаты поиска')
            return False

    def get_first_element(self, url: str) -> bool:
        """ Проверка корректности ссылки """
        search_result = self.elements_presence_of_all_located(Locators.SEARCH_ITEMS, 5)
        first_elem = search_result[0].find_element(*Locators.URL_TAG).get_attribute('href')
        if first_elem == url:
            logger.success('Ссылка ведет на корректный сайт')
            return True
        logger.error('Некорректная ссылка')
        return False

    def show_menu_list(self) -> None:
        """ Вызов меню сервисов """
        try:
            search = self.element_presence_located(Locators.SEARCH_AREA, 5)
            search.click()
            logger.success('Кликнул по строке поиска')
        except TimeoutException:
            logger.error('Не смог кликнуть по строке поиска')

    def menu_list(self) -> bool:
        """ Проверка видимости меню сервисов """
        try:
            self.element_presence_located(Locators.SUGGEST, 5)
            logger.success('Меню сервисов на месте')
            return True
        except TimeoutException:
            logger.error(f'Меню серсивов не обнаружено')
            return False
        except Exception as e:
            logger.error(e)
            return False

    def open_menu(self) -> None:
        """ Переход окно выбора сервисов """
        try:
            services = self.element_presence_located(Locators.MENU_SERVICES, 5)
            services.click()
            logger.success('Выбрал все категории')
        except TimeoutException:
            logger.error(f'Кнопка "Все сервисы" не обнаружена')
        except Exception as e:
            logger.error(e)

    def images_url(self) -> None:
        """ Выбор категории Картинки """
        try:
            images_page = self.element_presence_located(Locators.MENU_IMAGES, 5)
            images_page.click()
            logger.success('Выбрал категорию картинки')
        except TimeoutException:
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
            category = self.elements_presence_of_all_located(Locators.IMAGE_CATEGORIES, 10)
            category[0].click()
            logger.success('Выбрал первую категорию')
        except TimeoutException:
            logger.error('Не обнаружил элемент с первой категорией картинок')
        except Exception as e:
            logger.error(e)

    def get_category_mane_in_search(self) -> bool:
        """ Проверка наличия названия категории в строке поиска """
        try:
            search_area = self.element_presence_located(Locators.IMAGE_SEARCH_AREA, 10)
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
            images = self.elements_presence_of_all_located(Locators.IMAGES, 10)
            images[0].click()
            logger.info('Открыл первую картинку')
        except TimeoutException:
            logger.error('Не обнаружен элемент с первой картинкой')
        except Exception as e:
            logger.error(e)

    def get_image_url(self) -> Union[str, bool]:
        """ Проверка загрузки картинки (получить ссылку на картинку) """
        try:
            image_elem = self.element_presence_located(Locators.IMAGE_URL, 10)
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
            next_elems = self.elements_presence_of_all_located(Locators.IMAGE_LOCATE_BUTTONS, 10)
            next_elems[-1].click()
            logger.success('Перешли к следующей картинке')
        except TimeoutException:
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
            next_elems = self.elements_presence_of_all_located(Locators.IMAGE_LOCATE_BUTTONS, 10)
            next_elems[0].click()
            logger.success('Перешли к прошлой картинке')
        except TimeoutException:
            logger.error('Не смогли перейти к предыдущей картинке')
        except Exception as e:
            logger.error(e)
