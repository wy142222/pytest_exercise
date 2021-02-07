import unittest

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("前置条件")

    @classmethod
    def tearDownClass(cls):
        print("恢复原始状态")
    def setUp(self):
        print("用例开始")
    def tearDown(self):
        print("用例结束")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        # self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
class Testdemo(unittest.TestCase):
    def test_add(self):
        self.assertTrue(2==2)

if __name__ == '__main__':
    #1.执行所有的用例
    # unittest.main()
    # 2.将用例加入容器执行
    # suite=unittest.TestSuite()
    # suite.addTest(TestStringMethods("test_split"))
    # suite.addTest(TestStringMethods("test_upper"))
    # unittest.TextTestRunner().run(suite)
    # 3.测试多个类
    # suite1=unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Testdemo)
    # suite=unittest.TestSuite(suite2,suite1)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    #4.测试多个.py文件
    test_dir="./testcase"
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="./test*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)