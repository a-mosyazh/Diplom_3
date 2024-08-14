import allure
import pytest

from global_params import BASE_URL, ORDER_FEED_URL
from pages.orders_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title('Открытие модального окна с деталями заказа по клику на карточку заказа')
    @allure.description('Проверка: в окне с деталями заказа имеется номер заказа и наименование')
    def test_order_details_modal_window_is_opened(self, driver):
        driver.get(ORDER_FEED_URL)

        order_page = OrderFeedPage(driver)
        order_page.wait_for_order_in_the_list_load()
        order_id_in_list = order_page.get_order_id()
        order_name_in_list = order_page.get_order_name()

        order_page.click_on_order_panel()
        order_page.wait_for_modal_window_to_be_opened()

        order_id_in_modal_window = order_page.get_order_id_in_modal_window()
        order_name_in_modal_window = order_page.get_order_name_in_modal_window()

        assert order_id_in_list == order_id_in_modal_window and order_name_in_list == order_name_in_modal_window

    @allure.title('При создании нового заказа счётчик выполненных заказов увеличивается')
    @allure.description('Проверка: счетчик до создания заказа меньше, чем счетчик после создания заказа')
    @pytest.mark.parametrize("get_counter_value", [
        lambda order_page: order_page.get_total_count_value(),
        lambda order_page: order_page.get_daily_count_value(),
    ])
    def test_counter_is_increased_on_order_creation(self, driver, login_manager, get_counter_value):
        driver.get(BASE_URL)
        login_manager.login()

        order_page = OrderFeedPage(driver)

        order_page.click_on_order_feed_btn()
        order_page.wait_for_counters_load()
        counter_before = get_counter_value(order_page)

        order_page.click_on_constructor_btn()
        order_page.wait_for_order_button_load()
        order_page.create_order()
        created_order_id = f'0{str(order_page.get_modal_window_title())}'
        order_page.close_modal_window()

        order_page.click_on_order_feed_btn()
        order_page.wait_for_counters_load()
        # это ожидание позволяет дождаться окончательного обновления счетчиков,
        # т.к. счетчики ведут себя нестабильно, что приводит к нестабильности теста
        order_page.wait_for_order_to_be_in_progress(created_order_id)
        counter_after = get_counter_value(order_page)

        assert counter_before < counter_after

    @allure.title('После оформления заказа он появляется в столбце "В работе')
    @allure.description('Проверка: значение в столбце "В работе" == идентификатор созданного заказа')
    def test_created_order_is_in_progress_after_creation(self, driver, login_manager):
        driver.get(BASE_URL)
        login_manager.login()

        order_page = OrderFeedPage(driver)

        order_page.click_on_constructor_btn()
        order_page.wait_for_order_button_load()
        order_page.create_order()

        created_order_id = order_page.get_modal_window_title()
        order_id_to_compare = f'0{str(created_order_id)}'
        order_page.close_modal_window()

        order_page.click_on_order_feed_btn()
        order_page.wait_for_order_to_be_in_progress(order_id_to_compare)

        order_id_in_progress = order_page.get_order_id_in_progress()

        assert order_id_to_compare == order_id_in_progress

    @allure.title('Заказ пользователя отображается в истории заказов и в ленте всех заказов')
    @allure.description('Проверка: карточка с идентификатором созданного заказа '
                        'отображается в истории заказов и в ленте заказов')
    def test_created_order_is_in_history_and_feed(self, driver, login_manager):
        driver.get(BASE_URL)
        login_manager.login()

        order_page = OrderFeedPage(driver)

        order_page.click_on_constructor_btn()
        order_page.wait_for_order_button_load()
        order_page.create_order()
        created_order_id = order_page.get_modal_window_title()
        order_id = f'#0{str(created_order_id)}'
        order_page.close_modal_window()

        order_page.click_profile_btn()
        order_page.wait_for_load_profile_page()
        order_page.click_on_order_history_menu_option()
        order_page.wait_for_load_order_history_list()

        order_in_history = order_page.is_dynamic_order_displayed(order_id)

        order_page.click_on_order_feed_btn()
        order_page.wait_for_counters_load()

        order_in_feed = order_page.is_dynamic_order_displayed(order_id)

        assert order_in_history is True and order_in_feed is True
