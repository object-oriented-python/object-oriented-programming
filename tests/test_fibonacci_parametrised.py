import pytest
from fibonacci import fib


@pytest.mark.parametrize("n, ans", enumerate((0, 1, 1, 2, 3, 5, 8)))
def test_fibonacci(n, ans):
    assert fib(n) == ans
