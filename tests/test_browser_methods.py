
class TestMethods:

    image_1 = None

    def test_is_search_area(self, browser):
        browser.open()
        browser.is_captcha()
        assert browser.is_search_area() is True

    def test_is_suggest(self, browser):
        assert browser.is_suggest('Тензор') is True

    def test_is_search_result(self, browser):
        assert browser.is_search_result() is True

    def test_is_first_elem_in_search_result(self, browser):
        assert browser.get_first_element('https://tensor.ru/') is True

    def test_is_menu_list(self, browser):
        browser.open()
        browser.show_menu_list()
        assert browser.menu_list() is True

    def test_is_correct_images_url(self, browser):
        browser.open_menu()
        browser.images_url()
        browser.switch_tab()
        assert browser.get_image_page_url('https://yandex.ru/images/') is True

    def test_is_category_name_in_search_area(self, browser):
        browser.first_category()
        assert browser.get_category_mane_in_search() is True

    def test_opened_image(self, browser):
        browser.open_first_image()
        self.__class__.image_1 = browser.get_image_url()
        assert 'https://' in self.__class__.image_1

    def test_next_image(self, browser):
        browser.next_image()
        image_2 = browser.get_image_url()
        assert browser.compare_images(self.__class__.image_1, image_2) is False

    def test_back_to_previous_iamge(self, browser):
        browser.previous_image()
        image_3 = browser.get_image_url()
        assert browser.compare_images(self.__class__.image_1, image_3) is True
