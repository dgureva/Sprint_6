import allure
from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage

class DzenPage(BasePage):

    @allure.step('Получаем текст кнопки Найти')
    def get_dzen_find_text(self):
        tab = self.get_tab_and_switch()
        self.wait_for_element(DzenPageLocators.NEWS_TEXT)
        news_text = self.find_element(DzenPageLocators.NEWS_TEXT)
        return news_text.text