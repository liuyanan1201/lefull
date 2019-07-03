import unittest
import requests
from common.db import check_landlord
from common import case_log
from common import load_data
from config import config
import json


class TestLandLord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"TestLandLord")

    def test_1_landlord_new(self):
        print("新增甲方信息")
        case_data = load_data.get_case(self.sheet,"test_1_landlord_new")
        url=case_data[2]
        data=json.loads(case_data[3])
        res=requests.post(url=url,json=data)
        # print(res.text)
        case_log.log_case_info("test_landlord_new",url,data,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(18,check_landlord(18)[0][0])
        self.assertEqual(1,check_landlord(18)[0][1])
        self.assertEqual("十里河佰汇出租企业主体名称",check_landlord(18)[0][2])
        self.assertEqual(1,check_landlord(18)[0][3])
        self.assertEqual("十里河佰汇",check_landlord(18)[0][4])

    # @unittest.skip("跳过")
    def test_2_landlord_query(self):
        print("通过门店id查询甲方信息")
        url="https://api-test.lefull.cn/records//api/v1/landlord"
        params={
            "apartmentId":18
        }
        res=requests.get(url=url,params=params)
        # print(res.text)
        # case_log.log_case_info("test_landlord_query",url,params,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("十里河佰汇",res.json()["data"]["cardName"])
        self.assertEqual("18",res.json()["data"]["apartmentId"])
        self.assertEqual("220422199006091234",res.json()["data"]["cardNo"])
        self.assertEqual("十里河佰汇出租企业主体名称",res.json()["data"]["landlordTitle"])

    # @unittest.skip("跳过")
    def test_3_landlord_alter(self):
        print("修改甲方信息")
        url="https://api-test.lefull.cn/records//api/v1/landlord"
        data={
            "apartmentId": "18",
            "cardName": "十里河佰汇修改",
            "cardNo": "220422199006091234",
            "cardType": 1,
            "ifOwner": 0,
            "landlordId":"f756d642973311e9af8c02420a001304",
            "landlordTitle": "十里河佰汇出租企业主体名称修改",
            "landlordType": 1,
            "mobile": "15910457777"
        }
        res=requests.post(url=url,json=data)
        # print(res.text)
        case_log.log_case_info("test_landlord_alter",url,data,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(18,check_landlord(18)[0][0])
        self.assertEqual(1,check_landlord(18)[0][1])
        self.assertEqual("十里河佰汇出租企业主体名称修改",check_landlord(18)[0][2])
        self.assertEqual(1,check_landlord(18)[0][3])

    # @unittest.skip("跳过")
    def test_4_landlord_geren(self):
        print("新增甲方信息-出租主体是个人时")
        url="https://api-test.lefull.cn/records//api/v1/landlord"
        data={
            "apartmentId": "15",
            "cardName": "传媒大学1",
            "cardNo": "220422199006096666",
            "cardType": 1,
            "ifOwner": 0,
            "landlordTitle": "",
            "landlordType": 0,
            "mobile": "15910457777"
        }
        res=requests.post(url=url,json=data)
        # print(res.text)
        case_log.log_case_info("test_landlord_geren",url,data,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(18,check_landlord(18)[0][0])
        self.assertEqual(1,check_landlord(18)[0][1])
        self.assertEqual("十里河佰汇出租企业主体名称修改",check_landlord(18)[0][2])
        self.assertEqual(1,check_landlord(18)[0][3])
        self.assertEqual("十里河佰汇修改",check_landlord(18)[0][4])

if __name__=="__main__":
    unittest.main(verbosity=2)