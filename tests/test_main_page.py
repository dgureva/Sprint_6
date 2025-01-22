import allure
import pytest

from constants import MainPageConstants, URLSConstants
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize("answer, question_locator, answer_locator", [
        (MainPageConstants.QUESTION_ONE_ANSWER, MainPageLocators.ACCORDION_QUESTION_0,
         MainPageLocators.ACCORDION_ANSWER_0),
        (MainPageConstants.QUESTION_TWO_ANSWER, MainPageLocators.ACCORDION_QUESTION_1,
         MainPageLocators.ACCORDION_ANSWER_1),
        (MainPageConstants.QUESTION_THREE_ANSWER, MainPageLocators.ACCORDION_QUESTION_2,
         MainPageLocators.ACCORDION_ANSWER_2),
        (MainPageConstants.QUESTION_FOUR_ANSWER, MainPageLocators.ACCORDION_QUESTION_3,
         MainPageLocators.ACCORDION_ANSWER_3),
        (MainPageConstants.QUESTION_FIVE_ANSWER, MainPageLocators.ACCORDION_QUESTION_4,
         MainPageLocators.ACCORDION_ANSWER_4),
        (MainPageConstants.QUESTION_SIX_ANSWER, MainPageLocators.ACCORDION_QUESTION_5,
         MainPageLocators.ACCORDION_ANSWER_5),
        (MainPageConstants.QUESTION_SEVEN_ANSWER, MainPageLocators.ACCORDION_QUESTION_6,
         MainPageLocators.ACCORDION_ANSWER_6),
        (MainPageConstants.QUESTION_EIGHT_ANSWER, MainPageLocators.ACCORDION_QUESTION_7,
         MainPageLocators.ACCORDION_ANSWER_7),
    ],
         ids=(
             "FAQ_1",
             "FAQ_2",
             "FAQ_3",
             "FAQ_4",
             "FAQ_5",
             "FAQ_6",
             "FAQ_7",
             "FAQ_8",
         ),
    )
    @allure.title("Проверка блока Вопросы о важном")
    @allure.description("Раскрываем вопрос и проверяем корректность текста ответа")
    def test_faq(self, answer, question_locator, answer_locator, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.open_page(URLSConstants.START_PAGE)
        exp_text = answer
        text = main_page.get_faq_text(
            question_locator=question_locator,
            answer_locator=answer_locator
        )
        assert text == exp_text

