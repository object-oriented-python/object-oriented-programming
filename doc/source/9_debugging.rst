.. _debugging:

Debugging and testing
=====================

In :ref:`week 6 <errors_and_exceptions>` we learned about :term:`exceptions
<exception>` and how to read the :term:`traceback` that is printed when an
unhandled exception is raised. This week we will look at other tools and
techniques that we can use to understand what is wrong with a piece of code,
and therefore how to fix it. Before we do that, we'll take a quick look at
pandas. 

Pandas
------

If you have just excitedly clicked on the link for this section hoping for
some material on cute furry animals from China then, regrettably, you are in
for a disappointment. `Pandas <https://pandas.pydata.org>`__ is a Python
package which supports data analysis in Python. It's introduced here partly
because it's a very useful tool for applied mathematicians and statisticians
who need to work with real data, and partly because it's a convenient somewhat
larger library on which to practice tools and techniques for debugging.

At the core of pandas is the :class:`~pandas.DataFrame` class, which is
a two-dimensional dataset somewhat analogous to a spreadsheet. Unlike, for
example, a :class:`numpy.ndarray`, a :class:`~pandas.DataFrame` is not indexed
by a pair of numbers, but is instead organised as a collection of named
one-dimensional :class:`pandas.Series` of data. One can think of a
:class:`pandas.Series` as a column of data with a title. This perhaps best
illustrated with an example.



.. note::

    This is not a course about data processing. Pandas is capable of working
    with very large data sets, but the techniques here are chosen for
    readability and not performance. If you want to use Pandas on data sets
    with more than a few thousand entries, you will need to consider techniques
    beyond those used here.

Using a debugger
----------------

The :term:`traceback` that the Python interpreter prints when it
encounters an untrapped exception provides a lot of information about
an exception which has occurred, but it's not all the information
available, and it might not be enough to work out the cause of the
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
tab completion, and better-formatted tracebacks, `ipdb
<https://github.com/gotcha/ipdb#ipython-pdb>`_ provides a somewhat
friendlier command line to the same set of debugger commands as
:mod:`pdb`. We will therefore generally use :mod:`ipdb`, but in the
few circumstances where only :mod:`pdb` is available, its usage is
very similar. Finally, IDEs come with built-in support for debuggers.

Obtaining :mod:`ipdb`
.....................

Because :mod:`ipdb` does not form a part of the standard library, you
may not always find it installed by default. However, it's simply a
Python package so you can install it with:

.. code-block:: console

   $ python -m pip install ipdb

Postmortem debugging
....................

Postmortem debugging means using a debugger after an exception has
occurred (i.e. after the program has "died"). The default behaviour of
Python on an untrapped exception is to print a :term:`traceback` and
exit, in the case of a script, or continue with a new interactive
shell line in the case of an interactive shell. We, therefore, need to
take some positive action in order to have Python instead launch the
debugger on exception.

Invoking the debugger on a running program
..........................................

   

Debugging strategy
------------------

.. _debugging-mfe:

Creating a minimal failing example
..................................

.. _bisection-debugging:

Bisection debugging
...................


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
circumstances. Conversely, in science, there is no such absolute
certainty. A scientist states a hypothesis and then conducts
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
