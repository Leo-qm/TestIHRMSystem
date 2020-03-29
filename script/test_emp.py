# 按照设计顺序编写员工模块的增删改查场景测试用例脚本
# 如果能够按照设计顺序实现员工的增删改查，那么就证明，能够对员工模块进行操作了
# 也就证明大家能够使用代码完成接口测试了。

# 导包
import unittest
import logging
from utils import assert_common_utils
import requests
from api.emp_api import EmpApi
import app
from api.login_api import LoginApi


# 创建测试类
class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()
        self.emp_api = EmpApi()
        # 定义员工模块的URL
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    def tearDown(self):
        pass

    # 编写测试员工增删改查的案例
    def test01_test_emp_operation(self):
        # 1 实现登录接口
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        headers=app.HEADERS)
        #   获取登录接口返回的json数据
        result = response.json()
        # 输出登录的结果
        logging.info("员工模块登录接口的结果为：{}".format(result))
        #   把令牌提取出来，并保存到请求头当中
        token = result.get("data")
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 打印拼接完成的请求头
        logging.info("登录成功后设置的请求头为：{}".format(headers))

        # 2 实现添加员工接口
        response = self.emp_api.add_emp("1号选手蔡徐坤",
                                        "17643982666",
                                        headers)
        # 打印添加的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        #   把员工id提取出来，并保存到变量当中
        emp_id = add_result.get("data").get("id")
        # 打印获取的员工id
        logging.info("添加员工的id为：{}".format(emp_id))
        # 断言
        assert_common_utils(self,response,200,True,10000,"操作成功")

        # 3 实现查询员工接口
        # 发送查询员工的接口请求
        response = self.emp_api.query_emp(emp_id, headers)
        # 打印查询员工的结果
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

        # 4 实现修改员工接口
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(emp_id, "蔡徐坤爱打篮球", headers)
        # 打印修改员工的结果
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

        # 5 实现删除员工接口
        # 发送删除员工接口请求
        response = self.emp_api.delete_emp(emp_id, headers)
        # 打印删除员工的结果
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
