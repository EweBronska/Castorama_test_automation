from testsScripts.base_test import BaseTest


class DisplayingProductPage(BaseTest):
    def test_displaying_product_page(self):
        """
        TC 003 : User enters product page by clicking on search engine result item
        """
        driver = self.driver
        # Enter home page
        home_page = self.home_page
        # Accept cookie settings
        home_page.click_accept_cookies_button()
        # Enter searched phrase into search engine
        home_page.enter_searched_phrase(self.test_data.searched_phrase_existing)
        # Click search button
        search_results_page = home_page.click_search_button()
        searched_product_link = search_results_page.get_searched_product_first_title_link()
        searched_product_title = search_results_page.get_searched_product_first_title()
        # Enter first product on the results list
        product_page = search_results_page.click_on_searched_product_first_title()

        # Expected behaviour:
        # Current url is equal to searched product link from Search Results page
        self.assertEqual(searched_product_link, driver.current_url)
        # Title of the product opened is equal to the title from Search Results page
        self.assertEqual(searched_product_title, product_page.get_opened_product_title())

