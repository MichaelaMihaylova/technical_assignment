# Sogeti Technical Assignment

## Overview

This project has been created in orer to solve an automation technical assignment, given by Sogeti.
The **tests** folder contains the test scripts, required to solve all automation tasks.
Also included is a .csv file, necessary for executing one of the API tests.
When downloading, please keep all these files within the same directory.

This README.md file further contains details regarding environment requirements, along with instructions on how to execute the included test scripts.

## Environment requirements
The assumed environment is a Windows machine. 
Chrome is also assumed as a web client, since it is currently the most widely used browser on the market.

The following are required in order to run the automation test scripts:
- Python (v3.7 minimum)
- Selenium for Python
- Chromedriver (compatible with installed Chrome browser version)
- Python packages:
  - requests
  - parameterized

### Python
To install Python on Windows, go to the following link and download the latest Python version for Windows: https://www.python.org/downloads/
After downloading the .exe file, run it.

**IMPORTANT** select the "Add Python to PATH" option during installation, in order to be able to execute python scripts from any directory.

### Selenium for Python
To install Seleniumm with Python binding, use a Python package manager - for example, via pip.

To install pip on Windows, download the installation script from: https://bootstrap.pypa.io/get-pip.py and execute it on the command line:
```
py get-pip.py
```
Add the following to your sys PATH: "C:\Users\*user*\AppData\Local\Programs\Python\Python312\Scripts\".

Afterwards, install Selenium by executing the following in the command line:
```
py -m pip install selenium
```
### Chromedriver
Download the latest stable Chromedriver version suitable for your machine from: https://googlechromelabs.github.io/chrome-for-testing/#stable

To check for version compatibility with the installed Chrome version on your local machine, use this page: https://chromedriver.chromium.org/downloads/version-selection

Extract the contents of the downloaded zip file and move it to the directory of your choice, for example: C:\Users\*user*\Documents\Drivers\
Add the corresponding directory path to your sys PATH, for example:C:\Users\*user*\Documents\Drivers\chromedriver-win64

Restart local machine.

### Python packages
Install the required Python packages via the command line:
```
py -m pip install requests
py -m pip install parameterized
```

## Execution instructions
To execute the test scripts, navigate to the directory where the scripts have been downloaded via command line and execute the following:
```
py -m unittest *test script*
```
Example for the test script api_test_1.py:
```
py -m unittest api_test_1.py
```

