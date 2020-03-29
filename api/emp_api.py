# 导包
import requests

# 创建封装的测试类
class EmpApi:
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    def add_emp(self,username,mobile,headers):
        # 定义添加员工的请求头
        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2020-03-16",
                    "formOfEmployment": 2,
                    "departmentName": "snowsnow",
                    "departmentId": "1226092852421177344",
                    "correctionTime": "2020-03-15T16:00:00.000Z"
                    }
        return requests.post(url=self.emp_url,
                             json=jsonData,
                             headers=headers
                             )
    def query_emp(self,emp_id,headers):
        # 拼接查询员工的url
        query_emp_url = self.emp_url + "/" + emp_id
        return requests.get(url=query_emp_url,headers = headers)

    def modify_emp(self, emp_id, username, headers):
        # 拼接修改员工的URL
        modify_emp_url = self.emp_url + "/" + emp_id
        # 设置修改的请求体
        jsonData = {"username":username}
        return requests.put(url=modify_emp_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        # 拼接删除员工的URL
        delete_emp_url = self.emp_url + "/" + emp_id
        return requests.delete(url=delete_emp_url, headers=headers)
