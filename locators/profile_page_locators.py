from selenium.webdriver.common.by import By


class ProfilePageLocator:
    ORDER_HISTORY_LIST_OPTIONS = [By.XPATH, './/ul[contains(@class, "OrderHistory_list")]/li']
