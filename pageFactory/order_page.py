from selenium.webdriver.support.wait import WebDriverWait
from pageFactory.base_page import BasePage
from pageFactory.locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class OrderPage(BasePage):
    """
    Create Order Page Object
    """
    def enter_email(self, email):
        """
        Enters email
        """
        # Locate Email on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.EMAIL))
        # Enter email value into Email element
        el.send_keys(email)

    def enter_first_name(self, first_name):
        """
        Enters First Name
        """
        # Locate First Name on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.FIRST_NAME))
        # Enter first name value into First Name element
        el.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enters Last Name
        """
        # Locate Last Name on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.LAST_NAME))
        # Enter last name value into Last Name element
        el.send_keys(last_name)

    def enter_address(self, postal_code, city, street):
        """
        Enters address: postal_code, city and street
        """
        # Locate Postal Code on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.POSTAL_CODE))
        # Enter postal code value into Postal Code element
        el.send_keys(postal_code)

        try:
            # Try to locate Postal Code Error on the page, and if yes assert it has proper text
            el1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.POSTAL_CODE_ERROR))
            assert el1.text == "Nie znaleźliśmy miejscowości pod tym kodem pocztowym. Sprawdź czy kod jest poprawny."
            # If Postal Code Error can be located, then locate and enter City With Postal Code Validation Failed
            el2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.CITY_WITH_POSTAL_CODE_VALIDATION_FAILED))
            el2.send_keys(city)
            # If Postal Code Error can be located, then locate and enter Street With Postal Code Validation Failed
            el3 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.STREET_WITH_POSTAL_CODE_VALIDATION_FAILED))
            el3.send_keys(street)
        except:
            # If Postal Code Error cannot be located, then locate and enter City With Postal Code Validation Passed
            el4 = WebDriverWait(self.driver, 10).until(EC.element_attribute_to_include(OrderPageLocators.CITY_WITH_POSTAL_CODE_VALIDATION_PASSED, "value"))
            # If Postal Code Error cannot be located, then locate and enter Street With Postal Code Validation Passed
            el5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.STREET_WITH_POSTAL_CODE_VALIDATION_PASSED))
            el5.click()
            el5.send_keys(street)

    def enter_building_number(self, building_number):
        """
        Enter Building Number
        """
        # Locate Building Number on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.BUILDING_NUMBER))
        # Enter building number value into Building Number element
        el.send_keys(building_number)

    def enter_phone_number(self, phone_number):
        """
        Enters Phone Number
        """
        # Locate Phone Number on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.PHONE_NUMBER))
        # Enter phone number value into Phone Number element
        el.send_keys(phone_number)

    def if_popup_visible_then_close(self):
        """
        Checks if popup is visible, if yes then closes it
        """
        try:
            # Locate Popup Click Zone on the page
            el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.POPUP_CLICK_ZONE))
            # Create ActionChains class instance
            action = ActionChains(self.driver)
            # Move away from Popup Click Zone element and perform the click, to exit the popup
            action.move_to_element(el).move_by_offset(250, 0).click().perform()
        except:
            pass

    def click_go_to_payment_button(self):
        """
        Clicks Go To Payment Button
        """
        # Locate Go To Payment Button on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.GO_TO_PAYMENT_BUTTON))
        # Click Go To Payment Button
        el.click()

    def get_shipping_section_error_list(self):
        """
        Returns Shipping Section Error List
        """
        # Locate Shipping Section Error List on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(OrderPageLocators.SHIPPING_SECTION_ERROR_LIST))
        # Return Shipping Section Error List element
        return el

    def get_shipping_section_error_title(self):
        """
        Return Shipping Section Error Title text
        """
        # Locate Shipping Section Error Title on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.SHIPPING_SECTION_ERROR_TITLE))
        # Return text of Shipping Section Error Title element
        return el.text

    def get_shipping_data_section(self):
        """
        Return Shipping Data Section
        """
        # Locate Shipping Data Section on the page
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.SHIPPING_DATA_SECTION))
        # Return Shipping Data Section element
        return el

    def _verify_page(self):
        """
        Verifies Order Page
        """
        # Get current url address
        page_url = self.driver.current_url
        # Assert that current url equals correct url address
        assert "https://www.castorama.pl/checkout/onepage" == page_url
