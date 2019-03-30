#coding:utf-8


'''
单元测试
unittest模块

'''




import unittest

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('tear down')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('set up')

    @classmethod
    def tearDownClass(self):
    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
         print('tear down class')
         
    @classmethod
    def setUpClass(self):
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('set up class')

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例
        
    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例
        
if __name__ == '__main__':
    unittest.main()#运行所有的测试用例








