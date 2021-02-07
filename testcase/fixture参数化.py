import pytest
@pytest.fixture()
def connectdb():
    print("连接数据库前")
    yield
    print("连接数据库后")

@pytest.fixture(params=[1,2,3])
def login(request):
    print("获取参数")
    data=request.param
    yield data  #yield可以起到返回数据的作用，并且可以记忆执行的位置，用例结束后可以从这个位置运行
    print("结束")


def test_case1(login):
    print("测试用例1")
    print(login)

def test_connctdb(connectdb):
    print("执行测试conntdb")

if __name__=="__main__":
    pytest.main(["-s","fixture参数化.py"])
