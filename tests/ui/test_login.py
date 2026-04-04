import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from conftest import BASE_URL, VALID_USER, VALID_PASSWORD, LOCKED_USER, PROBLEM_USER

# website load

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver, BASE_URL)
    page.open()
    return page

# positive tests

@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login_redirects_to_inventory_page(login_page):
    """ should redirect to inventory.html after valid login """
    login_page.login(VALID_USER, VALID_PASSWORD)
    assert login_page.is_on_inventory_page(), (
    "User should be redirected to inventory page after valid login"
    )

@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login_shows_products_page_title(login_page, driver):
    """ should show 'products' title after valid login """
    login_page.login(VALID_USER, VALID_PASSWORD)
    inventory = InventoryPage(driver, BASE_URL)
    assert inventory.get_title() == "Products"

# negative tests

@pytest.mark.regression
@pytest.mark.ui
def test_empty_credentials_shows_error(login_page):
    """ should show error message when username and password are empty """
    login_page.click_login()
    assert login_page.is_error_visible()
    assert "Username is required" in login_page.get_error_message()

@pytest.mark.regression
@pytest.mark.ui
def test_wrong_password_shows_error(login_page):
    """ should show error message when password wrong """
    login_page.login(VALID_USER, "wrong_password")
    assert login_page.is_error_visible()
    assert "Username and password do not match" in login_page.get_error_message()

@pytest.mark.regression
@pytest.mark.ui
def test_nonexistent_user_shows_error(login_page):
    """ should show error message when username nonexistent """
    login_page.login("niemamnie", VALID_PASSWORD)
    assert login_page.is_error_visible()
    assert "Username and password do not match" in login_page.get_error_message()

@pytest.mark.regression
@pytest.mark.ui
def test_locked_out_user_shows_error(login_page):
    """ should show error message when user is locked out """
    login_page.login(LOCKED_USER, VALID_PASSWORD)
    assert login_page.is_error_visible()
    assert "locked out" in login_page.get_error_message()

@pytest.mark.regression
@pytest.mark.ui
def test_empty_username_shows_error(login_page):
    """ should show error message when username is empty """
    login_page.login("", VALID_PASSWORD)
    assert login_page.is_error_visible()
    assert "Username is required" in login_page.get_error_message()

@pytest.mark.regression
@pytest.mark.ui
def test_empty_password_shows_error(login_page):
    """ should show error message when password is empty """
    login_page.login(VALID_USER, "")
    assert login_page.is_error_visible()
    assert "Password is required" in login_page.get_error_message()

# session management tests

@pytest.mark.regression
@pytest.mark.ui
def test_cannot_access_inventory_without_login(driver):
    """ should not access inventory page without login """
    inventory = InventoryPage(driver, BASE_URL)
    inventory.open()
    assert "inventory" not in driver.current_url, (
    "User should not access inventory page without login"
    )

@pytest.mark.regression
@pytest.mark.ui
def test_logout_redirects_to_login_page(logged_in_driver):
    """ should redirect to login page after logout """
    inventory = InventoryPage(logged_in_driver, BASE_URL)
    inventory.logout()
    assert "saucedemo.com" in inventory.driver.current_url 
    assert "inventory" not in inventory.driver.current_url 