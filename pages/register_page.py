import random
import string
import time

from faker import Faker

import test_data
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def verify_register_with_valid_value_then_login(self):
        time.sleep(2)

        #click login menu
        self.wait_clickable(test_data.homepage.LOGIN_MENU, 15).click()

        time.sleep(0.5)

        #check page url
        self.url_is("https://bookcart.azurewebsites.net/login")

        #clickr register
        self.wait_clickable(test_data.register.REGISTER_MAIN_BTN, 15).click()

        #check page url
        self.url_is("https://bookcart.azurewebsites.net/register")

        fake = Faker()

        #input firstname
        firstnamevalue = fake.first_name()
        self.send_keys(10, test_data.register.FIRST_NAME, firstnamevalue)

        time.sleep(0.5)

        #input lastname
        lastnamevalue = fake.last_name()
        self.send_keys(10, test_data.register.LAST_NAME, lastnamevalue)

        time.sleep(0.5)

        # input username
        usernamevalue = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=9))
        self.send_keys(10, test_data.register.USER_NAME, usernamevalue)
        print(f"First username {usernamevalue}")

        time.sleep(0.5)

        # input password
        self.send_keys(10, test_data.register.PASSWORD, test_data.PASSWORD)
        print(f"First password {test_data.PASSWORD}")
        time.sleep(0.5)

        # input CONFIRM password
        self.send_keys(10, test_data.register.CONFIRM_PASS, test_data.PASSWORD)

        time.sleep(0.5)

        #click male
        male = self.wait_clickable(test_data.register.MALE, 10)
        self.action_click(male)

        #click registergbtn
        time.sleep(0.5)
        try:
             self.wait_clickable(test_data.register.REGISTER_BTN, 5).click()
        except:
            registerbtn = self.wait_clickable(test_data.register.REGISTER_BTN, 5)
            self.action_click(registerbtn)

        time.sleep(1)

        # input username
        username = self.wait_visibility(test_data.login.USERNAME, 15)
        self.action_send_keys_with_clear(username, usernamevalue)

        time.sleep(0.5)

        # input password
        password = self.wait_visibility(test_data.login.PASSWORD, 15)
        self.action_send_keys_with_clear(password, test_data.PASSWORD)

        time.sleep(0.5)

        # click login btn
        try:
            self.wait_clickable(test_data.login.LOGIN_BTN, 5).click()
        except:
            login = self.wait_clickable(test_data.login.LOGIN_BTN, 15)
            self.action_click(login)

        print(f"last {usernamevalue}")
        print(f"last password {test_data.PASSWORD}")
