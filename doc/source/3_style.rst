.. _style:

A matter of style
=================

The value of convention
-----------------------

Consider the following definition of the limit of a function :math:`f` at a point :math:`c`:

.. proof:definition::

   Suppose we have a function :math:`f(x): \mathbb{R} \rightarrow \mathbb{R}`. Then:

   .. math::

      \lim_{x\rightarrow c} f(x) = L \iff \forall \delta > 0,\ \exists \epsilon > 0,\ |x - c| < \epsilon \Rightarrow |f(x) - L| < \delta

This is a perfectly valid definition of a limit: you could use it to
go on and derive all the analysis you have learned so far. However, you
would confuse yourself and your readers horribly, because I have
swapped the roles of :math:`\delta` and :math:`\epsilon` in the
definition. The formal properties of mathematical objects do not
depend on the names we give them or, often, on how we lay out formulae
on a page. However, mathematics is designed to be read by humans with
their habit-forming, pattern-matching brains. So if everyone adopts
similar conventions for how to write down mathematics, everyone
schooled in those conventions will find that mathematics easier to
understand. This is vitally important because understanding
mathematics is *hard*. Non-standard notation makes it doubly hard
because the reader has to consciously remember the meaning of all the
symbols. Conversely, once a reader has learned the notational
conventions for a field of mathematics, the meanings of the symbols
become natural and don't require conscious thought. This leaves all
the available brainpower to concentrate on the mathematical content
at hand.

You might at first think that this logic does not apply to computer
programs. After all, a computer program is read by another computer
program, and is not understood but rather acted on
mechanically. Surely it doesn't matter how it looks or what symbols
you use, so long as it's correct, and possibly fast? This entirely
understandable sentiment has afflicted almost all programmers at some
point or another and typically has got them into more or less serious
difficulty before they realised that it's completely wrong.

In reality, a computer program is frequently read. Indeed, code is
typically read many more times than it is written or changed. Most
obviously, programmers read code in order to understand its functionality,
and in order to work out what is wrong with the code when it fails to
produce the correct results. Reading code is very much like reading
mathematics because a computer program is nothing but a realisation
of mathematical algorithms. Consequently, the observation that maths
can be very hard to read carries over to code, and therefore the need
to make code as easy to understand as possible also applies
here. Another analogy that carries over from mathematics is that very
often it's one's own work that one is trying to understand and
correct. This ought to create a very strong incentive to write very
clear code adhering to all the conventions because the poor
individual who has to read your work to find the bugs might very well
be you!

Just as in mathematics, programming has a whole set of conventions
which sit on top of the formal requirements of a programming language,
and largely exist in order to make the code easier for all programmers
to read. Some of these rules, typically the more formulaic ones about
matters such as code layout and naming conventions, are somewhat
different in different programming languages. Others, most especially
higher lever principles like parsimony and modularity, are universal
principles that apply more or less regardless of the language employed
or the sort of programming being undertaken. Good programming style,
like good writing style, is a skill learned through experience and
through receiving feedback on the code you write, and it is not the
intention of this chapter to produce an exhaustive guide. However, it
is useful to introduce some of the key concepts, rules and conventions
in a more formal way.

PEP 8
-----

Publishers, journals, and institutions often have style guides
designed to instil a certain uniformity in the use of English (or
other human languages). Similarly, style guides exist for programming
languages. In some languages, the preferred style can vary
significantly from project to project, and there can be vigorous
disagreement between factions about fine points of style, such as
whether or not an opening curly bracket should start on a new
line. Fortunately, the Python community has an essentially unified and
very widely followed set of conventions. These are codified in one of
the Python standards documents, `PEP 8
<https://www.python.org/dev/peps/pep-0008/>`_ [#pep]_. PEP 8 isn't all
that long, and it is worth taking the time to read. Not every rule in
PEP 8 is reproduced in this chapter, though many of the most commonly
encountered ones are. Conversely, PEP 8 is rather narrowly concerned
with code layout rules while this chapter roams more widely.

flake8
......

One of the helpful characteristics of PEP 8 is that many of its
strictures can be enforced automatically by a computer
program. Indeed, many Python editors can be configured to highlight
violations of PEP 8 visually in the editing window. Alternatively, one
can run a stand-alone program which will read Python source files and
create reports of (many of) the PEP 8 violations they contain. One
such program is called flake8. Running flake8 on all of the source
code in a project, preferably automatically on every commit, is an
excellent mechanism for keeping a project's code in PEP 8
conformance. Indeed, without a mechanism like this, there is a strong
tendency for programmers to cut style corners, with the effect that
the code in a project becomes harder and harder to read and work with.

Code layout
-----------

Perhaps surprisingly, one of the most important factors in making code
readable is the space, or lack of it, between and around the text
which makes up the code. Whitespace affects readability in many
ways. Too much code bunched together makes it hard for the eye to
separate programme statements, while leaving too much space limits the
amount of code which fits in the editor window at once. This requires
the programmer to scroll constantly and to have to remember
definitions which are not currently on the screen.

As in written prose, whitespace can also convey information by
grouping together concepts which are related and separating distinct
ideas. This gives the reader visual clues which can aid in
understanding the code. With this in mind, we now turn to some of the
PEP 8 rules around white space and code formatting.

Blank lines
...........

1. Classes and functions defined at the top level of a module
   (i.e. not nested in other classes or functions) have two blank
   lines before and after them. These are the largest and most
   distinct units in a module, so it helps the reader to make them
   quite distinct from each other.
2. Methods within a class are separated by a single blank
   line. Similarly, functions defined inside other functions are
   separated from surrounding code by a single blank line.
3. Statements within functions usually follow on the immediate next
   line, except that logical groups of statements, can be separated by
   single blank lines. Think of each statement as a sentence following
   on from the previous, with blank lines used to divide the function
   into short paragraphs.

**Do not add extra blank lines to space out code**. Vertical space on
the screen is limited, your readers will not thank you.
   
White space within lines
........................

1. Don't put a space after an opening bracket (of any shape), or
   before a closing bracket. This is because the role of brackets is
   to group their contents, so it's confusing to visually separate the
   bracket from the contents.

    .. container:: badcode

        .. code-block:: python3

            ( 1, 2) # Space after opening bracket.
            (1, 2 ) # Space after closing bracket.

    .. container:: goodcode

        .. code-block:: python3
        
            (1, 2) # No space between brackets and contents.

2. Similarly, don't put a space between the function name and the
   opening round bracket of a function call, or between a variable
   name and the opening square bracket of an index. In each of these
   cases, the opening bracket belongs to the object, so it's confusing
   to insert space between the object name and the bracket.

    .. container:: badcode

        .. code-block:: python3

            my_function (1) # Space between function name and bracket.
            x [0] # Space between variable name and index square bracket.

    .. container:: goodcode

        .. code-block:: python3

            my_function(1)
            x[0]
 
3. Put a space after a comma but not before it, exactly like you would
   in writing prose. Following the convention that everyone is used to
   from writing aids understanding. Where a trailing comma comes right
   before a closing bracket, then don't put a space. The rule that
   there are no spaces before a closing bracket is more important.

     .. container:: badcode

        .. code-block:: python3

            (1,2,3) # Spaces missing after commas.
            (1 ,2 ,3) # Spurious spaces before commas.
            (1, ) # Space before closing bracket.

     .. container:: goodcode

        .. code-block:: python3

            (1, 2, 3) # Spaces after commas.
            (1,) # No space before closing bracket.

4. Put exactly one space on each side of an :ref:`assignment <assignment>` (`=`) and an
   :ref:`augmented assignment <augassign>` (`+=`, `-=`, etc.). In an assignment
   statement, the most important distinction is between the left and
   right hand sides of the assignment, so adding space here aids the
   reader.

    .. container:: badcode

        .. code-block:: python3

            x=1 # Missing spaces around equals sign.
            x+=1 # Missing spaces around augmented addition operator.

            frog = 2
            cat  = 3 # Additional space before equals sign.

    .. container:: goodcode

        .. code-block:: python3

            x = 1
            x += 1

            frog = 2
            cat = 3

5. Do not put a space either before or after the equals sign of a :ref:`keyword
   argument <tut-keywordargs>`. In this case, grouping the parameter name and
   the argument is more important. Also creates a visual distinction between
   assignment statements and keyword arguments.

    .. container:: badcode

        .. code-block:: python3

            myfunction(arg1 = val1, arg2 = val2) # Spaces around equals signs.

    .. container:: goodcode

        .. code-block:: python3

            myfunction(arg1=val1, arg2=val2)


6. Put exactly one space before and after the lowest priority
   mathematical operators in an expression. This has the effect of
   visually separating the terms of an expression, as we
   conventionally do in mathematics.
7. **Never, ever** have blank spaces at the end of a line, even a blank
   line. These tend to get changed by editors, which results in lots
   of spurious differences between otherwise identical code. This can
   make the difference between two commits of a file very hard to read
   indeed.

Line breaks
...........

1. Have no lines longer than 79 characters. Limiting the line length
   makes lines easier to read, and prevents the editor from
   automatically wrapping the line in harder to read ways. Shorter
   lines are also very useful when using side-by-side differencing
   tools to show the differences between two versions of a piece of
   code.
2. When breaking lines to fit under 79 characters, it's better to
   break the lines using the implied continuation within round, square
   or curly brackets than explicitly with a backslash. This is because
   the brackets provide good visual "book ends" for the beginning and
   end of the continuation.
3. When a mathematical operator occurs at a line break, always put the
   operator first on the next line, and not last on the first
   line. Having the second line start with a mathematical operator
   provides a solid visual clue that the next line is a continuation
   of the previous line. (If you look closely, this is also the rule
   that most publishers of maths books use).

Indentation
...........

1. Indentation is *always* by four spaces per indentation level. If
   your text editor is not set to create 4 spaces per indentation
   level, Google how to change it!
2. When indenting continuation lines inside brackets, there are two
   options, usually depending on how many characters are already on
   the line before the opening bracket:
   
   a. With one or more items on the first line after the opening
      bracket.  Subsequent lines are indented to one space more than
      the opening bracket, so that the first items on each line start
      exactly under each other. The closing bracket comes on the same
      line as the final item.
   b. With the opening bracket as the last item on the first
      line. Subsequent lines are indented more than the first line but
      the same as each other. The closing bracket comes on a new line,
      and is either indented to the same level as the first line, or
      to the subsequent lines (but be consistent in nearby code about
      which).


Names
-----

Programs are full of names. Variables, classes, functions,
modules: much, perhaps most, of the text of a program is made up of
names. The choice of names, therefore, has a massive impact on the
readability of a program. There are two aspects to naming
conventions. One is a set of rules about the formatting of names: when
to use capitals, when underscores and so on. This is covered by PEP 8
and we reproduce some of the important rules below. The second aspect
is the choice of the letter, word, or words that make up a name. This
is much more a matter of judgement, though there are guiding principles
that greatly help with clarity.

PEP 8 name conventions
......................

PEP 8 has some rather detailed rules for naming, including for
advanced cases that we are unlikely to encounter in the short term,
but the most important rules are short and clear:

class names
  Class names use the CapWords convention: each word in a name is
  capitalised and words are concatenated, without underscores between.

exception names
  Exceptions are classes, so the rules for class names apply with the
  addition that exceptions that designate errors should end in
  `Error`.

function, variable, and module names
  Almost all names other than classes are usually written in all
  lower case, with underscores separating words. Even proper nouns are
  usually spelt with lower case letters to avoid being confused with
  class names.

method parameters
  The first parameter to an instance method is the class
  itself. *Always and without exception* name this parameter `self`.

non-public methods and attributes
  If a method or attribute is not intended to be directly accessed
  from outside the class, it should have a name starting with an
  underscore. This provides a clear distinction between the public
  interface of a class and its internal implementation.

Choosing names
..............

Short names help make short lines of code, which in turn makes it easier
to read and understand what the code does to the values it is
operating on. However short names can also be cryptic, making it
difficult to establish what the names mean. This creates a tension:
should names be short to create readable code, or long and descriptive
to clarify their meaning?

A good answer to this dilemma is that local variables should have
short names. These are often the most frequently occurring variables on
a line of code, which makes the statement more
intelligible. Should a reader be unclear what a variable stands for,
the definition of a local variable will not be very far
away. Conversely, a module, class, or function which might be used
far from its definition had better have a descriptive name which makes
its purpose immediately apparent.

Follow the mathematics
......................

Remember that the key objective of code style conventions is to make
it easier for readers to understand the code. If the code implements a
mathematical algorithm, then it's quite likely that readers of that
code will have at least a passing acquaintance with that area of
mathematics. You will therefore greatly help their intuition for what
your code does if the names in the code match the mathematical
conventions for the same concepts. You can use underscores to hint at
subscripts, just like in LaTeX: for example if you write a function
which changes coordinates, then `x_old` and `x_new` are likely to be
good names for the coordinate vector before and after the
transformation.

As an exception to the rules about variable case, it is a good idea to
use single capital letter names in circumstances where they would be
used in the maths, for example, to name a matrix.

Mathematicians often use Greek letters as variable names,
occasionally they venture further afield and use Cyrillic or Hebrew
letters. Python does allow for variable names written in other
alphabets, but these are hard to type on many keyboards. Someone
trying to fix bugs in your code will curse you if they can't even type
the names! Do, by all means, use Greek or other language variable
names where this will make the relationship between the maths and the
code obvious, but write out the Greek letter name in Roman
letters. For example, `theta` is a very good name for a variable
representing an angle. Capital Greek letters are sometimes represented
by capitalising the first letter of the Roman word, but take care to
avoid situations where this might be confused for a class name.

Parsimony and modularity
------------------------

Good programming style is primarily about making programmes easy to
understand. One of the key limitations of understanding is the sheer
number of objects that the reader can keep in their short term memory
at once. Without diverting into the psychology literature, this is
only a couple of handfuls of values at most. This means that the
largest amount of code that a reader can actively reason about is
limited to a few operations on a few variables. As a programmer, there
are two tools at your disposal to achieve this. The first is to be
parsimonious and not introduce unnecessary temporary variables. The
second is to use abstractions such as classes and function interfaces
to split the problem up into small pieces so that each individual
function or method is small enough for a reader to understand.

As a (somewhat contrived) example, assume that you need to create a list of all
the positive integers less than 9999 which are divisible by all the numbers up
to seven. You could write this in 5 difficult to understand lines:

.. container:: badcode

   .. code-block:: python3

         result = []

         for _ in range(1, 9999):
            if _ % 1 == 0 and _ % 2 == 0 and _ % 3 == 0 and _ % 4 == 0 \
                and _ % 5 == 0 and _ % 6 == 0 and _ % 7 == 0:
                    result.append(_)


Much better would be to write a single more abstract but simpler line:

.. container:: goodcode

    .. code-block:: python3

         result = [num for num in range(1, 9999) if all(num % x == 0 for x in range(1, 8))]


Use comprehensions
..................

It is very common to write loops to populate collection objects with
values. For example, we might make a list of the first 10 square
numbers for further use:

.. container:: badcode

    .. code-block:: python3

       squares = []
       for i in range(10):
           squares.append((i+1)**2)

This is a fairly typical, if simple, example. It takes three lines of
code: one to initialise the list, one to loop, and one to add the
values to the list. Alternatively, if we had used a :ref:`list
comprehension <tut-listcomps>`, all three steps would have been subsumed into a single
operation:

.. container:: goodcode

    .. code-block:: python3

       squares = [(i+1)**2 for i in range(10)]

At least for fairly simple operations, comprehensions are almost
always easier for the reader to understand than loops. In addition to
lists, comprehensions are also available for :ref:`sets <tut-sets>`
and :ref:`dictionaries <tut-dictionaries>`.

Redundant logical expressions
.............................

One exceptionally common failure of parsimony is to write expressions of the following form:

.. container:: badcode

   .. code-block:: python3

       if var == True:

To see the problem with this statement, let's write out its truth table:

.. rst-class:: center-align-center-col
      
   ===== =============
   `var` `var == True`
   ===== =============
   T     T
   F     F
   ===== =============

In other words, the expressions `var` and `var == True` are logically
equivalent (at least assuming `var` is a :ref:`boolean value <bltin-boolean-values>`), so it would
have been more parsimonious to write:

.. container:: goodcode

   .. code-block:: python3

      if var:

Similarly:

.. container:: badcode

   .. code-block:: python3

      if var == False:

is frowned upon by programmers in favour of:

.. container:: goodcode

   .. code-block:: python3

       if not var:

Finally, the use of :ref:`else <else>` (or :ref:`elif <elif>`) can reduce the number
of logical expressions that the reader has to read and
understand. This means that:

.. container:: badcode

    .. code-block:: python3

       if var:
           # Some code
       if not var:
           # Some other code

should be avoided in favour of:

.. container:: goodcode

    .. code-block:: python3

       if var:
           # Some code
       else:
           # Some other code.

In addition to having fewer logical operations which the reader needs
to understand, the `if...else` version explicitly ties
the two cases together as alternatives, which is an additional aid to
understanding.

Use the fact that every object is True or False
...............................................

Every Python object is logically either :data:`True` or :data:`False` according to the
following rules:

1. None is False.

2. Zero is False, all other numerical values are True.

3. An empty collection is False, any other container is true. For
   example, an empty list is False, but the list `[0, 0]` is True.

4. The null string `""` is False, a string containing any characters is True.

5. A user-defined class is True unless:

   a. It defines the :meth:`~object.__bool__` :term:`special
      method`. In this case the truth value is whatever this method
      returns.

   b. It doesn't define :meth:`~object.__bool__` but does define
      :meth:`~object.__len__`. In this case the object is False if the
      length is zero, and True otherwise.

These rules are laid out formally in :ref:`the Python documentation
<truth>`. One way that they can be used to write simpler, clearer code
is in the very common case of code that should only execute if a
collection object actually contains something. In that case, this form
of test is to be preferred:

.. container:: goodcode

    .. code-block:: python3

       if mysequence:
           # Some code using mysequence

instead of:

.. container:: badcode

    .. code-block:: python3

       if len(mysequence) > 0:
           # Some code using mysequence

.. _repetition:

Avoid repetitition
..................

Programmers very frequently need to do *nearly* the same thing over and over.
One obvious way to do this is to write code for the first case, then copy and
paste the code for subsequent cases, making changes as required. There are a
number of significant problems with this approach. First, it multiplies the
amount of code that a reader has to understand, and does so in a particularly
pernicious way. A reader will effectively have to play "spot the difference"
between the different code versions, and hope they don't miss something. Second,
it makes it incredibly easy for to get confused about which version of the code
a programmer is supposed to be working on. There are few things more frustrating
than attempting to fix a bug and repeatedly seeing that nothing changes, only to
discover hours (or days) later that you have been working on the wrong piece of
nearly-identical code. Finally, lets suppose that a bug is fixed - what happens
to the near-identical clones of that code? The chance is very high that the bug
stays unfixed in those versions thereby creating yet another spot the difference
puzzle for the next person encountering a bug.

Abstractions are essentially tools for removing harmful repetition. For example,
it may be possible to bundle up the repeated code in a function or class, and to
encode the differences between versions in the :term:`parameters <parameter>` to
the function or class constructor. If the differences between the versions of
the code require different code, as opposed to different values of some
quantities, then it may be possible to use :term:`inheritance` to avoid
repetition. We will return to this in :numref:`Chapter %s<inheritance>`.


Comments
--------

Comments are non-code text included in programs to help explain what
they do. Since comments exist to aid understanding, some programmers
come to the conclusion that more comments imply more
understanding. Indeed, some programmers are even taught that every
line of code should have a comment. This could not be more wrong!

While judiciously deployed comments can be an essential aid to
understanding, too many comments can be worse than too few. If the
code is simple, elegant, and closely follows how a reader would expect
the algorithm to be written, then it will be readily understood
without comments. Conversely, attempting to rescue obscure, badly
thought-through code by writing about it is unlikely to remedy the
situation.

A further severe problem with comments is that they can easily become
out of date. If a piece of code is modified, it is all too easy for the
programmer to neglect to update accompanying comments. The result is
comments which explain one thing, code which does something else, and
exceptionally baffled readers.

Three rules for commenting
..........................

1. If code is so simple, clear, and obvious that it can be easily
   understood without comments, don't comment.
2. If code is not easily understood without comments, the problem is
   probably the code. Refactor the code to be simpler and easier to
   understand.
3. If, and only if, you are convinced that it is strictly necessary to do
   something unobvious, then do so and include a comment.

Comment why, not what
.....................

Even where a comment is unavoidable, it should still usually be
obvious *what* it is that code does. It is far more likely to be
justifiable to include a comment about *why* a particular approach is
taken. For example, it might be worth commenting why an apparently
simpler alternative strategy is actually invalid.


Docstrings
----------

There is one enormous exception to the rule that comments should be
used only sparingly: docstrings. Docstrings (a portmanteau of
"documentation strings") are comments at the start of modules,
classes, and functions which describe public interfaces. The entire
point of a public interface is that the programmer using it should not
have to concern themselves with how it is implemented. They should,
therefore, not need to read the code in order to understand how to use
it. 

Glossary
--------

 .. glossary::
    :sorted:

    modularity
       The design principle that programs should be broken into small,
       easily understandable units, which communicate with each other
       through clearly specified interfaces.

    parsimony
       The design principle that unnecessary code, names, and objects
       should be avoided.

.. rubric:: Footnotes

.. [#pep] PEP stands for "Python Enhancement Proposal". PEPs describe
          everything from code style to voting algorithms among Python
          developers. Their main purpose, as the name suggests, is to
          document proposals for changes to the Python language. As
          such, they are usually of little interest to most Python
          users. However the PEPs having to do with style have wider
          significance.
