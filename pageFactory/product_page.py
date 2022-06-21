from selenium.webdriver.support.wait import WebDriverWait
from pageFactory.base_page import BasePage
from pageFactory.locators import ProductPageLocators, CartPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pageFactory.cart_page import CartPage


class ProductPage(BasePage):
    """
    Create Product Page Object
    """
    def get_opened_product_title(self):
        """
        Returns Opened Product Title text
        """
        # Locate Opened Product Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductPageLocators.OPENED_PRODUCT_TITLE))
        # Return text of Opened Product Title element in lower case format
        return el.text.lower()

    def get_product_quantity_value(self):
        """
        Returns Product Quantity Input value
        """
        # Locate Product Quantity Input on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_QUANTITY_INPUT))
        # Return value attribute of Product Quantity Input element
        return el.get_attribute("value")

    def get_cart_items_counter(self):
        """
        Returns Cart Items Counter text
        """
        # Locate Cart Items Counter on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductPageLocators.CART_ITEMS_COUNTER))
        # Return text of Cart Items Counter element
        return el.text

    def click_add_to_cart_button(self):
        """
        Clicks Add To Cart Button
        """
        # Locate Add To Cart Button on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        # Click Add To Cart Button
        el.click()

    def get_product_added_to_cart_message_text(self):
        """
        Returns Product Added To Cart Message text
        """
        # Locate Product Added To Cart Message on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_ADDED_TO_CART_MESSAGE))
        # Return text of Product Added To Cart Message element
        return el.text

    def click_select_market_button(self):
        """
        Clicks Select Market Button
        """
        # Locate Select Market Button on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProductPageLocators.SELECT_MARKET_BUTTON))
        # Click Select Market Button element
        el.click()

    def enter_into_select_market_input(self, market):
        """
        Enters Market into Select Market Input
        """
        # Locate Select Market Input on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductPageLocators.SELECT_MARKET_INPUT))
        # Enters Market into Select Market Input element
        el.send_keys(market)

    def get_market_result_first(self):
        """
        Returns Market Result First text
        """
        # Locate Market Result First on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProductPageLocators.MARKET_RESULT_FIRST))
        # Return text of Market Result First element
        return el.text

    def click_market_result_first(self):
        """
        Clicks Market Result First
        """
        # Locate Market Result First on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProductPageLocators.MARKET_RESULT_FIRST))
        # Click Market Result First element
        el.click()

    def click_go_to_cart_without_choosing_market(self):
        """
        Clicks Go To Cart Button Without Choosing Market and returns Cart Page instance
        """
        # Locate Go To Cart Button Without Choosing Market on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProductPageLocators.GO_TO_CART_BUTTON_WITHOUT_CHOOSING_MARKET))
        # Click Go To Cart Button Without Choosing Market element
        el.click()
        # Wait for Cart Page to open and display Cart Label element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.CART_LABEL))
        # Return next page (Cart Page)
        return CartPage(self.driver)

    def click_go_to_cart_with_market_chosen(self):
        """
        Clicks Go To Cart Button With Market Chosen and returns Cart Page instance
        """
        # Locate Go To Cart Button With Market Chosen on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProductPageLocators.GO_TO_CART_BUTTON_WITH_MARKET_CHOSEN))
        # Click Go To Cart Button With Market Chosen element
        el.click()
        # Wait for Cart Page to open and display Cart Label element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.CART_LABEL))
        # Return next page (Cart Page)
        return CartPage(self.driver)


