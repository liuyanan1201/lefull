import unittest
from test.case.basecase import BaseCase
from common.db import check_landlord

class TestRecordsBJPlot(BaseCase):
    def test_recordsbjplot(self):
        print("根据小区名称和区县id查询小区信息")
        case_data = self.get_case_data("test_recordsbjplot")
        res=self.send_request(case_data)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(17,res.json()["data"][0]["districtId"])

if __name__ == "__main__":
    unittest.main(verbosity=2)