import time


def test_presence_of_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button, "Кнопки на добавление в корзину нет"
