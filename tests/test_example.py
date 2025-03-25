import re, pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope='function', autouse=True)
def before_each_after_each(page:Page):
    print("before the test runs")
    page.goto("https://playwright.dev")
    yield

    print("after test runs")

def test_has_title(page:Page):

    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page:Page):

    page.get_by_role("link", name="Get Started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_recorded(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Water the plants")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Feed the dog")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Get groceries")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="Get groceries").get_by_label("Toggle Todo").check()
    expect(page.get_by_role("listitem").filter(has_text="Get groceries").get_by_label("Toggle Todo")).to_be_checked()
    page.get_by_role("listitem").filter(has_text="Feed the dog").get_by_label("Toggle Todo").check()
    expect(page.get_by_role("listitem").filter(has_text="Feed the dog").get_by_label("Toggle Todo")).to_be_checked()
    page.get_by_role("link", name="Completed").click()
    expect(page.locator("body")).to_contain_text("Feed the dog")
