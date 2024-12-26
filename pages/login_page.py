from playwright.sync_api import Page
from utils.locators import LoginPageLocators

class LoginPage(object):
    def __init__(self,page : Page):
        self.page = page

    def enter_username(self,text:str):
        self.page.get_by_label(LoginPageLocators.LOGIN_USERNAME["locator"]).fill(text)

    def enter_password(self,text:str):
        self.page.get_by_label(LoginPageLocators.LOGIN_PASSWORD["locator"]).fill(text)

    def submit(self):
        self.page.get_by_role(LoginPageLocators.LOGIN_BUTTON["role"], name=LoginPageLocators.LOGIN_BUTTON["name"]).click()

