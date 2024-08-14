from selenium.webdriver.common.by import By


class BasePageLocator:
    PROFILE_BTN = [By.XPATH, './/p[text()="Личный Кабинет"]']
    SAVE_BTN = [By.XPATH, './/button[text()="Сохранить"]']
    EMAIL_FIELD = [By.XPATH, './/input[@type="text" and @name="name"]']
    PASSWORD_FIELD = [By.XPATH, './/input[@type="password" and @name="Пароль"]']
    LOGIN_BTN = [By.XPATH, './/button[text()="Войти"]']
    CREATE_ORDER_BTN = [By.XPATH, './/button[text()="Оформить заказ"]']
    ORDER_HISTORY_MENU_OPTION = [By.XPATH, './/a[text()="История заказов"]']
    ORDER_HISTORY_LIST = [By.XPATH, './/ul[contains(@class, "OrderHistory_list")]']
    LOGOUT_BTN = [By.XPATH, './/button[text()="Выход"]']
    ORDER_FEED_BTN = [By.XPATH, './/p[text()="Лента Заказов"]']
    CONSTRUCTOR_BTN = [By.XPATH, './/p[text()="Конструктор"]']
    MODAL_WINDOW_TITLE = [By.XPATH, './/section[contains(@class, "modal_opened")]//'
                                    'h2[contains(@class, "modal__title")]']
