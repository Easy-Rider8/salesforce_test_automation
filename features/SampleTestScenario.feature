Feature: Sample Test Feature

  Scenario: Scenario_1
    Given Login to your Salesforce organization with your username "your_username" and password "your_password"
    When Go to the Setup -> Object Manager -> Account -> Fields and Relationships
    Then Create a new field with type:Text, label:"Account Region", Length:"255"

  Scenario: Scenario_2
    When Go to the "Accounts" tab. Create a new Account with Account Name: "Acc0unt", Account Region: "EMEA"
    Then Confirm that the Account record is saved
    When Go to the "Contacts" tab
    And Create a new contact with the following information:
      |Attribute      |Value    |
      |First Name     |Brad     |
      |Last Name      |Scott    |
      |Account Name   |Acc0unt  |
      |Languages      |English  |
    Then Confirm that the Contact record is saved
    And Verify that the Account Name is set as "Acc0unt" on the Contact
    When Go to the "Accounts" tab
    And Proceed to the "Acc0unt" record
    Then Under the Related tab, confirm that "Brad Scott" is visible as a contact in Contacts section

  Scenario: Scenario_3
    When On the Accounts tab, go to the Details section
    Then Verify that the Account Owner field shows you as the logged-in user
    When Click on the Change Owner button
    And Search for the user called "Integration User"
    And Select the "Integration User" user as the new owner of the record and click on Change Owner
    Then Verify that the Account owner is now "Integration User"

  Scenario: Background scenario for Scenario_4
    When On the "Test Account" page, upload 4 files to the Notes&Attachments section under the Related tab
    Then Verify that the uploads are complete

  Scenario Outline: Scenario_4
    # RECURSIVELY complete the following steps FOR ALL FILES:
    When Click on one of the files , "<file_name>"
    And Click on download on the preview page
    Then Verify that the file is downloaded and visible in the "downloads"
    And Delete the file from local
      Examples:
        | file_name    |
        | 1text        |
        | 2text        |
        | 3text        |
        | 4text        |

  Scenario: Scenario_5
    When Go to the "Contacts" tab
    Then Select "Brad Scott" from the contacts list
    When On the Activity tab on the right, click on Email section
    Then Verify that the From section is not blank
    When Type a valid email address to the To section
    And Enter subject as "Test Email"
    And On the email’s body section, type "Test Body"
    And Click on Attach file under Body area of the email
    And Select one of the files previously uploaded and click Add
    Then Verify that the file is attached
    When Click on Send
    And Verify that the email is sent with a success message