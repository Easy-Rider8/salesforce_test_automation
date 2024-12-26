# Salesforce Automation Project

# Overview 

This project is an automation tool designed for Salesforce using Python, Playwright, and Behave. It implements the Page Object Model (POM) structure to streamline the testing of Salesforce functionalities.

# Features 

Login Automation: Automated login to Salesforce using username and password. <br/>
Account Management: Create and manage accounts.<br/>
Contact Management: Add and manage contacts associated with accounts.<br/>
Setup Management: Automate the creation of custom fields in the object manager.<br/>

# Technologies Used 

Python: The programming language used for automation scripts.<br/>
Playwright: A library for automating browser actions and interactions.<br/>
Behave: A behavior-driven development (BDD) framework for writing tests in Gherkin language.<br/>
Salesforce: The platform being automated. 

# Prerequisites 

Python 3.x<br/>
Playwright<br/>
Behave<br/>
Allure<br/>

# Installation 

Clone the repository: 
```git clone```

Navigate to the project directory: 
```cd```

Install the required packages: 
```pip install -r requirements.txt```

Install Playwright browsers: 
```playwright install```

# Usage 

Run Tests: Execute the tests using Behave: 
```behave```

To run with allure;

```behave -f allure_behave.formatter:AllureFormatter -o {allure_report_folder} {path_to_feature_file}```

To see allure reports, need to download allure framework and execute ;

```allure serve {allure_report_folder}```

Some test results ;
![Result](https://github.com/user-attachments/assets/df75ff2b-796c-4ee5-8a28-780856b5df78)

![result](https://github.com/user-attachments/assets/4301ae45-1df0-483d-a1c7-fb654c7e3d97)

Modify Locators: Customize locators in the pages directory as needed for your Salesforce instance.<br/>
Configuration: Update the environment configuration in feature/environment.py


# Project Structure
```
├── feature
│ ├── environment.py
│ ├── SampleTestScenario.feature
│ └── steps
│       ├── step_def.py
├── pages
│ ├── login_page.py
│ ├── account_page.py
│ ├── contact_page.py
│ └── setup_page.py
├── utils
│ ├── locators.py
├── requirements.txt
└── README.md
```

# Notes 

There is locators.py under utils that have selector for the various methods of the playwright.<br/>

To change To mail in the Fifth scenario, you have to change `ContactPageLocators.TO_MAIL` value
