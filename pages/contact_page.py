from playwright.sync_api import Page
from utils.locators import ContactPageLocators

class ContactPage(object):
    def __init__(self,page : Page):
        self.page = page

    def fill_first_name(self,text:str):
        self.page.get_by_placeholder(ContactPageLocators.FIRST_NAME["locator"]).fill(text)

    def fill_last_name(self,text:str):
        self.page.get_by_placeholder(ContactPageLocators.LAST_NAME["locator"]).fill(text)

    def fill_account_name(self,text:str):
        self.page.get_by_placeholder("Search Accounts...").click()
        self.page.locator("span[title='"+text+"']").click()

    def fill_languages(self, text: str):
        self.page.get_by_label(ContactPageLocators.LANGUAGES["locator"]).fill(text)

    def click_save(self):
        self.page.get_by_role("button", name="Save", exact=True).click()

    def check_contact_is_created(self,text:str):
        try:
            self.page.get_by_text("Contact "+text+" was created.")
            return True
        except:
            return False

    def get_contact_name(self,text:str):
        return self.page.get_by_role("link", name=text).text_content()

    def get_account_name(self,text:str):
        return self.page.get_by_role("link", name=text).text_content()

    def click_contact(self,text:str):
        self.page.get_by_role("link", name=text).click()

    def filter_by_owner(self,text:str):
        self.page.get_by_role("button", name="Me", exact=True).click()
        self.page.get_by_placeholder("Search Users...").fill(text)
        self.page.get_by_role("option", name="Integration User", exact=True).click()

    def sclick_mail(self):
        self.page.get_by_role("button", name="Email",exact=True).click()

    def from_section(self):
        try:
            # Enter your username to Your_Username and mail to Your_Mail
            self.page.get_by_text("Your_Username <Your_Mail>")
            return True
        except:
            return False

    def to_section(self):
        self.page.get_by_role("combobox", name="To", exact=True).click()
        self.page.get_by_role("combobox", name="To", exact=True).fill(ContactPageLocators.TO_MAIL["to_mail"])

    def subject_section(self,text:str):
        self.page.get_by_placeholder("Enter Subject...").click()
        self.page.get_by_placeholder("Enter Subject...").fill(text)

    def body_section(self,text:str):
        self.page.locator("iframe[title=\"CK Editor Container\"]").content_frame.locator("iframe[title=\"Email Body\"]").content_frame.get_by_label("Email Body").click()
        self.page.locator("iframe[title=\"CK Editor Container\"]").content_frame.locator("iframe[title=\"Email Body\"]").content_frame.get_by_label("Email Body").fill(text)

    def sclick_add_file(self):
        self.page.get_by_role("button", name="Attach file").click()

    def sadd_file(self):
        self.page.get_by_role("option", name="4text").first.click()
        self.page.get_by_role("button", name="Add (1)").click()

    def scheck_attaced(self):
        try:
            self.page.get_by_role("link", name="4text")
            return True
        except:
            return False

    def send(self):
        self.page.get_by_role("button", name="Send").click()
        self.page.get_by_role("button", name="Attach and Send").click()

    def scheck_sent(self):
        try:
            self.page.get_by_text("Email was sent.")
            return True
        except:
            return False