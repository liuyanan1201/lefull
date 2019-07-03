import unittest
import requests

class TestMortagePay(unittest.TestCase):
    def test_mortagepay(self):
        print("修改押付方式")
        url="https://api-test.lefull.cn/data/api/v1/bill/mortgagePay"
        data={
            "contractId":"199",
            "howPay":"1"
        }
        res=requests.post(url=url,json=data)
        print(res.text)
