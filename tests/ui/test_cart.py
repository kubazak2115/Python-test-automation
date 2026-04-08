import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from conftest import BASE_URL

# fixtures
@pytest.fixture
def inventory(logged_in_driver):
    return InventoryPage(logged_in_driver, BASE_URL)

@pytest.fixture
def cart(logged_in_driver):
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()
    return CartPage(logged_in_driver, BASE_URL)

#basic tests
@pytest.mark.smoke
@pytest.mark.ui
def test_cart_is_empty_on_load(logged_in_driver):
    """ should show empty cart when no items added """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.go_to_cart()
    cart = CartPage(logged_in_driver, BASE_URL)
    assert cart.is_empty()

@pytest.mark.smoke
@pytest.mark.ui
def test_add_one_item_updates_cart_badge(inventory):
    """ should update cart badge to 1 after adding one item """
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == 1

# @pytest.mark.smoke
# @pytest.mark.ui
# def test_add_multiple_items_updates_cart_badge(inventory):
#     """ should update cart badge to correct count after adding multiple items """
#     inventory.add_item_to_cart_by_index(0)
#     inventory.add_item_to_cart_by_index(1)  
#     inventory.add_item_to_cart_by_index(2)
#     print(inventory.get_cart_count())
#     assert inventory.get_cart_count() == 3

@pytest.mark.smoke
@pytest.mark.ui
def test_cart_page_shows_added_items(logged_in_driver):
    """ should show correct items in cart after adding from inventory """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    first_product = inventory.get_product_names()[0]
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver, BASE_URL)
    assert first_product in cart.get_item_names()

@pytest.mark.smoke
@pytest.mark.ui
def test_cart_title_is_your_cart(cart):
    """ should show 'your cart' title on cart page """
    assert cart.get_title() == "Your Cart"

# remove items tests
# @pytest.mark.smoke
# @pytest.mark.ui
# def test_remove_item_decreases_badge(logged_in_driver):
#     """ should decrease cart badge count after removing item from cart """
#     inventory = InventoryPage(logged_in_driver, BASE_URL)
#     inventory.add_item_to_cart_by_index(0)
#     inventory.add_item_to_cart_by_index(1)
#     inventory.go_to_cart()

#     cart = CartPage(logged_in_driver, BASE_URL)
#     cart.remove_item_by_index(0)

#     assert inventory.get_cart_count() == 1

@pytest.mark.smoke
@pytest.mark.ui
def test_remove_all_items_clears_cart(logged_in_driver):
    """ should show empty cart after removing all items """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.add_item_to_cart_by_index(0)
    inventory.add_item_to_cart_by_index(1)
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver, BASE_URL)
    cart.remove_all_items()

    assert cart.is_empty() 

@pytest.mark.smoke
@pytest.mark.ui
def test_removed_item_no_longer_in_cart(logged_in_driver):
    """ should not show removed item in cart """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    first_product = inventory.get_product_names()[0]
    inventory.add_item_to_cart_by_index(0)
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver, BASE_URL)
    cart.remove_item_by_index(0)

    assert first_product not in cart.get_item_names()

# navigation tests
@pytest.mark.smoke
@pytest.mark.ui
def test_continue_shopping_goes_back_to_inventory(logged_in_driver):
    """ should navigate back to inventory page after clicking continue shopping """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.add_item_to_cart_by_index(0)
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver, BASE_URL)
    cart.continue_shopping()

    assert inventory.get_page_title() == "Products"

@pytest.mark.smoke
@pytest.mark.ui
def test_cart_persists_after_navigation(logged_in_driver):
    """ should keep items in cart after navigating back and forth """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.add_item_to_cart_by_index(0)
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver, BASE_URL)
    assert cart.get_item_count() == 1

    cart.continue_shopping()
    inventory.go_to_cart()

    assert cart.get_item_count() == 1