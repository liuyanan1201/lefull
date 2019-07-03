import os
import time
import logging

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

#数据库配置
db_host='123.56.216.225'
db_port=3306
db_user='root'
db_password='L3e5F7u8'
db='pms'

#文件路径配置
project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#日志文件根目录
log_file = os.path.join(project_path,'log','log_{}.txt'.format(today))

#报告文件路径
report_file = os.path.join(project_path,'report','report_{}.html'.format(now))

#数据用例文件路径
data_file = os.path.join(project_path,'data','data.xls')
data_file1 = os.path.join(project_path,'data','test_jgpt_data.xls')

#log配置
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a"
                    )


#邮件配置
smtp_server = "smtp.126.com"
smtp_user = "liuyn120731@126.com"
smtp_password = "liuyanan123"

receiver = ['694526779@qq.com','15910457235@163.com']
subject = "接口测试报告"
body = "hi,all,\n附件中是接口测试报告请查收。"

is_send_report = False
