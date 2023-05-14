from pages.actions_page import ActionsPage


def test_methods(browser):
    driver = ActionsPage(browser, 'https://ya.ru')
    driver.open()
    driver.is_captcha()
    assert driver.is_suggest('Тензор') is True
    assert driver.is_search_result() is True
    assert driver.get_first_element('https://tensor.ru/') is True
    driver.open()
    driver.show_menu_list()
    assert driver.menu_list() is True
    driver.open_menu()
    driver.images_url()
    driver.switch_tab()
    assert driver.get_image_page_url('https://yandex.ru/images/') is True
    driver.first_category()
    assert driver.get_category_mane_in_search() is True
    driver.open_first_image()
    image_1 = driver.get_image_url()
    assert 'https://' in image_1
    driver.next_image()
    image_2 = driver.get_image_url()
    assert driver.compare_images(image_1, image_2) is False
    driver.previous_image()
    image_3 = driver.get_image_url()
    assert driver.compare_images(image_1, image_3) is True


