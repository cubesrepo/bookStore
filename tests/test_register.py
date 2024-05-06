import pytest

from pages.register_page import RegisterPage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class TestRegister(BaseTest):

    def test_register_with_valid_values(self, driver):
        registerpage = RegisterPage(driver)
        registerpage.verify_register_with_valid_value_then_login()