import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def open_page(self, page):
        self.driver.get(page)

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Находим элемент')
    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    @allure.step('Скролим до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.title('Находим элемент и кликаем по нему')
    def find_element_and_click(self, locator):
        self.find_element(locator).click()

    @allure.title('Заполняем форму')
    def fill_form(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)

    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs