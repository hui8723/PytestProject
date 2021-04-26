import pytest
import time
import allure

# 并行执行命令：pytest -n xxx(并行数)
@pytest.mark.parametrize('x',list(range(10)))
def test_xdist(x):
    print(x)
    time.sleep(1)