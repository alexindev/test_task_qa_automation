
def test_search_result(browser):
    browser.get_page()
    browser.is_captcha()
    assert browser.is_suggest_area() is True
    assert browser.is_search_result() is True
    assert browser.get_first_element('https://tensor.ru/') is True
    browser.get_page()
    browser.show_menu_list()
    assert browser.menu_list() is True
    browser.open_menu()
    browser.images_url()
    browser.switch_tab()
    assert browser.get_image_page_url('https://yandex.ru/images/') is True
    browser.first_category()
    assert browser.get_category_mane_in_search() is True
    browser.open_first_image()
    image_1 = browser.get_image_url()
    assert 'https://' in image_1
    browser.next_image()
    image_2 = browser.get_image_url()
    assert browser.compare_images(image_1, image_2) is False
    browser.previous_image()
    image_3 = browser.get_image_url()
    assert browser.compare_images(image_1, image_3) is True
