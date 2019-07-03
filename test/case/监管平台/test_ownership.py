import unittest
import requests
import json
from test.case.basecase import BaseCase
from common.db import check_ownership,check_ownership_exist,delete_ownership,check_ownershipId


class TestOwnerShip(BaseCase):

    def test_1_ownership_new(self):
        print("新增权证信息")
        case_data = self.get_case_data("test_1_ownership_new")
        Apartment_id=int(json.loads(case_data.get("args")).get('apartmentId'))
        if check_ownership_exist(Apartment_id):
            delete_ownership(Apartment_id)
        res=self.send_request(case_data)
        # print(res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("北京百子湾花园",check_ownership(17)[0][0])
        self.assertEqual("百子湾权证号001",check_ownership(17)[0][1])
        self.assertEqual("百子湾花园",check_ownership(17)[0][2])
        self.assertEqual(0,check_ownership(17)[0][3])


    def test_2_ownership_query(self):
        print("查询权证信息")
        case_data = self.get_case_data("test_2_ownership_query")
        res=self.send_request(case_data)
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
        # print(res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("北京百子湾花园修改",check_ownership(17)[0][0])
        self.assertEqual("百子湾权证号修改001",check_ownership(17)[0][1])
        self.assertEqual("百子湾花园修改",check_ownership(17)[0][2])
        self.assertEqual(0,check_ownership(17)[0][3])


if __name__ == "__main__":
    unittest.main(verbosity=2)