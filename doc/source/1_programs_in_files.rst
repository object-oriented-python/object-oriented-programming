Programs in files
===================

You will previously have written Python code in Jupyter notebooks, and
possibly used an interactive Python environment such as
iPython. Jupyter notebooks are an excellent platform for writing and
documenting short pieces of code. However, they are much less good for
writing code which is designed to be used by other people. If the
intention is to write mathematical building blocks out of which more
complex algorithms can be constructed, then we need a different way of
storing code: one which is accessible in more automated ways than
typing in a web browser. As an introduction to writing code in files
we will first consider Python scripts. We'll then move on to making
code really reusable by creating Python modules and packages.

Python scripts and text editors
-------------------------------

A Python script is simply a plain text file containing Python code. If
we pass the file to Python, then all the code in the file will be
executed, it's that simple. So, we need a way to create files full of
Python code, and a way to feed them to Python. We create and edit
Python files with a program called a text editor. A good text editor
will help you to code by highlighting syntax, and helping with
indentation. Some text editors also feature advanced features such as
built-in access to documentation, or highlighting style problems in
your code. A more fully-featured option is an Integrated Development
Environment (IDE). IDEs combine an editor with a Python interpreter to
run your code, a debugger and often other features such as integration
with Git.

.. note::

   Fill in more details once it becomes apparent which editors we'll be using.

A first Python script
~~~~~~~~~~~~~~~~~~~~~

Tradition dictates that the first stand-alone program one writes in
any language simply prints out the string `Hello World`. Using a text
editor we create a file which we'll call `hello.py` containing just
the following line of Python code:

.. code-block:: python

   print("Hello World")

The `.py` file extension is not strictly required for Python scripts,
but it can be useful as it will cause most text editors to recognise
the file as a Python file. Having remembered to save `hello.py` to
disk from the text editor, we can now run the program. Open a
terminal, and change to the folder (directory) where you saved
`hello.py`. For example, if `hello.py` is in the directory `src` in
your home directory, then you would type the following:

.. code-block:: console

   ~ $ cd src
   src $ python3 hello.py

The dollar sign is the command prompt. Its different on some systems,
for example it's often a greater than sign (`>`). The text to the left
of the command prompt might also be different depending on which
terminal program you are using on which operating system, but we are
only concerned with the commands to the right of the prompt. The first
of these, `cd` (*change directory*) switches the current folder to
`src`. The second command actually runs the Python interpreter on
`hello.py`. Deepending on what is installed on your computer, it might
also be possible to leave off the `3` at the end of `python3`, however
on some systems the plain `python` command is still linked to the old
version 2 of Python, so it's better to be explicit and type
`python3`. When we press the `enter` key after the last line above,
our tiny Python script `hello.py` runs and the following is displayed:

.. code-block:: console

   Hello World

When to use scripts
~~~~~~~~~~~~~~~~~~~

The key advantage of a script is that it is repeatable: it can be
executed again and exactly the same commands will execute. Writing
scripts is an absolutely essential programming discipline in any
circumstance where you might want to know what you did and, possibly,
do it again. For example, suppose you have a project in a
computational statistics course, in which you need to apply a complex
sequence of operations to a dataset and then plot some resulting
quantities. You could simply do this in an interactive Python session,
but you are then totally dependent on your memory as to what
you did. If you make a mistake then you *might* notice an error in the
final result, but you will almost certainly not recall the inadvertent
mistake that led to it.

Conversely, had you written every step you took as a Python script
which outputs the final plot to a pdf for inclusion in your report,
you can go back over your work and find the error. A particularly
frustrating phenomenon, often encountered shortly before a submission
deadline, is to suddenly discover that something which used to work no
longer does. If you took the next logical step and committed your
scripts to a git repository, making a new commit every time you edit
it, you would also be able to go back and find the point at which the
script stopped working. We will return to this debugging technique in
:numref:`bisection-debugging`.


When not to use scripts
~~~~~~~~~~~~~~~~~~~~~~~

The one thing that scripts can do is run. This makes them an
exceptional tool for reproducing calculations. However, as
mathematicians and programmers we are also interested in building
tools which users can combine together in different ways. We also want
to make functions and other code objects which can be reused in
different contexts to perform more complex computations. Functions and
other data structures defined in a script can essentially only be used
in that script. As soon as a piece of code is intended to be used in
two different scripts, it should be taken out and placed in a
module. This means that scripts should usually be quite short lists of
calls out to code in modules. We'll see a simple example of this
shortly.

Modules
-------

A module is, like a script, a plain text file containing Python
code. Modules must have names ending in `.py`. So far, that's
identical to a script. Indeed, it's sometimes possible (though not
always advisable) to use the same file as both a script and a
module. The difference between a script and a module lies in how it is
used. A script is run, which means that a new Python interpreter
starts, executes the commands in the script, and then
exits. Conversely, a module is imported into a running Python
session. For example, suppose we create a file `fibonacci.py`
containing the following simple function:

.. code-block:: python

   def fib(n):
       """Return the n-th Fibonacci number."""
       if n == 0:
           return 0
       elif n == 1:
           return 1
       else:
           return fib(n-2) + fib(n-1)

If I now run IPython in the folder containing my new file
`fibonacci.py` then I will be able to import the :mod:`fibonacci`
module, and use the function :func:`fib`:

.. code-block:: ipython3

   In [1]: import fibonacci
   In [2]: fibonacci.fib(3)
   Out[2]: 2

Notice that we do not include the `.py` suffix when we import a
module. Importing a module provides access to whatever it
contains. This is a key tool in building up algorithms out of
components: we import the components we need at each stage of our
programs.

Importing and namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~

When we imported the module :mod:`fibonacci`, this created the name
`fibonacci` in the current environment. The code in `fibonacci.py` is
then run, and any names defined in that code (such as the function
:func:`fib`) are defined within the :term:`namespace` `fibonacci`. As we
begin to compose together code from different parts of mathematics,
the ability to separate identically named but different objects from
each other is essential. For example, Python has a module containing
core real-valued maths functions called :mod:`python:math`, and one
containing complex maths functions called
:mod:`python:cmath`. Clearly, it's important that we can distinguish
between :func:`python:math.sin` and :func:`python:cmath.sin`!

Other forms of import
~~~~~~~~~~~~~~~~~~~~~

Importing modules into their own namespaces is frequently what we
want: it clearly separates the names in the module from the names we
have defined ourselves, and makes it very obvious to a reader where
the names come from. The downside is that names in namespaces can be
quite long and cumbersome, which is particularly inconvenient if names
are to be used frequently or in the middle of formulae: you probably
don't really want to write :func:`math.sin` in every trig formula you
ever write. One alternative is to rename the module on import. This is
achieved using the keyword `as` in an import statement. For example,
it is usual to import the numerical Python module :mod:`numpy` in the
following way:

.. code-block:: python

   import numpy as np

This creates the local name :mod:`np <numpy>` instead of :mod:`numpy`,
so that the function for creating an evenly spaced sequence of values
between to end points is now accessible as :func:`np.linspace
<numpy.linspace>`.

A second option is to import particular names from a module directly
into the current namespace. For example, if we planned to use the
fuctions :func:`math.sin` and :func:`math.cos` a lot in our script, we
might use the following import statement:

.. code-block:: python

   from math import sin, cos

Now we can use the names :func:`sin <math.sin>` and :func:`cos
<math.cos>` directly. What if we also wanted to use a short name for
their complex counterparts? We can't have two functions with the same
name in a single :term:`namespace`. Fortunately, the keyword `as`
comes to our rescue again:

.. code-block:: python

   from cmath import sin as csin, cos as ccos

Renaming on import is a double-edged sword. You must always take care
that renaming does not add to confusion. As a somewhat extreme example
example, should you ever type the following code, you should expect
the wrath of your users to be without bounds:

.. code-block:: python

  from math import sin as cos, cos as sin

It is possible to import all of the names from a module into the current namespace:

.. code-block:: python

   from math import *

Now everything in the math module can be used without a namespace
prefix. This may seem superficially attractive, but actually importing
`*` is a frequent source of problems. For starters, if you import `*`
from more than one module, it becomes impossible for the reader of the
code to work out from which module each name comes. Further, if a
module from which you import `*` contains a name that you have already
used, then the meaning of that name will be overwritten with the one
from the module (without any warning or error). This is a frequent
source of confusion. For this reason, importing `*` is usually a bad
idea.

Python venvs
------------

Packages
--------

Relative imports
~~~~~~~~~~~~~~~~

Testing frameworks
------------------


Glossary
--------

 .. glossary::
    :sorted:

    module
       A text file containing Python code which is accessed using the :ref:`import statement <python:import>`.

    namespace
       A collection of names. Within a single namespace, each
       name has a single defined meaning. Names in different spaces
       can be referred to using the syntax `namespace.name` where
       `namespace` is an name for the namespace. namespaces are
       themselves named, so they can be nested (`namespace.inner_namespace.name`).

    scope
       The scope of a name is the section of code for which that name is valid.

    script
    program
       A text file containing a sequence of Python statements to be
       executed. In Python, program and script are synonymous.
