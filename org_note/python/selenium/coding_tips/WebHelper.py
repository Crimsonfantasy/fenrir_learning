from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string import Template


class WebHelper:

    @staticmethod
    def wait_2_click(driver: webdriver, css_path: str):
        wait2 = WebDriverWait(driver, 10)
        clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, css_path))
        wait2.until(clickable).click()

    @staticmethod
    def wait_2_input(driver: webdriver, css_path: str, txt: str):
        wait2 = WebDriverWait(driver, 10)
        input_able = EC.element_to_be_clickable((By.CSS_SELECTOR, css_path))
        _input = wait2.until(input_able)
        _input.clear()
        _input.send_keys(txt)

    @staticmethod
    def wait_2_move(driver: webdriver, error_dialog: str):
        wait0 = WebDriverWait(driver, 10)
        visible_condition = EC.visibility_of_element_located((By.XPATH, error_dialog))
        target_ele = wait0.until(visible_condition)
        ActionChains(driver).move_to_element(target_ele).perform()

    @staticmethod
    def wait_check_visible(driver: webdriver, path: str) -> bool:
        wait0 = WebDriverWait(driver, 5)
        visible_condition = EC.visibility_of_element_located((By.CSS_SELECTOR, path))
        try:
            target_ele = wait0.until(visible_condition)
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_2_change_inner_html(driver: webdriver, path: str, data: str):
        wait0 = WebDriverWait(driver, 10)
        visible_condition = EC.visibility_of_element_located((By.CSS_SELECTOR, path))
        element = wait0.until(visible_condition)
        t = Template("let ele=arguments[0]; ele.innerHTML = '$replace';")
        js = t.substitute(replace=data)
        driver.execute_script(js, element)
