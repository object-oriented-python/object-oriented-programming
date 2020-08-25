.. _errors_and_exceptions:

Errors and exceptions
=====================

It is a sight familiar to every programmer: instead of producing the
desired result, the screen is filled with seemingly unintelligible
garbage because an error has occurred. Producing errors is an
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
and ask the author what they meant. The :term:`Python interpreter`, upon
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

An important rule in interpreting Python errors, the reasons for which we will
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
exceptions occur because the interpreter attempts to evaluate a
statement or expression and encounters a problem. Syntax errors are a
special case: when a syntax error occurs, the interpreter can't even
get as far as attempting to evaluate because the sequence of
characters it has been asked to execute do not make sense in
Python. This does, however, have one advantage, which is that the
error message shows the precise point in the line at which the Python
interpreter found a problem. This is indicated by the caret symbol
(`^`). In this case, the reason that the expression doesn't make any
sense is that the modulo operator (`%`) is not a permissible second
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
the error message which the :term:`Python interpeter` prints when this code is run is:

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

This means that the :term:`Python interpreter` can only know that something is
wrong when it sees `print`, because `print` cannot follow `2` in a
tuple constructor. The interpreter, therefore, reports that the `print`
is a syntax error.

.. hint::

   If the Python interpreter reports a syntax error at the start of a
   line, always check to see if the actual error is on the previous
   line.

Exceptions
----------

Aside from syntax errors, which are handled directly by the
interpreter, errors occur when Python code is executed and something
goes wrong. In these cases the Python code in which the problem is
encountered must signal this to the interpreter. It does this using a
special kind of object called an :term:`exception`. When an exception
occurs, the interpreter stops executing the usual sequence of Python
commands. Unless the programmer has taken special measures, to which
we will return in :numref:`handling_exceptions`, the execution will
cease and an error message will result. 

Because there are many things that can go wrong, Python has many types
of exception built in. For example, if we attempt to access the number
2 position in a tuple with only two entries, then an
:class:`IndexError` exception occurs:

.. code-block:: ipython3

    In [1]: (0, 1)[2]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-1-def0bb43ba85> in <module>
    ----> 1 (0, 1)[2]

    IndexError: tuple index out of range

The exception type provides some indication as
to what has gone wrong, and there is usually also an error message and
sometimes more data to help diagnose the problem. The :doc:`full list
of built-in exceptions <library/exceptions>` is available in the
Python documentation. Python developers can define their own
exceptions so there are many more defined in third-party packages.

Tracebacks: finding errors
--------------------------

The errors we have looked at so far have all been located in the top
level of code either typed directly into iPython or executed in a
script. However, what happens if an error occurs in a function call or
even several functions down? Consider the following code, which uses
the :class:`~polynomial.Polynomial` class from
:numref:`chapter %s <objects>`:

.. code-block:: ipython3

    In [1]: from polynomial import Polynomial

    In [2]: p = Polynomial(("a", "b"))

    In [3]: print(p)
    bx + a

So, perhaps surprisingly, we are able to define a polynomial whose
coefficients are letters, and we can even print the resulting
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
encountered, however, the same principles apply. We start by reading
the last line. This tells us that the error was a :class:`TypeError`
caused by attempting to concatenate (add) an integer to a
string. Where did this error occur? This is a more involved question
than it may first appear, and the rest of the error message above is
designed to help us answer this question. This type of error message
is called a :term:`traceback`, as the second line of the error message
suggests. In order to understand this message, we need to understand a
little about how a Python program is executed, and in particular about
the call stack.

The call stack
..............

A Python program is a sequence of Python statements, which are
executed in a sequence determined by the flow control logic of the
program itself. Each statement contains zero or more function calls [#function]_,
which are executed in the course of evaluating that statement.

One of the most basic features of a function call is that the contents
of the function execute, and then the code which called the function
continues on from the point of the function call, using the return
value of the function in place of the call. Let's think about what
happens when this occurs. Before calling the function, there is a
large amount of information which describes the context of the current
program execution. For example, there are all of the module, function,
and variable names which are in scope, and there is the record of
which instruction is next to be executed. This collection of
information about the current execution context is called a
:term:`stack frame`. We learned about :term:`stacks <stack>` in
:numref:`stacks`, and the term "stack frame" is not a coincidence. The
Python interpreter maintains a :term:`stack` of stack frames called
the :term:`call stack`. It is also sometimes called the
:term:`execution stack` or :term:`interpreter stack`.

The first frame on the stack contains the execution context for the
Python script that the user ran or, in the case where the user worked
interactively, for the iPython shell or Jupyter notebook into which
the user was typing. When a function is called, the Python interpreter
creates a new stack frame containing the local execution context of
that function and pushes it onto the call stack. When that function
returns, its stack frame is popped from the call stack, leaving the
interpreter to continue at the next instruction in the stack frame
from which the function was called. Because functions can call
functions which call functions and so on in a nearly limitless
sequence, there can be a number of stack frames in existence at any
time.

.. note::

   FIXME: put in an illustration of a call stack here. Probably an
   animation.

Interpreting tracebacks
.......................

Let's return to the traceback for our erroneous polynomial addition:

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

This shows information about a :term:`call stack` comprising three
:term:`stack frames <stack frame>`. Look first at the bottom-most
frame, which corresponds to the function in which the exception
occured. The traceback for this frame starts:

.. code-block:: ipython3

    ~/docs/object-oriented-programming/src/polynomial.py in __add__(self, other)

This indicates that the frame describes code in the file
`polynomial.py` (which on the author's computer is located in the
folder `~~/docs/object-oriented-programming/src/`). Specifically, the
stack frame describes the execution of the :meth:`__add__` method,
which is the :term:`special method` responsible for polynomial
addition. The lines below this show the line on which execution
stopped (line 40, in this case) and a couple of lines on either side,
for context.

The stack frame above this shows the function from which the
:meth:`__add__` method was called. In this case, this is the reverse
addition :term:`special method`, :meth:`__radd__`. On line 59 :meth:`__radd__` calls
:meth:`__add__` through the addition of `self` and `other`.

Finally, the top stack frame corresponds to the command that the user
typed in iPython. This stack frame looks a little different from the
others. For starters, instead of the file name there is the string
`<ipython-input-5-141816221609>`. This is simply the :term:`Python
interpreter`'s internal name for a notional "file" containing one line
of iPython input. Similarly, because the line the user typed is not in
any function, the interpreter treats it as code written in the top
level of an unnamed module called `<module>`. Finally, because the
interpreter treats every line of input as a separate file, the call to
:meth:`__radd__` implementing the reverse addition of the number 1 to
the polynomial `p` occurs on line 1 even though we are on the fourth
line of the iPython session.

.. hint::

   The proximate cause of the error will be in the last :term:`stack
   frame` printed, so always read the :term:`traceback` from the
   bottom up. However, the ultimate cause of the problem is likely to
   be further up the :term:`call stack`, so don't stop reading at the
   bottom frame!

.. _handling_exceptions:

Raising and handling exceptions
-------------------------------

Thus far we've noticed that an exception occurs when something goes
wrong in a program, and that the :term:`Python interpreter` will stop
at that point and print out a :term:`traceback`. We'll now examine the
process by which an exception occurs, and look at how to handle
exceptions without the program coming to a halt.

An exception is triggered using the :keyword:`raise` keyword. For
example, suppose we want to ensure that the input to our Fibonacci
function is an integer. All Python integers are :term:`instances
<instance>` of :class:`numbers.Integral`, so we can check this. If we
find a non-integer type then the consequence should be a
:class:`TypeError`. This is achieved by *raising* the appropriate
exception, using the :keyword:`raise` statement. The keyword
:keyword:`raise` is followed by the exception. Almost all exceptions
take a string argument, which is the error message to be printed. In
:numref:`typesafe_fib`, we inform the user that we were expecting an
integer rather than the type actually provided.

.. _typesafe_fib:

.. code-block:: python3
   :emphasize-lines: 6,7,8
   :caption: A version of the Fibbonacci function which raises an
             exception if a non-integer type is passed as the
             argument.

   from numbers import Integral

   def typesafe_fib(n):
       """Return the n-th Fibonacci number, raising an exception if a
       non-integer is passed as n."""
       if not isinstance(n, Integral):
              raise TypeError(
                     f"fib expects an integer, not a {type(n).__name__}")
       if n == 0:
           return 0
       elif n == 1:
           return 1
       else:
           return fib(n-2) + fib(n-1)

If we now pass a non-integer value to this function, we observe the following:


.. code-block:: ipython3

    In [2]: typesafe_fib(1.5)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-2-c3aeb16193d4> in <module>
    ----> 1 typesafe_fib(1.5)

    ~/docs/object-oriented-programming/fibonacci/fibonacci.py in typesafe_fib(n)
         14        non-integer is passed as n."""
         15        if not isinstance(n, Integral):
    ---> 16               raise TypeError(
         17                      f"fib expects an integer, not a {type(n).__name__}")
         18        if n == 0:

    TypeError: fib expects an integer, not a float

This is exactly what we have come to expect: execution has stopped and
we see a :term:`traceback`. Notice that the final line is the error
message that we passed to :class:`TypeError`. The only difference
between this and the previous errors we have seen is that the bottom
:term:`stack frame` explicitly shows the exception being raised, while
previously the stack showed a piece of code where an error had
occured. This minor difference has to do with whether the particular
piece of code where the exception occured is written in Python, or is
written in a language such as C and called from Python. This
distinction is of negligible importance for our current purposes.

.. note::

   An exceptionally common mistake that programmers make when first
   trying to work with exceptions is to write:

   .. container:: badcode

      .. code-block:: python3

      return Exception

   instead of:

   .. container:: goodcode

   .. code-block:: python3

         raise Exception

   This mistake is the result of a confusion about what
   :keyword:`return` and :keyword:`raise` do. :keyword:`return` means
   "the function is finished, here is the result". :keyword:`raise`
   means "something exceptional happened, execution is stopping
   without a result".

Handling exceptions
...................

So far we have seen several different sorts of exception, how to raise
them, and how to understand the resulting :term:`traceback`. The
:term:`traceback` is very helpful if the exception was caused by a bug
in our code, so that we need to understand and correct the
error. However, sometimes an exception is a valid result of a valid
input, and we just need the program to do something out of the
ordinary to deal with the situation. For example, Euclid's algorithm
for finding the greatest common divisor of :math:`a` and :math:`b` can
very nearly be written recursively as:

.. code-block:: python

   def gcd(a, b):
       return gcd(b, a % b)

This works right up to the point where `b` becomes zero, at which
point we should stop the recursion and return `a`. What actually
happens if we run this code? Let's try:

.. code-block:: ipython

       In [5]: gcd(10, 12)
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-5-d0750d9f2658> in <module>
    ----> 1 gcd(10, 12)

    <ipython-input-4-1ab7512041a6> in gcd(a, b)
          1 def gcd(a, b):
    ----> 2     return gcd(b, a % b)

    <ipython-input-4-1ab7512041a6> in gcd(a, b)
          1 def gcd(a, b):
    ----> 2     return gcd(b, a % b)

    <ipython-input-4-1ab7512041a6> in gcd(a, b)
          1 def gcd(a, b):
    ----> 2     return gcd(b, a % b)

    <ipython-input-4-1ab7512041a6> in gcd(a, b)
          1 def gcd(a, b):
    ----> 2     return gcd(b, a % b)

    ZeroDivisionError: integer division or modulo by zero

Notice how the recursive call to :func:`gcd` causes several
:term:`stack frames <stack frame>` that look the same. That makes
sense: Euclid's algorithm runs until `b` is zero, and then we get a
:class:`ZeroDivisionError` because modulo zero is undefined. To
complete this function, what we need to do is to tell Python to stop
at the :class:`ZeroDivisionError` and return `a`
instead. :numref:`gcd` illustrates how this can be achieved.

.. _gcd:

.. code-block:: python3
    :caption: A recursive implementation of Euclid's algorithm which
              catches the :class:`ZeroDivisionError` to implement the
              base case.
    :emphasize-lines: 2,4,5

    def gcd(a, b):
        try:
            return gcd(b, a % b)
        except ZeroDivisionError:
            return a

The new structure here is the :keyword:`try`... :keyword:`except`
block. The :keyword:`try` keyword defines a block of code, in this
case just containing `return gcd(b, a % b)`. The :keyword:`except` is
optionally followed by an exception class, or a tuple of exception
classes. This case, the :keyword:`except` is only followed by the
:class:`ZeroDivisionError` class. What this means is that if a
:class:`ZeroDivisionError` is raised by any of the code inside the
:keyword:`try` block then, instead of execution halting and a
:term:`traceback` being printed, the code inside the :keyword:`except`
block is run.

In the example here, this means that once `b` is zero, instead of
`gcd` being called a further time, a is returned. If we run this
version of :func:`gcd` then we have, as we might expect:

.. code-block:: ipython3

    In [2]: gcd(10, 12)
    Out[2]: 2

Creating new exception classes
------------------------------


Exceptions are not always errors
--------------------------------


Glossary
--------

 .. glossary::
    :sorted:

    stack frame
        An object encapsulating the set of variables which define the
        execution of a Python script or function. This information
        includes the code being executed, all the local and gobal
        names which are visible, the last instruction that was
        executed, and a reference to the stack frame which called this
        function.

    call stack
    execution stack
    interpreter stack
        The :term:`stack` of :term:`stack frames <stack frame>` in existence. The
        current item on the stack is the currently executing function,
        while the deepest item is the stack frame corresponding to the
        user script or interpreter.

    syntax
        The set of rules which define what is a well-formed Python
        statement. For example the rule that statements which start
        blocks must end with a colon (:) is a syntax rule.

    syntax error
        The :term:`exception` which occurs when a statement violates
        the :term:`syntax` rules of Python. Mismatched brackets,
        missing commas, and incorrect indentation are all examples of
        syntax errors.

    traceback
    stack trace
    back trace
        A text representation of the :term:`call stack`. A traceback
        shows a few lines of code around the current execution point
        in each :term:`stack frame`, with the current frame at the
        bottom and the outermost frame at the top.
      
.. rubric:: Footnotes


.. [#function] "Function call" here includes :term:`method` calls and
               operations implemented using a :term:`special method`.
