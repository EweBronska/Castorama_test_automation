from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pageFactory.base_page import BasePage
from pageFactory.locators import CartPageLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pageFactory.login_page import LoginPage


class CartPage(BasePage):
    """
    Create Cart Page Object
    """
    def get_cart_items_counter(self):
        """
        Returns Cart Items Counter text
        """
        # Locate Cart Items Counter on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.CART_ITEMS_COUNTER))
        # Return text of Cart Items Counter element
        return el.text

    def get_items_in_cart_list(self):
        """
        Returns Items In Cart List
        """
        # Locate Items In Cart List on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(CartPageLocators.ITEMS_IN_CART_LIST))
        # Return Items In Cart List element
        return el

    def get_product_in_cart_title(self):
        """
        Returns Product In Cart Title text
        """
        # Locate Product In Cart Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_IN_CART_TITLE))
        # Return text of Product In Cart Title element in lower case format
        return el.text.lower()

    def get_product_availability_info(self):
        """
        Returns Product Availability Info text
        """
        # Locate Product Availability Info on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_AVAILABILITY_INFO))
        # Return text of Product Availability Info element
        return el.text

    def get_product_max_available_quantity(self):
        """
        Returns Product Max Available Quantity text
        """
        # Locate Product Max Available Quantity on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_MAX_AVAILABLE_QUANTITY))
        # Return text of Product Max Available Quantity element and separate out the number only
        return el.text.split(" ", 1)[0]

    def get_product_unit_price(self):
        """
        Returns Product Unit Price text
        """
        # Locate Product Unit Price on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_UNIT_PRICE))
        # Return text of Product Unit Price element
        return el.text

    def get_product_total_price(self):
        """
        Returns Product Total Price text
        """
        # Locate Product Total Price on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_TOTAL_PRICE))
        # Return text of Product Total Price element
        return el.text

    def get_product_quantity_value(self):
        """
        Returns Product Quantity Input value
        """
        # Locate Product Quantity Input on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_QUANTITY_INPUT))
        # Return value of Product Quantity Input element
        return el.get_attribute("value")

    def get_market_info_box_text(self):
        """
        Return Market Info Box text
        """
        # Locate Market Info Box on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.MARKET_INFO_BOX))
        # Return text of Market Info Box element
        return el.text

    def clear_and_enter_product_new_quantity(self, product_new_quantity):
        """
        Clears content of Product Quantity Input and enters Product New Quantity
        """
        # Locate Product Quantity Input on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CartPageLocators.PRODUCT_QUANTITY_INPUT))
        # Clear the current content of Product Quantity Input element
        el.click()
        el.send_keys(Keys.DELETE)
        # Enter Product New Quantity into Product Quantity Input element
        el.send_keys(product_new_quantity)

    def get_cart_summary_price(self):
        """
        Returns Cart Summary Price text
        """
        # Locate Cart Summary Price on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.CART_SUMMARY_PRICE))
        # Return text of Cart Summary Price element
        return el.text

    def get_product_quantity_unavailable_message(self):
        """
        Return Product Quantity Unavailable Message text
        """
        # Locate Product Quantity Unavailable Message on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.PRODUCT_QUANTITY_UNAVAILABLE_MESSAGE))
        # Return text of Product Quantity Unavailable Message element
        return el.text

    def click_go_to_order_button(self):
        """
        Click Go To Order Button and return Login Page class instance
        """
        # Locate Go To Order Button on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CartPageLocators.GO_TO_ORDER_BUTTON))
        # Click Go To Order Button element
        el.click()
        # Wait for Login Page to open and display Buy As A Guest Label element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.BUY_AS_A_QUEST_LABEL))
        # Return next page (Login Page)
        return LoginPage(self.driver)

    def if_popup_visible_then_close(self):
        """
        Checks if popup is visible, if yes then closes it
        """
        try:
            # Locate Popup Click Zone on the page
            el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.POPUP_CLICK_ZONE))
            # Create ActionChains class instance
            action = ActionChains(self.driver)
            # Move away from Popup Click Zone element and perform the click, to exit the popup
            action.move_to_element(el).move_by_offset(250, 0).click().perform()
        except:
            pass

    def _verify_page(self):
        """
        Verifies Cart Page
        """
        # Get current url address
        page_url = self.driver.current_url
        # Assert that current url equals correct url address
        assert "https://www.castorama.pl/checkout/cart" == page_url
