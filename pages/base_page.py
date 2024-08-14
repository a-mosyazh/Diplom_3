import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from global_params import USER_PASSWORD, USER_EMAIL
from locators.base_page_locators import BasePageLocator
from locators.home_page_locators import HomePageLocator
from utils.helpers import order_id_is_changed


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки кнопки "Оформить заказ"')
    def wait_for_order_button_load(self):
        self.wait_for_element_to_be_visible(BasePageLocator.CREATE_ORDER_BTN)

    @allure.step('Ожидание загрузки кнопки "Войти"')
    def wait_for_login_button_load(self):
        self.wait_for_element_to_be_visible(BasePageLocator.LOGIN_BTN)

    @allure.step('Ожидание кликабельности кнопки "Выход"')
    def wait_for_logout_btn_load(self):
        self.wait_for_element_to_be_clickable(BasePageLocator.LOGOUT_BTN)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_profile_btn(self):
        self.click_on_element(BasePageLocator.PROFILE_BTN)

    @allure.step('Ожидание загрузки Личного Кабинета')
    def wait_for_load_profile_page(self):
        self.wait_for_element_to_be_clickable(BasePageLocator.SAVE_BTN)

    @allure.step('Клик по пункту "История заказов"')
    def click_on_order_history_menu_option(self):
        self.click_on_element(BasePageLocator.ORDER_HISTORY_MENU_OPTION)

    @allure.step('Ожидание загрузки Истории заказов')
    def wait_for_load_order_history_list(self):
        self.wait_for_element_to_be_visible(BasePageLocator.ORDER_HISTORY_LIST)

    @allure.step('Установка пароля')
    def set_password(self):
        self.driver.find_element(*BasePageLocator.PASSWORD_FIELD).send_keys(USER_PASSWORD)

    @allure.step('Установка почты')
    def set_email(self):
        self.driver.find_element(*BasePageLocator.EMAIL_FIELD).send_keys(USER_EMAIL)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        self.driver.find_element(*BasePageLocator.LOGIN_BTN).click()

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_btn(self):
        self.driver.find_element(*BasePageLocator.LOGOUT_BTN).click()

    @allure.step('Клик по кнопке Лента Заказов')
    def click_on_order_feed_btn(self):
        self.click_on_element(BasePageLocator.ORDER_FEED_BTN)

    @allure.step('Клик по кнопке Конструктор')
    def click_on_constructor_btn(self):
        self.click_on_element(BasePageLocator.CONSTRUCTOR_BTN)

    @allure.step('Получение заголовка модального окна')
    def get_modal_window_title(self):
        return self.get_element_text(BasePageLocator.MODAL_WINDOW_TITLE)

    @allure.step('Клик по элементу')
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Установить почту')
    def set_value(self, element, value):
        self.driver.find_element(*element).send_keys(value)

    @allure.step('Получение текущей ссылки вкладки')
    def get_current_link(self):
        return self.driver.current_url

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, element):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(element))

    @allure.step('Ожидание загрузки элемента')
    def wait_for_element_to_be_visible(self, element):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(element))

    @allure.step('Получение текста элемента')
    def get_element_text(self, element):
        return self.driver.find_element(*element).text

    @allure.step('Ожидание закрытия элемента')
    def wait_for_element_to_be_invisible(self, element):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(element))

    @allure.step('Проверка того, что элемент более не виден')
    def is_element_visible(self, element):
        try:
            return self.driver.find_element(*element).is_displayed()
        finally:
            return False

    @allure.step('Перетаскивание ингредиента в контруктор')
    def drag_and_drop(self):
        source_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomePageLocator.INGREDIENT_TITLE)
        )
        target_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomePageLocator.BASKET_LIST)
        )
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step('Клик по кнопке создания заказа')
    def click_on_create_order_button(self):
        self.click_on_element(BasePageLocator.CREATE_ORDER_BTN)

    @allure.step('Ожидание идентификатора заказа')
    def wait_for_order_id(self):
        WebDriverWait(self.driver, 5).until(lambda d: order_id_is_changed(d, BasePageLocator.MODAL_WINDOW_TITLE))

    @allure.step('Клик по кнопке закрытия модального окна')
    def close_modal_window(self):
        self.click_on_element(HomePageLocator.MODAL_WINDOW_CLOSE_BTN)

    @allure.step('Создание заказа')
    def create_order(self):
        self.drag_and_drop()
        self.click_on_create_order_button()
        self.wait_for_element_to_be_visible(HomePageLocator.MODAL_WINDOW)
        self.wait_for_order_id()

    @allure.step('Поиск элемента')
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
