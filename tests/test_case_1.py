import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestCase3(unittest.TestCase):

    #initializing Chromedriver & opening web page
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.sogeti.com/")
        
    #tear down procedure at end of the test to close down Chromedriver instance
    def tearDown(self):
        self.driver.close()
        
    #closing the cookie prompt by clicking on "Decline optional cookies"
    def test_case_3(self):
        for button in WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(., 'Decline optional cookies')]"))):
            button.click()

        #hovering over the Services link
        services_link = self.driver.find_element(By.XPATH,"//span[text()='Services']")
        actions = ActionChains(self.driver)
        hover = actions.move_to_element(services_link).perform()

        #clicking on the Automation list item
        automation_link = self.driver.find_element(By.LINK_TEXT,'Automation')
        automation_link.click()

        #verify that Automation screen is displayed & "Automation" text is visible in page
        page_heading = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-heading')))
        page_heading_list = page_heading.find_elements(By.XPATH,"//span[text()='Automation']")
        if not page_heading_list:
            print("Automation text is not present in page.")
        else:
            page_heading_automation = page_heading_list[0]
            if page_heading_automation.is_displayed():
                print("Automation text is visible in page.")
            else:
                print("Automation text is not visible in page.")

        #hovering over the Services link
        services_link = self.driver.find_element(By.XPATH,"//span[text()='Services']")
        actions.move_to_element(services_link).perform()

        #verify that Services is selected
        services_link_li = services_link.find_element(By.XPATH,'../..')
        if 'selected' in services_link_li.get_attribute('class'):
            print("Services is selected.")
        else:
            print("Services is not selected.")

        #verify that Automation is selected
        automation_link = self.driver.find_element(By.LINK_TEXT,'Automation')
        automation_link_li = automation_link.find_element(By.XPATH,'..')
        if 'selected' in automation_link_li.get_attribute('class'):
            print("Automation is selected.")
        else:
            print("Automation is not selected.")
