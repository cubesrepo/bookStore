from selenium.webdriver.common.by import By

BASE_URL = "https://bookcart.azurewebsites.net/"

USERNAME = "testdummy"
PASSWORD = "Password123"
class login:

    USERNAME = By.XPATH, "(//input[@id='mat-input-7'])[1]"
    PASSWORD = By.XPATH, "(//input[@id='mat-input-8'])[1]"
    LOGIN_BTN = By.XPATH, "(//span[@class='mdc-button__label'][normalize-space()='Login'])[2]"
    ERROR_MESSAGE = By.XPATH, "(//mat-error[@id='mat-mdc-error-0'])[1]"
class register:
    REGISTER_MAIN_BTN = By.XPATH, "(//span[normalize-space()='Register'])[1]"
    FIRST_NAME = By.XPATH, "(//input[@id='mat-input-2'])[1]"
    LAST_NAME = By.XPATH, "(//input[@id='mat-input-3'])[1]"
    USER_NAME = By.XPATH, "(//input[@id='mat-input-4'])[1]"
    PASSWORD = By.XPATH, "(//input[@id='mat-input-5'])[1]"
    CONFIRM_PASS = By.XPATH, "(//input[@id='mat-input-6'])[1]"
    MALE = By.XPATH, "(//mat-radio-button[@id='mat-radio-2'])[1]"
    REGISTER_BTN = By.XPATH, "(//span[normalize-space()='Register'])[1]"
class homepage:
    LOGIN_MENU = By.XPATH, "(//span[normalize-space()='Login'])[1]"
    LABEL_NAME_MENU = By.XPATH, "(//span[contains(text(),'testdummy')])[1]"
    FAVORITES_BADGE = By.ID, "mat-badge-content-1"
    LOGOUT_BTN = By.XPATH, "(//span[normalize-space()='Logout'])[1]"
    FAVORITE_MENU = By.XPATH, "//button[@ng-reflect-router-link='/wishlist']"
class cart:
    CART_BADGE = By.XPATH, "(//span[@id='mat-badge-content-0'])[1]"
    CHECKOUT_BTN = By.XPATH, "//button[@ng-reflect-router-link='/checkout']"
    CART_MENU = By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[3]"

    NAME = By.XPATH, "//input[@formcontrolname='name']"
    ADDRESS_ONE = By.XPATH, "//input[@placeholder='Address Line 1']"
    ADDRES_TWO = By.XPATH, "//input[@placeholder='Address Line 2']"
    PINCODE = By.XPATH, "//input[@placeholder='Pincode']"
    STATE = By.XPATH, "//input[@placeholder='State']"

    PLACE_ORDER = By.XPATH, "(//span[normalize-space()='Place Order'])[1]"