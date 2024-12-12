import os
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, pytestconfig):
    base_url = pytestconfig.getoption("base_url")
    context = browser.new_context(viewport={"width":1920, "height":1080})
    page = context.new_page()
    page.goto(base_url)
    yield page
    context.close()

@pytest.fixture(scope="session", autouse=True)
def load_user_env():
    env_path = os.path.join('config', 'env', 'users.env')
    success = load_dotenv(dotenv_path=env_path)
    if not success:
        raise FileNotFoundError(f"Could not load env file from {env_path}")

@pytest.fixture
def user_creds():
    return {
        "standard_user": os.getenv('STANDARD_USER'),
        "locked_user": os.getenv('LOCKED_USER'),
        "problem_user": os.getenv('PROBLEM_USER'),
        "performance_user": os.getenv('PERFORMANCE_USER'),
        "error_user": os.getenv('ERROR_USER'),
        "visual_user": os.getenv('VISUAL_USER'),
        "password": os.getenv('PASSWORD')
    }

@pytest.fixture
def product_titles():
    return {
        "backpack": "Sauce Labs Backpack",
        "bike_light": "Sauce Labs Bike Light",
        "bolt_shirt": "Sauce Labs Bolt T-Shirt",
        "jacket": "Sauce Labs Fleece Jacket",
        "onesie": "Sauce Labs Onesie",
        "all_things_shirt": "Test.allTheThings() T-Shirt (Red)"
    }

@pytest.fixture
def product_descriptions():
    return {
        "backpack": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled "
        "laptop and tablet protection.",
        "bike_light": "A red light isn't the desired state in testing but it sure helps when riding your bike at "
                      "night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        "bolt_shirt": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed "
        "cotton, heather gray with red bolt.",
        "jacket": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything "
        "from a relaxing day outdoors to a busy day at the office.",
        "onesie": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, "
        "two-needle hemmed sleeved and bottom won't unravel.",
        "all_things_shirt": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. "
        "Super-soft and comfy ringspun combed cotton."
    }

@pytest.fixture
def product_prices():
    return {
        "backpack": "$29.99",
        "bike_light": "$9.99",
        "bolt_shirt": "$15.99",
        "jacket": "$49.99",
        "onesie": "$7.99",
        "all_things_shirt": "$15.99"
    }