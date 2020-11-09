

def except_demo(n):
    """A simple demonstration of all the clauses of a :keyword:`try` block."""

    print(f"Attempting division by {n}")
    try:
        print(0./n)
    except ZeroDivisionError:
        print("Zero division")
    except TypeError:
        print(f"Can't divide by a {type(n).__name__}.")
    else:
        print("Division successful.")
    finally:
        print("Finishing up.")
