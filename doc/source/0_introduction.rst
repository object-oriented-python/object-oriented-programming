.. _introduction:

Introduction: abstraction in mathematics and programming
========================================================

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
constructive laziness: it simultaniously allows the mathematician to
achieve more and do less work.

This course is a second course in programming, building a previously
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

All of the new material we cover in this course is presented in the notes. They
always the starting point for your work. Each chapter will introduce new
concepts in programming, often tied back to related mathematical concepts, and
always illustraded by practical code examples. Python has excellent `official
online documentation <https://docs.python.org/3/>`_, and we link to that
throughout the text. External links show up in orange while :ref:`internal links
to other parts of the notes <introduction>` are red. Sometimes we introduce
counterexamples: illustrations of code errors or bad implementation ideas. These
will be flagged with a big red cross:

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
chapter and just jumping to the glossary!

The chapters broadly alternate between introducing new programming concepts,
such as :ref:`objects`, :ref:`abstract data types`, or :ref:`inheritance`, and
covering various aspects of the craft of programming, such as :ref:`style`,
:ref:`debugging`. In this way the course combines specific programming knowledge
with more general coding skills.

The videos
..........

Throughout the notes are links to videos. These aren't typical lecture videos in
that they're not primarily focussed on delivering the new ideas in the course.
In particular, the videos don't set out to duplicate the delivery of the
material in the notes. Instead, the videos focus on putting the concepts into
practice, often by showing live coding sessions. Usually you'll want to watch
the video for a given section *after* reading the corresponding notes.

The quizes
..........

Towards the end of each chapter is a link back to a quiz on Imperial's
Blackboard system. The quizes are designed to allow you to convince yourself
that you've understood the material in the chapter. Sometimes they will simply
be multiple choice questions testing your understanding of the material, but
sometimes you will need to open up Python and try things out in order to work
out the right answer. The quizes do not contribute to your module grade, but how
well you are doing on them is an indication of your progress on the module.

The exercises
.............

As we've already noted, really learning to program better is only achieved by
writing code. The core of each week's activities is therefore to put the new
concepts and programming structures you've learned into practice. The
programming exercises are given at the end of each chapter, just before the
glossary. Each time there will be a skeleton code available from GitHub
Classroom (we'll introduce that in :numref:`github_classroom`) which provides
the starting point. Sometimes you might be asked to complete a piece of code
while on other occasions you'll need to write a whole Python module from
scratch. Each set of exercises will come with a matching set of tests. These are
small programs which check whether your code produces the correct responses to a
range of inputs. Tests like this provide immediate feedback and enable you to
know how you are doing without having to wait for code to be submitted and
marked.

Getting help
............

.. note::

    Write this bit once the interaction format is finalised.

Writing an issue report
.......................

.. note::

    Write this bit.

Assessment
..........


Obtaining the right software tools
----------------------------------

In order to do this module, you'll need some core software tools. As the module
proceeds we'll also install several more Python packages, but you don't need to
install those right now. The core tools you will need are:

    1. Python version 3.6 or later.
    2. Git (the revision control system we're going to use).
    3. A Python-aware text editor. Visual Studio Code is recommended, and all
       the instructions in this course will assume that this is what you are using.

Windows
.......

If you already have Python (3.6 or later) installed, for example because you
have installed Anaconda then this is likely to be fine. Otherwise, Python for
Windows can be obtained from the `official Python website
<https://www.python.org/downloads/>`_. Simply click on the download button and
follow the instructions.

Git for Windows can be downloaded from the `official Git website
<https://git-scm.com/download/win>`_.

Visual Studio Code can be downloaded from `Microsoft
<https://code.visualstudio.com>`_.

MacOS
.....

MacOS comes with Python3, but unfortunately it's a broken version. Usually the
best option is to install the package manager `Homebrew <https://brew.sh>`_ and
use that to install Python (and Git). In order to do this, you'll need to open a
terminal. This is a program which comes with MacOS and enables you to run other
programs by typing text commands. Press ⌘ + `space` to open Spotlight Search,
and type `terminal` followed by return. Now copy the following line and paste it
into the terminal:

.. code-block:: console

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    
and press the return key (⏎). Enter your Mac user password when asked and
Homebrew will install. Next install Python 3 and git by typing the following in
the terminal window:

.. code-block:: console

    brew install python git

Once again, you finish by pressing the return key (⏎).

To install Visual Studio Code, follow the instructions on the `Microsoft website
<https://code.visualstudio.com/docs/setup/mac>`_.

Linux
.....

If you are running a fairly recent version of Linux then you almost certainly
have a suitable Python installed already, and may also have git installed. Open
a terminal (the way you do this depends a little on distribution, but if you're
a Linux user we'll assume you know how to do this). At the terminal prompt run
this command:

.. code-block:: console

    python --version

so long as it shows at least version 3.6 you should be fine. If an earlier
version is shown then you'll need to either update your distribution, or search
online for how to install a more recent Python. The method will vary from
distribution to distribution so we can't provide a general solution.

Next, type the following command in the terminal:

.. code-block:: console

    git --version

So long as this actually returns a version number everything is probably fine
(we don't need a particularly new git). If you get an error that git is not
found then you'll need to install it using the package manager for your
distribution. For example, if you are running Ubuntu or another Debian-based
distribution, the command would be:

.. code-block:: console

    sudo apt-get install git

while on RedHat-distributions such as Fedora or CentOS, the command would be:

.. code-block:: console

    sudo dnf install git-all

On other distributions the command will be different. The simplest option is to
search online for how to install git on your distribution.

In order to install Visual Studio code you simply follow the instructions on the
`Microsoft website <https://code.visualstudio.com/download>`_.




