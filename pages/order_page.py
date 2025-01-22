import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем форму Для кого самокат и нажимаем Далее')
    def fill_for_who_form(
            self,
            name,
            sure_name,
            address_name,
            metro_name_locator,
            phone_number,

    ):
        self.wait_for_element(OrderPageLocators.NAME_INPUT)
        self.fill_form(OrderPageLocators.NAME_INPUT, name)
        self.fill_form(OrderPageLocators.SURE_NAME_INPUT, sure_name)
        self.fill_form(OrderPageLocators.ADDRESS_INPUT, address_name)
        self.find_element_and_click(OrderPageLocators.METRO_INPUT)
        self.find_element_and_click(metro_name_locator)
        self.fill_form(OrderPageLocators.PHONE_INPUT, phone_number)
        self.find_element_and_click(OrderPageLocators.BUTTON_NEXT)
        self.wait_for_element(OrderPageLocators.INPUT_DATE)

    @allure.step('Заполняем форму Про аренду и нажимаем Заказать')
    def fill_about_rent_form(
            self,
            date_selector_locator,
            rent_period_locator,
            color_locator,
            comment_text

    ):
        self.find_element_and_click(OrderPageLocators.INPUT_DATE)
        self.find_element_and_click(date_selector_locator)
        self.find_element_and_click(OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.find_element_and_click(rent_period_locator)
        self.find_element_and_click(color_locator)
        self.fill_form(OrderPageLocators.INPUT_COMMENT, comment_text)
        self.find_element_and_click(OrderPageLocators.BUTTON_ORDER)
        self.wait_for_element(OrderPageLocators.BUTTON_ACCEPTION_POP_UP_YES)
        self.find_element_and_click(OrderPageLocators.BUTTON_ACCEPTION_POP_UP_YES)
        self.wait_for_element(OrderPageLocators.BUTTON_SHOW_STATUS)
        self.find_element_and_click(OrderPageLocators.BUTTON_SHOW_STATUS)

    @allure.step('Нажимаем кнопку Самокат в хэдере')
    def click_scooter_button(self):
        self.find_element_and_click(OrderPageLocators.SCOOTER_BUTTON)

