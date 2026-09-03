import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Предуслови и постусловия автотеста
@pytest.fixture() # Показывает, что функция - предусловие
def browser():
    options = Options()
    options.add_argument('--headless') # Визуально не отображает браузер
    browser = webdriver.Chrome(options=options) # Открыли браузер хром
    browser.maximize_window() # Развернули окно
    browser.implicitly_wait(25) # Ждет 3 секунды после ошибки для новой попытки
    yield browser # - Место для запуска теста. То что после него - постусловие
    browser.close() # Постусловие, чтобы браузер закрылся

# Конгец Предуслови и постусловия автотеста