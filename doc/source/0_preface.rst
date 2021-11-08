Preface
=======

Computers have revolutionised mathematics, as well as the many scientific,
engineering and economic fields in which mathematics is applied. In
the applications of mathematics the role of computation has long been obvious
and prominent. Now, the development of theorem proving software is increasing
the prominence of computing in pure mathematics. What this means is that
the ability to write computer programs is an indispensible part of the toolkit
of a 21st century mathematician and, indeed, scientist or engineer.

Regrettably, university courses in mathematics and its sibling disciplines have
often failed to reflect this revolution in the way that mathematics is
practised. Far too often the sum total of programming education in an
undergraduate degree is a computational methods module in which students are
shown elementary programming constructs such as functions, loops, and perhaps
plotting. These are introduced in the context of solving particular
computational mathematics or statistics problems, and the programming
constructs introduced are driven by what is needed to solve those problems. 

The assumptions underpinning this approach seem to be some combination of a
belief that maths degrees should only teach maths, as well a feeling that the
mathematical algorithms are some how the difficult part and that programming is
a mere technical skill that students will somehow pick up along the way. The
regrettable consequence of this approach is that many maths students and
graduates end up without the programming, software development, and debugging
skills that they need to make effective use of computers in their further
studies or working careers.

What is this book for?
----------------------

This book is the result of a significant change in the mathematics curriculum
at Imperial College London. Rather than assume that students will somehow
acquire programming skills along the way, we have introduced first and second
year courses with the sole objective of teaching students to programme well.
This book is the text for the second of these courses. Named "Principles of
Programming", the course aims to take students with a knowledge of basic Python
programming (functions, loops, plotting and so forth) and introduce them to
higher level programming concepts. The course has also been taught to masters

The objective of this course is to graduate better programmers, so material on
new programming constructs and concepts is accompanied by chapters on good
programming style, so that students learn how to write code that they and
others can understand, and on errors, exceptions and debugging, so that
students learn how to get themselves out of trouble. 

An underlying theme throughout this book is that programming has strong
connections with mathematics. In particular, both mathematics and programming
depend on building higher level, more abstract objects which encapsulate and
hide the underlying complexity of operations. It is in taking this mathematical
approach to programming that this book is "for mathematicians".

The examples are chosen from across mathematics. For example, it appears to be
traditional in object oriented programming books to use a telephone directory
as the initial example of classes. We eschew this in favour of a class
implementing polynomials. This provides the opportunity to introduce
encapsulation and operator overloading for a familiar mathematical object. In
contrast to the traditional computational methods courses, the examples are
chosen to illustrate and explain the programming concepts we study rather than
the converse. 

Who is this book for?
---------------------

This book is for anyone with mathematical, scientific, or engineering interests
who would like to learn to be a more capable programmer. The mathematical
examples assume that you know how to differentiate functions of one variable,
but very little beyond that. This is not an introduction to basic Python: it's
assumed that the reader knows the sort of basic Python usually covered in a
first programming or computational methods course. In particular the reader
will be assumed to be familiar with writing functions, variable assignments,
loops, and list comprehensions. The reader is also assumed to have used numeric
and string data values, as well as dictionaries, lists, and tuples.

Many introductory Python courses exclusively use Jupyter notebooks, so nothing
beyond that is assumed. Getting set up with a working Python installation is
covered in :numref:`introduction` while the Python command line and using a
text editor to create programmes in files are introduced from scratch in
:numref:`programs_files`.

How to use this book
--------------------

You can, of course, simply sit down and read this book from cover to cover, or
dip in to see what it has to say on particular subjects. However, reading a
book about programming will not teach you to program. For that, you need to get
your hands dirty writing code and debugging your mistakes. To help with this
there is a book website at:

    `https://object-oriented-programming.github.io
    <https://object-oriented-programming.github.io>`__
    
As well as a web version of the full text of the book, the website contains
videos and the code needed to do the programming exercises at the end of each
chapter.

The videos
..........

The videos were created to accompany the course at Imperial College London.
They're not primarily lecture videos but are instead practical demonstrations
of the programming concepts being introduced at the relevant point. Usually
it's better to watch the video *after* reading the relevant section.

.. only:: latex

    The videos are marked in the text by a blue box at the right hand side,
    containing the video number. This corresponds to the list of links at:

        `https://object-oriented-programming.github.io/edition1/videos.html
        <https://object-oriented-programming.github.io/edition1/videos.html>`__

The exercises
.............

At the end of each chapter are exercises. These usually depend on a skeleton
code which is available on GitHub. Sometimes you might be asked to complete a piece of code while on other
occasions you'll need to write a whole Python module from scratch. Each set of
exercises will come with a matching set of tests. These are small programs which
check whether your code produces the correct responses to a range of inputs.
Tests like this provide immediate feedback and enable you to know how you are
doing. Links to the skeleton code for each chapter are provided at:

        `https://object-oriented-programming.github.io/edition1/exercises.html
        <https://object-oriented-programming.github.io/edition1/exercises.html>`__

The mechanism for accessing the exercises will be covered in
:numref:`introduction`.

Conventions employed
--------------------

Each chapter starts by introducing new material, supported by the videos and
exercises. At the end of each chapter is a glossary containing many of the key
concepts introduced in that chapter. Terms to be found in a glossary are given
*in italics* and can be looked up in the index.

.. only:: not book

    Python has excellent `official online documentation
    <https://docs.python.org/3/>`_, and we link to that throughout the text.
    External links show up in orange while :ref:`internal links to other parts
    of the notes <introduction>` are red.

The text sometimes introduces counterexamples: illustrations of code errors or
bad implementation ideas. These will be flagged with a big red cross:

.. container:: badcode

    .. code-block:: python3

        print "Hello World"

Conversely, if it's necessary in context to highlight which approach is the
correct one, the code will come with a big green tick:

.. container:: goodcode

    .. code-block:: python3

        print("Hello World")


Teaching this course elsewhere
------------------------------

The course of which this book forms the text has been given to master's
students at the University of Oxford, as well as to undergraduate students at
Imperial College London. Instructors are welcome to use this material to teach
elsewhere, and are encouraged to contact the author for assistance with access
to materials.

Acknowledgements
----------------

The course Principles of Programming, and the notes on which this book is
based, were first delivered in spring 2020, when university teaching was
completely online during the COVID pandemic. I'd like to thank teaching fellow
Dr Matthew Woolway who worked tirelessly with me on the module and who put
together many of the tests on the exercies, and the graduate teaching
assistants Miguel Boland, Sophia Vorderwuelbecke and Connor Ward whose
professionalism in delivering the course in very complex circumstances was
outstanding. Pulling out all the stops to deliver the written and video
materials for online learning meant a lot of evenings and weekends. I am
exceptionally grateful to my wife Gebina Ham for disproportionately picking up
our childcare responsibilities in that period in order to make this possible.

This is a textbook about programming in Python, so it would be remiss of me not
to also thank the developers of the Python language, its CPython reference
implementation, and all the third party packages which on which this book
depends. In that regard, the developers of Numpy, Flake8, Pytest, PDB++ and
IPython deserve particular mention.

This book is typeset using the Sphinx documentation system. Among other things
this facilitates generating the web, PDF, and print versions of the book from a
single source. Thanks are due to its authors as well as those of the underlying
LaTeX and TeX typesetting systems.
