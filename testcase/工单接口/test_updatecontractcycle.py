import unittest
import requests

class TestUpdateContractCycle(unittest.TestCase):
    def test_updatacontractcycle(self):
        print("修改合同周期")
        url="https://api-test.lefull.cn/data/api/v1/updateContractCycle"
        data={
            "contractId":"883",
            "contractCycle":6,
            "operatorEmployeeId":"0",
            "subjectList":""
        }
        res=requests.post(url=url,json=data)
        print(res.text)