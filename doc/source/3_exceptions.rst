Errors, exceptions, and debugging
=================================

It is a sight familiar to every programmer: instead of producing the
desired result, the screen is filled with seemingly unintelligible
garbage because an error has occured. Producing errors is an
unavoidable part of programming, so learning to understand and correct
them is an essential part of learning to program.

What is an error?
-----------------

In mathematics, we are used to the idea that an expression might not
be defined. For example, in the absence of further information,
:math:`0/0` does not have a well-defined value. Similarly, the string
of symbols :math:`3 \times \%` does not have a mathematical
meaning. It is likewise very easy to create statements or expressions
in a programming language which either don't have a well-defined
meaning, or which just don't amount to a meaningful statement within
the rules of the language. A mathematician confronting an undefined
mathematical expression can do little else than throw up their hands
and ask the author what they meant. The Python interpreter, upon
encountering code which has no defined meaning, responds similarly,
though rather than raising its non-existent hands, it raises an
exception. It is then up to the programmer to divine what to do next.

Let's take a look at what Python does in response to a simple
error:

.. code-block:: ipython3
  
    In [3]: 0./0.
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-3-4e5c12397e23> in <module>
    ----> 1 0./0.

    ZeroDivisionError: float division by zero

An important rule in iterpreting Python errors, the reasons for which we will
return to, is to always read the error message from the bottom up. In
this case, the last line contains the name of the exception which has
been raised :obj:`ZeroDivisionError`, followed by a colon, followed by
a descriptive string providing more information about what has gone
wrong. In this case, that more or less says the same as the exception
name, but that won't be the case for all exceptions. The four lines
above the exception are called a traceback. We'll return to
interpreting tracebacks presently.

Syntax errors
.............

Now consider the case of an expression that doesn't make mathematical sense:

.. code-block:: ipython3

    In [5]: 3 * %  
      File "<ipython-input-5-442f22cdc61f>", line 1
        3 * %
            ^
    SyntaxError: invalid syntax

This creates a syntax error, signified by a :obj:`SyntaxError`
exception. In programming languages, as with human languages, the
syntax is the set of rules which defines which expressions are
well-formed. Notice that the earlier lines of a syntax error appear
somewhat different to those of the previous exception. Almost all
exceptions occur because the interpreter attempts to evaluate an
statement or expression and encounters a problem. Syntax errors are a
special case: when a syntax error occurs, the interpreter can't even
get as far as attempting to evaluate because the sequence of
characters it has been asked to execute do not make sense in
Python. This does, however, have one advantage, which is that the
error message shows the precise point in the line at which the Python
interpreter found a problem. This is indicated by the caret symbol
(`^`). In this case, the reason that the expression doesn't make any
sense is that the modulo operator (`%`) is not a permissable second
operand to multiplication (`*`), so the Python interpreter places the
caret under the modulo operator.

Even though the Python interpreter will highlight the point at which
the syntax doesn't make sense, this might not quite actually be the
point at which you made the mistake. In particular, failing to finish
a line of code will result in the interpreter assuming that the
expression continues on the next line of program text, resulting in
the syntax error appearing to be one line later than it really
occurs. Consider the following code:

.. code-block:: python3

    a = (1, 2
    print(a)

The error here is a missing closing bracket on the first line, however
the error message which the Python interpeter prints when this code is run is:

.. code-block:: python3

      File "syntax_error.py", line 2
        print(a)
            ^
    SyntaxError: invalid syntax

To understand why Python reports the error on the line following the
actual problem, we need to understand that the missing closing bracket
was not by itself an error. The user could, after all, validly
continue the :class:`tuple` constructor on the next line. For example,
the following code would be completely valid:

.. code-block:: python3

    a = (1, 2
         )
    print(a)

This means that the Python interpreter can only know that something is
wrong when it sees `print`, because `print` cannot follow `2` in a
tuple constructor. The interpreter therefore reports that the `print`
is a syntax error.

.. hint::

   If the Python interpreter reports a syntax error at the start of a
   line, always check to see if the actual error is on the previous
   line.

Exceptions
----------

Python has many types of exception built in, and Python developers can
define their own exceptions so there are many more defined in
third-party packages. The :doc:`full list of built-in exceptions
<library/exceptions>` is available in the Python documentation.


Tracebacks: finding errors
--------------------------

The errors we have looked at so far have all been located in the top
level of code either typed directly into iPython or executed in a
script. However what happens if an error occurs in a function call, or
even several functions down? Consider the following code, which uses
the :class:`~polynomial.Polynomial` class from
:numref:`chapter %s <objects>`:

.. code-block:: ipython3

    In [1]: from polynomial import Polynomial

    In [2]: p = Polynomial(("a", "b"))

    In [3]: print(p)
    bx + a

So, perhaps surprisingly, we are able to define a polynomial whose
coefficents are letters, and we can even print the resulting
object. However, if we attempt to add this polynomial to the number 1,
we are in trouble:

.. code-block:: ipython3

    In [4]: print(1 + p)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-5-141816221609> in <module>
    ----> 1 print(1 + p)

    ~/docs/object-oriented-programming/src/polynomial.py in __radd__(self, other)
         57     def __radd__(self, other):
         58 
    ---> 59         return self + other

    ~/docs/object-oriented-programming/src/polynomial.py in __add__(self, other)
         38 
         39         if isinstance(other, Number):
    ---> 40             return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])
         41 
         42         elif isinstance(other, Polynomial):

    TypeError: can only concatenate str (not "int") to str

This is a much larger error message than those we have previously
encountered, however the same principles apply. We start by reading
the last line. This tells us that the error was a :class:`TypeError`.

