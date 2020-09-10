# pytest_selenium_pom

This is a simple example of test scripts written using **Python**, **Selenium WebDriver**, **PyTest**
and **Allure**. 
This framework is utilizing Page Object Model (POM). 
conftest.py includes code to use specific chromedriver version based on your Operating System.
**ChromeDriver** version is 83 and located inside resources folder. 
Please update it according to your version of Google Chrome 
installed on your machine when running locally.

**Pre-requisites:**

Please make sure you have **Python** installed https://www.python.org/downloads/

Please make sure you have **PyCharm** installed https://www.jetbrains.com/pycharm/download/

Please make sure you have **Git** installed https://git-scm.com/downloads

1. Open your PyCharm
2. Navigate to VCS - Git - Clone and paste repository URL 
3. Select "New Window" option.
4. Click on "Terminal" at the bottom of the page
5a. For Windows users, type in **pip install pipenv** and press Enter
5b. For mac OS users, type in **pip3 install pipenv** and press Enter
6. Type in **pipenv install selenium** and press Enter
7. Type in **pipenv install pytest** and press Enter
8. Type in **pipenv install allure-pytest** and press Enter

Navigate to "Edit Configurations.." at the top right of the PyCharm

Reports will open in your default browser (I recommend Firefox or Chrome).

