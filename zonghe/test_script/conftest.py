'''
脚本层的一些公共方法
'''
'''
python导入包的规则，搜索包的规则：
1.使用IDE执行时：当前工程路径、当前执行文件路径、python安装目录下找包
2.命令行执行时：当前执行文件路径、python安装目录下找包
命令行执行时，报错找不到包。解决办法：把工程路径，放到sys.path中
'''
import sys
import os

cp = os.path.realpath(__file__)
cd = os.path.dirname(cp)
cd = os.path.dirname(cd)
cd = os.path.dirname(cd)
sys.path.append(cd)
import pytest

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests

env_path = r"data_env\env.ini"


# 读取env.ini中的url，设置session级别的，整个执行过程读一次
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path, "url")


@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path, "db"))


# 创建一个BaseRequests的实例，设置session级别的，整个执行过程只有一个实例，自动管理cookie
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()
