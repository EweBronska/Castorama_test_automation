from selenium.webdriver.common.by import By


class HomePageLocators():
    """
    Locators used on Home Page
    """
    SEARCH_ENGINE_INPUT = (By.ID, "search-input-desktop")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search_mini_formdesktop"]/button')
    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//*[@class="cookie-bar__buttons"]/button')

class SearchResultsPageLocators():
    """
    Locators used on Search Results Page
    """
    SEARCHED_TITLE = (By.XPATH, '//*[@id="main-gsa-header"]/div[1]/h1')
    SEARCHED_PRODUCT_FIRST_TITLE = (By.XPATH, '//*[@class="row products-grid"]/li[1]/div/h2/a')
    NO_RESULTS_MESSAGE = (By.XPATH, '//*[@id="message-wrapper"]//h1')

class ProductPageLocators():
    """
    Locators used on Product Page
    """
    OPENED_PRODUCT_TITLE = (By.XPATH, '//*[@class="product-main-data col-12 col-md-8 col-lg-7"]/h1')
    PRODUCT_QUANTITY_INPUT = (By.XPATH, '//*[@class="add-to-cart-or-wishlist-with-qty product-page-sidebar__action-button"]/input')
    CART_ITEMS_COUNTER = (By.XPATH, '//*[@class="cart-header"]/a/span')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@class="add-to-cart-or-wishlist-with-qty product-page-sidebar__action-button"]/button ')
    PRODUCT_ADDED_TO_CART_MESSAGE = (By.XPATH, '//*[@class="cart-popup-content__header--message"]')
    SELECT_MARKET_BUTTON = (By.XPATH, '//*[@class="input-chosen market-selectable-input__select input-chosen--static input-chosen--cart"]/button')
    SELECT_MARKET_INPUT = (By.XPATH, '//*[@class="input-base input-chosen__box--choose"]')
    MARKET_RESULT_FIRST = (By.XPATH, '//*[@class="input-chosen__box--list"]/li[1]/button/span')
    GO_TO_CART_BUTTON_WITHOUT_CHOOSING_MARKET = (By.XPATH, '//*[@class="choose-market__content--go-to-cart"]/a')
    GO_TO_CART_BUTTON_WITH_MARKET_CHOSEN = (By.XPATH, '//*[@class="cart-popup-content__header--add-to-cart"]/a')

class CartPageLocators():
    """
    Locators used on Cart Page
    """
    CART_LABEL = (By.XPATH, '//*[@class="heading-base heading-base--h2"]')
    CART_ITEMS_COUNTER = (By.XPATH, '//*[@class="cart-header"]/a/span')
    ITEMS_IN_CART_LIST = (By.XPATH, '//*[@class="checkout-cart-product checkout-cart-item"]')
    PRODUCT_IN_CART_TITLE = (By.XPATH, '//*[@class="product-info__details"]/h5/a')
    PRODUCT_AVAILABILITY_INFO = (By.XPATH, '//*[@class="availability-text availability-text--in checkout-cart-product__availability-text"]')
    PRODUCT_MAX_AVAILABLE_QUANTITY = (By.XPATH, '//*[@class="checkout-cart-product__availability-information"]')
    PRODUCT_QUANTITY_INPUT = (By.XPATH, '//*[@class="integer-input integer-input--cart"]/input')
    PRODUCT_UNIT_PRICE = (By.XPATH, '//*[@class="checkout-cart-product__cell checkout-cart-product__unit-price"]/div/div[1]/span[1]')
    PRODUCT_TOTAL_PRICE = (By.XPATH, '//*[@class="checkout-cart-product__cell checkout-cart-product__price"]/div/div/span[1]')
    MARKET_INFO_BOX = (By.XPATH, '//*[@class="market-info-box"]/p')
    CART_SUMMARY_PRICE = (By.XPATH, '//*[@class="checkout-cart-summary-old__details-price"]/section/span[1]')
    PRODUCT_QUANTITY_UNAVAILABLE_MESSAGE = (By.XPATH, '//*[@class="tooltip-rectangle__content"]')
    GO_TO_ORDER_BUTTON = (By.XPATH, '//*[@class="button-base checkout-cart-summary-old__go-to-order-button button-base--horizontal button-base--deep-canynon"]')
    POPUP_CLICK_ZONE = (By.XPATH, '//*[@id="dws-shop-popup-mask"][1]/div/a')

class LoginPageLocators():
    BUY_AS_A_QUEST_LABEL = (By.XPATH, '//*[@class="section-base login-page__form-wrapper"]/h4')
    BUY_AS_A_GUEST_BUTTON = (By.XPATH, '//*[@class="section-base login-page__form-wrapper"]/a')
    POPUP_CLICK_ZONE = (By.XPATH, '//*[@id="dws-shop-popup-mask"][1]/div/a')

class OrderPageLocators():
    EMAIL = (By.ID, "email")
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    COUNTRY = (By.ID, "country")
    POSTAL_CODE = (By.ID, "zipCode")
    POSTAL_CODE_ERROR = (By.XPATH, '//*[@class="form-builder-input-wrapper multistep-checkout-shipping-data-form__input-wrapper multistep-checkout-shipping-data-form__input-wrapper--zip-code"]/div/span')
    CITY_WITH_POSTAL_CODE_VALIDATION_PASSED = (By.ID, "city")
    CITY_WITH_POSTAL_CODE_VALIDATION_FAILED = (By.XPATH, '//*[@id="shippingDataForm"]/form/div[6]/div/div/input')
    STREET_WITH_POSTAL_CODE_VALIDATION_PASSED = (By.ID, "street")
    STREET_WITH_POSTAL_CODE_VALIDATION_FAILED = (By.XPATH, '//*[@id="shippingDataForm"]/form/div[7]/div/div/input')
    BUILDING_NUMBER = (By.ID, "buildingNumber")
    PHONE_NUMBER = (By.ID, "areaCodeWithPhone")
    GO_TO_PAYMENT_BUTTON = (By.XPATH, '//*[@class="multistep-checkout-step-footer"]/button')
    SHIPPING_SECTION_ERROR_LIST = (By.XPATH, '//*[@class="validation-section validation-section--in-one-column multistep-checkout__validation-section multistep-checkout__validation-section--shipping"]/div')
    SHIPPING_SECTION_ERROR_TITLE = (By.XPATH, '//*[@class="base-text base-text--line-height-normal validation-section-block__title"]')
    SHIPPING_DATA_SECTION = (By.ID, "shippingDataSection")
    POPUP_CLICK_ZONE = (By.XPATH, '//*[@id="dws-shop-popup-mask"][1]/div/a')
