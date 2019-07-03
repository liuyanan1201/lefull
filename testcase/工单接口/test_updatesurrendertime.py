import unittest
import requests
from common.db import check_updatesurrendertime
from common import case_log

class TestUpdateSurrenderTime(unittest.TestCase):
    def test_updatesurrendertime(self):
        print("修改退租时间")
        url="https://api-test.lefull.cn/data/api/v1/surrender/updateSurrenderTime"
        data={
            "contractId":"10",
            "surrenderTime":1470412800
        }
        res=requests.post(url=url,data=data)
        print(res.text)
        case_log.log_case_info("test_updatesurrendertime",url,data,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(1,res.json()["data"])
        self.assertEqual(1470412800,check_updatesurrendertime(10)[0][0])