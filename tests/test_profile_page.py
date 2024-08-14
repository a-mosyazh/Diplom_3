import allure
from global_params import BASE_URL, PROFILE_URL, ORDER_HISTORY_URL, LOGIN_URL
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка открытия Личного кабинета по клику на кнопку "Личный кабинет"')
    @allure.description(f'Проверка: после клика по ссылке get_current_link() == {PROFILE_URL}')
    def test_profile_page_opens(self, driver, login_manager):
        driver.get(BASE_URL)
        login_manager.login()

        profile_page = ProfilePage(driver)
        profile_page.click_profile_btn()
        profile_page.wait_for_load_profile_page()

        assert profile_page.get_current_link() == PROFILE_URL

    @allure.title('Проверка открытия Истории заказов в Личном кабинете по клику на пункт "История заказов" в меню')
    @allure.description(f'Проверка: после клика по опции "История заказов" в меню слева '
                        f'get_current_link() == {ORDER_HISTORY_URL} и длина списка заказов больше 0')
    def test_order_history_list_opens(self, driver, login_manager):
        driver.get(BASE_URL)
        login_manager.login()

        profile_page = ProfilePage(driver)
        profile_page.click_profile_btn()
        profile_page.wait_for_load_profile_page()

        profile_page.click_on_order_history_menu_option()

        profile_page.wait_for_load_order_history_list()

        assert (profile_page.get_current_link() == ORDER_HISTORY_URL
                and profile_page.get_length_of_order_history_list() > 0)

    @allure.title('Проверка выхода из аккаунта по клику на кнопку "Выход"')
    @allure.description(f'Проверка: после клика по кнопке "Выход" в меню Личного кабинета '
                        f'get_current_link() == {LOGIN_URL}')
    def test_log_out_and_redirect_to_login_page(self, driver, login_manager):
        driver.get(BASE_URL)
        login_manager.login()
        login_manager.logged_in = False

        profile_page = ProfilePage(driver)
        profile_page.click_profile_btn()
        profile_page.wait_for_load_profile_page()

        profile_page.click_logout_btn()
        profile_page.wait_for_login_button_load()

        assert profile_page.get_current_link() == LOGIN_URL
