from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCORDION_QUESTION_0 = (By.XPATH, "//div[@id='accordion__heading-0']") #1-ая кнопка FAQ
    ACCORDION_ANSWER_0 = (By.XPATH, "//div[@id='accordion__panel-0']//p")  #1-ый ответ FAQ
    ACCORDION_QUESTION_1 = (By.XPATH, "//div[@id='accordion__heading-1']") #2-ая кнопка FAQ
    ACCORDION_ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-1']//p")  #2-ой ответ FAQ
    ACCORDION_QUESTION_2 = (By.XPATH, "//div[@id='accordion__heading-2']") #3-ья кнопка FAQ
    ACCORDION_ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-2']//p")  #3-ий ответ FAQ
    ACCORDION_QUESTION_3 = (By.XPATH, "//div[@id='accordion__heading-3']") #4-ая кнопка FAQ
    ACCORDION_ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-3']//p")  #4-ый ответ FAQ
    ACCORDION_QUESTION_4 = (By.XPATH, "//div[@id='accordion__heading-4']") #5-ая кнопка FAQ
    ACCORDION_ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-4']//p")  #5-ый ответ FAQ
    ACCORDION_QUESTION_5 = (By.XPATH, "//div[@id='accordion__heading-5']") #6-ая кнопка FAQ
    ACCORDION_ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-5']//p")  #6-ой ответ FAQ
    ACCORDION_QUESTION_6 = (By.XPATH, "//div[@id='accordion__heading-6']") #7-ая кнопка FAQ
    ACCORDION_ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-6']//p")  #7-ой ответ FAQ
    ACCORDION_QUESTION_7 = (By.XPATH, "//div[@id='accordion__heading-7']") #8-ая кнопка FAQ
    ACCORDION_ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-7']//p")  #8-ой ответ FAQ
    YANDEX_BUTTON = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")  #Кнопка Яндекс в хэдере
    BUTTON_ORDER_IN_HEADER = (By.XPATH, "(//button[contains(., 'Заказать')])[1]")  #Кнопка Заказать в хэдере
    BUTTON_ORDER_IN_CENTER = (By.XPATH, "(//button[contains(., 'Заказать')])[2]")  #Кнопка Заказать в хэдере
    TEXT_ABOUT_SCOOTER = (By.XPATH, "//div[text()='Привезём его прямо к вашей двери,']")  #Текст на главной стр
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")  #Кнопка куки нотификейшен
