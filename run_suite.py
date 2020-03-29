# 导包
import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner
from script.test_login_para import TestLogin
from script.test_emp_parameterized import TestEmp
import app

# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))
# 定义测试报告名称
# ihrm_report_path = app.BASE_DIR + "/report/ihrm {}.html".format(time.strftime("%Y%m%d %H%M%S"))
ihrm_report_path = app.BASE_DIR + "/report/ihrm.html"
with open(ihrm_report_path, 'wb') as f:
    # 实例化htmltestrunner
    runner = HTMLTestRunner(f, verbosity=2, title="IHRM人力资源管理系统", description="这是使用HTMLTestRunner_PY3生成的报告")
    # 使用实例化的htmltestrunner运行测试套件
    runner.run(suite)

print("更改输出数据，检查轮巡构建，最长不会超过一分钟。")