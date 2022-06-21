from testsScripts.base_test import BaseTest


class AddingProductToCartTest(BaseTest):
    def test_adding_product_to_cart(self):
        """
        TC 004 : User from product page adds the product to cart
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

        # Cart Items Counter is equal to "0", because there is nothing yet in the cart
        self.assertEqual("0", product_page.get_cart_items_counter())
        # Default Product Quantity is equal to "1"
        self.assertEqual("1", product_page.get_product_quantity_value())

        # Add product to cart
        product_page.click_add_to_cart_button()
        # Proper message informing about product successfully added to cart is displayed
        self.assertEqual("Produkt został dodany do koszyka", product_page.get_product_added_to_cart_message_text())
        # Go to Cart
        cart_page = product_page.click_go_to_cart_without_choosing_market()

        # Expected behaviour:
        # Cart Items Counter is updated to "1"
        self.assertEqual("1", cart_page.get_cart_items_counter())
        # Cart contents list has only one position
        self.assertEqual(1, len(cart_page.get_items_in_cart_list()))
        # Title of product in the cart is equal to the title from Product page
        self.assertEqual(opened_product_title, cart_page.get_product_in_cart_title())


