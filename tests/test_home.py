import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestHome(BaseTest):

    def test_home_page_favorite_functionality(self, driver):
        homepage = HomePage(driver)
        homepage.verify_favorite_functionality()