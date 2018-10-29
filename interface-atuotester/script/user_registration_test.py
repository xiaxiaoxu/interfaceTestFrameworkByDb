#encoding=utf-8
import unittest, requests
from interface.public_info import *
import os, sys,json


class User_Registration(unittest.TestCase):
    """用户注册"""
    def setUp(self):
        self.dbd = DB_Data()
        self.base_url = "http://39.106.41.11:8080/register/"

    def test_user_registration_1(self):
        """1"""
        payload = {"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        print "测试用"
        self.assertEqual(r.status_code, 200)
        self.dbd.store_data(1, 1, {"request":["username","password"]}, {"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}, result)
        check_point = {"code":"00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))


    def test_user_registration_2(self):
        """2"""
        payload = {"username":"test1201","password":"test123test","email":"test@qq.com"}
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        self.dbd.store_data(3, 1, {"request":["username","password"]}, {"username":"test1201","password":"test123test","email":"test@qq.com"}, result)
        check_point = {"code":"00","username":{"R":"[a-zA-Z]+"}}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))


    def tearDown(self):
        self.dbd.close_connect()


if __name__ == '__main__':
    unittest.main()
