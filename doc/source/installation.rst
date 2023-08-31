:orphan:

Installing the necessary software
=================================

In order to do the exercises in this book, you will need Python, Git, and a
suitable text editor or :term:`Integrated Development Environment`. Visual
Studio Code is recommended as the :term:`IDE`.

Instructions are provided here for Windows, MacOS, and Linux. Chromebook users
can follow the Linux instructions if they first `activate Linux on their
Chromebook <https://support.google.com/chromebook/answer/9145439>`__.

Homebrew for Mac
----------------

The easiest way to install additional programming software on a Mac is to first
install the Homebrew package manager. Open a terminal (press :kbd:`⌘` +
:kbd:`space` to open Spotlight Search and then type `terminal` in the search
window) and run the following command:

.. code-block:: console

    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Don't type the :kbd:`$`. That's the terminal prompt (it might appear as another
symbol such as :kbd:`%` for you).

This will start the install process, and ask you for confirmation before
installing Homebrew. 

Further documentation about Homebrew and its dependencies is available on the
`Homebrew website <https://brew.sh>`_.


Python 
------

There are a number of different ways of obtaining Python, depending a little on
which operating system your computer runs. The routes suggested here are ones
that have been easiest for students taking the course at Imperial, however any
sufficiently recent Python should be sufficient.

Windows
.......

Install `Python from the Microsoft Store
<https://www.microsoft.com/en-us/p/python-310/9pjpw5ldxlz5>`__. 

MacOS
.....

MacOS comes with Python 3, but it's a cut down version not suitable for our
purposes. Instead, install Python from Homebrew:

.. code-block:: console

    $ brew install python

Linux
.....

Every Linux distribution ships with Python 3 by default. However, they don't
always have the Python package manager Pip installed by default. We will need
that so you'll need to use your distribution's package manager to install it.
For example on Ubuntu or Debian you would run:

.. code-block:: console

    $ sudo apt install python3-pip

while on Fedora and related distributions you would run:

.. code-block:: console

    $ sudo dnf install python-pip

Git
---

Git is a revision control system. Revision control systems enable you to keep
track of the different versions of a piece of code as you work on them, and to
have these versions on different computers as well as backed up in the cloud. We
will use Git and GitHub classroom as a mechanism for distributing, working with
and submitting code exercises.

Windows
.......

Download and install the `Git package <https://git-scm.com/download/win>`__.

MacOS
.....

MacOS comes with a perfectly acceptable Git installation. However you can also
install a more recent version from Homebrew:

.. code-block:: console

    $ brew install git

Linux
.....

Use your distribution package manager to install Git. For example on Ubuntu or
Debian:

.. code-block:: 

    $ sudo apt install git-all

On Fedora:

.. code-block::

    $ sudo apt install git-all


Visual Studio Code
------------------

Visual Studio Code is a Python-aware Integrated Development Environment (IDE).
This means that it incorporates editing files with other programming features
such as :ref:`debugging`, Git support, and built-in terminal. 

Windows
.......

`Download and install the package <https://code.visualstudio.com/download>`__.

MacOS
.....

Use Homebrew to install Visual Studio Code:

.. code-block:: console

    $ brew install visual-studio-code


Linux
.....

`Download the package <https://code.visualstudio.com/download>`__ and then use
your package manager to install it `following these instructions
<https://code.visualstudio.com/docs/setup/linux>`__.
