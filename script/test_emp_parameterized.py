# 按照设计顺序编写员工模块的增删改查场景测试用例脚本
# 如果能够按照设计顺序实现员工的增删改查，那么就证明，能够对员工模块进行操作了
# 也就证明大家能够使用代码完成接口测试了。

# 导包
import unittest
import logging

import requests
from app import HEADERS
import app
from api.login_api import LoginApi
from api.emp_api import EmpApi
from utils import assert_common_utils
from parameterized import parameterized
from utils import read_emp_data


# 创建测试类
class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()
        # 实例化封装的员工接口
        self.emp_api = EmpApi()
        # 定义员工模块的URL
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    def tearDown(self):
        pass

    # 编写测试员工增删改查的案例
    def test01_login(self):
        # 1 实现登录接口
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        app.HEADERS)
        #   获取登录接口返回的json数据
        result = response.json()
        # 输出登录的结果
        logging.info("员工模块登录接口的结果为：{}".format(result))
        #   把令牌提取出来，并保存到请求头当中
        token = result.get("data")
        app.HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("登录成功后设置的请求头为：{}".format(app.HEADERS))

    # 定义员工数据文件的路径
    filename = app.BASE_DIR + "/data/emp.json"

    @parameterized.expand(read_emp_data(filename, "add_emp"))
    def test02_add_emp(self, username, mobile, http_code, success, code, message):
        # 2 实现添加员工接口
        response = self.emp_api.add_emp(username, mobile, app.HEADERS)
        # 打印添加的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        #   把员工id提取出来，并保存到变量当中
        app.EMP_ID = add_result.get("data").get("id")
        # 打印获取的员工ID
        logging.info("app.EMPID为：{}".format(app.EMP_ID))
        # 断言
        assert_common_utils(self, response, http_code, success, code, message)

    @parameterized.expand(read_emp_data(filename, "query_emp"))
    def test03_query_emp(self, http_code, success, code, message):
        # 3 实现查询员工接口
        # 发送查询员工的接口请求
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        # 打印查询员工的结果
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, http_code, success, code, message)

    @parameterized.expand(read_emp_data(filename, "modify_emp"))
    def test04_modify_emp(self, username, http_code, success, code, message):
        # 4 实现修改员工接口
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(app.EMP_ID, username, app.HEADERS)
        # 打印修改员工的结果
        logging.info("修改员工的结果为：{}".format(response.json()))

        # 现在由于修改员工返回的响应数据当中，没有修改的username
        # 所有我们并不知道修改的username有没有成功
        # 那么怎么办？
        # 我们需要连接到ihrm数据库中，然后按照添加员工返回的员工id查询这个员工id对应的
        # username的值，如果数据库的username与修改的username一致，那么就证明修改成功了
        # 实际数据：数据库查询出来的数据；预期：修改的数据
        # 我们执行的SQL语句，在navicat中是查不到任何数据的，原因是因为执行完毕之后，员工被删除了
        # 如果添加员工失败，那么员工ID提取失败，也会导致查询失败
        # 导包
        import pymysql
        # 连接数据库
        conn = pymysql.connect(host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 定义SQL语句
        sql = "select username from bs_user where id={}".format(app.EMP_ID)
        # 输出SQL语句
        logging.info("打印SQL语句：{}".format(sql))
        # 执行查询的SQL语句
        cursor.execute(sql)
        # 获取执行结果
        result = cursor.fetchone()
        # 调试打印执行的SQL结果
        logging.info("执行SQL语句查询的结果为：{}".format(result))
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        # 断言数据库查询的结果
        self.assertEqual(username, result[0])

        # 断言
        assert_common_utils(self, response, http_code, success, code, message)

    @parameterized.expand(read_emp_data(filename, "delete_emp"))
    def test05_delete_emp(self, http_code, success, code, message):
        # 5 实现删除员工接口
        # 发送删除员工接口请求
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 打印删除员工的结果
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, http_code, success, code, message)