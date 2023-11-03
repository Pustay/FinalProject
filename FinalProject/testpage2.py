import time

from FinalProject.BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestLocators:
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)

    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])

    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])


class Operations(BasePage, TestLocators):
    with open('./testdata.yaml') as f:
        info = yaml.safe_load(f)

    def enter_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['input_username'])
        if input1:
            input1.send_keys(self.info['username'])
        else:
            logging.error('Login field not found')

    def enter_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['input_passwd'])
        if input2:
            input2.send_keys(self.info['password'])
        else:
            logging.error('Password field not found')

    def click_login_button(self):
        logging.debug('Click login button ')
        btn = self.find_element(self.ids['btn_selector'])
        if btn:
            btn.click()
        else:
            logging.error('Button not found')

    def get_hello_user(self):
        hello = self.find_element(self.ids['auth_user'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('User not logged in')
            return None

    def click_about_button(self):
        logging.debug('Click contact button ')
        cont_btn = self.find_element(self.ids['about_btn'])
        if cont_btn:
            cont_btn.click()
        else:
            logging.error('Button "Contact" not found')

    #
    def header_find(self):
        logging.info("Page About opened")
        header_name = self.find_element(self.ids['header'])
        if header_name:
            text = header_name.text
            logging.info(f'Title name  {text}')
            return text
        else:
            logging.error('Title not found')
            return None

    def header_font_size(self):
        logging.info("Title About font size")
        font_size = self.get_element_property(self.ids['header'], 'font-size')
        if font_size:
            logging.info(f'Title size  {font_size}')
            return font_size
        else:
            logging.error('Cant find title font size')
            return None


