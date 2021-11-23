.. _introduction:

Introduction: abstraction in mathematics and programming
========================================================

.. .. details:: Video introduction.

..     .. vimeo:: 486106801

..     .. only:: html

..         Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ee8cae7f-1b42-4db3-adc0-ac840144de53>`_

A core tool of mathematics is to define abstract objects and the
operations which apply to them. This approach defines all the basic
building blocks which enable us to reason mathematically and perform
calculations. We start off with basic objects like numbers and define
arithmetic operations on them. As we become more sophisticated, we
define more and more complex objects, with appropriately more involved
operations: matrices, polynomials, sets, groups, algebras. Being able
to reason at the level of abstract objects is essential in making
mathematics comprehensible. Consider matrices: linear algebra would be
highly impractical at best if we could not define matrix addition and
multiplication, and had instead to work directly with sums of products
of scalars. More generally, without abstraction the edifice of higher
mathematics would rapidly collapse under the weight of its own
complexity.

The situation in computer programming is strikingly similar. At the
simplest level, the central processing unit of a computer is capable
only of a limited set of rather primitive arithmetic and logical
operations on a few finite subsets of the integers, and of the
floating point numbers. However, on this tiny foundation is built
every piece of software in existence, including very sophisticated
programs for text manipulation, higher mathematics, sound and
video. Moreover, this software is routinely created by ordinary people
using relatively modest amounts of effort. How is this possible? It is
possible because of the same principle of abstraction which underpins
mathematics: more abstract objects and the operations on them are
defined in terms of simpler ones.

Think about plotting a graph on a computer. As a 21st century
mathematician you don't write loops over arrays to compute the pixel
values that will result in the right curve appearing on a screen, you
use a high-level language such as Python which has plotting objects
which take in data and perform all of those calculations for
you. Where did those plotting objects come from? They are the result
of the manipulation of lower-level abstract objects in a chain that
eventually ends up with primitive operations on integers and floating
point numbers. But, critically, as the person wanting to plot some
data *you don't care*.

Why, then, as a mathematician should you care about abstraction in
programming? There are two key reasons. First, because an
understanding of the abstractions on which software is built will give
you a better understanding of how that software works and will
therefore make you a better user of that software. The second is that
making appropriate use of abstractions will make you a better
programmer of mathematics and other software. Applied well, objects
and abstraction produce software which is easier to write, easier to
understand, easier to debug, and easier to extend. Indeed, as with
abstraction in mathematics, abstraction in coding is a form of
constructive laziness: it simultaneously allows the mathematician to
achieve more and do less work.

.. _tools:

Obtaining the right software tools
----------------------------------

In order to do the exercises in this book, you'll need some core software
tools. At various points you'll also need install several more Python packages,
but you don't need to install those right now. The core tools you will need
are:

    1. Python version 3.6 or later.
    2. Git (the revision control system we're going to use).
    3. A Python-aware text editor or :term:`integrated development
       environment` (IDE). Visual Studio Code is recommended, and all the
       instructions will assume that this is what you are using.

.. only:: book

    Installation instructions are the piece of information most liable to go
    rapidly out of date. Further, at the point at which you install software,
    you are essentially by definition seated at a computer with internet
    access. Rather than provide the install information here, this information
    is instead provided on the book website:

        `https://object-oriented-programming.github.io/installation.html
        <https://object-oriented-programming.github.io/installation.html>`__

.. only:: latex and not book

    Installation instructions are the piece of information most liable to go
    rapidly out of date. Further, at the point at which you install software,
    you are essentially by definition seated at a computer with internet
    access. Rather than provide the install information here, this information
    is instead provided on `the book website: 
    <https://object-oriented-programming.github.io/installation.html>`__.

.. only:: html

    Installation instructions for these pieces of code are provided `on this
    page <https://object-oriented-programming.github.io/installation.html>`__`.

This is not a course about Git, but a minimal familiarity with Git and GitHub
will be needed in order to work with the examples. :numref:`Appendix %s <git>`
provides an elementary introduction to these tools for readers not already
familiar with them.

Python versions
...............

Python is a living language which regularly releases new versions. One very big
transition, which took over a decade, was the switch from version 2 to version
3 of the language. For many years both versions were in widespread use and
texts needed to cover their differences. However, Python 2 officially reached
end of life on 1 January 2020 and not even critical security updates are now
made to that version. You should, therefore, only ever use Python 3, and all
references in this book are to that version. 

Within Python 3, there is a minor version release approximately every year.
Once released, this receives security updates for 5 years. At the time of
writing, Python 3.10 is the newest release version, and Python 3.6 is the
oldest version that still recieves security fixes. The user-facing differences
between minor Python versions are usually fairly minimal, so for the purposes
of this book it doesn't matter which of the currently supported versions of
Python you use. 

.. warning::

    The example code in the exercises uses :ref:`f-strings <tut-f-strings>`
    which were introduced in Python 3.6, so the code will not work in earlier
    versions of Python.

.. _venv:

Setting up a Python virtual environment
---------------------------------------

.. details:: Video: setting up your virtual environment.

    .. vimeo:: 486546635

    .. only:: html

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=011d73de-d93c-4dc8-8996-ac8501521b33>`__

In the course of the exercises, You're going to create, edit, and install a
whole bunch of Python packages. It's highly desirable have a predictable
programming environment in which the experiments you're doing don't interfere
with anything else for which you might be using Python, and conversely which
remains unaffected by any packages you may have installed elsewhere. This
separation can be achieved by working in a Python :term:`virtual
environment`, or :term:`venv`. 

A virtual environment is a folder containing a local installation of Python
which links back to the Python you installed on your computer. This means that
virtual environments behave like separate Python installations for most
purposes, but are fast to install and take very little space because they share
most of their files with the already installed Python.

Creating a working folder
.........................

Start by creating a completely fresh folder for your work on this book. You can
call this anything you like. On my computer this is called
:file:`principles_of_programming`. You can create this folder using the
Windows File Explorer, Mac Finder, or by typing the following in a terminal:

.. code-block:: console

    $ mkdir principles_of_programming

Obviously you replace :file:`principles_of_programming` with whatever you
decide to call the folder. The dollar sign is the command prompt. Its different
on some systems, for example, it's often a greater than sign (`>`) or a percent
symbol (`%`). The text to the left of the command prompt might also be
different depending on which terminal program you are using on which operating
system, but we are only concerned with the commands to the right of the prompt.

.. hint::

    Modern operating systems are quite capable of dealing with folder names and
    file names containing spaces. However, there are many pieces of software
    (including some Python packages) that don't correctly deal with spaces in
    folder and file names. It's therefore a safer option to avoid spaces and
    instead to separate words with underscores (:file:`_`).

Creating the venv
.................

Now that we have our working folder, we will switch to doing everything in our
:term:`IDE`, so launch Visual Studio Code. Click on `Open...` in
the main window or in the `File` menu and select the folder you just created.
This will open a Visual Studio Code workspace in that folder. You will probably
be able to see a terminal window at the bottom of the screen. If it's not
there then open the `View` menu and select `Terminal` to make it appear.

The most straightforward way to create a venv is on the terminal
command line, not from within Python itself. This is accomplished
using Python's :mod:`venv` package. The venv has to be given a name. You will
want this to be short, but distinctive enough that you know which venv you are
using. For example, to create a venv
called `PoP_venv` on Windows, you would type:

.. code-block:: console

    > py -m venv PoP_venv

while on Mac or Linux you would type:

.. code-block:: console

    $ python3 -m venv PoP_venv

Don't forget that the `>` or `$` stands for the command prompt: you don't
type it. This command will create the folder `PoP_venv` and various
subfolders containing things like the Python program itself and space
for any packages which you install in the venv. If there was already a
file or folder called `PoP_venv` in the current folder then you'll get
an error, so make sure you choose a new name.

.. note::

    Running `py` on Windows or `python3` on Mac or Linux is a mechanism to
    attempt to ensure that the right version of Python runs. If you have
    multiple Python installations on your computer then you might end up
    running the wrong one. If this happens then you will need to type the full
    path to the Python you want to use (starting with `/` on Mac or Linux or
    `\\` on Windows). Once the venv is installed and activated, it will be
    sufficient to type `python` as the venv will ensure that this is the
    correct version.

A venv doesn't usually contain any particularly valuable data, so you
should regard them as essentially disposable. In particular, if
something goes wrong when creating a venv, just delete it and start
again. In the bash or zsh shells you would type:

.. code-block:: console

   $ rm -rf PoP_venv

.. warning::

   `rm -rf` will delete its argument and all its subdirectories
   without further prompts or warnings. There is no undo operation.
   Be very careful about what you delete.

.. _activate_venv:

Using a venv
............

If you run Python from the terminal, then the simplest way to use the
venv is to source its activate script. If using bash or zsh on Mac or
Linux you would type:

.. code-block:: console

    $ source PoP_venv/bin/activate

while using bash on Windows you would type:

.. code-block:: console

    $ source PoP_venv/Scripts/activate

If using PowerShell on Windows then you type:

.. code-block:: powershell

    > .\PoP_venv\Scripts\activate.ps1

Obviously, you would use the folder name of your venv instead of
`PoP_venv`. In either case, your command prompt will change to indicate
that you are now using the venv. It might look something like:

.. code-block:: console

   (PoP_venv) $

Any subsequent invocations of Python commands such as `python3` will
now use the version from the venv, with access to whatever packages
you have installed in that venv. If you are using a terminal shell
other than bash or zsh, then see the :mod:`venv` package documentation
for the correct activation command.

.. hint::

    The default permissions settings on your Windows computer may not permit you
    to run the activation script. This can be fixed by running:

    .. code-block:: console

        > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    .. only:: not book

        For further information, see :doc:`the official Python venv documentation
        <library/venv>`.

    .. only:: book

        For further information, see the official Python venv documentation.
        [#venv]_


.. hint::

    Venv activation is just for one terminal session. You need to activate the
    venv every time you open a new terminal, though if you are lucky then
    Visual Studio Code will notice the venv and activate it for you. If you
    find that Python can't find your packages or tests, then the first thing to
    check is whether you remembered to activate the venv.

Installing Python packages
--------------------------

Suppose we've created and activated a venv, and now there's a Python package
we'd like to have access to. Installation of Python packages is handled by the
Python package :doc:`Pip <pip:index>`, which you will usually find
pre-installed in your Python installation. Pip has many usage options, which
enable a large number of different installation configurations. However, for
most users most of the time, a few simple pip commands suffice. As with
venv creation, package installation is best accomplished from the
terminal and not from within Python itself. Don't forget to activate the venv!

.. _install-from-pypi:

Installing packages from PyPI
.............................

`PyPI <https://pypi.org>`__ is the Python Package Index. It is the
official download location for publicly released Python packages which
aren't themselves a part of the built-in :doc:`Python Standard Library
<python:library/index>`. Many important mathematical packages
including :mod:`numpy` and `sympy <https://www.sympy.org>`__ are
distributed from PyPI. Suppose your venv doesn't have :mod:`numpy`
installed and you need it. You would install it with the following
terminal command:

.. code-block:: console

   (PoP_venv) $ python -m pip install numpy

It is also possible to invoke pip directly using the command `pip3`,
but there are some circumstances where that might result in pip using
the wrong Python installation. The approach used here is safer.

Python packages may depend on other Python packages, so it's quite
likely that pip will install more packages than those you directly
asked for. This is necessary if those packages are to actually work.

Pip can also be used to upgrade a package to the latest version:

.. code-block:: console

   (PoP_venv) $ python -m pip install --upgrade numpy

Glossary
--------

.. glossary::
    :sorted:

    IDE
    integrated development environment
        A program designed to help a software developer write code. An IDE
        combines a text editor with features such as syntax highlighting and
        checking, debugging capabilities, revision control interfaces and
        inbuilt terminal windows.

    venv
    virtual environment
        A lightweight private Python installation with its own set of
        Python packages installed.



.. Exercises
.. ---------

.. This week's exercises are designed to ensure that you are set up with the core
.. tools that you will need for the rest of the module. Exceptionally, there is no
.. quiz this week as we haven't yet started with the substantive contents of the
.. module. Nonetheless, this week's exercises are an important baseline. Skipping
.. them is likely to result in you having to play catchup in the coming weeks.

.. .. proof:exercise::
    
..     Install Python using  the :doc:`FoNS Python installation instructions <fons:python>`.

.. .. proof:exercise::

..     Install Git and work through the entire Git, GitHub, and GitHub Classroom
..     tutorial on the :doc:`FoNS Git instructions webpage <fons:git>`.

.. .. proof:exercise::

..     Install Visual Studio Code using the :doc:`FoNS Visual Studio Code
..     installation instructions <fons:vscode>`.
    
.. .. proof:exercise::

..     With one or two friends from the class, follow the  
..     :ref:`Live Share instructions <vscode-liveshare>`. 
..     Ensure that each of you can start a Live Share session and have the other
..     successfully join, and that all of you can edit files.

.. only:: book

    .. rubric:: Footnotes

    .. [#venv] `https://docs.python.org/3/library/venv.html
        <https://docs.python.org/3/library/venv.html>`__ 
