.. _introduction:

Introduction: abstraction in mathematics and programming
========================================================

.. details:: Video introduction.

    .. vimeo:: 486106801

    .. only:: html

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ee8cae7f-1b42-4db3-adc0-ac840144de53>`_

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

This is a second course in programming, building a previously
acquired basic understanding of programming in Python. In covering
more advanced programming, we will pay particular attention to objects
and abstraction as they occur in Python. Furthermore, we will do so
from a mathematician's perspective, understanding programming as a
process of defining and manipulating mathematical objects, and
scientifically testing and debugging the results.

How to do this course
---------------------

Programming, like mathematics, is a practical, problem solving discipline. It's
not possible to learn to program just by reading notes and watching lectures. To
learn to program you need to put the content of the course into practice by
writing code. The structure of this course is designed to help you to really
understand new concepts in programming by putting them into practice. Each week,
we run through the same cycle:

1. Read the notes
2. Watch the videos
3. Do the quiz
4. Write the code

The notes
.........

All of the new material we cover in this course is presented in these notes.
Each chapter contains the material for one week of term, so in week :math:`n`,
you work through chapter :math:`n`. The notes always the starting point for your work.
Each chapter will introduce new concepts in programming, often tied back to
related mathematical concepts, and always illustrated by practical code
examples. Python has excellent `official online documentation
<https://docs.python.org/3/>`_, and we link to that throughout the text.
External links show up in orange while :ref:`internal links to other parts of
the notes <introduction>` are red. Sometimes we introduce counterexamples:
illustrations of code errors or bad implementation ideas. These will be flagged
with a big red cross:

.. container:: badcode

    .. code-block:: python3

        print "Hello World"

Conversely, if it's necessary in context to highlight which approach is the
correct one, the code will come with a big green tick:

.. container:: goodcode

    .. code-block:: python3

        print("Hello World")

At the end of each chapter there is a glossary containing key new concepts
introduced in that chapter. Always check the glossary and convince yourself that
you understand all the terms introduced there, this is a good check on whether
you have understood the chapter as a whole. However, there is more to learning
new concepts than just the vocabulary, so don't be tempted to skip reading the
chapter and just jump to the glossary!

The chapters broadly alternate between introducing new programming concepts,
such as :ref:`objects <objects>`, :ref:`abstract data types
<abstract_data_types>`, or :ref:`inheritance <inheritance>`, and
covering various aspects of the craft of programming, such as :ref:`style
<inheritance>` and :ref:`debugging <debugging>`. In this way the course combines specific programming knowledge
with more general coding skills.

The videos
..........

Throughout the notes are links to videos. These aren't typical lecture videos in
that they're not primarily focussed on delivering the new ideas in the course.
In particular, the videos don't set out to duplicate the delivery of the
material in the notes. Instead, the videos focus on putting the concepts into
practice, often by showing live coding sessions. Usually you'll want to watch
the video for a given section *after* reading the corresponding notes.

The quizzes
...........

Towards the end of each chapter is a link back to a quiz on Imperial's
Blackboard system. The quizzes are designed to allow you to convince yourself
that you've understood the material in the chapter. Sometimes they will simply
be multiple choice questions testing your understanding of the material, but
sometimes you will need to open up Python and try things out in order to work
out the right answer. The quizzes do not contribute to your module grade, but how
well you are doing on them is an indication of your progress on the module.

The exercises
.............

As we've already noted, really learning to program better is only achieved by
writing code. The core of each week's activities is therefore to put the new
concepts and programming structures you've learned into practice. The
programming exercises are given at the end of each chapter, just before the
glossary. Each time there will be a skeleton code available from
:ref:`GitHub Classroom <fons:github_classroom_exercise>` which provides the starting
point. Sometimes you might be asked to complete a piece of code while on other
occasions you'll need to write a whole Python module from scratch. Each set of
exercises will come with a matching set of tests. These are small programs which
check whether your code produces the correct responses to a range of inputs.
Tests like this provide immediate feedback and enable you to know how you are
doing without having to wait for code to be submitted and marked.

.. note::

    Solutions to exercises will not be issued. The notes and accompanying
    example code contain examples of the same programming constructs that the
    exercises require you to implement, and the tests provide a mechanism to
    know when you have a correct answer. There are also help mechanisms via the
    course forum and the lab sessions. Issuing solutions to problems would
    simply encourage students to study the solutions rather than write code, and
    the only way to learn to program is to write code.

Assessment
..........

The weekly quiz and exercises are not assessable: they are formative activities
designed to help you learn the module. Instead, the module will be assessed by
two controlled programming assessments, effectively programming exams. The first
programming assessment will be held in week 7 and will be worth 20% of the
marks for the course. This provides an opportunity to receive feedback in the
middle of the term, and is a practice for the main exam. The :ref:`course contents for
week 7 <midterm>` will comprise practice programming exercises for this midterm test.
The second programming assessment will be held in the main May exam period and
will count for the other 80% of the course.

The instructions and skeleton code for the programming exercises will be
released at a fixed time on GitHub Classroom, and the code which you have
committed to GitHub by the end of the allotted time will be marked.

The exam questions will be similar to the weekly exercises in the course,
and may include new programmes to write from specification, modifications or
extensions to be made to code which is provided, and debugging exercises in
which defective code is provided which you need to correct. Marks will be
allocated both for the functional correctness of the code written, and for
good style and following Python coding conventions.


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
