""" bind_pool_executor 测试模块。"""

from bind_pool_executor import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Rontomai"
    assert __email__ == "rontomai@gmail.com"
    assert __version__ == "0.1.3"
