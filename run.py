import unittest
from config import config
from common.HTMLTestReportCN import HTMLTestRunner
from common.send_email import send_report

suite = unittest.defaultTestLoader.discover("./test/case/监管平台")

if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(suite)
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file,"wb") as f:
        HTMLTestRunner(stream=f,title="乐乎-监管平台接口测试报告",description="测试报告").run(suite)

    if config.is_send_report:
        send_report()
        config.logging.info("发送成功")

    config.logging.info("测试结束"+"="*50)