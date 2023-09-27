def except_demo(n):
    """Demonstrate all the clauses of a `try` block."""

    print(f"Attempting division by {n}")
    try:
        print(0./n)
    except ZeroDivisionError:
        print("Zero division")
    else:
        print("Division successful.")
    finally:
        print("Finishing up.")
