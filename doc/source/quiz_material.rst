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


.. code-block:: python3

    False if a and b else True

.. code-block:: python3

    not (a and b)

.. code-block:: python3

   not a and b

.. code-block:: python3

   not a or not b

.. code-block:: python3

   a and b

.. code-block:: python3

   (not a) and b

`not` has `and`

`integrate`

`IntegrationMeasure`

`__hash__`

`_prepare_integration`

`problemDomain`

`Lebesgue_Measure`

.. code-block:: ipython3

    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    ~/traceback.py in <module>
        15 
        16 
    ---> 17 print(b(5, 2, 0))

    ~/traceback.py in b(x, y, z)
        5 def b(x, y, z):
        6     s = a(x, y)
    ----> 7     t = c(s, z)
        8     return t
        9 

    ~/traceback.py in c(x, y)
        11 def c(x, y):
        12     if x > y:
    ---> 13         return c(x-1, y)
        14     return a(x, y)
        15 

    ~/traceback.py in c(x, y)
        11 def c(x, y):
        12     if x > y:
    ---> 13         return c(x-1, y)
        14     return a(x, y)
        15 

    ~/traceback.py in c(x, y)
        11 def c(x, y):
        12     if x > y:
    ---> 13         return c(x-1, y)
        14     return a(x, y)
        15 

    ~/traceback.py in c(x, y)
        12     if x > y:
        13         return c(x-1, y)
    ---> 14     return a(x, y)
        15 
        16 

    ~/traceback.py in a(x, y)
        1 def a(x, y):
    ----> 2     return x/y
        3 
        4 
        5 def b(x, y, z):

    ZeroDivisionError: float division by zero


.. code-block:: python3

    assert math.isclose(calc.peek(), answer, rel_tol=1.e-5), \