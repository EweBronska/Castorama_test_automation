from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pageFactory.base_page import BasePage
from pageFactory.locators import LoginPageLocators, OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pageFactory.order_page import OrderPage


class LoginPage(BasePage):
    """
    Create Login Page Object
    """
    def if_popup_visible_then_close(self):
        """
        Checks if popup is visible, if yes then closes it
        """
        try:
            # Locate Popup Click Zone on the page
            el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.POPUP_CLICK_ZONE))
            # Create ActionChains class instance
            action = ActionChains(self.driver)
            # Move away from Popup Click Zone element and perform the click, to exit the popup
            action.move_to_element(el).move_by_offset(250, 0).click().perform()
        except:
            pass

    def click_buy_as_a_guest_button(self):
        """
        Clicks Buy As A Guest Button and returns Order Page instance
        """
        # Locate Buy As A Guest Button on the page
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.BUY_AS_A_GUEST_BUTTON))
        # Click Buy As A Guest Button element
        el.click()
        # Wait for Order Page to open and display Shipping Data Section element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.SHIPPING_DATA_SECTION))
        # Return next page (Order Page)
        return OrderPage(self.driver)

    def _verify_page(self):
        """
        Verifies Login Page
        """
        # Get current url address
        page_url = self.driver.current_url
        # Assert that current url equals correct url address
        assert "https://www.castorama.pl/customer/account/login?type=checkout" == page_url


