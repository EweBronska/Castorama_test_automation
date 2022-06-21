from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageFactory.base_page import BasePage
from pageFactory.locators import HomePageLocators
from pageFactory.search_results_page import SearchResultsPage


class HomePage(BasePage):
    """
    Landing Page Object
    """
    def click_accept_cookies_button(self):
        """
        Clicks Accept Cookies Button
        """
        # Locate Accept Cookies Button
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.ACCEPT_COOKIES_BUTTON))
        # Click Accept Cookies Button element
        el.click()

    def enter_searched_phrase(self, searched_phrase):
        """
        Enters Searched Phrase into Search Engine Input field
        """
        # Locate Search Engine Input on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.SEARCH_ENGINE_INPUT))
        # Enter Searched Phrase into Search Engine Input element
        el.send_keys(searched_phrase)

    def click_search_button(self):
        """
        Clicks Search Button and returns Search Results Page instance
        """
        # Locate Search Button on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.SEARCH_BUTTON))
        # Click Search Button element
        el.click()
        # Return next page (SearchResultsPage)
        return SearchResultsPage(self.driver)

    def _verify_page(self):
        """
        Verifies Home Page
        """
        # Get current url address
        page_url = self.driver.current_url
        # Assert that current url equals correct url address
        assert "https://www.castorama.pl/" == page_url

