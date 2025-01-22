import allure
import pytest

from constants import OrderPageConstants, URLSConstants
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.dzen_page import DzenPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        "order_button, name, sure_name, address_name, metro_name_locator, phone_number, date_selector_locator, \n"
        "rent_period_locator, color_locator, comment_text",
        [
            (MainPageLocators.BUTTON_ORDER_IN_HEADER,
             OrderPageConstants.NAME[0],
             OrderPageConstants.SURE_NAME[0],
             OrderPageConstants.ADDRESS[0],
             OrderPageLocators.METRO_ROKOSOVSKI_SELECTOR,
             OrderPageConstants.PHONE[0],
             OrderPageLocators.SELECTOR_DATE_ONE,
             OrderPageLocators.SELECTOR_RENTAL_PERIOD_ONE_DAY,
             OrderPageLocators.SELECTOR_COLOR_BLACK,
             OrderPageConstants.COMMENT[0]),

            (MainPageLocators.BUTTON_ORDER_IN_CENTER,
             OrderPageConstants.NAME[1],
             OrderPageConstants.SURE_NAME[1],
             OrderPageConstants.ADDRESS[1],
             OrderPageLocators.METRO_CHERKIZOVSKAYA_SELECTOR,
             OrderPageConstants.PHONE[1],
             OrderPageLocators.SELECTOR_DATE_TWO,
             OrderPageLocators.SELECTOR_RENTAL_PERIOD_TWO_DAYS,
             OrderPageLocators.SELECTOR_COLOR_GREY,
             OrderPageConstants.COMMENT[1]),

        ],
        ids=(
                "Order_from_header_first_data_set",
                "Order_from_center_second_data_set",
        ),
    )
    @allure.title("Проверка Заказа самоката")
    @allure.description("Заполняем форму заказа и проверяем оформление")
    def test_order(self, driver, order_button, name, sure_name, address_name, metro_name_locator, phone_number,
                   date_selector_locator, rent_period_locator, color_locator, comment_text
                   ):

        base_page = BasePage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        dzen_page = DzenPage(driver)

        base_page.open_page(URLSConstants.START_PAGE)
        main_page.order_click(order_button)
        order_page.fill_for_who_form(
            name=name,
            sure_name=sure_name,
            address_name=address_name,
            metro_name_locator=metro_name_locator,
            phone_number=phone_number,
        )
        order_page.fill_about_rent_form(
            date_selector_locator=date_selector_locator,
            rent_period_locator=rent_period_locator,
            color_locator=color_locator,
            comment_text=comment_text,
        )
        order_page.click_scooter_button()
        main_page_text = main_page.get_main_scooter_text()
        assert main_page_text == 'Привезём его прямо к вашей двери,\nа когда накатаетесь — заберём'
        main_page.click_yandex_button()
        dzen_text = dzen_page.get_dzen_find_text()
        assert dzen_text == 'Новости'