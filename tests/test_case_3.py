import unittest
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase3(unittest.TestCase):
  
  #initialize a new Chromedriver instance and open up web page
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("https://www.sogeti.com/")
  
  #tear down procedure at end of the test to close down Chromedriver instance
  def tearDown(self):
    self.driver.close()

  #cookie dialogues must be settled at every new Chromedriver instance
  #close the cookie prompt by clicking on "Decline optional cookies"
  def test_case_3(self):
    button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Decline optional cookies')]")))
    button.click()

    #locate and click on the Worldwide link
    worldwide_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Worldwide']")))
    worldwide_link.click()

    #extract the list of country specific Sogeti links
    country_list = self.driver.find_element(By.ID,'country-list-id')
    country_list_items = country_list.find_elements(By.TAG_NAME,'li')
    for item in country_list_items:
      item_anchor = item.find_element(By.TAG_NAME,'a')
      country_url = item_anchor.get_attribute('href')
      #sending a GET request to each URL and asserting that the expected HTTP code is received
      #additional feedback provided in case the assertion fails
      request_check = requests.get(country_url)
      self.assertEqual(request_check.status_code, 200, "URL: {} is not reachable".format(country_url))
    print("All country specific Sogeti links are working.")

