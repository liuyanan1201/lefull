import unittest
import requests
from common import case_log

class TestRecordsBJPlot(unittest.TestCase):
    def test_recordsbjplot(self):
        print("根据小区名称和区县id查询小区信息")
        url="https://api-test.lefull.cn/records//api/v1/recordsBjPlot"
        params={
            "plotName":"天通苑",
            "district":"17"
        }
        res=requests.get(url=url,params=params)
        print(res.text)
        case_log.log_case_info("test_recordsBJplot",url,params,res.text)
        self.assertEqual("200",res.json()["code"])
        self.assertEqual("成功",res.json()["msg"])
        self.assertEqual(17,res.json()["data"][0]["districtId"])