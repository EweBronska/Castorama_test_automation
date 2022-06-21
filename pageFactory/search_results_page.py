from selenium.webdriver.support.wait import WebDriverWait
from pageFactory.base_page import BasePage
from pageFactory.locators import SearchResultsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pageFactory.product_page import ProductPage


class SearchResultsPage(BasePage):
    """
    Create Search Results Page Object
    """
    def get_searched_title(self):
        """
        Returns Searched Title text
        """
        # Locate Searched Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SearchResultsPageLocators.SEARCHED_TITLE))
        # Return text of Searched Title element
        return el.text

    def get_searched_product_first_title(self):
        """
        Returns Searched Product First Title text
        """
        # Locate Searched Product First Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SearchResultsPageLocators.SEARCHED_PRODUCT_FIRST_TITLE))
        # Return text of Searched Product First Title element in lower case format
        return el.text.lower()

    def get_searched_product_first_title_link(self):
        """
        Returns Searched Product First Title link
        """
        # Locate Searched Product First Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SearchResultsPageLocators.SEARCHED_PRODUCT_FIRST_TITLE))
        # Return href attribute of Searched Product First Title element
        return el.get_attribute("href")

    def get_no_results_message_text(self):
        """
        Returns No Results Message text
        """
        # Locate No Results Message on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SearchResultsPageLocators.NO_RESULTS_MESSAGE))
        # Return text of No Results Message element
        return el.text

    def click_on_searched_product_first_title(self):
        """
        Clicks on Searched Product First Title and returns Product Page instance
        """
        # Locate Searched Product First Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(SearchResultsPageLocators.SEARCHED_PRODUCT_FIRST_TITLE))
        # Click on Searched Product First Title element
        el.click()
        # Return next page (Product Page)
        return ProductPage(self.driver)

    def _verify_page(self):
        """
        Verifies Search Results Page
        """
        # Get current url address
        page_url = self.driver.current_url
        # Assert that current url starts with correct url address
        assert page_url.startswith("https://www.castorama.pl/result/?q=")
