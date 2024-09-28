# Test Automation Framework

This is a Selenium-based automation framework designed for testing the user journey flows in an e-commerce website.


### **Summary**

This automation framework provides:
- A modular and maintainable structure using design patterns (Page Object Model and Factory Pattern).
- Parallel test execution using `pytest-xdist`.
- User-friendly HTML reports with `pytest-html`.
- Dockerization for running tests in any environment.
- Documentation to ensure usability by non-technical users.

This setup is scalable and can be integrated easily into any CI/CD pipeline for continuous testing, ensuring quality and stability for e-commerce flows.


## Setup Instructions

1. Clone the repository.
2. Build the Docker image:
     docker-compose build
