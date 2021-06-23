import pytest

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 创建计算器实例
@pytest.fixture()
def get_calculator():
    return Calculator()
