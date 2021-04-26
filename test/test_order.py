import pytest

# 安装pip install pytest-ordering
@pytest.mark.run(order=1)
def test_last():
    print("aa")
    assert 1!=2

@pytest.mark.last
def test_one():
    print("bb")
    assert 2==2

# 安装pip3 install pytest-assume    python -m pip install xxx
def test_assume():
    # 断言失败之后依然能执行
    pytest.assume(2==0)
    pytest.assume(1==2)

