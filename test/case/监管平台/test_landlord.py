import unittest
from test.case.basecase import BaseCase
from common.db import check_landlord

class TestLandLord(BaseCase):

    def test_landlord_new(self):
        print("新增甲方信息")
        case_data = self.get_case_data("test_landlord_new")
        res=self.send_request(case_data)

        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(18,check_landlord(18)[0][0])
        self.assertEqual(1,check_landlord(18)[0][1])
        self.assertEqual("十里河佰汇出租企业主体名称",check_landlord(18)[0][2])
        self.assertEqual(1,check_landlord(18)[0][3])
        self.assertEqual("十里河佰汇",check_landlord(18)[0][4])

    def test_landlord_query(self):
        print("通过门店id查询甲方信息")
        case_data = self.get_case_data("test_landlord_query")
        res=self.send_request(case_data)

        # print(res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual("十里河佰汇",res.json()["data"]["cardName"])
        self.assertEqual("18",res.json()["data"]["apartmentId"])
        self.assertEqual("220422199006091234",res.json()["data"]["cardNo"])
        self.assertEqual("十里河佰汇出租企业主体名称",res.json()["data"]["landlordTitle"])


    def test_landlord_alter(self):
        print("修改甲方信息")
        case_data = self.get_case_data("test_landlord_alter")
        res=self.send_request(case_data)
        # print(res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(18,check_landlord(18)[0][0])
        self.assertEqual(1,check_landlord(18)[0][1])
        self.assertEqual("十里河佰汇出租企业主体名称修改",check_landlord(18)[0][2])
        self.assertEqual(1,check_landlord(18)[0][3])
        self.assertEqual("十里河佰汇修改",check_landlord(18)[0][4])


if __name__ == '__main__':
    unittest.main(verbosity=2)

