# 封装通用断言函数
import os
import json

def assert_common_utils(self,
                        response,
                        http_code,
                        success,
                        code,
                        message):
    # self：是从测试脚本中传入的测试类，继承了unittest.TestCase
    # response：也是从测试脚本中传入的响应数据
    # http_code,success,code,message4个是预期要断言的响应状态码、success的值、code和message的值
    self.assertEqual(http_code, response.status_code)  # 与用例中文档的预期响应状态码进行比较断言
    self.assertEqual(success, response.json().get("success"))  # 与用例文档中的预期json数据中的success的值进行比较
    self.assertEqual(code, response.json().get("code"))  # 与用例文档中预期json数据中的code进行比较
    self.assertIn(message, response.json().get("message"))  # 与用例文档中预期的json数据中的message进行比较

# 封装读取登录数据的函数
def read_login_data(filename):
    # filename：是指登录数据的路径和名称
    # with open(filename, "r", encoding="utf-8") as f:
    with open(filename, 'r', encoding='utf-8') as f:
        # 加载json数据 jsonData = json.load(f)
        jsonData = json.load(f)
        # 定义一个存放登录数据的空列表 result = []
        result_list = []
        # 遍历这个jsonData，取出每一条登录测试点的数据包括请求体和断言 for login_data in jsonData:
        for login_data in jsonData:
            # 将所有的登录数据以嵌套元组的形式存在空列表result_list中:
            # result_list.append(tuple(login_data.value()))
            result_list.append(tuple(login_data.values()))
    # 返回提取的数据 return result_list
    return result_list

def read_emp_data(filename, interface_name):
    # filename:员工的数据文件路径
    # interface_name:要加载的对应员工接口的数据(只有增删改查4个数字)
    with open(filename, 'r', encoding='utf-8') as f:
        # 把数据文件加载成json格式
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        # 存放员工的某个接口的数据到空列表
        result_list.append(tuple(jsonData.get(interface_name).values()))

    return result_list


if __name__ == '__main__':
    # 调试读取登录数据的代码
    filename = os.path.dirname(os.path.abspath(__file__)) + "/data/login.json"
    print("路径为：", filename)
    result = read_login_data(filename)
    print(result)

    # 调试读取员工数据的代码
    # filename = os.path.dirname(os.path.abspath(__file__)) + "/data/emp.json"
    # result = read_emp_data(filename, "modify_emp")
    # print(result)