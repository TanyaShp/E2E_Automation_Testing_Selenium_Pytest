# Selenium PyTest Testing for Flask Web Application

This repository contains automated testing scripts for a Flask web application located at https://github.com/TanyaShp/Flask_Python_Book_Review. Selenium WebDriver is used for end-to-end testing and PyTest for unit testing. The goal of this project is to automate the process of testing new features and bug fixes, helping to ensure the reliability and robustness of the application.

## Features

- Automated testing for various parts of functionality.
- Custom testing routes in Flask app for test data management.
- Usage of fixtures to manage setup and teardown for tests.
- Isolated testing using separate test database.
- Integration with Selenium for end-to-end testing.

## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

- Python 3.8+
- PyTest
- Selenium WebDriver

### Installation

1. Clone the repository:
```sh
git clone https://github.com/TanyaShp/E2E_Automation_Testing_Selenium_Pytest
```

2. Change to the project directory:
```
cd E2E_Automation_Testing_Selenium_Pytest
```

2. Install Python packages:
```
pip install -r requirements.txt
```

3. Setup config.py, see the section below:

### Setup

This project requires a configuration file named `config.py` in the project's root directory. This file should contain constants defining the URLs needed for the application. This is not included in the repository as it can contain sensitive information.

Here is an example of what `config.py` might look like:

```python
INDEX_URL = "http://127.0.0.1:5000/"
LOGIN_URL = "http://127.0.0.1:5000/login"
SIGNUP_URL = "http://127.0.0.1:5000/signup"
CLEANUP_URL = "http://127.0.0.1:5000/cleanup"
DEL_USR_URL = "http://127.0.0.1:5000/delete_user/"
```

### Running Tests
All tests are located in the tests directory. You can run them using PyTest:
```
pytest tests
```

## Future Improvements
1. **Test Coverage Expansion**: Additional testing scripts to cover more features of the web application, improving the test coverage.

2. **Continuous Integration**: Integration with a continuous integration (CI) service such as GitHub Actions or Jenkins to automate the running of tests whenever new code is pushed to the repository.

3. **Performance Testing**: In addition to functional testing, performance testing to ensure that the application can handle expected user load.

4. **Security Testing**: Test for potential security vulnerabilities as the application evolves.

## Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.

## Authors
- Tetiana Shpychka
