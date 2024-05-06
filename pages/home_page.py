import time

from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException

class HomePage(BasePage):

    def verify_favorite_functionality(self):
        time.sleep(2)

        # Loop for clicking 20 favorite products
        for i in range(1, 7):
            favorite_xpath = By.XPATH, f"(//div[@class='favourite mat-elevation-z8 ng-star-inserted'])[{i}]"

            try:
                self.wait_clickable(favorite_xpath, 5).click()
            except ElementClickInterceptedException:
                fav_btn = self.wait_clickable(favorite_xpath, 5)
                self.action_click(fav_btn)
            time.sleep(0.5)
