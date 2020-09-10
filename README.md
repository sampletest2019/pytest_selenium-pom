# pytest_selenium_pom

This is a simple example of test scripts written using **Python**, **Selenium WebDriver**, **PyTest**
and **Allure**. 
This framework is utilizing Page Object Model (POM). 
conftest.py includes code to use specific chromedriver version based on your Operating System.
**ChromeDriver** version is 85 and located inside resources folder. 
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

Click on "+" (Add New Configuration). Select pytest as on the screenshot below.

[![Screen-Shot-2020-09-10-at-4-51-00-PM.png](https://i.postimg.cc/MGR6V9QM/Screen-Shot-2020-09-10-at-4-51-00-PM.png)](https://postimg.cc/CZhpVHJS)

Your configuration should look similar to this one (use smoketest OR regressiontest):

[![Screen-Shot-2020-09-10-at-5-28-23-PM.png](https://i.postimg.cc/d3mfRysK/Screen-Shot-2020-09-10-at-5-28-23-PM.png)](https://postimg.cc/Zvnj40vf)

After you will run your test(s). To execute report add shell script to Run Configuration similar to below:

It will automatically execute "allure serve reports" command and your Allure Report will open in the default browser

[![Screen-Shot-2020-09-10-at-5-30-20-PM.png](https://i.postimg.cc/CLrN3N6Q/Screen-Shot-2020-09-10-at-5-30-20-PM.png)](https://postimg.cc/kB8K8xCQ)

To stop executing "allure serve reports" command, press Ctrl + C in your PyCharm terminal.

