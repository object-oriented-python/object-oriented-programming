.. _style.rst

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
go on and derive all the analysis you have learned so far. However you
would confuse yourself and your readers horribly, because I have
swapped the roles of :math:`\delta` and :math:`\epsilon` in the
definition. The formal properties of mathematical objects do not
depend on the names we give them or, often, on how we lay out formulae
on a page. However mathematics is designed to be read by humans with
their habit-forming, pattern-matching brains. So if everyone adopts
similar conventions for how to write down mathematics, everyone
schooled in those conventions will find that mathematics easier to
understand. This is vitally important, because understanding
mathematics is *hard*. Non-standard notation makes it doubly hard,
because the reader has to consciously remember the meaning of all the
symbols. Conversely, once a reader has learned the notational
conventions for a field of mathematics, the meanings of the symbols
become natural and don't require conscious thought. This leaves all
the available brain power to concentrate on the mathematical content
at hand.

You might at first think that this logic does not apply to computer
programs. After all, a computer program is read by another computer
program, and is not understood but rather acted on
mechanically. Surely it doesn't matter how it looks or what symbols
you use, so long as it's correct, and possibly fast? This entirely
understandable sentiment has aflicted almost all programmers at some
point or another, and typically has got them into more or less serious
difficulty before they realised that it's completely wrong.

In reality, a computer program is frequently read. Indeed, code is
typically read many more times than it is written or changed. Most
obviously, programmers read code in order to understand its functionality,
and in order to work out what is wrong with the code when it fails to
produce the correct results. Reading code is very much like reading
mathematics, because a computer program is nothing but a realisation
of mathematical algorithms. Consequently the observation that maths
can be very hard to read carries over to code, and therefore the need
to make code as easy to understand as possible also applies
here. Another analogy that carries over from mathematics is that very
often it's one's own work that one is trying to understand and
correct. This ought to create a very strong incentive to write very
clear code adhering to all the conventions, because the poor
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
intention of this chapter to produce an exhaustive guide. However it
is useful to introduce some of the key concepts, rules and conventions
in a more formal way.

PEP 8
-----

Publishers, journals, and institutions often have style guides
designed to instill a certain uniformity in the use of English (or
other human language). Similarly, style guides exist for programming
languages. In some languages the preferred style can vary
significantly from project to project, and there can be vigorous
disagreement between factions about fine points of style, such as
whether or not an opening curly bracket should start on a new line
(Google it, it's as bizarre as it sounds). Fortunately, the Python
community has an essentially unified and very widely followed set of
conventions. These are codified in one of the Python standards
documents, `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_
[#pep]_. PEP 8 isn't all that long and it is worth taking the time to
read. Not every rule in PEP 8 is reproduced in this chapter, though
many of the most commonly encountered ones are. Conversely, PEP 8 is
rather narrowly concerned with code layout rules while this chapter
roams more widely.

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
   line, except that logical groups of statements can be separated by
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
2. Similarly, don't put a space between the function name and the
   opening round bracket of a function call, or between a variable
   name and the opening square bracket of an index. In each of these
   cases, the opening bracket belongs to the object, so it's confusing
   to insert space between the object name and the bracket.
3. Put a space after a comma but not before it, exactly like you would
   in writing prose. Following the convention that everyone is used to
   from writing aids understanding. Where a trailing comma comes right
   before a closing bracket, then don't put a space. The rule that
   there are no spaces before a closing bracket is more important.
4. Put exactly one space on each side of an assignment (`=`) and an
   augmented assignment (`+=`, `-=`, etc.). In an assignment
   statement, the most important distinction is between the left and
   right hand sides of the assignment, so adding space here aids the
   reader.
5. Put exactly one space before and after the lowest priority
   mathematical operators in an expression. This has the effect of
   visually separating the terms of an expression, as we
   conventionally do in mathematics.
6. **Never, ever** have blank spaces at the end of a line, even a blank
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
names. The choice of names therefore has a massive impact on the
readability of a program. There are two aspects to naming
conventions. One is a set of rules about the formatting of names: when
to use capitals, when underscores and so on. This is covered by PEP 8
and we reproduce some of the important rules below. The second aspect
is the choice of the letter, word, or words that make up a name. This
is much more a matter of judgment, though there are guiding principles
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
  interface of a class, and its internal implementation.

Choosing names
..............

Short names help make short lines of code, which in turn makes it easier
to read and understand what the code does to the values it is
operating on. However short names can also be cryptic, making it
difficult to establish what the names mean. This creates a tension:
should names be short to create readable code, or long and descriptive
to clarify their meaning?

A good answer to this dilemma is that local variables should have
short names. These are often the most frequently occuring variables on
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
code will have at least a passing acquantence with that area of
mathematics. You will therefore greatly help their intuition for what
your code does if the names in the code match the mathematical
conventions for the same concepts. You can use underscores to hint at
subscripts, just like in LaTeX: for example if you write a function
which changes coordinates, then `x_old` and `x_new` are likely to be
good names for the coordinate vector before and after the
transformation.

As an exception to the rules about variable case, it is a good idea to
use single capital letter names in circumstances where they would be
used in the maths, for example to name a matrix.

Mathematicians often use Greek letters as variable names,
occasionally they venture further afield and use Cyrilic or Hebrew
letters. Python does allow for variable names written in other
alphabets, but these are hard to type on many keyboards. Someone
trying to fix bugs in your code will curse you if they can't even type
the names! Do, by all means, use Greek or other language variable
names where this will make the relationship between the maths and the
code obvious, but write out the Greek letter name in Roman
letters. For example, `theta` is a very good name for a variable
representing an angle. Capital greek letters are sometimes represented
by capitalising the first letter of the Roman word, but take care to
avoid situations where this might be confused for a class name.

Parsimony and simplicity
------------------------

Redundant logical expressions
.............................


Comments
--------

Comments are non-code text included in programs to help explain what
they do. Since comments exist to aid understanding, some programmers
come to the conclusion that more comments implies more
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
out of date. If a piece of code is modified, it is all to easy for the
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
taken. For example it might be worth commenting why an apparently
simpler alternative strategy is actually invalid.


Docstrings
..........

There is one enormous exception to the rule that comments should be
used only sparingly: docstrings. Docstrings (a portmanteau of
"documentation strings") are comments at the start of modules,
classes, and functions which describe public interfaces. The entire
point of a public interface is that the programmer using it should not
have to concern themselves with how it is implemented. They should
therefore not need to read the code in order to understand how to use
it. 


.. rubric:: Footnotes

.. [#pep] PEP stands for "Python Enhancement Proposal". PEPs describe
          everything from code style to voting algorithms among Python
          developers. Their main purpose, as the name suggests, is to
          document proposals for changes to the Python language. As
          such, they are usually of little interest to most Python
          users. However the PEPs having to do with style have wider
          significance.
