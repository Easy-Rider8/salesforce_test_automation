# Locator file that can be customizable and resizable for the locators

class LoginPageLocators:

    LOGIN_USERNAME      =   {"locator": "Username"}
    LOGIN_PASSWORD      =   {"locator": "Password"}
    LOGIN_BUTTON        =   {"role": "button", "name": "Log In"}

class SetupPageLocators:

    OBJECT_MANAGER      =   {"role": "tab", "name": "Object Manager"}
    ACCOUNT             =   {"role": "link", "name": "Account"}
    FIELD_RELATIONS     =   {"role": "tab", "name": "Fields & Relationships"}
    IFRAME              =   {"locator": "iframe[title='Account: New Custom Field ~ Salesforce - Developer Edition']"}

class AccountPageLocators:

    NEW_FIELD           =   {"role": "button", "name": "New"}
    ACCOUNT_NAME        =   {"locator": "*Account Name"}
    ACCOUNT_REGION      =   {"locator": "Account Region"}
    SAVE_BUTTON         =   {"role": "button", "name": "Save"}

class ContactPageLocators:

    FIRST_NAME          =   {"locator": "First Name"}
    LAST_NAME           =   {"locator": "Last Name"}
    LANGUAGES           =   {"locator": "Languages"}
    TO_MAIL             =   {"to_mail": "xyz@xyz.xyz"}