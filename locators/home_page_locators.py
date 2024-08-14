from selenium.webdriver.common.by import By

from data.data import LINK_TO_INGREDIENT


class HomePageLocator:
    INGREDIENT_TITLE = [By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]']
    ORDER_FEED_HEADER = [By.XPATH, './/h1[text()="Лента заказов"]']
    MODAL_WINDOW = [By.XPATH, './/section[contains(@class, "modal_opened")]/div[contains(@class, "modal__container")]']
    MODAL_WINDOW_CLOSE_BTN = [By.XPATH, './/section[contains(@class, "modal_opened")]//button']
    BASKET_LIST = [By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list")]']
    INGREDIENT_COUNTER = [By.XPATH, f'.//a[@href="{LINK_TO_INGREDIENT}"]//p[contains(@class, "counter__num")]']
