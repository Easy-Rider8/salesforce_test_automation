from playwright.sync_api import Page
from utils.locators import SetupPageLocators

class SetupPage(object):
    def __init__(self,page : Page):
        self.page = page

    def get_title(self):
        self.page.wait_for_load_state('networkidle')
        return self.page.title()

    def object_manager(self):
        self.page.get_by_role(SetupPageLocators.OBJECT_MANAGER["role"], name=SetupPageLocators.OBJECT_MANAGER["name"]).click()

    def accounts(self):
        self.page.get_by_role(SetupPageLocators.ACCOUNT["role"], name=SetupPageLocators.ACCOUNT["name"]).click()

    def fields_relationships(self):
        self.page.get_by_role(SetupPageLocators.FIELD_RELATIONS["role"], name=SetupPageLocators.FIELD_RELATIONS["name"]).click()

    def create_new_field(self):
        self.page.get_by_role("button", name="New Custom Field").click()

    def iframe_select_text(self):
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.locator('//*[@id="dtypeS"]').click()

    def iframe_next(self):
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_role("button",name="Next").first.click()

    def iframe_enter_label(self,text:str):
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_label("*Field Label").click()
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_label("*Field Label").fill(text)

    def iframe_enter_length(self,text:str):
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_label("*Length").click()
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_label("*Length").fill(text)

    def iframe_visibility(self):
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_role("checkbox", name="Visible",exact=True).check()

    def iframe_save(self):
        self.page.locator(SetupPageLocators.IFRAME["locator"]).content_frame.get_by_role("button", name="Save").first.click()

    def applauncher(self):
        self.page.get_by_role("button", name="App Launcher").click()

    def search_on_applauncher(self,text:str):
        self.page.wait_for_load_state('networkidle')
        self.page.get_by_role("button", name="App Launcher").click()
        self.page.get_by_placeholder("Search apps and items...").click()
        self.page.get_by_placeholder("Search apps and items...").fill(text)
        self.page.wait_for_selector("a:has-text('"+text+"')")
        self.page.get_by_role("option", name=text).click()