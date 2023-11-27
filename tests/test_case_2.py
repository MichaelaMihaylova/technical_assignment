import unittest
import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCase2(unittest.TestCase):

    #initializing Chromedriver & opening web page
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.sogeti.com/")
        
    #tear down procedure at end of the test to close down Chromedriver instance
    def tearDown(self):
        self.driver.close()

    #generate random data for First Name, Last Name, Email,Phone and Message; since no constraints have been given 
    #for the type of data that should be generated, it is assumed it will include upper & lower case ASCII letters,
    #along with ASCII punctionation characters; a limit of up to 30 characters long is also assumed
    def random_str_generator(length=30, chars=string.ascii_letters + string.digits + string.punctuation):
      return ''.join(random.choice(chars) for _ in range(1,30))

    #closing the cookie prompt by clicking on "Decline optional cookies"
    def test_case_2(self):
      for button in WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(., 'Decline optional cookies')]"))):
        button.click()

      #hovering over the Services link
      actions = ActionChains(self.driver)
      services_link = self.driver.find_element(By.XPATH,"//span[text()='Services']")
      hover = actions.move_to_element(services_link).perform()

      #clicking on the Automation list item
      automation_link = self.driver.find_element(By.LINK_TEXT,'Automation')
      automation_link.click()
      print("Navigated to the Automation page.")

      #scrolling to the Contact us form
      contact_form_title = self.driver.find_element(By.CLASS_NAME,'Form__Title')
      self.driver.execute_script("arguments[0].scrollIntoView()", contact_form_title)
      print("Scrolled to the contact form.")

      #locate the form text fields
      contact_form_body = self.driver.find_element(By.CLASS_NAME,'Form__MainBody')
      form_fields = contact_form_body.find_elements(By.CLASS_NAME,'Form__Element.FormTextbox')

      #find the relevant text fields and fill them in with random generated data
      for form_field in form_fields:
        field_caption = form_field.find_element(By.TAG_NAME,'label')
        field_caption_text = field_caption.text
        
        if field_caption_text == "First Name*" or field_caption_text == "Last Name*" or field_caption_text == "Email*" or field_caption_text == "Phone":
          field_input = form_field.find_element(By.TAG_NAME,'input')
          random_data = self.random_str_generator()
          field_input.send_keys(random_data)
        if field_caption_text == "Message*":
          field_textarea = form_field.find_element(By.TAG_NAME,'textarea')
          random_data = self.random_str_generator()
          field_textarea.send_keys(random_data)
      print("Filled in First Name, Last Name, Email, Phone and Message form fields.")

      #scroll to the bottom of the form into view, using the submit button for orientation
      submit_button = contact_form_body.find_element(By.TAG_NAME,'button')
      actions.move_to_element(submit_button).perform()
              
      #locate and click on the I agree checkbox
      form_checkbox = contact_form_body.find_element(By.CLASS_NAME,'Form__Element.FormChoice.ValidationRequired')
      actions.move_to_element(form_checkbox).click().perform()
      print("Clicked on the I Agree checkbox.")
      
      #click on the submit button
      actions.move_to_element(submit_button).click().perform()
      print("Clicked on the Submit button.")
      print("This test could not be completed. Please read the comments for more information.")
      
"""""
There are the following 3 reasons why the test cannot be completed as described, with the exact given conditions:
  - incorrect syntax of the data entered into the Email fiels: there are syntax constraints in regards to the 
    data entered into the email; with randomly generated data there is no guarantee that these syntax conditions
    will be met; 
      -> an alternative would be to at least generate a string like "{random_data}@{random_data}.{random_data}"; to 
      avoid entering an existing realworld account, there are 2 options: 1)exclude realworld email providers in the
      string above, 2)use a message routing system like Mailinator
  - mandatory fields are left empty: the Company and Country form fields are mandatory and they must be filled, 
    else the form will not successfully be submitted
  - reCAPTCHA check needs to be passed: the goal of this check to distinguish between human and computer users and
    to exclude computers from proceeding further;
      -> a solution could be solving the reCAPTCHA directly thrrough a combination of OCR (e.g. via tesseract) 
        and image recognition (e.g. via NumPy)
      -> another solution that would take less time and effort implement is to use already available packages for
        Python (e.g. Selenium-recaptcha-solver)
      -> both solution cannot provide a consistent 100% success rate, so an extra verification step should be 
        added to check whether the reCAPTCHA has successfully been resolved, in order to exclude false positive 
        results;
"""""


      



