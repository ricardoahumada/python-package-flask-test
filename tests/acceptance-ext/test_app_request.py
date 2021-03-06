import json
import unittest
import requests

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1'

    def test_1_get_none(self):
        url=f"{self.base_url}/customers/"
        response = requests.get(url)
        data=json.loads(response.text)
        print(f"get 1: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [])

    def test_2_post(self):
        url=f"{self.base_url}/customers/"
        test_data = {"address": "5 Spenser Plaza",
                     "email": "kbraksper0@mac.com",
                     "name": "Kelbee"}
        response = requests.post(url, json=test_data)
        data=json.loads(response.text)
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)

    def test_3_get_none(self):
        url=f"{self.base_url}/customers/"
        response = requests.get(url)
        data=json.loads(response.text)
        print(f"get 2: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)
