"""Basic proof of life check for numpoly."""


def test_numpoly():
    import numpoly
    x = numpoly.symbols("x")
    p = x**2 + 3*x + 1

    assert numpoly.diff(p, x) == 2*x + 3
