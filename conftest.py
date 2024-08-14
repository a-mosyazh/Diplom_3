import pytest
from selenium import webdriver

from locators.home_page_locators import HomePageLocator
from pages.base_page import BasePage


@pytest.fixture(scope='class')
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


class LoginManager:
    def __init__(self, driver):
        self.driver = driver
        self.logged_in = False
        self.window_is_opened = False

    def login(self):
        BasePage(self.driver).click_profile_btn()
        BasePage(self.driver).wait_for_login_button_load()
        BasePage(self.driver).set_password()
        BasePage(self.driver).set_email()
        BasePage(self.driver).click_login_btn()
        BasePage(self.driver).wait_for_order_button_load()
        self.logged_in = True

    def logout(self):
        if self.logged_in:
            BasePage(self.driver).click_profile_btn()
            BasePage(self.driver).wait_for_logout_btn_load()
            BasePage(self.driver).click_logout_btn()
            BasePage(self.driver).wait_for_login_button_load()
            self.logged_in = False

    def close_modal_window(self):
        if self.window_is_opened:
            BasePage(self.driver).click_on_element(HomePageLocator.MODAL_WINDOW_CLOSE_BTN)
            self.window_is_opened = False


@pytest.fixture
def login_manager(driver):
    manager = LoginManager(driver)
    yield manager
    manager.close_modal_window()
    manager.logout()
