import time

from pages import homepage
from pages.homepage import HomePage
from pages.product import ProductPage, ProductPage


def test_open_s6(browser):
    homepage=HomePage(browser) # Создаем сессию ищ класса HomePage
    homepage.open()# Открываем страницу из сессии
    homepage.click_galaxy_s6()
    time.sleep(25)
    productpage = ProductPage(browser)
    productpage.check_title_is_('Samsung galaxy s6')

def test_two_monitors(browser):
    homepage=HomePage(browser) # Создаем сессию ищ класса HomePage
    homepage.open()# Открываем страницу из сессии
    homepage.click_monitor()
    time.sleep(25) # Просим ждать 16 секунд перед следующим шагом. Так делать нельзя
    homepage.check_products_count(2) # считает количество элементов массива

