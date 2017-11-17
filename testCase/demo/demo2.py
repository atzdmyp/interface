import requests
import unittest


class InterfaceTestDemo2(unittest.TestCase):
    def setUp(self):
        global json, json1, json2
        self.url = "http://api.sheinde.com/v2/User/Member/loginCommon"
        self.loginload = {'email': 'interface2@163.com',
                          'password': '123456'}
        self.headers = {'SiteUID': 'm',
                        'token': '41090_584a473b8e04f9.79839892_4d0b15f75cb8dfcab62a6850b297840693c1d65c'}
        json = []
        json1 = []
        json2 = []

    def testInterfaceDemo2(self):
        response = requests.post(self.url, data=self.loginload, headers=self.headers)
        json = response.json()
        json1 = json['info']
        json2 = json1['member']
        print("Token:" + json2['token'])
        print("Email:" + json2['email'])
        self.assertEqual(json['msg'], 'ok')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
