from behave import step
import os
# import time # if necessary for the related step

@step('Login to your Salesforce organization with your username "{username}" and password "{password}"')
def login_action(context,username,password):
    # Login credentials
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.submit()
    # Check Title
    message = "Home | Salesforce"
    assert context.setup_page.get_title() == message, "Page is not loaded"

@step('Go to the Setup -> Object Manager -> Account -> Fields and Relationships')
def go_to_fr(context):
    # Go to Fields and Relationships
    context.setup_page.object_manager()
    context.setup_page.accounts()
    context.setup_page.fields_relationships()

@step('Create a new field with type:Text, label:"{label}", Length:"{length}"')
def create_new_field(context,label,length):
    # Create New Field
    context.setup_page.create_new_field()
    # Set Attributes
    context.setup_page.iframe_select_text()
    context.setup_page.iframe_next()
    context.setup_page.iframe_enter_label(label)
    context.setup_page.iframe_enter_length(length)
    context.setup_page.iframe_next()
    context.setup_page.iframe_visibility()
    context.setup_page.iframe_next()
    context.setup_page.iframe_save()

@step('Go to the "{tab}" tab. Create a new Account with Account Name: "{account_name}", Account Region: "{region}"')
def create_account(context,tab,account_name,region):
    context.account_name = account_name
    # Go to Accounts
    context.setup_page.search_on_applauncher(tab)
    # Add new account
    context.account_page.new_field()
    context.account_page.enter_account_name(account_name)
    context.account_page.enter_account_region(region)
    context.account_page.click_save()

@step('Confirm that the Account record is saved')
def check_account_is_created(context):
    assert context.account_page.check_account_is_created(context.account_name) is True,'The Account record is not saved.'

@step('Go to the "{tab}" tab')
def go_to_tab(context, tab):
    context.setup_page.search_on_applauncher(tab)

@step('Create a new contact with the following information')
def new_contact(context):
    context.account_page.new_contact()
    context.data = {row['Attribute']: row['Value'] for row in context.table}
    context.contact_page.fill_first_name(context.data.get('First Name'))
    context.contact_page.fill_last_name(context.data.get('Last Name'))
    context.contact_page.fill_account_name(context.data.get('Account Name'))
    context.contact_page.fill_languages(context.data.get('Languages'))
    context.contact_page.click_save()

@step('Confirm that the Contact record is saved')
def check_contact_is_created(context):
    assert context.contact_page.check_contact_is_created(f'{context.data.get("First Name")} {context.data.get("Last Name")}'),'The Contact record is not saved.'

@step('Verify that the Account Name is set as "{contact_account_name}" on the Contact')
def check_contact_account_name(context,contact_account_name):
    assert context.contact_page.get_account_name(contact_account_name) == contact_account_name,f'{context.contact_page.get_account_name()}The Account name is not set as "{contact_account_name}"'

@step('Proceed to the "{s_account_name}" record')
def click_account(context,s_account_name):
    context.account_page.click_account(s_account_name)

@step('Under the Related tab, confirm that "{name}" is visible as a contact in Contacts section')
def check_name(context,name):
    assert context.account_page.get_contact_name(name) == name ,f'The "{name}" is not visible'

@step('On the Accounts tab, go to the Details section')
def go_to_details(context):
    context.account_page.go_details()

@step('Verify that the Account Owner field shows you as the logged-in user')
def check_user(context):
    logged_user = context.account_page.get_loggedin_user()
    assert logged_user in context.account_page.get_owner(), 'Account owner is not equal as expected'

@step('Click on the Change Owner button')
def click_change_owner(context):
    context.account_page.change_owner()

@step('Search for the user called "{user}"')
def change_the_user(context,user):
    context.account_page.search_user(user)

@step('Select the "{user}" user as the new owner of the record and click on Change Owner')
def select_user(context,user):
    context.account_page.switch_user(user)
    context.account_page.click_change_button()

@step('Verify that the Account owner is now "{owned_user}"')
def check_owner(context,owned_user):
    assert context.account_page.check_integration_user_owned(owned_user) is True , "The Account owner couldn't be changed"

@step('On the "Test Account" page, upload 4 files to the Notes&Attachments section under the Related tab')
def upload_files(context):
    context.account_page.click_related_tab()
    # The files path
    files = [
        "uploads/1text",
        "uploads/2text",
        "uploads/3text",
        "uploads/4text"
    ]
    context.account_page.scroll_down_to_upload()
    # Get files as a list
    context.account_page.upload_files(files)
    context.account_page.done_after_upload()

@step('Verify that the uploads are complete')
def verify_uploads(context):
    assert context.account_page.check_files_uploaded() is True, "Upload verification failed: files are not uploaded"
    context.account_page.view_files()

@step('Click on one of the files , "{file_name}"')
def click_file(context,file_name):
    context.account_page.click_files(file_name)

@step('Click on download on the preview page')
def download_file(context):
    context.account_page.click_download_file()
    # time.sleep(5) # activate to see downloaded files on the folder

@step('Verify that the file is downloaded and visible in the "{download_folder}"')
def verify_download_and_visible(context,download_folder):
    context.download_folder = download_folder
    downloaded_files = os.listdir(download_folder)
    assert any(file.endswith("text") for file in downloaded_files), "File not downloaded."

@step('Delete the file from local')
def delete_files(context):
    downloaded_files = os.listdir(context.download_folder)
    for file in downloaded_files:
        file_path = os.path.join(context.download_folder, file)
        os.remove(file_path)

@step('Select "{contact_name}" from the contacts list')
def select_from_contact(context,contact_name):
    # Since we changed the account owner , to see created contact, filter the owner
    context.contact_page.filter_by_owner('Integration User')
    context.contact_page.click_contact(contact_name)

@step('On the Activity tab on the right, click on Email section')
def click_email(context):
    context.contact_page.sclick_mail()

@step('Verify that the From section is not blank')
def check_from_not_emtpy(context):
    assert context.contact_page.from_section() is not None and context.contact_page.from_section() != "",'From section is empty'

@step('Type a valid email address to the To section')
def enter_to_section(context):
    context.contact_page.to_section()

@step('Enter subject as "{testmail}"')
def enter_subject(context,testmail):
    context.contact_page.subject_section(testmail)

@step('On the email’s body section, type "{testbody}"')
def enter_body(context,testbody):
    context.contact_page.body_section(testbody)

@step('Click on Attach file under Body area of the email')
def click_add_file(context):
    context.contact_page.sclick_add_file()

@step('Select one of the files previously uploaded and click Add')
def add_file_to_mail(context):
    context.contact_page.sadd_file()

@step('Verify that the file is attached')
def check_attached(context):
    assert context.contact_page.scheck_attaced() is True, "The file is not attached"

@step('Click on Send')
def click_send(context):
    context.contact_page.send()

@step('Verify that the email is sent with a success message')
def check_sent(context):
    assert context.contact_page.scheck_sent() is True , "Mail couldn't sent"


