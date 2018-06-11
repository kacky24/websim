import argparse
from selenium import webdriver
from config.local_config import websim_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import login
from utils import Config
from utils import setting
import time


def main(args):
    # load config
    config = Config(args.config_path)
    # load txt
    with open(config.alpha_path, 'r') as f:
        lines = f.readlines()

    driver = webdriver.Chrome(config.chromedriver_path)

    # access url
    driver.get(args.access_url)
    # login
    if driver.title == "Login / Register":
        login(driver, websim_config)
    # setting
    if args.change_setting:
        WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.test-settingslink')))
        elements = driver.find_elements_by_class_name('test-settingslink')
        for e in elements:
            e.click()
        setting(driver, 'region', config.region)
        setting(driver, 'univid', config.univid)
        setting(driver, 'delay', config.delay)
        setting(driver, 'decay', config.decay)
        setting(driver, 'optrunc', config.optrunc)
        setting(driver, 'opneut', config.opneut)
        time.sleep(0.5)
        for e in elements:
            e.click()
        time.sleep(0.5)

    for alpha in lines:
        driver.get(args.access_url)
        # login
        if driver.title == "Login / Register":
            login(driver, websim_config)
        # wait moving to simulate page
        WebDriverWait(driver, 60).until(
                lambda driver: driver.title.lower().startswith('simulate'))
        try:
            single_simulate(driver, alpha.strip())
        except TimeoutException as ex:
            print(ex.args)
            pass

        # access url
        driver.get(args.access_url)
        # login
        if driver.title == "Login / Register":
            login(driver, websim_config)


def single_simulate(driver, alpha):
    try:
        # wait for preparation for simulation
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'code-editor-container')))
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.sim-action-simulate')))
        # execute
        elem = driver.find_element_by_id("code-editor-container")
        elem.click()
        actions = webdriver.ActionChains(driver)
        actions.send_keys(alpha).perform()
        elem.click()
        elem.click()
        elements = driver.find_elements_by_class_name('sim-action-simulate')
        for e in elements:
            e.click()
        # wait during simulation
        WebDriverWait(driver, 30).until(
                lambda driver: driver.title.lower().startswith('wait'))
        WebDriverWait(driver, 300).until(
                lambda driver: driver.title.lower().startswith('result'))
        return True

    except Exception as ex:
        print(ex.args)
        print('NO')
        # return driver
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulation')
    parser.add_argument('--config_path', type=str,
                        default='./config/config.yml')
    parser.add_argument(
            '--access_url', type=str,
            default='https://websim.worldquantchallenge.com/simulate')
    parser.add_argument('--change_setting', type=bool,
                        default=True)
    args = parser.parse_args()
    main(args)
