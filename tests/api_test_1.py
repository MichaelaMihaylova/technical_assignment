import unittest
import requests


class APITest1(unittest.TestCase):
  def test_verify_response(self):
    url = "http://api.zippopotam.us/de/bw/stuttgart"
    response = requests.get(url)
    
    #verify that the HTTP response code is 200
    self.assertEqual(response.status_code, 200, "Response with incorrect HTTP status code received. HTTP response codereceived: {}".format(response.status_code))
    print("Verified: response code is HTTP 200.")
    
    #verify that the content type is JSON
    response_content_type = response.headers['Content-Type']
    assert response_content_type == "application/json"
    self.assertEqual(response_content_type, "application/json", "Response with incorrect content type received. Content type received: {}".format(response_content_type))
    print("Verified: response content type is JSON.")
  
    #verify that server response time is less than 1s
    response_time = response.elapsed.total_seconds()
    self.assertLess(response_time, 1, "Response time is not below 1s. Response time: {}".format(response_time))
    print("Verified: response time is below 1s.")
    
    #verify in response contents that "country" is "Germany"
    response_content = response.json()
    self.assertEqual(response_content['country'], "Germany", "Response contains incorrect Country value. Country received: ".format(response_content['country']))
    print("Verified: in response contents - country is Germany.")

    #verify in response contents that "state" is "Baden-Württemberg"
    self.assertEqual(response_content['state'], "Baden-Württemberg", "Response contains incorrect State value. State received: ".format(response_content['state']))    
    print("Verified: in response contents - state is Baden-Württemberg.")

    #verify in response contents that for "post code" "70597" there is a "place name" "Stuttgart Degerloch"
    search_flag = False
    places = response_content['places']
    for index in range(len(places)):
      post_code = places[index]['post code']
      if post_code == "70597":
        place_name = places[index]['place name']
        if place_name == "Stuttgart Degerloch":
          search_flag = True
    
    self.assertTrue(search_flag, "Response content does not contain the place name 'Stuttgart Degerloch' for the post code '70597'")
    print("Verified: in response contents - for post code 70597 there is a placename of Stuttgart Degerloch.")
    







  
