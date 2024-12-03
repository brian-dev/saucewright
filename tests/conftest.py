import os
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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
