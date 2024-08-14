import allure

from data.data import EXPECTED_BORDER_STYLE
from global_params import LOGIN_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL, USER_EMAIL
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description(f'Проверка: после клика по ссылке get_current_link() == {FORGOT_PASSWORD_URL}')
    def test_redirect_from_login_page_to_forgot_password_page(self, driver):
        driver.get(LOGIN_URL)

        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.wait_for_reset_link_load()
        reset_pass_page.click_reset_password_link()

        assert reset_pass_page.get_current_link() == FORGOT_PASSWORD_URL

    @allure.title('Проверка перехода к форме восстановления пароля по кнопке «Восстановить»')
    @allure.description(f'Проверка: после ввода почты и клика по кнопке get_current_link() == {RESET_PASSWORD_URL}')
    def test_redirect_from_forgot_password_to_reset_password(self, driver):
        driver.get(FORGOT_PASSWORD_URL)

        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.wait_for_reset_button_to_be_clickable()
        reset_pass_page.set_email_for_reset(USER_EMAIL)
        reset_pass_page.click_reset_button()
        reset_pass_page.wait_for_password_field_to_be_enabled()

        assert reset_pass_page.get_current_link() == RESET_PASSWORD_URL

    @allure.title('После клика по кнопке показать/скрыть пароль у поля появляется подсветка')
    @allure.description(
        f'Проверка: после клика по кнопке "показать пароль" проверяется стиль элемента')
    def test_password_field_changes_border_color_on_click(self, driver):
        driver.get(FORGOT_PASSWORD_URL)

        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.wait_for_reset_button_to_be_clickable()
        reset_pass_page.set_email_for_reset(USER_EMAIL)
        reset_pass_page.click_reset_button()
        reset_pass_page.wait_for_password_field_to_be_enabled()

        reset_pass_page.click_show_password_button()
        reset_pass_page.wait_for_border_color_to_be_changed()

        border_style = reset_pass_page.get_element_border_style()

        assert border_style == EXPECTED_BORDER_STYLE
