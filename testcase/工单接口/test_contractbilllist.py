import unittest
import requests

class TestContractBillList(unittest.TestCase):
    def test_contractbilllist(self):
        print("合同账单列表")
        url="https://api-test.lefull.cn/data/api/v1/contractBillList"
        params={"contractId":16}
        res=requests.get(url=url,params=params)
        print(res.text)
        self.assertEqual("成功", res.json()["msg"])
        self.assertEqual("200",res.json()["code"])

    if __name__=="__main__":
        unittest.main(verbosity=2)