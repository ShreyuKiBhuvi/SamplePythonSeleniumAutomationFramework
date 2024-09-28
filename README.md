# Test Automation Framework

This is a Selenium-based automation framework designed for testing the user journey flows in an e-commerce website.

### **Summary**

This automation framework provides:
- A modular and maintainable structure using design patterns (Page Object Model and Factory Pattern).
- Parallel test execution using `pytest-xdist`.
- User-friendly HTML reports with `pytest-html`.
- Dockerization for running tests in any environment.

This setup is scalable and can be integrated easily into any CI/CD pipeline for continuous testing, ensuring quality and stability for e-commerce flows.

# Test Automation Framework Structure
/pythonProject
│
├── /POMFiles
│   ├── __init__.py
│   └── common_page_methods.py
|   └── element_locators.py
|   └── home_page.py
|   └── login_page.py
|   └── shopping_cart.py
│
├── /TestScripts
│   ├── test_about_flow.py
│   └── test_finish_checkout_flow.py
│
├── /Utilities
│   ├── general_utils.py
│
├── conftest.py
├── docker-compose.yaml
├── Dockerfile
├── README.md
└── pytest.ini
└── requirements.txt

## Setup Instructions

1. Clone the repository.
2. CD into the project root 
3. Run the below command in terminal. (Make sure you have docker installed.)
     docker-compose build
