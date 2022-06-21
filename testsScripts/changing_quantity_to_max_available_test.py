from testsScripts.base_test import BaseTest
import time


class ChangingQuantityToMaxAvailableTest(BaseTest):
    def test_changing_quantity_to_max_available(self):
        """
        TC 005 : User changes quantity of the product added to the cart to max quantity available in the chosen market
        """
        # Enter home page
        home_page = self.home_page
        # Accept cookie settings
        home_page.click_accept_cookies_button()
        # Enter searched phrase into search engine
        home_page.enter_searched_phrase(self.test_data.searched_phrase_existing)
        # Click search button
        search_results_page = home_page.click_search_button()
        # Enter first product on the results list
        product_page = search_results_page.click_on_searched_product_first_title()
        opened_product_title = product_page.get_opened_product_title()
        # Add product to cart
        product_page.click_add_to_cart_button()
        # Select the market
        product_page.click_select_market_button()
        product_page.enter_into_select_market_input(self.test_data.market_location)
        self.assertEqual(self.test_data.market_location, product_page.get_market_result_first())
        product_page.click_market_result_first()
        # Go to cart
        cart_page = product_page.click_go_to_cart_with_market_chosen()

        # Market location visible in left top corner of the page is equal to market chosen in previous step
        self.assertEqual(self.test_data.market_location, cart_page.get_market_info_box_text())
        # Cart Item Counter is equal to "1"
        self.assertEqual("1", cart_page.get_cart_items_counter())
        # Title of product in the cart is equal to the title from Product page
        self.assertEqual(opened_product_title, cart_page.get_product_in_cart_title())
        # Product in cart is marked as "Available"
        self.assertEqual("Dostępny", cart_page.get_product_availability_info())
        # Default Product Quantity is equal to "1"
        self.assertEqual("1", cart_page.get_product_quantity_value())
        # Product Unit Price is equal to Total Price, because the quantity is "1"
        self.assertEqual(cart_page.get_product_unit_price(), cart_page.get_product_total_price())

        # If popup visible on Cart page then close it
        cart_page.if_popup_visible_then_close()
        # Change product quantity into max available in chosen market
        max_available_quantity = cart_page.get_product_max_available_quantity()
        cart_page.clear_and_enter_product_new_quantity(max_available_quantity)
        product_new_quantity = cart_page.get_product_quantity_value()
        time.sleep(5)

        # Expected behaviour:
        # New product quantity is equal to max quantity available in chosen market
        self.assertEqual(max_available_quantity, product_new_quantity)
        time.sleep(5)
        # Cart Items Counter is updated to product max available quantity
        self.assertEqual(product_new_quantity, cart_page.get_cart_items_counter())
        # Cart contents list has still only one position
        self.assertEqual(1, len(cart_page.get_items_in_cart_list()))

        product_unit_price_float = float(cart_page.get_product_unit_price().replace(",", "."))
        product_total_price_float = float(cart_page.get_product_total_price().replace(",", "."))
        product_new_quantity_float = float(product_new_quantity.replace(",", "."))
        cart_summary_price_float = float(cart_page.get_cart_summary_price().replace(",", "."))
        # Product Total Price is equal to Unit Price multiplied by product new quantity
        self.assertEqual((product_unit_price_float * product_new_quantity_float).__round__(2), product_total_price_float)
        # Product Total Price is equal to Cart Summary Price
        self.assertEqual(product_total_price_float, cart_summary_price_float)


