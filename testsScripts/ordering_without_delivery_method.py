from testsScripts.base_test import BaseTest


class OrderingWithoutDeliveryMethodTest(BaseTest):
    def test_ordering_without_delivery_method(self):
        """
        TC 007 : User places an order as a quest without providing information about delivery method
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
        # Add product to cart
        product_page.click_add_to_cart_button()
        # Select the market
        product_page.click_select_market_button()
        product_page.enter_into_select_market_input(self.test_data.market_location)
        product_page.click_market_result_first()
        # Go to Cart
        cart_page = product_page.click_go_to_cart_with_market_chosen()
        # If popup visible on Cart page then close it
        cart_page.if_popup_visible_then_close()
        # Go to order
        login_page = cart_page.click_go_to_order_button()
        # If popup visible on Login page then close it
        login_page.if_popup_visible_then_close()
        # Choose buy as a quest option
        order_page = login_page.click_buy_as_a_guest_button()
        # If popup visible on Order page then close it
        order_page.if_popup_visible_then_close()
        # Enter email
        order_page.enter_email(self.test_data.email)
        # Enter first name
        order_page.enter_first_name(self.test_data.first_name)
        # Enter last name
        order_page.enter_last_name(self.test_data.last_name)
        # Enter address (postal code, city and street)
        order_page.enter_address(self.test_data.postal_code, self.test_data.city, self.test_data.street)
        # Enter building number
        order_page.enter_building_number(self.test_data.building_number)
        # Enter phone number
        order_page.enter_phone_number(self.test_data.phone_number)
        # If popup visible on Order page then close it
        order_page.if_popup_visible_then_close()
        # Go to payment
        order_page.click_go_to_payment_button()

        # Expected behaviour:
        # There is only one error type visible
        self.assertEqual(1, len(order_page.get_shipping_section_error_list()))
        # Error type displayed informs the User about not selecting the delivery method
        self.assertEqual("Nie wybrano metody dostawy", order_page.get_shipping_section_error_title())
        # Shipping data section is still displayed, next step of the form is not opened yet
        self.assertTrue(order_page.get_shipping_data_section().is_displayed())
