.. _git-windows:

Installing Git on Windows
-------------------------

Direct download
~~~~~~~~~~~~~~~

To install Git directly, navigate to `the Git Windows download website
<https://git-scm.com/download/win>`__. If the download doesn't start
immediately, click on `Click here to download manually`. Run the installer.
Unless you have specific reasons to do otherwise, it's reasonable to accept all
the defaults by clicking `next` each time.

Now proceed to :ref:`check the install <check_git>`.

Software Hub
~~~~~~~~~~~~

Follow the instructions on `the Imperial Software Hub website
<https://www.imperial.ac.uk/admin-services/ict/self-service/computers-printing/devices-and-software/get-software/software-hub/>`_.

The version of Git on Software Hub is somewhat older and has compatibility
issues with the most recent versions of :ref:`Visual Studio Code
<visual-studio-code>`.

Now proceed to :ref:`check the install <check_git>`.

Installing Git on Mac
---------------------

All recent versions of MacOS come with Git pre-installed. This version is likely
to be good enough for many students on many modules, though it probably won't be
the most recent release.

If you want a more recent version and you've :ref:`installed Homebrew
<homebrew>` then installing Git is as simple as :ref:`opening a terminal
<terminal-mac>` and running the following command:

.. code-block:: console

    $ brew install git

Now proceed to :ref:`check the install <check_git>`.

If you need a more recent version of Git and you don't want to install Homebrew
for whatever reason, then there are more options on `the Git MacOS download
website <https://git-scm.com/download/mac>`_.

Installing Git on Linux or Chrome OS [#Chrome]_
-----------------------------------------------

Every Linux distribution ships Git through its package manager. The easiest way
to install Git is usually to simply do whatever it is that is normal on your
distribution to install software. For example on Ubuntu or any other
Debian-based system you would run this in the terminal:

.. code-block:: console

    $ sudo apt-get install git

While on Fedora and related distributions, you would run:

.. code-block:: console

    $ sudo dnf install git

or if you're using an older version of these distributions:

.. code-block:: console

    $ sudo yum install git

If you're using a different Linux distribution then you'll probably find the
correct install line `on the Git Linux download website <https://git-scm.com/download/linux>`_.
