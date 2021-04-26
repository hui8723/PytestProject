import pytest
import allure


# allure生成文件命令：pytest --alluredir ./report/allure_raw --allure-servrities=blocker,critical
# allure生成可视化洁界面命令：allure server report/allure_raw

@allure.step("步骤一：点xxx")
def step_1():
    print("11")

@allure.step("步骤二：带你xxx")
def step_2():
    print("222")

@allure.feature("编辑工单接口")
class TestEdit():
    '''编辑工单'''

    # blocker，critical，normal，minor，trivial
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("这是一个xx用例")
    @allure.issue("https://blog.csdn.net/powerccna/article/details/55833030") #bug地址
    @allure.testcase("https://blog.csdn.net/powerccna/article/details/55833030")#用例地址
    @allure.title("标题")
    def test_1(self):
        '''用例描述：先登陆，再执行'''
        step_1()
        step_2()
        print("xxx")

    @allure.story("这是一个yyy的用例")
    def test_2(self):
        '''用例描述：yyy'''
        step_1()
        print("yyy")

# allure.attach报告可以展示许多不同类型的附件，用来补充测试，步骤等信息