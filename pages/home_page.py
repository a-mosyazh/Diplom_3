import allure

from locators.home_page_locators import HomePageLocator
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидание заголовка ингредиента')
    def wait_for_ingredient_title(self):
        self.wait_for_element_to_be_clickable(HomePageLocator.INGREDIENT_TITLE)

    @allure.step('Ожидание заголовка страницы Лента Заказов')
    def wait_for_order_feed_title(self):
        self.wait_for_element_to_be_visible(HomePageLocator.ORDER_FEED_HEADER)

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(HomePageLocator.INGREDIENT_TITLE)

    @allure.step('Ожидание модального окна с деталями ингредиента')
    def wait_for_ingredient_modal_window(self):
        self.wait_for_element_to_be_visible(HomePageLocator.MODAL_WINDOW)

    @allure.step('Клик по кнопке закрытия модального окна')
    def click_on_close_button(self):
        self.click_on_element(HomePageLocator.MODAL_WINDOW_CLOSE_BTN)

    @allure.step('Ожидание закрытия модального окна с ингредиентом')
    def wait_for_ingredient_modal_window_to_be_closed(self):
        self.wait_for_element_to_be_invisible(HomePageLocator.MODAL_WINDOW)

    @allure.step('Проверка того, отображается ли модальное окно')
    def is_modal_window_visible(self):
        return self.is_element_visible(HomePageLocator.MODAL_WINDOW)

    @allure.step('Перетаскивание ингредиента в контруктор')
    def add_ingredient_to_order(self):
        self.drag_and_drop()

    @allure.step('Получение каунтера ингредиента')
    def get_ingredient_counter(self):
        return self.get_element_text(HomePageLocator.INGREDIENT_COUNTER)
