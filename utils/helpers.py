from data.data import EXPECTED_BORDER_STYLE, DEFAULT_ORDER_ID


def is_highlighted(driver, element):
    return driver.find_element(*element).value_of_css_property("border") == EXPECTED_BORDER_STYLE


def order_id_is_changed(driver, element):
    order_id = driver.find_element(*element).text
    return int(order_id) != DEFAULT_ORDER_ID


def order_is_in_progress(driver, element, value):
    order_id = driver.find_element(*element).text
    return str(order_id) == str(value)
