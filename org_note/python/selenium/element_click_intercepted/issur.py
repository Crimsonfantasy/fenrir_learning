from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settting import full_quick_config

if __name__ == '__main__':
    options = Options()
    options = options
    driver = webdriver.Chrome()  # 開啟firefox
    driver.get(url=full_quick_config.home_url)  # 前往這個網址

    wait0 = WebDriverWait(driver, 10)
    dialogBox = EC.visibility_of_element_located((By.XPATH, '/html/body/ion-app/ion-alert/div'))
    dialogBoxEle = wait0.until(dialogBox)
    ActionChains(driver).move_to_element(dialogBoxEle).perform()

    # 10 次會有2次發生 Message: element click intercepted:
    # wait1 = WebDriverWait(driver, 10)
    # lineErrorBtn = EC.element_to_be_clickable((By.XPATH, '/html/body/ion-app/ion-alert/div/div[3]'))
    # wait1.until(lineErrorBtn).click()

    # 一個需要控制滑鼠向下捲動的炒飯按鈕
    # wait2 = WebDriverWait(driver, 10)
    # btnK = EC.element_to_be_clickable((By.XPATH, '//*[@id="scrollDiv"]/ul[9]/li[5]/a/div[2]'))
    # wait2.until(btnK).click()

    # selector
    err_btn = driver.find_element_by_css_selector(css_selector="body > ion-app > ion-alert > div >"
                                                               " div.alert-button-group > "
                                                               "button")
    err_btn.click()

    # 一個需要控制滑鼠向下捲動的炒飯按鈕
    # fire_rice = driver.find_element_by_xpath(xpath='//*[@id="scrollDiv"]/ul[9]/li[5]/a/div[2]')
    # fire_rice.click()

    # search_input = driver.find_element_by_name("q")
    # search_input.send_keys('pornhub')
    # start_search_btn = driver.find_element_by_xpath(xpath='//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    # start_search_btn.click()
    # wait2 = WebDriverWait(driver, 10)
    # https: // selenium - python - zh.readthedocs.io / en / latest / waits.html?highlight = element_to_be_clickable
    # btnK = EC.element_to_be_clickable((By.NAME, 'btnK'))
    # element1 = wait2.until(btnK)
    # element1.click()
    # driver.close()
