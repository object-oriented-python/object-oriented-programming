.. _programs_files:

Programs in files
===================

This week we will start to learn how to combine pieces of code into larger units,
and how to package up your code so that you or others can do the same. 
You will previously have written Python code in Jupyter notebooks, and
possibly used an interactive Python environment such as
iPython. Jupyter notebooks are an excellent platform for writing and
documenting short pieces of code. However, they are much less good for
writing code which is designed to be used by other people. If the
intention is to write mathematical building blocks out of which more
complex algorithms can be constructed, then we need a different way of
storing code: one which is accessible in more automated ways than
typing in a web browser. As an introduction to writing code in files,
we will first consider Python scripts. We'll then move on to making
code really reusable by creating Python modules and packages.

Setting up a Python environment for this course
-----------------------------------------------

.. dropdown:: Video: setting up your virtual environment.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/486546635"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=011d73de-d93c-4dc8-8996-ac8501521b33>`__


During this course, we're going to create, edit, and install a whole bunch of
Python packages. In order to have a predictable programming environment in which
the experiments we're doing don't interfere with anything outside the course for
which we might be using Python, and conversely to ensure that nothing we've
installed elsewhere interferes with how we're doing the course, we'll do
everything in a Python :term:`virtual environment`, or :term:`venv`. You should read up on Python
virtual environments on the :ref:`Faculty of Natural Sciences Python installation
page <fons:python_virtual_environments>`.

.. hint::

   Don't forget that you need to activate the venv in every new :ref:`terminal <fons:terminal>` session.

Installing Python packages
--------------------------

Suppose we've created and activated a venv, and now there's a Python
package we'd like to have access to. Installation of Python packages
is handled by :doc:`pip:index`. Pip has many usage options, which
enable a large number of different installation
configurations. However, for most users most of the time, a few simple
pip commands suffice. As with :term:`venv` creation, package
installation is best accomplished from the terminal and not from
within Python itself. Don't forget to activate the venv!

Installing packages from PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PyPI <https://pypi.org>`__ is the Python Package Index. It is the
official download location for publicly released Python packages which
aren't themselves a part of the built-in :doc:`Python Standard Library
<python:library/index>`. Many important mathematical packages
including :mod:`numpy` and `sympy <https://www.sympy.org>`__ are
distributed from PyPI. Suppose your venv doesn't have :mod:`numpy`
installed and you need it. You would install it with the following
terminal command:

.. code-block:: console

   (my_venv) $ python -m pip install numpy

It is also possible to invoke pip directly using the command `pip3`,
but there are some circumstances where that might result in pip using
the wrong Python installation. The approach used here is safer.

Python packages may depend on other Python packages, so it's quite
likely that pip will install more packages than those you directly
asked for. This is necessary if those packages are to actually work.

Pip can also be used to upgrade a package to the latest version:

.. code-block:: console

   (my_venv) $ python -m pip install --upgrade numpy

The Python interpreter
----------------------

.. dropdown:: Video: a first Python script.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/486557682"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0f9a50a0-59b4-4bdf-ab90-ac850154fafb>`__

Before we dive into the various different ways that Python code can be
organised and run, it's helpful to have a mental model of what it
actually means for Python code to execute. Python is an interpreted
language. This means that the program that runs is not made up of the
primitive machine-level instructions that the processor in your
computer executes. Instead, the Python program is read and executed by
another piece of software, the Python interpreter. The Python
interpreter takes a sequence of Python statements and performs the
actions they specify. The Python interpreter takes care of allocating
the required memory and causes the right sequences of primitive
machine-level instructions to execute on the actual hardware for your
programme to run.

The Python interpreter is the same no matter whether you use Jupyter
notebooks, an interactive Python terminal such as IPython, or execute
code written in Python scripts. These are all just different ways of
providing a sequence of Python commands to the interpreter, and
conveying the output back to the user. This means that the same Python
code works in essentially the same way no matter how you use
Python. The Python interpreter also sits between the Python code and
the operating system, so for most purposes, it also doesn't matter
whether your Python program is running on Windows, macOS, Linux, or
maybe something more exotic. Usually, when we refer to Python doing
something or responding to code in a particular way, what we mean is
that this is what the interpreter does in those circumstances.


Python scripts and text editors
-------------------------------

A Python script is simply a plain text file containing Python code. If
we pass the file to the Python interpreter, then all the code in the
file will be executed, it's that simple. So, we need a way to create
files full of Python code, and a way to feed them to Python. We create
and edit Python files with a program called a text editor. A good text
editor will help you to code by highlighting syntax and helping with
indentation. Some text editors also feature advanced features such as
built-in access to documentation, or highlighting style problems in
your code. A more fully-featured option is an Integrated Development
Environment (IDE). IDEs combine an editor with a Python interpreter to
run your code, a debugger and often other features such as integration
with Git.

During this course, it will be assumed that you're using the IDE Microsoft
Visual Studio Code. You don't have to do so, and if you have a strong preference
for another text editor or IDE then you are welcome to use it. That said, if
your text editor does not have a collaborative editing facility equivalent to
Visual Studo Code's Live Share, then you are likely to need to use Visual Studio
Code when you ask for help so that the helper can share your editor session.

.. note:: Text files

    You are doubtless familiar with the concept of a file stored in a folder on
    your computer. You will also be aware that there are many different types of
    file, more or less related to the type of data they contain and the programs
    which created them. Files fall into two important categories, binary files
    and text files. A binary file is a stream of data whose contents make
    sense under the rules of the application which created it, but not
    otherwise. Word documents, PDFs, and JPEGs are examples of binary files.
    Plain text files are files which, as the name suggests, consist of a string
    of characters. Anyone looking at the content of a text file can
    understand it, so long as they understand the human or computer language in
    which it is written. LaTeX source files and Python scripts are examples of
    text files. This matters when you come to edit these files. Text files are
    edited using a text editor, or an IDE. Usually you can use whichever text
    editor you like, though some will have better support for writing some
    computer languages than others. Importantly, you can't edit text files in a
    program such as Microsoft Word and expect to end up with something usable.


A first Python script
~~~~~~~~~~~~~~~~~~~~~

Tradition dictates that the first stand-alone program one writes in
any language simply prints out the string `Hello World`. Using a text
editor, we create a file which we'll call :file:`hello.py` containing just
the following line of Python code:

.. code-block:: python

   print("Hello World")

The :file:`.py` file extension is not strictly required for Python scripts,
but it can be useful as it will cause most text editors to recognise
the file as a Python file. Having remembered to save :file:`hello.py` to
disk from the text editor, we can now run the program. Open a
terminal, and change to the folder (directory) where you saved
:file:`hello.py`. For example, if :file:`hello.py` is in the directory :file:`src` in
your home directory, then on most operating systems, you would type the following:

.. code-block:: console

    $ cd src
    $ python3 hello.py

on Windows you might instead need to type:

.. code-block:: console

    > cd src
    > py hello.py


The dollar sign is the command prompt. Its different on some systems, for
example, it's often a greater than sign (`>`). The text to the left of the
command prompt might also be different depending on which terminal program you
are using on which operating system, but we are only concerned with the commands
to the right of the prompt. The first of these, `cd` (*change directory*)
switches the current folder to :file:`src`. The second command actually runs the
Python interpreter on :file:`hello.py`. Depending on what is installed on your
computer, it might also be possible to leave off the `3` at the end of
`python3`, however on some systems the plain `python` command is still linked to
the old version 2 of Python, so it's better to be explicit and type `python3`.
Once we start working with Python :term:`virtual environments <virtual
environment>`, it will always be safe to use `python` without the 3. When we
press the :kbd:`enter` key after the last line above, our tiny Python script
:file:`hello.py` runs and the following is displayed:

.. code-block:: console

   Hello World

When to use scripts
~~~~~~~~~~~~~~~~~~~

The key advantage of a script is that it is repeatable: it can be
executed again, and exactly the same commands will execute. Writing
scripts is an absolutely essential programming discipline in any
circumstance where you might want to know what you did and, possibly,
do it again. For example, suppose you have a project in a
computational statistics course, in which you need to apply a complex
sequence of operations to a dataset and then plot some resulting
quantities. You could simply do this in an interactive Python session,
but you are then totally dependent on your memory as to what
you did. If you make a mistake, then you *might* notice an error in the
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
mathematicians and programmers, we are also interested in building
tools which users can combine together in different ways. We also want
to make functions and other code objects which can be reused in
different contexts to perform more complex computations. Functions and
other data structures defined in a script can essentially only be used
in that script. As soon as a piece of code is intended to be used in
two different scripts, it should be taken out and placed in a
module. This means that scripts should usually be quite short lists of
calls out to code in modules. We'll see a simple example of this
shortly.

.. _modules:

Modules
-------

.. dropdown:: Video: a first Python module.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/486845755"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=972f92c6-6b55-4510-9c2c-ac8600fca11a>`__

A module is, like a script, a plain text file containing Python
code. Modules must have names ending in :file:`.py`. So far, that's
identical to a script. Indeed, it's sometimes possible (though not
always advisable) to use the same file as both a script and a
module. The difference between a script and a module lies in how it is
used. A script is run, which means that a new Python interpreter
starts, executes the commands in the script, and then
exits. Conversely, a module is imported into a running Python
session. For example, suppose we create a file :file:`fibonacci.py`
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
:file:`fibonacci.py` then I will be able to import the :mod:`fibonacci`
module, and use the function :func:`fib`:

.. code-block:: ipython3

   In [1]: import fibonacci
   In [2]: fibonacci.fib(3)
   Out[2]: 2

Notice that we do not include the :file:`.py` suffix when we import a
module. Importing a module provides access to whatever it
contains. This is a key tool in building up algorithms out of
components: we import the components we need at each stage of our
programs.

Importing and namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~

When we imported the module :mod:`fibonacci`, this created the name
`fibonacci` in the current environment. The code in `fibonacci.py` is
then run, and any names defined in that code (such as the function
:func:`fib`) are defined within the :term:`namespace` `fibonacci`. As
we begin to compose together code from different parts of mathematics,
the ability to separate identically named but different objects from
each other is essential. For example, Python has a module containing
core real-valued maths functions called :mod:`python:math`, and one
containing complex maths functions called
:mod:`python:cmath`. Clearly, it's important that we can distinguish
between :func:`python:math.sin` and :func:`python:cmath.sin`. Here the
module names :mod:`math` and :mod:`cmath` form the namespaces that
differentiate between the two :func:`sin` functions. There are
essentially only two core namespace concepts. One of them is that
every name is in a namespace, and any given time points to a unique
value. The second one is that namespaces can be nested, so a name in a
namespace can itself be another namespace. For example, the math
namespace contains the value :obj:`math.pi`, which itself defines a
namespace for some operations that are built into Python numbers. The
(somewhat uninteresting) imaginary part of π can be accessed as
:obj:`math.pi.imag`.

Namespaces are a simple but fundamental concept in programming. To
quote one of the key developers of the Python language:

  Namespaces are one honking great idea -- let's do more of those! [#peters]_

.. note::

   :term:`Namespaces <namespace>` may look unfamiliar at first, but
   actually, they are such a natural concept that you have been working
   with them for as long as you have used a computer, without even
   thinking about it. This is because folders are simply namespaces
   for files. Each filename can exist only once in each folder, and
   you can nest folders inside folders. 

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
achieved using the keyword :keyword:`as <import>` in an import statement. For example,
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
functions :func:`math.sin` and :func:`math.cos` a lot in our script, we
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
that renaming does not add to the confusion. As a somewhat extreme
example, should you ever type the following code, you should expect
the wrath of your users to be without bounds:

.. container:: badcode

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

The full details of all the ways that the import statement can be used
is in :ref:`the official Python documentation. <python:import>`

Packages
--------

.. dropdown:: Video: a first Python package.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/487003753"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c4b0aedd-02a8-45d1-946b-ac86015b6d0b>`__


Modules are the principal mechanism for storing code which is intended
to be used by other code. However, putting all of the code for a
complex area of mathematics in a single huge Python file is not a
great idea. Readers of that code will struggle to see the logical
structure of thousands or tens of thousands of lines of code. It would
be much more logical, and much easier to work with, to split the code
up into several files of more reasonable length. This is where
packages come in. A Python package is a collection of module files,
which can be imported together. The basic folder structure of a Python
package looks like the following::

    my_git_repo
    ├── my_package
    │   ├── __init__.py
    │   ├── module_1.py
    │   ├── module_2.py
    │   └── subpackage
    │       ├── __init__.py
    │       └── module_3.py
    └── setup.py

If you haven't seen a diagram like this before, the names with lines
descending from their first letter are folder names, and the
descending line connects the folder name to the files and folders it
contains. Let's walk through these files and folders to understand how
they make up the Python package.

:file:`my_git_repo`
    This is not really a part of the package at all, but the
    :file:`my_package` folder needs to be in some folder, and this is a
    reminder that all your work should be in a revision control system
    such as :ref:`git <fons:git>`. It would be usual for
    package folders to be contained immediately in the top level of
    the repository, in the manner shown here.

:file:`my_package`
    This is the actual package. The name of this folder sets the
    package name, so if you really made a package folder with this
    name, then you would type:

    .. code-block:: python3

        import my_package

    to access the package.

:file:`__init__.py`
    Every package must contain a file with *exactly* this name. This is
    how Python recognises that a folder is a package. :file:`__init__.py`
    can be an empty file, or it can contain code to populate the top
    level :term:`namespace` of the package. See :numref:`importing_packages` below.

:file:`module_1.py`, :file:`module_2.py`
    These are just Python :term:`modules <module>`. If the user imports
    `my_package` using the line above then these modules will appear
    as `my_package.module_1` and `my_package.module_2` respectively.

:file:`subpackage`
    Packages can contain packages. A subpackage is just a folder
    containing a file :file:`__init__.py`. It can also contain modules and
    further subpackages.

:file:`setup.py`
    This file is outside the package folder and is not
    actually a part of the package. The role of :file:`setup.py` will be
    covered in :numref:`installable_packages`.

.. _importing_packages:

Importing packages
~~~~~~~~~~~~~~~~~~

The system for importing packages is the same as that described in
:numref:`modules`, though the nested nature of packages makes the
process somewhat more involved. Importing a package also imports all
the modules it contains, including those in subpackages. This will
establish a set of nested namespaces. In the example above, after
importing :mod:`my_package`, :mod:`module_3` will be accessible as
`my_package.subpackage.module_3`. The usual rules about the `from`
keyword still apply, so:

.. code-block:: python3

   from my_package.subpackages import module_3

would import the name `module_3` straight into the current local
namespace.

The file :file:`__init__.py` is itself a module and will be imported when
the package is imported. However, names defined in :file:`__init__.py` will
appear directly in the namespace of the package. This is usually used
to extract names from submodules that are supposed to be directly
accessed by users of the package. 

For example, suppose that `module_1` contains a function
`my_func`. Then the top level :file:`__init__.py` in `my_package` might contain
the line:

.. code-block:: python3

   from .module_1 import my_func

The result of this would be that the user of `my_package` would be
able to access `my_func` as `my_package.my_func` (though
`my_package.module_1.my_func` would also work). This sort of
arrangement provides a mechanism for the programmer to arrange the
internal module structure of a package in a logical way while still
providing users with direct access to the most important or most
frequently used features.

The eagle-eyed reader will have noticed the extra . in front of
`.module_1`. This marks this import as a *relative import*. In other
words, in looking for :file:`module_1.py`, Python should look for files in
the same folder as the module where the import statement occurs,
instead of looking for an external package called `module_1`. We could
have equivalently written:

.. code-block:: python3

   from my_package.module_1 import my_func

but the relative import is shorter and provides a reminder to the
reader that the import is from the current package.

.. _installable_packages:

Making packages installable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order for the :ref:`import statement <python:import>` to work, Python needs
to know that the package being imported exists, and where to find it. This is
achieved by *installing* the package. In order to make a package installable, we
need to provide Python with a bit more information about it. This
information is contained in a Python script which must be called :file:`setup.py`.
This file isn't part of the package and does not go in the package folder.
Instead, it should be placed in the top-level folder of your git repository, so
that the Python package installer will be able to find it.

At the very least, :file:`setup.py` should contain the following:

.. code-block:: python3

   from setuptools import setup, find_packages
   setup(
       name="my_package",
       version="0.1",
       packages=find_packages(),
   )

`Setuptools <https://setuptools.readthedocs.io/en/latest/index.html>`__
is a Python package which exists to help with the packaging and
installation of Python packages. The :func:`~setuptools.setup`
function records metadata such as the installation name to be given to
your whole set of packages, and the version. It also needs to know
about all of the packages in the current repository, but this can be
automated with the :func:`~setuptools.find_packages` function, which
will return a list of folders containing a file named :file:`__init__.py`.

This very simple :file:`setup.py` will suffice for packages that you only
intend to use yourself. Should you wish to publish packages for use by
other people, then you'll need to add some more information to the
file. The canonical guide to this is the `Python packaging user guide
<https://packaging.python.org/tutorials/packaging-projects/>`__.

Installing a package from local code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another important case is where the Python package exists in files
(hopefully a git repository!) on your local computer. This is usually
the case where you are developing the package yourself. In this case,
you would type:

.. code-block:: console

   (my_venv) $ python -m pip install -e folder/

replacing `folder` with the name of the top-level folder of your
repository: the folder containing :file:`setup.py`. The option flag `-e`
tells pip to install the package in 'editable' mode. This means that
instead of copying the package files to your venv's Python packages
folder, symbolic links will be created. This means that any changes
that you make to your package will show up the next time the package
is imported in a new Python process, avoiding the need to reinstall
the package every time you change it.

.. warning::

   If you edit a package, even one installed in editable mode, an
   already running Python process which has already imported that
   package will not notice the change. This is a common cause of
   confusion for users who are editing packages and testing them using
   an interactive Python tool such as IPython or a Jupyter Notebook. A
   major advantage of a Python script is that a new Python process is
   started every time the script is run, so the packages used are
   guaranteed to be up to date.

Testing frameworks
------------------

.. dropdown:: Video: introducing Pytest.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/486987209"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c636383d-6125-4a7c-bad7-ac86015b6d4c>`__

Attempting to establish whether a program correctly implements the
intended algorithm is core to effective programming, and programmers
often spend more time correcting bugs than writing new code. We will
turn to the question of how to debug in :numref:`debugging`. However,
right from the start, we need to test the code we write, so we will cover
the practical details of including tests in your code here.

There are a number of Python packages which support code testing. The
concepts are largely similar so rather than get bogged down in the
details of multiple frameworks, we will introduce :doc:`pytest
<pytest:index>`, which is one of the most widely used. Pytest is simply a Python
package, so you can install it into your current environment using:

.. code-block:: console

    $ python -m pip install pytest

Pytest tests
~~~~~~~~~~~~

A Pytest test is simply a function whose name starts with `test_`. In
the simplest case, the function has no arguments. Pytest will call each
such function in turn. If the function executes without error, then the
test is taken to have passed, while if an error occurs then the test
has failed. This behaviour might at first seem surprising - we don't
just want the code to run, it has to get the right answer. However,
thinking about it the other way around, we certainly want the test to
fail if an error occurs. It's also very easy to arrange things such
that an error occurs when the wrong answer is reached. This is most
readily achieved using :ref:`the assert statement <python:assert>`.
This simply consists of `assert` followed
by a Python expression. If the expression is true, then execution just
continues, but if it's false, then an error occurs. For example:

.. code-block:: ipython3

   In [1]: assert 1 == 0
   ---------------------------------------------------------------------------
   AssertionError                            Traceback (most recent call last)
   <ipython-input-1-e99f91a18d62> in <module>
   ----> 1 assert 1 == 0

   AssertionError:

Pytest files
~~~~~~~~~~~~

Pytest looks for tests in files whose name starts with :file:`test_` and
ends with :file:`.py`. Continuing with our Fibonacci example, we might
create a file called :file:`test_fibonacci.py` containing:

.. code-block:: python3

   from fibonacci import fib

   def test_fibonacci_values():

       for i, f in enumerate([1, 1, 2, 3, 5, 8]):
           assert fib(i+1) == f

These files don't themselves form part of the package, instead they
are usually gathered in a separate tests folder. For example::

    fibonacci
    ├── fibonacci
    │   ├── __init__.py
    │   └── fibonacci.py
    ├── tests
    │   └── test_fibonacci.py
    └── setup.py

We can then invoke the tests from the shell:

.. code-block:: console

    $ cd fibonacci
    $ pytest tests
    ========================== test session starts ===========================
    platform darwin -- Python 3.7.7, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dham/docs/object-oriented-programming, inifile: setup.cfg
    collected 1 item                                                         

     .                                          [100%]

    =========================== 1 passed in 0.01s ============================

The single dot indicates that we passed the one test in
`test_fibonacci.py`. Had we made an error in our code, we would
instead see something like:

.. code-block:: console

    $ pytest tests
    ========================== test session starts ===========================
    platform darwin -- Python 3.7.7, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dham/docs/object-oriented-programming, inifile: setup.cfg
    collected 1 item                                                         

    tests/test_fibonacci.py F                                          [100%]

    ================================ FAILURES ================================
    _________________________ test_fibonacci_values __________________________

        def test_fibonacci_values():

            for i, f in enumerate([1, 1, 2, 3, 5, 8]):
    >           assert fib(i+1) == f
    E           assert 2 == 1
    E            +  where 2 = fib((1 + 1))

    tests/test_fibonacci.py:6: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_fibonacci.py::test_fibonacci_values - assert 2 == 1
    =========================== 1 failed in 0.12s ============================

Here we can see an `F` after `tests/test_fibonacci.py` indicating
that the test failed, and we see some output detailing what went
wrong. We will learn how to interpret this output in :numref:`debugging`.

Additional useful pytest tricks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It can be useful to run a specific test file, which is achieved simply by naming
that file as the argument to pytest. For example:

.. code-block:: console

    $ pytest tests/test_fibonacci.py

It is even possible to select an individual test to run, using a double colon
`::` followed by the test name:

.. code-block:: console

    $ pytest tests/test_fibonacci.py::test_fibonacci_values

Often if one test fails then the same problem in your code will cause a whole
series of tests to fail, resulting in a very long list of error messages which
is hard to read. A useful tool in this circumstance is the `-x` option, which
tells pytest to stop after the first test fail. For example:

.. code-block:: console

    $ pytest -x tests

The tests are usually arranged in increasing order of sophistication, so the
earlier tests are likely to catch the most basic errors in your code. For this
reason, it is usually the best policy to try to fix the first error first, and
only move onto the next problem when the previous test passes.

.. note::

    The exercise repositories in this course will usually contain a
    :file:`tests` folder full of tests that check that you have correctly
    implemented the week's exercises. You should get in the habit of running the
    tests as you work through the exercises, as they are designed not just to
    pass if your code is correct, but to provide feedback as to what might be
    going wrong if your code contains errors.

Writing code to a specified interface
-------------------------------------

Creating more capable programmes depends completely on being able to interface
different pieces of code. You will write code which calls code written by other
people, and others will call code written by you. This can only work if the
caller and the callee agree exactly on the interface: what are the names of the
:term:`packages <package>`, :term:`modules <module>` and functions being
called. How many arguments do they take? What are the names of the
:term:`keyword parameters <parameter>`? Computer languages are notoriously pedantic about such
things: they have no capability to simply read through small differences as a
human would. You have doubtless already encountered the frustrating situation of
spending extended periods repeatedly getting errors until you realised that
something has to be spelt slightly differently, or that you used a capital
letter where you should have used a lower case one. 

What changes as you move on to write code which will be called by other code is
that this need for precision and pedantry now flows in both directions. Not only
do you need to call other code using precisely the correct interface, you also
need to provide precisely the correct interface to the code that will call you.
This will be the case all the way through this course as the tests for each
exercise will call your code. The exercises will specify what the correct
interface is, either in the exercise question itself, or through the skeleton
code which is provided.

Your code needs to follow exactly the specification in the exercise: all the
right names, accepting arguments of the correct type and so on. If it does not,
then the tests will simply fail. Changing the tests to suit your preferred
interface is not an acceptable answer, your code needs to comply with the
interface specified in the tests [#interface_errors]_.

This requirement to code to a published specification is not an artifact of the
testing framework: it is often the case that code written in a research or
business setting needs to conform with a standard or other published interface
exactly to create the sort of interoperability we've been discussing. Learning
to code to specification is therefore an important programming skill.

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

    package
       A grouping of related :term:`modules <module>` into a single importable unit.

    Python interpreter
       The piece of software which interprets and executes Python commands. 

    scope
       The scope of a name is the section of code for which that name is valid.

    script
    program
       A text file containing a sequence of Python statements to be
       executed. In Python, program and script are synonymous.

    venv
    virtual environment
       A lightweight private Python installation with its own set of
       Python packages installed.

Exercises
---------

.. panels::
    :card: quiz shadow

    .. link-button:: https://bb.imperial.ac.uk/webapps/assessment/take/launchAssessment.jsp?course_id=_25965_1&content_id=_2054443_1&mode=cpview
        :text: This week's quiz
        :classes: stretched-link 

.. proof:exercise::

    Follow the :ref:`instructions on the Faculty of Natural Sciences Python
    installation page <fons:python_folders>` to create the folder structure
    you will use for this course on your computer. Start with an overall folder
    for the module, and create a virtual environment in that module.

.. _course_repo:

.. proof:exercise::

    Visit the `GitHub repository for these notes
    <https://github.com/object-oriented-python/object-oriented-programming>`__.
    Clone that git repository into your course folder, and install the Python
    package it contains into your virtual environment. Check that it has
    installed correctly by installing pytest, and running:

    .. code-block:: console

        $ pytest tests/test_fibonacci.py

    You could also run iPython,  import :mod:`fibonacci` and try out
    :func:`fibonacci.fib <fibonacci.fibonacci.fib>` yourself.

.. proof:exercise::

    Accept the `first Github Classroom assignment for this module
    <https://classroom.github.com/a/VltGa-Xl>`__ and clone it into your course folder. The assignment
    repository just contains a :file:`README` and some tests. Your job in the
    following exercises will be to populate it with the remaining content.

.. proof:exercise::

    Create a new Python :term:`package` named :mod:`math_utils` containing a
    :term:`module` called :mod:`primes`. In the :mod:`primes` module define a
    function :func:`isprime` which takes in a single integer argument and
    returns `True` or `False` depending on whether or not the argument is prime.
    There is no need to be sophisticated in the algorithm used to check for
    primeness, simply checking whether the number is zero modulo any of the
    integers less than its square root will be fine. Test your code by running
    the following in your week 2 exercise repository:

    .. code-block:: console

        $ pytest tests/test_exercise_2_4.py

    Then push your code to GitHub and check that the tests pass there too.

    .. hint::

        The Python modulo operator is `%`. For example:

        .. code-block:: ipython3

            In [1]: 4 % 3
            Out[1]: 1

    .. note:: 

        After this and every exercise in which you write code, ensure that you
        add any new files to git, commit all of your changes, and push to
        GitHub. Then ensure that the tests pass on GitHub. For more information
        about how to do any of these, refer back the :ref:`Faculty of Natural Sciences
        Git instructions <github_classroom_exercise>`.

.. proof:exercise::

    Following :numref:`installable_packages`, create a :file:`setup.py` file in
    your exercise repository, so that the :mod:`math_utils` :term:`package` is
    installable.

    Pytest can't easily test installability for you, so once you have managed to
    install your package yourself, commit and push to github to check that the
    tests there are also able to install your package.

.. proof:exercise::

    Add an :keyword:`import` to :file:`math_utils.__init__.py` so that the following
    code will work:

    .. code-block:: python3

        from math_utils import isprime

.. rubric:: Footnotes

.. [#peters] Tim Peters, `"PEP 20 -- The Zen Of Python" (2004) <https://www.python.org/dev/peps/pep-0020/>`__

.. [#interface_errors] Of course if you find a case where it appears that the
   tests don't honour the interface published in the exercise, you should raise
   an issue reporting this.