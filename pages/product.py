from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,browser):
        self.browser = browser

    def check_title_is_(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, 'h2')  # Нашли элемент по тэгу html
        assert page_title.text == title  # Проверка что текст правильный