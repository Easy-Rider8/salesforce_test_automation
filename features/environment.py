# environment.py
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.setup_page import SetupPage
from pages.account_page import AccountPage
from pages.contact_page import ContactPage


def before_feature(context, feature):
    context.browser = sync_playwright().start().chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto('https://login.salesforce.com')
    context.login_page = LoginPage(context.page)
    context.setup_page = SetupPage(context.page)
    context.account_page = AccountPage(context.page)
    context.contact_page = ContactPage(context.page)

def after_feature(context, feature):
    context.browser.close()