import unittest
import requests
from common import case_log
from common.db import check_ownership,check_ownership_exist,delete_ownership,check_ownershipId
import ddt,data
class TestOwnerShip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  #整个测试只执行一次  是测试准备方法
        Apartment_id=17
        if check_ownership_exist(Apartment_id):
            delete_ownership(Apartment_id)

    # @unittest.skip("跳过测试用例")#无条件跳过
    def test_1_ownership_new(self):
        print("新增权证信息")
        # Apartment_id=17
        # if check_ownership_exist(Apartment_id):
        #     delete_ownership(Apartment_id)
        url="https://api-test.lefull.cn/records//api/v1/ownership"
        data={
            "address": "北京百子湾花园",
            "apartmentId": "17",
            "certNo": "百子湾权证号001",
            "certType": 1,
            "ownerCardNo": "220422199009088888",
            "ownerCardType": 0,
            "ownerName": "百子湾花园",
            "ownerType": 0,
            "ownershipId": ""
        }
        print(data)
        res=requests.post(url=url,json=data)
        print(res.text)
        case_log.log_case_info("test_ownership_new",url,data,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("北京百子湾花园",check_ownership(17)[0][0])
        self.assertEqual("百子湾权证号001",check_ownership(17)[0][1])
        self.assertEqual("百子湾花园",check_ownership(17)[0][2])
        self.assertEqual(0,check_ownership(17)[0][3])

    # @unittest.skip()#无条件跳过
    def test_2_ownership_query(self):
        print("查询权证信息")
        url="https://api-test.lefull.cn/records//api/v1/ownership"
        params={
            "apartmentId": 17
        }
        res=requests.get(url=url,params=params)
        print(res.text)
        # case_log.log_case_info("test_ownership_query",url,params,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("北京百子湾花园",res.json()["data"]["address"])
        self.assertEqual("百子湾权证号001",res.json()["data"]["certNo"])
        self.assertEqual("220422199009088888",res.json()["data"]["ownerCardNo"])
        self.assertEqual("17",res.json()["data"]["apartmentId"])
        self.assertEqual(0,res.json()["data"]["ownerType"])

    def test_3_ownership_alter(self):
        print("修改权证信息")
        url="https://api-test.lefull.cn/records//api/v1/ownership"
        data={
            "address": "北京百子湾花园修改",
            "apartmentId": "17",
            "certNo": "百子湾权证号修改001",
            "certType": 1,
            "ownerCardNo": "220422199009088800",
            "ownerCardType": 0,
            "ownerName": "百子湾花园修改",
            "ownerType": 0,
            "ownershipId":check_ownershipId(17)[0][0]
        }
        res=requests.post(url=url,json=data)
        print(res.text)
        case_log.log_case_info("test_ownership_alter",url,data,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("北京百子湾花园修改",check_ownership(17)[0][0])
        self.assertEqual("百子湾权证号修改001",check_ownership(17)[0][1])
        self.assertEqual("百子湾花园修改",check_ownership(17)[0][2])
        self.assertEqual(0,check_ownership(17)[0][3])



if __name__=="__main__":
    unittest.main(verbosity=2)
