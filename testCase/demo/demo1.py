import requests
import unittest


class InterfaceTestDemo1(unittest.TestCase):

    def setUp(self):
        global json
        self.url = "http://app.shetest4.cn/index.php"
        self.params = {'model': 'account', 'action': 'txc', 'code': '11'}
        self.headers = {'Language': 'ar'}
        json = []

    def testInterfaceGet(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        json = response.json()
        print(json['errormsg'])
        self.assertEqual(json['errormsg'], "قمت بالفعل بحفظ هذه السلعة")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
