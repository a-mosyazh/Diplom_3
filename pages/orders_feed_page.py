import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.orders_feed_page_locators import OrderFeedPageLocator
from pages.base_page import BasePage
from utils.helpers import order_is_in_progress


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидание загрузки карточки заказа в списке')
    def wait_for_order_in_the_list_load(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocator.FIRST_ORDER_ID)

    @allure.step('Получение идентификатора заказа из карточки заказа')
    def get_order_id(self):
        return self.get_element_text(OrderFeedPageLocator.FIRST_ORDER_ID)

    @allure.step('Получение наименования заказа из карточки заказа')
    def get_order_name(self):
        return self.get_element_text(OrderFeedPageLocator.FIRST_ORDER_NAME)

    @allure.step('Клик по карточке заказа')
    def click_on_order_panel(self):
        self.click_on_element(OrderFeedPageLocator.FIRST_ORDER_ID)

    @allure.step('Ожидание открытия модального окна')
    def wait_for_modal_window_to_be_opened(self):
        self.wait_for_element_to_be_visible(OrderFeedPageLocator.MODAL_WINDOW)

    @allure.step('Получение идентификатора заказа из модального окна')
    def get_order_id_in_modal_window(self):
        return self.get_element_text(OrderFeedPageLocator.MODAL_WINDOW_ORDER_ID)

    @allure.step('Получение наименования заказа из модального окна')
    def get_order_name_in_modal_window(self):
        return self.get_element_text(OrderFeedPageLocator.MODAL_WINDOW_TITLE)

    @allure.step('Получение значения каунтера "Выполнено за все время"')
    def get_total_count_value(self):
        return self.get_element_text(OrderFeedPageLocator.TOTAL_COUNT)

    @allure.step('Ожидание загрузки каунтеров')
    def wait_for_total_counter_load(self):
        self.wait_for_element_to_be_visible(OrderFeedPageLocator.TOTAL_COUNT)

    @allure.step('Ожидание загрузки каунтера "Выполнено за сегодня"')
    def wait_for_daily_counter_load(self):
        self.wait_for_element_to_be_visible(OrderFeedPageLocator.DAILY_COUNT)

    @allure.step('Ожидание загрузки каунтеров')
    def wait_for_counters_load(self):
        self.wait_for_total_counter_load()
        self.wait_for_daily_counter_load()

    @allure.step('Получение значения каунтера "Выполнено за сегодня"')
    def get_daily_count_value(self):
        return self.get_element_text(OrderFeedPageLocator.DAILY_COUNT)

    @allure.step('Получение идентификатора заказа, находящегося в работе')
    def get_order_id_in_progress(self):
        return self.get_element_text(OrderFeedPageLocator.ORDER_IN_PROGRESS)

    @allure.step('Ожидание загрузки заказа, находящегося в работе')
    def wait_for_order_to_be_in_progress(self, value):
        WebDriverWait(self.driver, 10).until(lambda d:
                                             order_is_in_progress(d, OrderFeedPageLocator.ORDER_IN_PROGRESS, value))

    @allure.step('Проверка наличия заказа с указанным идентификатором на странице')
    def is_dynamic_order_displayed(self, text):
        dynamic_locator = (By.XPATH, f'.//p[text()="{text}"]')
        return self.find_element(*dynamic_locator).is_displayed()
