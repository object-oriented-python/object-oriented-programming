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

An important rule in iterpreting errors, the reasons for which we will
return to, is to always read the error message from the bottom up. In
this case, the last line contains the name of the exception which has
been raised :obj:`ZeroDivisionError`, followed by a colon, followed by
a descriptive string providing more information about what has gone
wrong. In this case, that more or less says the same as the exception
name, but that won't be the case for all exceptions. The four lines
above the exception are called a traceback. We'll return to
interpreting tracebacks presently. 

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

Tracebacks: finding errors
--------------------------




Exceptions
----------

Python has many types of exception built in, and Python developers can
define their own exceptions so there are many more defined in
third-party packages. The :doc:`full list of built-in exceptions
<library/exceptions>` is available in the Python documentation.
