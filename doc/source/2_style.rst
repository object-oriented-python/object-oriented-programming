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

PEP 8 and flake8
----------------

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
6. *Never, ever* have blank spaces at the end of a line, even a blank
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


Naming conventions
------------------

Comments
--------

Docstrings
..........

Parsimony
---------


.. rubric:: Footnotes

.. [#pep] PEP stands for "Python Enhancement Proposal". PEPs describe
          everything from code style to voting algorithms among Python
          developers. Their main purpose, as the name suggests, is to
          document proposals for changes to the Python language. As
          such, they are usually of little interest to most Python
          users. However the PEPs having to do with style have wider
          significance.
