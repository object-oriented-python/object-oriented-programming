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
understand, easier to debug and easier to extend. Indeed, as with
abstraction in mathematics, abstraction in coding is a form of
constructive laziness: it simultaneously allows the mathematician to
achieve more and do less work.

Obtaining the right software tools
----------------------------------

In order to do this module, you'll need some core software tools. As the module
proceeds we'll also install several more Python packages, but you don't need to
install those right now. The core tools you will need are:

    1. Python version 3.6 or later.
    2. Git (the revision control system we're going to use).
    3. A Python-aware text editor. Visual Studio Code is recommended, and all
       the instructions in this course will assume that this is what you are using.

The Faculty of Natural Sciences at Imperial has 
:doc:`centralised instructions for installing all of these tools <fons:index>`, and we'll follow those. 

Python 
......

Follow the :doc:`FoNS Python instructions <fons:python>`. We will exclusively
use :ref:`virtual environments <fons:python_virtual_environments>` so it doesn't matter at
all whether you use Python from Anaconda or from another source. Mac users
should note, though that the built-in Python will not do, so you should use
either Homebrew or Anaconda.

.. note::

    The example code in the exercises uses :ref:`f-strings <tut-f-strings>`
    which were introduced in Python 3.6, so the code will not work in earlier
    versions of Python.

Git
...

Git is a revision control system. Revision control systems enable you to keep
track of the different versions of a piece of code as you work on them, and to
have these versions on different computers as well as backed up in the cloud. We
will use Git and GitHub classroom as a mechanism for distributing, working with
and submitting code exercises.

.. warning::

    When you come to the assessable programming tests that make up 100% of the
    assessment for this module, the code will be distributed and submitted using
    Git. It is therefore essential that you incorporate Git into your day to day
    workflow so that when you come to the test, it's second nature. You will not
    receive marks for test answers that are not committed and pushed.

Visual Studio Code
..................

Visual Studio Code is a Python-aware Integrated Development Environment (IDE).
This means that it incorporates editing files with other programming features
such as :ref:`debugging`, Git support, and built-in :ref:`terminal
<terminal-vscode>`. Visual Studio Code also provides an incredibly useful remote
collaborative coding feature called Live Share. This will be very useful for
getting remote help from an instructor. 

Setting up a Python environment for this course
-----------------------------------------------

.. details:: Video: setting up your virtual environment.

    .. vimeo:: 486546635

    .. only:: html

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

Suppose we've created and activated a venv, and now there's a Python package
we'd like to have access to. Installation of Python packages is handled by the
Python package :doc:`Pip <pip:index>`, which you will usually find
pre-installed in your Python installation. Pip has many usage options, which
enable a large number of different installation configurations. However, for
most users most of the time, a few simple pip commands suffice. As with
:term:`venv` creation, package installation is best accomplished from the
terminal and not from within Python itself. Don't forget to activate the venv!

.. _install-from-pypi:

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




Exercises
---------

This week's exercises are designed to ensure that you are set up with the core
tools that you will need for the rest of the module. Exceptionally, there is no
quiz this week as we haven't yet started with the substantive contents of the
module. Nonetheless, this week's exercises are an important baseline. Skipping
them is likely to result in you having to play catchup in the coming weeks.

.. proof:exercise::
    
    Install Python using  the :doc:`FoNS Python installation instructions <fons:python>`.

.. proof:exercise::

    Install Git and work through the entire Git, GitHub, and GitHub Classroom
    tutorial on the :doc:`FoNS Git instructions webpage <fons:git>`.

.. proof:exercise::

    Install Visual Studio Code using the :doc:`FoNS Visual Studio Code
    installation instructions <fons:vscode>`.
    
.. proof:exercise::

    With one or two friends from the class, follow the  
    :ref:`Live Share instructions <vscode-liveshare>`. 
    Ensure that each of you can start a Live Share session and have the other
    successfully join, and that all of you can edit files.
