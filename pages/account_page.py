from playwright.sync_api import Page
from utils.locators import AccountPageLocators
import os
import re

class AccountPage(object):
    def __init__(self, page: Page):
        self.page = page

    def new_field(self):
        self.page.get_by_role(AccountPageLocators.NEW_FIELD["role"], name=AccountPageLocators.NEW_FIELD["name"]).click()

    def enter_account_name(self,text:str):
        self.page.get_by_label(AccountPageLocators.ACCOUNT_NAME["locator"]).fill(text)

    def enter_account_region(self,text:str):
        self.page.get_by_label(AccountPageLocators.ACCOUNT_REGION["locator"]).fill(text)

    def click_save(self):
        self.page.get_by_role(AccountPageLocators.SAVE_BUTTON["role"], name=AccountPageLocators.SAVE_BUTTON["name"], exact=True).click()

    def check_account_is_created(self,text:str):
        try:
            self.page.get_by_text("Account "+text+" was created.")
            return True
        except:
            return False

    def new_contact(self):
        self.page.get_by_role("button", name="New").click()

    def click_account(self,text:str):
        self.page.get_by_role("link", name=text).click()

    def get_contact_name(self,text:str):
        return self.page.get_by_label("Contacts").get_by_role("link",name=text).text_content()

    def go_details(self):
        self.page.get_by_role("tab", name="Details").click()

    def get_loggedin_user(self):
        self.page.get_by_role("button", name="View profile").click()
        # Enter your username as Your_Username
        return self.page.get_by_role("heading", name="Your_Username").get_by_role("link").text_content()

    def get_owner(self):
        # Enter your username as Your_Username
        return self.page.get_by_label("Details").locator("span").filter(has_text=re.compile(r"^Your_UsernameOpen Your_Username Preview$")).text_content()

    def change_owner(self):
        self.page.locator("records-highlights2").get_by_role("button", name="Change Owner").click()

    def search_user(self,text:str):
        self.page.get_by_placeholder("Search Users...").fill(text)

    def switch_user(self,text:str):
        self.page.get_by_role("option", name=text, exact=True).click()

    def click_change_button(self):
        self.page.get_by_role("button", name="Change Owner").click()

    def check_integration_user_owned(self,text:str):
        try:
            self.page.get_by_text('f"{text} now owns the record"')
            return True
        except:
            return False

    def click_related_tab(self):
        self.page.get_by_role("tab", name="Related").click()

    def scroll_down_to_upload(self):
        # Scroll until to element visible
        while True:
            page_height = self.page.evaluate("document.body.scrollHeight")

            if self.page.is_visible("//a//span[@title='Partners']"):
                break

            self.page.evaluate("window.scrollBy(0, window.innerHeight);")
            new_page_height = self.page.evaluate("document.body.scrollHeight")

            if new_page_height == page_height:
                break
            page_height = new_page_height

    def upload_files(self,file):
        self.page.get_by_role("textbox", name="Upload Files Or drop files").set_input_files(file)

    def done_after_upload(self):
        self.page.get_by_role("button", name="Done").click()

    def check_files_uploaded(self):
        try:
            self.page.get_by_text("file was added to the Account.")
            return True
        except:
            return False

    def view_files(self):
        self.page.get_by_role("link", name="View All Notes & Attachments").click()

    def click_files(self,file_name:str):
        self.page.get_by_role("link", name="Unknown file type "+file_name).click()

    def click_download_file(self):
        with self.page.expect_download() as download_info:
            self.page.locator("button[title='Download']").first.click()
        download = download_info.value
        download_path = os.path.join("downloads", download.suggested_filename)
        download.save_as(download_path)  # Save the related path
        self.page.locator("button[title='Close']").click()




