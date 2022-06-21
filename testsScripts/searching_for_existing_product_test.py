from testsScripts.base_test import BaseTest


class SearchingForExistingProductTest(BaseTest):
    def test_searching_for_existing_product(self):
        """
        TC 001 : User is searching for existing product using search engine
        """
        driver = self.driver
        searched_phrase = self.test_data.searched_phrase_existing
        # Enter home page
        home_page = self.home_page
        # Accept cookie settings
        home_page.click_accept_cookies_button()
        # Enter searched phrase into search engine
        home_page.enter_searched_phrase(searched_phrase)
        # Click search button
        search_results_page = home_page.click_search_button()

        # Expected behaviour:
        # Searched Title Text contains searched phrase
        self.assertEqual("Wyniki wyszukiwania hasła: " + searched_phrase, search_results_page.get_searched_title())
        # Current url title contains searched phrase
        self.assertEqual("www.castorama.pl - " + searched_phrase, driver.title)
        # Searched Product First Title contains searched phrase
        searched_words_list = searched_phrase.split(" ")
        searched_product_first_title = search_results_page.get_searched_product_first_title()
        for element in searched_words_list:
            self.assertIn(element, searched_product_first_title)

