from selenium.webdriver.common.by import By


class OrderFeedPageLocator:
    MODAL_WINDOW = [By.XPATH, './/section[contains(@class, "modal_opened")]/div[contains(@class, "modal__container")]']
    MODAL_WINDOW_TITLE = [By.XPATH, './/section[contains(@class, "modal_opened")]//'
                                    'h2[contains(@class, "text_type_main")]']
    MODAL_WINDOW_ORDER_ID = [By.XPATH, './/section[contains(@class, "modal_opened")]/div/div/'
                                       'p[contains(@class, "text_type_digits")]']
    TOTAL_COUNT = [By.XPATH, './/div[contains(@class, "OrderFeed_ordersData")]/div[2]/'
                             'p[contains(@class, "OrderFeed_number")]']
    DAILY_COUNT = [By.XPATH, './/div[contains(@class, "OrderFeed_ordersData")]/div[3]/'
                             'p[contains(@class, "OrderFeed_number")]']
    FIRST_ORDER_ID = [By.XPATH, './/ul[contains(@class, "OrderFeed_list")]/li[1]//'
                                'div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits")]']
    FIRST_ORDER_NAME = [By.XPATH, './/ul[contains(@class, "OrderFeed_list")]/li[1]//h2']
    ORDER_IN_PROGRESS = [By.XPATH, './/ul[contains(@class, "OrderFeed_orderListReady")]/li[1]']
