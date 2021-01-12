from fibonacci import fib


def test_fibonacci_values():

    for i, f in enumerate([1, 1, 2, 3, 5, 8]):
        assert fib(i+1) == f
