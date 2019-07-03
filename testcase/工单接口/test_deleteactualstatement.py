import unittest
import requests

class TestDeleteActualStatement(unittest.TestCase):
    def test_deleteactualstatement(self):
        print("根据票据号删除实收")
        url="https://api-test.lefull.cn/data/api/v1/surrender/deleteActualStatement"
        data={
            "billNumber":"123"
        }
        res=requests.post(url=url,json=data)
        print(res.text)