import allure

from data.data import INGREDIENT_MODAL_WINDOW_TITLE, INGREDIENT_COUNTER, DEFAULT_ORDER_ID
from global_params import BASE_URL, LOGIN_URL, ORDER_FEED_URL
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Открытие страницы Конструктор')
    @allure.description(f'После клика по ссылке проверяем, что get_current_link() == {BASE_URL}')
    def test_constructor_page_opens_via_constructor_btn(self, driver):
        driver.get(LOGIN_URL)

        home_page = HomePage(driver)
        home_page.wait_for_login_button_load()
        home_page.click_on_constructor_btn()
        home_page.wait_for_ingredient_title()

        assert home_page.get_current_link() == BASE_URL

    @allure.title('Открытие страницы Лента Заказов по клику на кнопку Лента Заказов в хедере')
    @allure.description(f'Проверка: после клика по ссылке и редиректа get_current_link() == {ORDER_FEED_URL}')
    def test_order_feed_page_opens_via_order_feed_btn(self, driver):
        driver.get(LOGIN_URL)

        home_page = HomePage(driver)
        home_page.wait_for_login_button_load()
        home_page.click_on_order_feed_btn()
        home_page.wait_for_order_feed_title()

        assert home_page.get_current_link() == ORDER_FEED_URL

    @allure.title('Открытие модального окна с деталями ингредиента')
    @allure.description(f'Проверка: после клика по карточке ингредиента '
                        f'открывается модальное окно с заголовком "Детали ингредиента"')
    def test_modal_window_with_ingredient_details_opens(self, driver):
        driver.get(BASE_URL)

        home_page = HomePage(driver)
        home_page.wait_for_ingredient_title()
        home_page.click_on_ingredient()
        home_page.wait_for_ingredient_modal_window()

        assert home_page.get_modal_window_title() == INGREDIENT_MODAL_WINDOW_TITLE

    @allure.title('Закрытие модального окна с деталями ингредиента')
    @allure.description(f'Проверка: после клика по кнопке закрытия проверяем, что окно больше не отображается')
    def test_modal_window_with_ingredient_details_closes(self, driver):
        driver.get(BASE_URL)

        home_page = HomePage(driver)
        home_page.wait_for_ingredient_title()
        home_page.click_on_ingredient()
        home_page.wait_for_ingredient_modal_window()
        home_page.click_on_close_button()
        home_page.wait_for_ingredient_modal_window_to_be_closed()

        assert not home_page.is_modal_window_visible()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер добавленного ингредиента')
    @allure.description(f'Проверка: после перетаскивания ингредиента каунтер ингредиента == {INGREDIENT_COUNTER}')
    def test_ingredient_counter_increases_when_adding_ingredient_to_cart(self, driver):
        driver.get(BASE_URL)

        home_page = HomePage(driver)
        home_page.wait_for_ingredient_title()
        home_page.drag_and_drop()

        assert home_page.get_ingredient_counter() == INGREDIENT_COUNTER

    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description(f'Проверка: создание заказа под авторизованным пользователем '
                        f'и идентификатор заказа в модальном окне > 0')
    def test_user_with_auth_is_able_to_create_order(self, driver, login_manager):
        driver.get(BASE_URL)
        login_manager.login()
        login_manager.window_is_opened = True

        home_page = HomePage(driver)
        home_page.wait_for_ingredient_title()
        home_page.create_order()

        assert (int(home_page.get_modal_window_title()) != DEFAULT_ORDER_ID
                and int(home_page.get_modal_window_title()) > 0)
