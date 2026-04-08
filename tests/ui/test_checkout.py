import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from conftest import BASE_URL

# fixtures
@pytest.fixture
def checkout(logged_in_driver):
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver, BASE_URL)
    cart.proceed_to_checkout()
    return CheckoutPage(logged_in_driver, BASE_URL)

# step 1
@pytest.mark.smoke
@pytest.mark.ui
def test_valid_info_proceeds_to_step_two(checkout, logged_in_driver):
    """ should proceed to step two after entering valid info """
    checkout.fill_info("John", "Doe", "12345")
    checkout.click_continue()
    assert checkout.is_on_step_two()

@pytest.mark.smoke
@pytest.mark.ui
def test_empty_first_name_shows_error(checkout):
    """ should show error when checkout info is empty """
    checkout.fill_info("", "Doe", "12345")
    checkout.click_continue()

    assert checkout.is_error_visible()
    assert "First Name is required" in checkout.get_error_message()

@pytest.mark.smoke
@pytest.mark.ui
def test_empty_last_name_shows_error(checkout):
    """ should show error when last name is empty """
    checkout.fill_info("John", "", "12345")
    checkout.click_continue()

    assert checkout.is_error_visible()
    assert "Last Name is required" in checkout.get_error_message()

@pytest.mark.smoke
@pytest.mark.ui
def test_empty_postal_code_shows_error(checkout):
    """ should show error when postal code is empty """
    checkout.fill_info("John", "Doe", "")
    checkout.click_continue()

    assert checkout.is_error_visible()
    assert "Postal Code is required" in checkout.get_error_message()

@pytest.mark.smoke
@pytest.mark.ui
def test_all_fields_empty_shows_error(checkout):
    """ should show error when all fields are empty """
    checkout.fill_info("", "", "")
    checkout.click_continue()

    assert checkout.is_error_visible()
    assert "First Name is required" in checkout.get_error_message()

# step 2
@pytest.mark.smoke
@pytest.mark.ui
def test_item_total_tax_and_total_calculated_correctly(checkout):
    """ should show correct item total, tax and total on step two """
    checkout.fill_info("John", "Doe", "12345")
    checkout.click_continue()

    item_total = checkout.get_item_total()
    tax = checkout.get_tax()
    total = checkout.get_total()

    assert abs((item_total + tax) - total) < 0.01  # round error 

@pytest.mark.smoke
@pytest.mark.ui
def test_finish_button_completes_order(checkout):
    """ should complete order and show confirmation message """
    checkout.fill_info("John", "Doe", "12345")
    checkout.click_continue()
    checkout.click_finish()

    assert checkout.is_order_confirmed()

@pytest.mark.smoke
@pytest.mark.ui
def test_confirmation_message_shown_after_order(checkout):
    """ should show confirmation message after completing order """
    checkout.fill_info("John", "Doe", "12345")
    checkout.click_continue()
    checkout.click_finish()

    assert "Thank you" in checkout.get_confirmation_message()

#e2e flow
@pytest.mark.smoke
@pytest.mark.ui
def test_checkout_flow(logged_in_driver):
    """ should complete checkout flow successfully """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    first_product = inventory.get_product_names()[0]
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == 1

    inventory.go_to_cart()
    cart = CartPage(logged_in_driver, BASE_URL)
    assert first_product in cart.get_item_names()

    cart.proceed_to_checkout()
    checkout = CheckoutPage(logged_in_driver, BASE_URL)
    checkout.fill_info("John", "Doe", "12345")
    checkout.click_continue()

    assert checkout.is_on_step_two()
    assert checkout.get_item_total() > 0

    checkout.click_finish()
    assert "Thank you" in checkout.get_confirmation_message()

@pytest.mark.smoke
@pytest.mark.ui
def test_back_home_after_purchase(checkout):
    """ should go back to inventory page after completing order and clicking back home """
    checkout.fill_info("John", "Doe", "12345")
    checkout.click_continue()
    checkout.click_finish()
    checkout.go_back_home()

    assert checkout.is_on_inventory_page()