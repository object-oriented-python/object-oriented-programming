.. _debugging:

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
happens when this happens. Before calling the function, there is a
large amount of information which describes the context of the current
program execution. For example, there are all of the module, function,
and variable names which are in scope, and there is the record of
which instruction is next to be executed. This collection of
information about the current execution context is called a
:term:`stack frame`.

When a function is called, the Python interpreter creates a new stack
frame containing the local execution context of that
function. Importantly, the new stack frame contains a reference back
to the stack frame from which the function was called. This enables
execution of the calling routine to continue when the newly called
function returns. Because functions can call functions which call
functions and so on in a nearly limitless sequence, there can be a
number of stack frames in existence at any time. These form a sequence
back from the current function which is being executed, through the
function which called it, through the function that called that one
and so forth until the very first stack frame. This frame contains the
execution context for the Python script that the user ran, or for the
iPython shell or Jupyter notebook the user was typing into in the case
where the user worked interactively.

The trail of stack frames from the currently executing statement all
the way back to the user script or command line is an example of a
type of data structure called a :term:`stack`, which we will study in
more detail later. Consequently, the term for this collection of stack
frames is the :term:`call stack`. It is also sometimes called the
:term:`execution stack` or :term:`interpreter stack`.

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
folder `~/docs/object-oriented-programming/src/`). Specifically, the
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
`<ipython-input-5-141816221609>`. This is simply the Python
interpreter's internal name for a notional "file" containing one line
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
   

Using a debugger
----------------

The :term:`traceback` that the Python interpreter prints when it
encounters an untrapped exception provides a lot of information about
an exception which has occurred, but it's not all the information
available and it might not be enough to work out the cause of the
bug. The next tool in our forensic armoury is called a "debugger"
which is a software tool which attaches a Python command line to a
running or just terminated Python programme. This enables us to look
at or set variables in any of the :term:`frames <stack frame>` on the
:term:`call stack`, or even type and run Python code. This is
exceptionally useful in determining the source of errors.

Python has an inbuilt debugger, :mod:`pdb`, which is part of the
Python standard library. This is a highly capable debugger, however
its command line interface is essentially that of the default Python
shell, with all the limitations that brings. Just as `IPython
<https://ipython.readthedocs.io>`_ provides a more powerful Python
command line including features such as colour syntax highlighting,
tab completion, and better formatted tracebacks, `ipdb
<https://github.com/gotcha/ipdb#ipython-pdb>`_ provides a somewhat
friendlier command line to the same set of debugger commands as
:mod:`pdb`. We will therefore generally use :mod:`ipdb`, but in the
few circumstances where only :mod:`pdb` is abvailable, its usage is
very similar.

Obtaining :mod:`ipdb`
.....................

Because :mod:`ipdb` does not form a part of the standard library, you
may not always find it installed by default.

.. note::

   FIXME: Put in a link to the installation instructions here.

Postmortem debugging
....................

Postmortem debugging means using a debugger after an exception has
occured (i.e. after the program has "died"). The default behaviour of
Python on an untrapped exception is to print a :term:`traceback` and
exit, in the case of a script, or continue with a new interactive
shell line in the case of an interactive shell. We therefore need to
take some positive action in order to have Python instead launch the
debugger on exception.

Invoking the debugger on a running program
..........................................

   

Debugging strategy
------------------

.. _bisection-debugging:

Bisection debugging
...................




Raising and handling exceptions
-------------------------------

Creating new exception classes
..............................


Testing code
------------

However,
before we get there it's essential to introduce the concept of testing
and its implementation.

Testing as a science
~~~~~~~~~~~~~~~~~~~~

At this stage, it's informative to remind ourselves of the distinction
between logical truth in the mathematical sense, and experimentally
established knowledge in the scientific sense. A theorem is the
deductive consequence of its assumptions. So long as the logic is
valid, we can be assured that the theorem will be true in all
circumstances. Conversely, in science there is no such absolute
certainty. A scientist states a hypothesis, and then conducts
experiments which are designed in such a way that particular outcomes
would demonstrate that the hypothesis is false. If a suitably
exhaustive set of experiments is conducted then the scientists
confidence in the hypothesis 


Glossary
--------

 .. glossary::
    :sorted:

    debugger
       A piece of software which enables an interactive Python command
       line to be attached to a running, or just terminated, Python
       program. This enables the state of the program to be examined
       to determine the cause of problems.

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
