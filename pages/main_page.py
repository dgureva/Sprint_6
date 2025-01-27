import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Нажимаем на вопрос и получаем ответ')
    def get_faq_text(self, question_locator, answer_locator):
        self.wait_for_element(question_locator)
        self.scroll_to_element(question_locator)
        self.wait_for_element(question_locator)
        self.find_element_and_click(question_locator)
        self.wait_for_element(answer_locator)
        faq_text_element = self.find_element(answer_locator)
        return faq_text_element.text

    @allure.step('Нажимаем Заказать')
    def order_click(self, order_locator):
        self.find_element_and_click(MainPageLocators.COOKIE_BUTTON)
        self.wait_for_element(order_locator)
        self.scroll_to_element(order_locator)
        self.wait_for_element(order_locator)
        self.find_element_and_click(order_locator)

    @allure.step('Нажимаем кнопку Яндекс в хэдере')
    def click_yandex_button(self):
        self.find_element_and_click(MainPageLocators.YANDEX_BUTTON)

    @allure.step('Получаем текст на главной')
    def get_main_scooter_text(self):
        self.wait_for_element(MainPageLocators.TEXT_ABOUT_SCOOTER)
        scooter_text = self.find_element(MainPageLocators.TEXT_ABOUT_SCOOTER)
        return scooter_text.text


