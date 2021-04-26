import pytest
import logging

@pytest.fixture(scope='session',autouse=True)
def session():
    print("所有模块执行前运行")
    logging.basicConfig(level=logging.INFO)
    yield
    print("所有模块执行后运行")

@pytest.fixture(scope='module')
def module():
    print('before py file')
    yield
    print('after py file')

@pytest.fixture(scope='class')
def classFixture():
    print('before class')
    yield
    print('after class')

@pytest.fixture()
def function():
    print('before function')
    yield
    print('after function')

