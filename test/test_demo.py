import json
from pprint import pprint

import pytest
import requests
import settings


@pytest.fixture()
def login():
    return 'username:Jerry'

class TestA:

    def test_A(self, login):
        print(login)
        pprint(login) # 简单格式化输出

@pytest.mark.skip
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
])
def test_B(a,b):
    assert a+1 == b

def jsom_format():
    data = "aaa"
    # str -> json
    jsonData = json.loads(data)
    # json -> str
    datanNew = json.dumps(jsonData)


def test_C():
    pytest.xfail(reason='将用例定义为xfail，后续不会执行。')
    assert 1!=2

@pytest.mark.xfail
def test_D():
    print("此标记依然会执行所有用例，成功显示xpassed，失败显示xfailed")
    assert 1!=2

@pytest.mark.usefixtures("module")
@pytest.mark.usefixtures("classFixture")
@pytest.mark.usefixtures("function")
def test_F():
    print("pytest -v -m webtest 执行自定义标记的用例")
    assert 1!=2



def test_settings():
    print(settings.DATABASE['host'])
    assert 1 == 2

def test_weather():
    response = requests.request('get', 'http://api.k780.com/?app=weather.today&weaid=1&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json')
    # response = requests.request('get', 'https://www.tianqiapi.com/api/')
    print(response.json())