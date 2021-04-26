import pytest

'''
-v:指定以某种形式运行用例
-m 以mark方式运行
-k：匹配用例名称
只运行smoke的用例
pytest -v -m smoke

运行smoke以外的用例
pytest -v -m "not smoke" 
'''

@pytest.mark.web
def test_web():
    print("web test")

@pytest.mark.smoke
def test_smoke():
    print("smoke test")

@pytest.mark.secure
def test_secure():
    print("secure test")
    assert 2!=2