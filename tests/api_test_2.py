import unittest
import requests
import csv

from parameterized import parameterized


with open("./../data/data.csv") as test_data_file:
  TEST_DATA = [tuple(line) for line in csv.reader(test_data_file)]


class APITest2(unittest.TestCase):
  
  @parameterized.expand(TEST_DATA)

  def test_verify_response(self, country, postal_code, place_name_expected):
    
    
    url = "http://api.zippopotam.us/{}/{}".format(country,postal_code)
    response = requests.get(url)
    
    #verify that the HTTP response code is 200
    self.assertEqual(response.status_code, 200, "Response with incorrect HTTP status code received. HTTP response codereceived: {}".format(response.status_code))
    print("Verified for country: {}, postal code: {} - response code is HTTP 200.".format(country,postal_code))

    
    #verify that the content type is JSON
    response_content_type = response.headers['Content-Type']
    assert response_content_type == "application/json"
    self.assertEqual(response_content_type, "application/json", "Response with incorrect content type received. Content type received: {}".format(response_content_type))
    print("Verified for country: {}, postal code: {} - response content type is JSON.".format(country,postal_code))
  
    #verify that server response time is less than 1s
    response_time = response.elapsed.total_seconds()
    self.assertLess(response_time, 1, "Response time is not below 1s. Response time: {}".format(response_time))
    print("Verified for country: {}, postal code: {} - response time is below 1s.".format(country,postal_code))
    
    #verify in response contents that expected place name
    response_content = response.json()
    places = response_content['places']
    place_name = places[0]['place name']
    self.assertEqual(place_name, place_name_expected, "Response contains incorrect Place name value. Place name received: {}".format(place_name))    
    print("Verified for country: {}, postal code: {} - in response contents - place name is: {}.".format(country,postal_code,place_name))








  
