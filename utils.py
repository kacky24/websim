from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import yaml
from easydict import EasyDict as edict


def login(driver, websim_config):
    driver.implicitly_wait(20)
    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'EmailAddress')))
    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'Password')))
    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.login-btn')))
    try:
        driver.find_element_by_id('EmailAddress').send_keys(
                websim_config['mail'])
        driver.find_element_by_id('Password').send_keys(
                websim_config['password'])
        elements = driver.find_elements_by_class_name('login-btn')
        for e in elements:
            e.click()
    except Exception as ex:
        print(ex.args)
        pass


def setting(driver, name, value):
    try:
        if name == 'decay' or name == 'optrunc':
            elem = driver.find_elements_by_name(name)[0]
            elem.clear()
            elem.send_keys(value)
        else:
            Select(driver.find_element_by_name(name)).select_by_value(value)
    except Exception as ex:
        print(ex.args)
        pass


def Config(filename):

    with open(filename, 'r') as f:
        parser = edict(yaml.load(f))
    return parser
