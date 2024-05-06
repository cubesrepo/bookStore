import random
import time

from faker import Faker
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class CartPage(BasePage):

    def add_to_cart_all_products_in_favorites(self):
        time.sleep(2)

        #favorite menu click
        self.wait_clickable(test_data.homepage.FAVORITE_MENU, 15).click()

        time.sleep(0.5)

        #loop for cliking add to cart
        for i in range(1, 7):
            add_to_cart_btn = By.XPATH, f"(//span[contains(text(),'Add to Cart')])[{i}]"
            if i % 3 == 0:
                self.scroll_by_amount(0, 150)
            time.sleep(0.5)

            try:
                addtocart = self.wait_clickable(add_to_cart_btn, 5)
                addtocart.click()
            except:
                self.wait_clickable(add_to_cart_btn, 5).click()
            time.sleep(0.5)

        time.sleep(1)

    def checkout_all_products(self):
        time.sleep(2)

        #click cart menu
        self.wait_clickable(test_data.cart.CART_MENU, 5).click()

        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); ")
        time.sleep(0.5)
        #click checkout btn
        self.wait_clickable(test_data.cart.CHECKOUT_BTN, 5).click()

        time.sleep(0.5)

        fake = Faker()
        #input name
        namevalue = fake.name()
        self.send_keys(15, test_data.cart.NAME, namevalue)

        time.sleep(0.5)

        # input address
        addressvalue = "address one"
        self.send_keys(15, test_data.cart.ADDRESS_ONE, addressvalue)

        time.sleep(0.5)

        # input address
        addresstwovalue = "address two"
        self.send_keys(15, test_data.cart.ADDRES_TWO, addresstwovalue)

        time.sleep(0.5)

        # input pincode
        pincodevalue = "164346"
        self.send_keys(15, test_data.cart.PINCODE, pincodevalue)

        time.sleep(0.5)

        # input STATE
        statevalue = "golden state"
        self.send_keys(15, test_data.cart.STATE, statevalue)

        time.sleep(0.5)

        #click placeorder
        self.wait_clickable(test_data.cart.PLACE_ORDER, 15).click()