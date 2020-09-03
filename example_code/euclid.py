def gcd(a, b):
    """Return the greatest common divisor of a and b using a recursive
    implementation of Euclid's algorithm."""
    try:
        return gcd(b, a % b)
    except ZeroDivisionError:
        return a
