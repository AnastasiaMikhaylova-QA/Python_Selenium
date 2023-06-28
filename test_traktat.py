"""
ТС-1:Smoke test
"""
import pytest
from selenium.webdriver.common.by import By


def test_smoke(browser):
    """
    smoke test
    """
    browser.get("https://www.traktat.com/")

    element = browser.find_element(by=By.CSS_SELECTOR, value="#menu-item-44")
    element.click()

    element = browser.find_element(by=By.CSS_SELECTOR, value="body > div.wrapper > div.content > header > div:nth-child(3) > a")
    element.click()

    sku = browser.find_element(By.CLASS_NAME, value="mt-none")

    assert sku.text == 'Пригласить нас на тендер', "Unexpected sku"
    assert True, ""

    