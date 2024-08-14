from selenium.webdriver.common.by import By


class ResetPasswordPageLocator:
    RESET_PASSWORD_LINK = [By.XPATH, './/a[text()="Восстановить пароль"]']
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']
    RESET_PASSWORD_BTN = [By.XPATH, './/button[text()="Восстановить"]']
    PASSWORD_FIELD = [By.XPATH, './/input[@type="password"]']
    PASSWORD_FIELD_ACTIVE = [By.XPATH, './/div[contains(@class, "input_status_active")]']
    SHOW_PASSWORD_ICON = [By.XPATH, './/div[contains(@class, "input__icon")]']
