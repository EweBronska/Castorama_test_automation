import unittest
from testsScripts.searching_for_existing_product_test import SearchingForExistingProductTest
from testsScripts.searching_for_nonexistent_product_test import SearchingForNonExistentProductTest
from testsScripts.adding_product_to_cart_test import AddingProductToCartTest
from testsScripts.displaying_product_page_test import DisplayingProductPage
from testsScripts.changing_quantity_to_max_available_test import ChangingQuantityToMaxAvailableTest
from testsScripts.changing_quantity_to_unavailable_test import ChangingQuantityToUnavailableTest
from testsScripts.ordering_without_delivery_method import OrderingWithoutDeliveryMethodTest

# Loading tests to execute
searching_for_existing_product_test = unittest.TestLoader().loadTestsFromTestCase(SearchingForExistingProductTest)
searching_for_nonexistent_product_test = unittest.TestLoader().loadTestsFromTestCase(SearchingForNonExistentProductTest)
adding_product_to_cart_test = unittest.TestLoader().loadTestsFromTestCase(AddingProductToCartTest)
displaying_product_page_test = unittest.TestLoader().loadTestsFromTestCase(DisplayingProductPage)
changing_quantity_to_max_available_test = unittest.TestLoader().loadTestsFromTestCase(ChangingQuantityToMaxAvailableTest)
changing_quantity_to_unavailable_test = unittest.TestLoader().loadTestsFromTestCase(ChangingQuantityToUnavailableTest)
ordering_without_delivery_method_test = unittest.TestLoader().loadTestsFromTestCase(OrderingWithoutDeliveryMethodTest)

# Creating list of tests to be executed
tests_for_run = [
    searching_for_existing_product_test,
    searching_for_nonexistent_product_test,
    displaying_product_page_test,
    adding_product_to_cart_test,
    changing_quantity_to_max_available_test,
    changing_quantity_to_unavailable_test,
    ordering_without_delivery_method_test
    ]

# Creating Test Suite to connect tests
test_suite = unittest.TestSuite(tests_for_run)

# Executing tests
unittest.TextTestRunner().run(test_suite)