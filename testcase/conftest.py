import pytest


@pytest.fixture(params=[[1,2,3],[4,5,6]],ids=["case1","case2"])
def fixture_cal_add(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算结束")

@pytest.fixture(params=[[2,2,0],[4,5,-1]],ids=["case1","case2"])
def fixture_cal_sub(request):
    print("开始计算")
    data=request.param
    yield data
    print("计算结束")
@pytest.fixture(params=[[1,2,2],[4,5.0,20]],ids=["case1","case2"])
def fixture_cal_mul(request):
    print("开始计算")
    data=request.param
    yield data
    print("计算结束")
@pytest.fixture(params=[[1,2,0.5],[2,2,1]],ids=["case1","case2"])
def fixture_cal_div(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算结束")