.. code-block:: python3

    class a:
        def __init__(self, b):
            self.b = b

        def c(self):
            return float(self.b)


    d = a
    e = a(2)
    f = e.c()
    g = e.c
