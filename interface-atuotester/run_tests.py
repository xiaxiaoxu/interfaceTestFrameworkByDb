#encoding=utf-8
import time, sys
sys.path.append('./script')
from utils.HTMLTestRunner import HTMLTestRunner
from io import BytesIO as StringIO
from unittest import defaultTestLoader
from interface.create_script import create_script
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 生成测试脚本
create_script()

if __name__ == "__main__":
    # 执行测试用例
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 指定测试用例为当前文件夹下的 interface 目录
    test_dir = './script'
    testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='接口自动化测试',description='接口自动化测试结果报告')
    runner.run(testsuit)
    fp.close()

