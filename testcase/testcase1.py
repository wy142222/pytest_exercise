'''
作业：
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
'''
import pytest
import cal
c= cal.Cal()
@pytest.mark.run(order=1)
def test_add(fixture_cal_add):
    add_result=c.add(fixture_cal_add[0],fixture_cal_add[1])
    assert add_result==fixture_cal_add[2]
@pytest.mark.run(order=4)
def test_div(fixture_cal_div):
    div_result=c.div(fixture_cal_div[0], fixture_cal_div[1])
    assert div_result==fixture_cal_div[2]
@pytest.mark.run(order=2)
def test_sub(fixture_cal_sub):
    sub_result=c.sub(fixture_cal_sub[0], fixture_cal_sub[1])
    assert sub_result == fixture_cal_sub[2]
@pytest.mark.run(order=3)
def test_mul(fixture_cal_mul):
    mul_result=c.mul(fixture_cal_mul[0], fixture_cal_mul[1])
    assert mul_result==fixture_cal_mul[2]
# pytest testcase1.py --alluredir=../report/allurereport/testcase1/result
# allure serve ../report/allurereport/testcase1/result