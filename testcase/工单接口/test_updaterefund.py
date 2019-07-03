import unittest
import requests


class TestUpdateRefund(unittest.TestCase):
    def test_updaterefund_normal(self):
        print("退款科目增减及金额调整")
        url="https://api-test.lefull.cn/data/api/v1/updateRefund"
        data={
            "contractId":"3881",
            "isForce":0,
            "items":[
                {
                    "costAmount":100,
                    "costType":2,
                    "subjectInfoId":"8",
                    "subjectName":"网费"
                }
            ],
            "surrenderTime": 1554134400
        }
        res=requests.post(url=url,json=data)
        print(res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(100,res.json()["data"])
