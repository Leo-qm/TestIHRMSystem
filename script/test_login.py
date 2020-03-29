# 导包
import  unittest
import logging
import app
from api.login_api import LoginApi
from utils import assert_common_utils

# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        ...

    # 编写测试用例
    # 登录成功
    def test01_login_success(self):
        # 定义登录成功所需的请求体
        jsonData = {"mobile":"13012345678","password":"123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData,app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

    # 密码错误
    def test02_password_is_error(self):
        # 定义密码错误所需的请求体
        jsonData = {"mobile": "13012345678", "password": "12345"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exist(self):
        # 定义账号不存在所需的请求体
        jsonData = {"mobile": "13012345670", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 输入手机号码有英文字符
    def test04_mobile_has_eng(self):
        # 定义机号码有英文字符所需的请求体
        jsonData = {"mobile": "1301234567a", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码有特殊字符
    def test05_mobile_has_special(self):
        # 定义特殊字符所需的请求体
        jsonData = {"mobile": "1301234567/", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空
    def test06_moible_is_None(self):
        # 定义手机号码为空所需的请求体
        jsonData = {"mobile": "", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_password_is_None(self):
        # 定义密码为空所需的请求体
        jsonData = {"mobile": "13012345678", "password": ""}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参-多出1个参数
    def test08_more_params(self):
        # 定义多参-多出1个参数所需的请求体
        jsonData = {"mobile": "13012345678", "password": "123456", "code":"000"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

    # 少参-缺少mobile
    def test09_less_mobile(self):
        # 定义少参-缺少mobile所需的请求体
        jsonData = {"password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test10_less_password(self):
        # 定义少参-缺少password所需的请求体
        jsonData = {"mobile": "13012345678"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参
    def test11_none_params(self):
        # 定义无参所需的请求体
        jsonData = None
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 99999, "系统繁忙")

    # 错误参数--输入错误的参数
    def test12_params_is_error(self):
        # 定义无参所需的请求体
        jsonData = {"mobile1": "13012345678", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 日志器打印登录结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
