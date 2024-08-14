import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.reset_password_page_locators import ResetPasswordPageLocator
from pages.base_page import BasePage
from utils.helpers import is_highlighted


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидание загрузки ссылки "Восстановить пароль"')
    def wait_for_reset_link_load(self):
        self.wait_for_element_to_be_visible(ResetPasswordPageLocator.RESET_PASSWORD_LINK)

    @allure.step('Клик по ссылке "Восстановить пароль"')
    def click_reset_password_link(self):
        self.click_on_element(ResetPasswordPageLocator.RESET_PASSWORD_LINK)

    @allure.step('Ожидание кликбельности кнопки "Восстановить"')
    def wait_for_reset_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(ResetPasswordPageLocator.RESET_PASSWORD_BTN)

    @allure.step('Указание почты')
    def set_email_for_reset(self, name):
        self.set_value(ResetPasswordPageLocator.EMAIL_FIELD, name)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_reset_button(self):
        self.click_on_element(ResetPasswordPageLocator.RESET_PASSWORD_BTN)

    @allure.step('Ожидание загрузки поля "Пароль"')
    def wait_for_password_field_to_be_enabled(self):
        self.wait_for_element_to_be_clickable(ResetPasswordPageLocator.PASSWORD_FIELD)

    @allure.step('Получение стиля границы поля "Пароль"')
    def get_element_border_style(self):
        style = (self.driver.find_element(*ResetPasswordPageLocator.PASSWORD_FIELD_ACTIVE)
                 .value_of_css_property("border"))
        return style

    @allure.step('Клик по кнопке для показа введенного пароля')
    def click_show_password_button(self):
        self.click_on_element(ResetPasswordPageLocator.SHOW_PASSWORD_ICON)

    @allure.step('Ожидание окончательной смены цвета границы поля')
    def wait_for_border_color_to_be_changed(self):
        WebDriverWait(self.driver, 5).until(lambda d: is_highlighted(d, ResetPasswordPageLocator.PASSWORD_FIELD_ACTIVE))
