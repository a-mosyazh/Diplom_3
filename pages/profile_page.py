import allure

from locators.profile_page_locators import ProfilePageLocator
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Получение длины списка истории заказов')
    def get_length_of_order_history_list(self):
        list_element = self.driver.find_elements(*ProfilePageLocator.ORDER_HISTORY_LIST_OPTIONS)
        return len(list_element)
