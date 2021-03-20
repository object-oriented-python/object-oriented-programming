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

.. _student_data:

.. csv-table:: Extract from some fictional student records. The full records
    are in the `course repository
    <https://github.com/object-oriented-python/object-oriented-programming>`__ 
    in :file:`data/students.csv`.
    :header-rows: 1
    :width: 70%

    FirstName,Surname,Username
    Patrick,Forth,PF1118
    Lorene,Vaux,LV1918
    Gwendolyn,Ulbrich,GU918
    Richard,Mccoy,RM518
    Marjorie,Jackson,MJ1418

:numref:`student_data` shows the first few records in a table of student data.
Having installed pandas:

.. code-block:: console

    $ python -m pip install pandas

the following code enables us to access the data from within Python:

.. code-block:: ipython

    In [1]: import pandas as pd

    In [2]: students = pd.read_csv("data/students.csv")

    In [3]: type(students)
    Out[3]: pandas.core.frame.DataFrame

    In [4]: students.keys()
    Out[4]: Index(['FirstName', 'Surname', 'Username'], dtype='object')

    In [5]: students['FirstName'][:6]
    Out[5]: 
    0      Patrick
    1       Lorene
    2    Gwendolyn
    3      Richard
    4     Marjorie
    5       Morgan
    Name: FirstName, dtype: object

    In [6]: type(students['FirstName'])
    Out[6]: pandas.core.series.Series

Observe that the :class:`~pandas.DataFrame` acts as a dictionary of
one-dimensional data :class:`~pandas.Series`. A :class:`pandas.Series` can be
indexed and sliced like any other Python :ref:`sequence type <typesseq>`. This
very high level introduction is all we'll need to use pandas in demonstrations
this week. Much more documentation is available on the `pandas website <https://pandas.pydata.org/docs/>`__.

.. note::

    This is not a course about data processing. Pandas is capable of working
    with very large data sets, but the techniques here are chosen for
    readability and not performance. If you want to use Pandas on data sets
    with more than a few thousand entries, you will need to consider techniques
    beyond those used here.

Using a debugger
----------------

The :term:`traceback` that the Python interpreter prints when it encounters an
untrapped exception provides a lot of information about an exception which has
occurred, but it's not all the information available, and it might not be
enough to work out the cause of the bug. The next tool in our forensic armoury
is called a :term:`debugger`, which is a software tool that enables us to stop and
examine a running program. This enables us to look at or set variables in any
of the :term:`frames <stack frame>` on the :term:`call stack`, or even type and
run Python code. This is exceptionally useful in determining the source of
errors.

Python has an inbuilt debugger, :mod:`pdb`, which is part of the Python
standard library. This is a highly capable debugger, however its command line
interface is essentially that of the default Python shell, with all the
limitations that brings. Just as `IPython <https://ipython.readthedocs.io>`_
provides a more powerful Python command line including features such as colour
syntax highlighting, tab completion, and better-formatted tracebacks, `ipdb
<https://github.com/gotcha/ipdb#ipython-pdb>`_ provides a somewhat friendlier
command line to the same set of debugger commands as :mod:`pdb`. ipdb has the
advantage that integrates well with IPython. Another advanced command-line
debugger is `pdb++
<https://github.com/pdbpp/pdbpp#pdb-a-drop-in-replacement-for-pdb>`__. The
distinct advantage of pdb++ is that it replaces the built-in pdb. Among other
things, this means it can be triggered from a failed `pytest
<https://docs.pytest.org/en/stable/>`__ test. 

The alternative to a command-line debugger is to use a graphical debugger
integrated with your :term:`IDE`. Visual Studio Code integrates with the
`debugpy` module, so we will learn to use that. In many respects, a graphical
debugger is the most powerful tool, however the convenience of being able to
easily drop into a command-line debugger from an interactive session or from a
failed test means that it is exceptionally useful to know how to use both kinds
of debugger.

Debuggers
.........

Other than the built-in pdb, debuggers typically come as Python packages, so to
install all the ones mentioned so far, run:

.. code-block:: console

    $ python -m pip install ipdb pdbpp debugpy

pdb++ isn't a legal package name, which is why the package in that case is
called pdbpp. 

Using a graphical debugger
--------------------------

.. dropdown:: Video: using a graphical debugger.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/520604326"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ab1c83e9-d1c8-42d1-821e-ace4010ae319>`__.

The simplest way to understand a graphical debugger is to see it in action, so
this section is provided by video rather than text. Microsoft also provide
documentation on `using the Python debugger in Visual Studio Code
<https://code.visualstudio.com/docs/python/debugging>`__.

Invoking a command-line debugger
--------------------------------

.. dropdown:: Video: command line debuggers.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/520605730"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f9dd4578-b7af-4208-8b04-ace4010bf486>`__.

A command-line debugger, by its very nature, is somewhat easier to explain in
text than is a graphical debugger. Command-line debuggers are both stand-alone
programs and Python modules that can be invoked from within a running program.
There are many ways of launching a debugger depending on the circumstances in
which an error occurs. Here we restrict ourselves to a few of the more common ones.

Postmortem debugging
....................

Postmortem debugging means using a debugger after an exception has
occurred (i.e. after the program has "died"). The default behaviour of
Python on an untrapped exception is to print a :term:`traceback` and
exit, in the case of a script, or continue with a new interactive
shell line in the case of an interactive shell. We, therefore, need to
take some positive action in order to have Python instead launch the
debugger on exception. The way we do this depends very much on how we were
using Python.

Invoking ipdb from within IPython
.................................

IPython supports a class of non-Python built-in commands called *magics*. A
magic is distinguished from a Python command by starting with a percent symbol
(`%`). There are two magics for debugging. If the last command raised a
:term:`exception` then `%debug` will launch ipdb at the site where the
exception was raised. Alternatively, you can use the `%pdb` magic to switch on
automatic debugger launching every time an untrapped exception occurs. `%pdb`
acts as a toggle switch, so you use the same command to switch off automatic
debugger calling.

Invoking pdbpp from a failed test
.................................

`Pytest <https://docs.pytest.org/en/stable/>`__ has built-in support for
calling a debugger at the point that a test exceptions. By default this
debugger is pdb, but if pdbpp is installed then it is called instead. The option to
do this is `--pdb`. However, in order to have a useful debugging session two
other options are usually required. The first issue is that, by default, pytest
does not print the output of tests. Using a debugger without seeing the output
is a somewhat fruitless endevour, so we pass `-s` to have pytest print all
output. Finally, if one test is failing then often many will, and we usually
want to work on one test at a time. We therefore run, for example:

.. code-block:: console

    $ pytest --pdb -s -x tests/test_pandas_fail.py

Invoking the debugger from a running program
............................................

The alternative to post-mortem debugging is to invoke the debugger from within
a program that is running normally. This is often useful if the erroneous
behaviour you are concerned about is not an exception but rather the
calculation of an incorrect value. This is a process entirely analogous to
inserting a :term:`breakpoint` in a graphical debugger, but instead of clicking
in an IDE window, insert a line of code. For ipdb, the line to insert is:

.. code-block:: ipython3

    import ipdb; ipdb.set_trace()

while pdb and pdbpp can use the built-in :func:`breakpoint()` function that was
introduced in Python 3.7, or use their own function:

.. code-block:: ipython3

    import pdb; pdb.set_trace()

Command-line debugger commands
------------------------------

Whichever way your command-line debugger is invoked, it will give you a command
line with a prompt somewhat different from the Python prompt, so that you know
that you're in the debugger. For example, the pdb++ prompt looks like this:

.. code-block:: python3

    (Pdb++)

All of the debuggers we are concerned with will support the same core set of
commands, though there are some differences in more advanced functionality. The
basic debugger commands are also typically similar between languages, so
learning to use ipdb will also help equip you with the skills to use, for
example, `gdb <https://www.gnu.org/software/gdb/>`__ on code written in
languages such as C and C++. :numref:`debug-commands` shows a basic set of
debugger commands that is enough to get started.

.. csv-table:: Common debugger commands. For a much more complete list see 
    `the pdb documentation <debugger-commands>`__. The part before the brackets
    is an abbreviated command which saves typing.
    :width: 100%
    :widths: 15, 60, 25
    :escape: '
    :name: debug-commands
    
    Command, Effect, Available postmortem
    h(elp), Print help. `h command` prints help on `command`., Yes
    s(tep), Execute the next instruction', stepping *into* function calls., No
    n(ext), Execute the next instruction', stepping *over* function calls., No
    c(ontinue), Continue execution until the next :term:`breakpoint`., No
    l(ist), List some lines of code arount the current instruction., Yes
    p `expression`, Evaluate `expression` and print the result., Yes
    u(p), Change the view to the :term:`stack frame` above this one., Yes
    d(own), Change the view to the :term:`stack frame` below this one., Yes
    q(uit), Quit the debugger and terminate the Python script., Yes

.. hint::

    It is also possible to simply type a Python expression into a debugger and
    have it print the result. This is a slightly dangerous practice in pdb and
    ipdb, because these debuggers will choose the debugger command in
    preference to evaluating a Python variable with the same name. This can
    mean that, rather than displaying the value of a variable called `q`, the
    debugger will just quit.

    pdb++ reverses this behaviour, so it will prefer evaluating a variable to
    executing a debugger command. Should you really need to execute a
    debugger command whose name coincides with a variable, you can do so by
    prefacing it with two exclamation marks:
     
    .. code-block:: python3

        (Pdb++) !!q

Debugging strategy
------------------

The tools and techniques we have discussed thus far are all about how to find
the source of a problem. However, how do you know that you've actually found
the root of the issue? 

There is an informal answer to this, which goes something along the lines of:

1. Observe an unexpected result (for example an exception or a wrong answer).
2. Use tools like a debugger, to find the first place that
   something is wrong.
3. Fix the code at that point.

This is intuitively appealing, and it is indeed the way that simple bugs are
often quickly fixed. However, it's a very hit and miss approach, and it's in
particular vulnerable to two problems. One is that finding the source of a bug
may be very difficult. The second is that you may easily find something
which you think is wrong with your code but which either isn't wrong, or is
wrong but isn't the cause of the particular problem you observe.

In order to overcome the limitations of this informal approach, it is necessary
to become much more systematic about debugging. An important part of this
systemisation is hypothesis testing.

Hypothesis testing in code
..........................

At this stage, it's informative to remind ourselves of the distinction
between logical truth in the mathematical sense, and experimentally
established knowledge in the scientific sense. A theorem is the
deductive consequence of its assumptions. So long as the logic is
valid, we can be assured that the theorem will be true in all
circumstances. Conversely, in science, there is no such absolute
certainty. A scientist states a hypothesis and then conducts
experiments which are designed in such a way that particular outcomes
would demonstrate that the hypothesis is false. If a suitably
exhaustive set of experiments is conducted then the scientist's
confidence in the hypothesis increases.

Software is simply a series of mathematical operations, so one might think that
the way to have correct software would be to mathematically prove it correct.
Though proving software is an important activity in theoretical computer
science, it is seldom a practical approach for most software. This leaves us
with the scientific approach. The program is our object of study, and the
hypothesis is that the program's functionality matches the mathematical process
that we intend it to embody. This general form of hypothesis is not of direct
use to us, but for any given program it yields any number of more specific
hypotheses that we can test directly. For example:

1. That when given input for which we know the expected output, the program
   will produce that output.
2. That when given incorrect input of a particular form, the expected
   :term:`exception` is raised.
3. That all the expected classes, functions, methods, and attributes exist and
   have the expected interfaces.
4. That the time taken and memory consumption of the program scale in the way
   predicted by the :term:`algorithmic complexity` of the algorithm.

These lead to very specific computations that can be undertaken to
experimentally validate the software. It's important to always remember that
experimental validation is not a proof: it's always possible that the cases
which would show that the program has a bug are simply not part of the suite of
tests being run.

Hypothesis-based debugging
..........................

What does all of this have to do with debugging? If you're debugging you
presumably already have an observed error. If you're lucky then it will be an
exception, and if you are less lucky then it will be the program returning the
wrong value. If the error is very obvious, then you may well immediately spot
the error and fix it. However if there is not an immediately obvious cause of
the problem, then the scientific hypothesis-based approach can help to produce
a somewhat systematic way to get out of trouble.

The recipe for hypothesis-based debugging runs something like the following:

1. Hypothesis Formation
   
   What statements would be true were this issue not occurring. For example:
    a. Are there variables which should have a known type or value, or would
       have a known type or value in response to a different input?
    b. Does it appear that a particular code that should have run already has
       not, or code that should not run has run?
    c. Looking at a value which I observe to be wrong, where is the operation that
       computes that value? Does a. or b. apply to any of the inputs to that
       operation.

This process requires intuition and understanding of the problem. This is the
least systematic part of the process. The following steps are much more systematic.

2. Hypothesis testing

   Based on 1, what calculation or observation (for example with a debugger)
   would falsify the hypothesis? I.e. how would I know if my hypothesis is
   wrong. For example, if my hypothesis is that a particular input will produce
   a particular value in a variable at a particular point in the calculation, I
   set a :term:`breakpoint` at the location I need to observe, and run the
   required calculation. By looking at the variable I can see whether I was
   wrong.
   
3. Hypothesis refinement

   Based on my hypotheses testing, I now have more information. I know that the
   hypothesis or hypotheses I have tested are false, or that there is reason to
   believe they are true. Using this information, I either now know exactly
   what is wrong and I can fix it, or I go back to step 1 and use this new
   information to make new hypotheses to test.


Test-driven development
.......................

It's not necessary to write the code in order to formulate hypotheses about
what a correctly performing program would do. Indeed, you are presumably
writing the software because you want it to do something, and in at least some
cases you know what that something should be. Furthermore, as soon as you write
code, the possibility exists that it contains bugs, so it will be necessary to
test it. People may be innocent until proven guilty, but code is presumed buggy
until thoroughly tested. The result of this reasoning is a strategy called
test-driven development, in which the tests that attempt to establish that a
piece of software performs correctly are written before the software itself.

Most of the exercises in this course are examples of test-driven
development: the tests are written to the problem specification, and you then
write code implementing the specification which you test using the tests.

Test-driven development is not only a good way of knowing when you have coded
correctly. The process of creating the tests is also a very good way of
establishing whether you understand the problem, and that specification is
well-posed.

Debugging tactics
-----------------

.. dropdown:: Video: minimal failing examples and bisection.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/520604328"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4f499827-2cce-4cbf-8a2e-ace4010ad8df>`__.


.. _debugging-mfe:

Creating a minimal failing example
..................................

One of the frequent problems encountered in debugging is that the program is
too large to understand all at once, and certainly far to large to show to
someone else to ask for help. If you are going to post a question in a web
forum, then you can usually include at most a couple of dozen lines of code if
you expect anyone to bother reading and responding to your work.

This means that one of the most effective debugging strategies is to make a
smaller piece of code which exhibits the same error. This is, in fact, a
special case of hypothesis-based debugging. What you need to do is form a
hypothesis about what parts of your code are relevant to your bug, and which do
not matter. You test this hypothesis by progressively removing the things you
think are irrelevant, each time testing that the bug still occurs. A minimal
failing example is the smallest piece of code that still fails in the same way
as the original code.

The mere process of forming a minimal failing example may be sufficient to reduce the
problem to such a simple piece of code that you can immediately see the cause
of the bug. It's also possible that the process of paring down the code will
reveal that the cause of the bug involved something of which you were unaware,
because the behaviour changes when something unexpected is removed. Even if
producing the minimal failing example does not shed light on the problem, you
at least now have a much smaller piece of code to ask for help with.

.. _bisection-debugging:

Bisection debugging
...................

Throughout this module we have used git as a mechanism for accessing and saving
code. However, revision control offers a lot more to the programmer than a
place to keep code. In particular, one of the key benefits is the ability to go
back to a previous version. This is particularly helpful in debugging
:term:`regressions <regression>`: things that used to work but no longer do. Of
course in a perfect world where we have full test suite coverage of all
functionality, and the test suite is run on every commit, this situation will
never occur. However the reality is that test coverage is never complete, and
there will always be untested functionality in any non-trivial piece of
software. Regressions are a particularly vexxing form of bug: there is little
more frustrating to be coming up to a deadline and to discover that something
that used to work no longer does.

If revision control has been used well over the course of a coding project, it
offers a mechanism for debugging regressions. We just have to roll back the
repository to previous versions until we find one in which the bug does not
occur. In fact, we can think of this process mathematically. We can think of
our repository as a function defined on the ordered set of commits which takes
a positive value at commits without the bug in question, and negative values at
commits which exhibit the bug. Our task is to find the zero of this function.
In other words, to find a pair of adjacent commits such that the bug is absent
in the first commit, but present in the second commit. Once we have established
this, then we know that the bug is caused by one of the (hopefully small) set
of changes introduced in that commit.

In finding a zero of an unknown function for which we have no information other
than the ability to evaluate it, our go to algorithm is bisection. We first
look back in the git history to find a commit at which the bug is not present.
That forms the start of our bisection interval. The end of the bisection
interval is a failing commit, such as the current state of the repository.
Next, we choose the commit half way between those two commits and check if it
passes. If it passes then we move the start of the interval to that commit, if
it fails then we move the end of the interval to that commit. We repeat this
process until the commits are adjacent. We then know that the later of these
two commits introduced the bug.

Bisection support in git
........................

Git has built-in support for bisection and can even automate the process. What
we need is the start and end points of our bisection interval, and a command
that we can run at the command line which succeeds if the bug is not present,
and fails if it is. 

Creating a test command
~~~~~~~~~~~~~~~~~~~~~~~

A pytest test is a perfect example of such a command, so we
in effect write the test that we wish had existed at the time the bug slipped
into our code. The bisection search effectively enables us to retrospectively
introduce this test into our repository. Because we're going to be rolling back
the state of our repository to before we created this command, this is one
exception to the rule that you must always commit all of your work to the git
repository. Make a copy of this command (for example the Python file containing
the pytest test) outside your repository. For the rest of this section, we'll
assume that you've created a pytest test in a file called :file:`bug_test.py`
which you have placed in the folder containing your repository (if you followed
the instructions in :numref:`week %s <programs_files>` then this folder might be
called :file:`principles_of_programming`). With the top folder of your
repository as the working directory, we would then run this test with:

.. code-block:: console

    $ python -m pytest ../bug_test.py

Finding the starting point
~~~~~~~~~~~~~~~~~~~~~~~~~~

We start by looking at the list of commit messages in our repository. This can
be accessed on the command line using:

.. code-block:: console

    $ git log

or by browsing the list of commits on GitHub. When you run git log, the
terminal will display a list of commits and commit messages that you can scroll
backwards and forwards using the arrow keys (:kbd:`⬆️` and :kbd:`⬇️`). Press
:kbd:`q` to return to the command line. Where to start looking for a failing
commit is a judgment call on your part. This is a test of how good your commit
messages are! If all else fails, try from the first commit in the repo. You
will obviously need to roll back the repository to one or more of these commits
in order to check if the bug is present there. The command to do that is:

.. code-block:: console

    $ git reset --hard 66a10d5d374de796827ac3152f0c507a46b73d60

Obviously you replace the commit ID with the commit you wish to roll back to.
We can see what we've done by checking the status of the repository:

.. code-block:: console

    $ git status
    On branch main
    Your branch is behind 'origin/main' by 7 commits, and can be fast-forwarded.
    (use "git pull" to update your local branch)

    nothing to commit, working tree clean

We could, for example, run our test to check if the bug is present:

.. code-block:: console

    $ python -m pytest ../bug_test.py

It's useful to know that you can retrieve the commit ID of the current state of
the repository with:

.. code-block:: console

    $ git rev-parse HEAD
    66a10d5d374de796827ac3152f0c507a46b73d60

If we want to take the repository back to the newest commit then we do as the
status message told us, and pull:

.. code-block:: console

    $ git pull

If we now check the status of our repository, we find we're at the head of our
branch with a clean working tree:

.. code-block:: console

    $  git status
    On branch main
    Your branch is up to date with 'origin/main'.
    
    nothing to commit, working tree clean

We may next need to repeat this process to find an end point for our bisection,
but since the usual scenario is that the bug is present in the current state of
the repository, we can simply use that.

Running the bisection
~~~~~~~~~~~~~~~~~~~~~

First, check that you are up to date with ``main`` (or whatever your current
branch is called). And that you know the commit id you want to start from. To
set up the bisection we run:

.. code-block:: console

    $ git bisect start HEAD 66a10d5d374de796827ac3152f0c507a46b73d60 -- 

Obviously you replace the commit ID with your starting point. ``HEAD`` is a git
shorthand for the current state of the repository, so it's a suitable end point
in most cases. You can also substitute an explicit commit ID there. The final
``--`` is required and acts to distinguish the commit IDs we are providing from
any files names that we might be passing to the command (we won't be covering
that case). Next we run the actual bisection:

.. code-block:: console

    $ git bisect run python -m pytest ../bug_test.py

When the bisection terminates, the current state of the repository will be on
the first commit that exhibits the bug. We can check the difference between
that commit and the previous one using:

.. code-block:: console

    $ git diff HEAD~1

Here ``HEAD~1`` refers to the previous commit. Indeed, if we thought that the
bug had been introduced in, say, the last 20 commits then we could have used
``HEAD~20`` as the starting point for our bisection search.

Once we are done finding our error, we need to end our bisection session with:

.. code-block:: console

    $ git bisect reset

This will return our repository to our starting point, which is usually the
most recent commit.

.. hint::

    There is a more complete description of git's bisection capabilities in the
    `official git documentation <https://git-scm.com/docs/git-bisect>`__.

.. warning::

    This is our first foray into moving around the history of our git
    repository. This is an exceptionally powerful debugging tool but it can
    also be somewhat confusing. In particular, make sure that you have ended
    your bisection session and that your repository is up to date with the
    ``main`` branch before you start fixing the bug.


Glossary
--------

 .. glossary::
    :sorted:

    breakpoint
        A line of code at which the debugger is instructed to
        stop. The debugger will stop every time the breakpoint is executed.

    debugger
        A piece of software which enables an interactive Python command
        line to be attached to a running, or just terminated, Python
        program. This enables the state of the program to be examined
        to determine the cause of problems.

    minimal failing example
        The shortest piece of code which exhibits a particular bug. A true
        minimal failing example contains no code which can be removed without
        the bug disappearing.

    postmortem debugging
        Running a :term:`debugger` on a piece of code after an exception has
        occurred (i.e. after the program has "died").

    regression
        A bug which occurs in the current version of a program which did not
        occur in a previous version. The functionality of the software has
        "gone backwards".

Exercises
---------

The exercises work a little differently this week, because the objective is not
to write code but to practice debugging techniques. The quiz is not on
BlackBoard but is instead a Google form, because that offers instant feedback.
You should work through the the exercises and quiz together. For most of exercises,
there are quiz questions which you will be able to answer if you are
successfully able to do the exercise.

Obtain the `skeleton code for these exercises from GitHub classroom
<https://classroom.github.com/a/mi6I-jcG>`__.

.. panels::
    :card: quiz shadow

    .. link-button:: https://forms.gle/cL5eZycNC9Js19uL7
        :text: This week's quiz
        :classes: stretched-link 

.. proof:exercise:: Debugging python code

    The skeleton code contains a Python script :file:`scripts/tests_report`.
    Run this script under the Visual Studio code debugger and answer the quiz
    questions about what you find.
    
.. proof:exercise:: Minimal failing example

    In the file :file:`scripts/tests_report_mfe.py` construct a :term:`minimal failing
    example` which exhibits the error you discovered in the previous section.
    Your minimal failing example should contain one import and one other line
    of code. :file:`tests/test_mfe.py` is a pytest test for this exercise.

.. proof:exercise:: Bisection

    The Unified Form Language (UFL) is a computer symbolic algebra package used to
    represent partial differential equations in software applying a numerical
    technique called the finite element method. Clone the `course fork of the
    UFL repository <https://github.com/object-oriented-python/ufl>`__. At some
    point in the past, the following code worked:

    .. code-block:: python3

        import ufl
        argyris = ufl.FiniteElement("Argyris", degree=6, cell=ufl.triangle)

    Use `git bisect` to identify the first commit at which this code failed,
    and the last commit at which it worked, and answer the corresponding quiz
    questions.