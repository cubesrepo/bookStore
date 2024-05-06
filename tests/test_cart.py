import pytest

from pages.cart_page import CartPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class TestCart(BaseTest):

    def test_add_to_cart_all_products_in_favorites(self, driver):
        cartpage = CartPage(driver)
        cartpage.add_to_cart_all_products_in_favorites()
    def test_checkout_all_products(self, driver):
        cartpage = CartPage(driver)
        cartpage.checkout_all_products()