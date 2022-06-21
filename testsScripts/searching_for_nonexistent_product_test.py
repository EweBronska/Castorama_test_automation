from testsScripts.base_test import BaseTest


class SearchingForNonExistentProductTest(BaseTest):
    def test_searching_for_nonexistent_product(self):
        """
        TC 002 : User is searching for nonexistent product using search engine
        """
        driver = self.driver
        searched_phrase = self.test_data.searched_phrase_nonexistent
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
        # Proper message informing about no results for searched phrase is displayed
        self.assertEqual("Brak wyników", search_results_page.get_no_results_message_text())
