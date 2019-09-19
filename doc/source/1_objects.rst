Objects and abstraction
=======================

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

Abstraction in action
=====================

Consider this line of Python code::
  print(a + b)

What does it do? Well, assuming that `a` and `b` suitably defined, it
prints their sum. This, however, begs the question: what is "suitably
defined", and what is "sum"? For example::
  a = 1
  b = 2
  print(a + b)

prints::
  3

You're unlikely to be surprised that Python can add integers. On the other hand::
  a = 'fr'
  b = 'og'
  print(a + b)

prints::
  'frog'

So the meaning of `+` depends on what is being added. What happens if
we add an integer to a string?::
  a = 1
  b = 'og'
  print(a + b)

results in this error::
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-9-bd58363a63fc> in <module>
  ----> 1 a + b

  TypeError: unsupported operand type(s) for +: 'int' and 'str'

Python is complaining that `+` does not make sense if the items being
added (the "operands") are a in integer and a string. This makes our
understanding of "suitably defined" more concrete: clearly some pairs
of objects can be added and others can't. However, we should be
careful in the conclusions we draw. We might be tempted to believe
that we can add two values if they are of the same type. However, if
we try this with a pair of sets then we're also in trouble:: a = {1,
2} b = {2, 3} print(a + b)

results in::


We might be tempted
to conclude that two values can be added only if they are of the same
type. However it is perfectly legal to add an integer and a floating
point value::
  a = 1
  b = 2.5
  print(a + b)




