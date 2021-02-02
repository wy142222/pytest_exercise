import pytest
import yaml

from cal import Cal
with open("cal.yaml") as f:
    data = yaml.safe_load(f)["con"]
    add_data=data["add"]
    div_data=data["div"]
    divids_data=data["divids"]

class TestCal:

    def setup_class(self):
        self.c = Cal()
        print("执行开始")
    def teardown_class(self):
        print("执行完成")

    @pytest.mark.parametrize(
        "a, b,expect", add_data
    )
    def testadd(self,a,b,expect):
        result=self.c.add(a,b)
        if type(result)==float:
            result=round(result,2)
        assert result==expect

    @pytest.mark.parametrize(
        # "a, b,expect",[(1, 1,1), (2, 2,1),(3,0,0),(3.3,1.1,3)],ids=["int","float","除数为0","小数"]
        "a, b,expect",div_data,ids=divids_data
    )
    def testdiv(self,a,b,expect):
        result1=self.c.div(a,b)
        if type(result1)==float:
            result1=round(result1,2)
        assert result1==expect
# pytest -v -m "high or medium" test_08_execute_with_m.py --html=TempTestReport/HtmlReport/test_08_report.html
