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
---------------------

Consider this line of Python code::
  
  print(a + b)

What does it do? Well, assuming that `a` and `b` are suitably defined, it
prints their sum. This, however, begs the question: what is "suitably
defined", and what is "sum"? For example:

.. code-block:: ipython3
  
  In [1]: a = 1
  
  In [2]: b = 2

  In [3]: print(a + b)                                                                                                                                                                                                  
  3

You're unlikely to be surprised that Python can add integers. On the
other hand:
  
.. code-block:: ipython3
  
  In [1]: a = 'fr'
  
  In [2]: b = 'og'

  In [3]: print(a + b)                                                                                                                                                                                                  
  'frog'

So the meaning of `+` depends on what is being added. What happens if
we add an integer to a string?

.. code-block:: ipython3

  In [1]: a = 1                                                                                                                                                                                                       

  In [2]: b = 'og'                                                                                                                                                                                                    

  In [3]: print(a + b)                                                                                                                                                                                                
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-3-0ae8b1612688> in <module>
  ----> 1 print(a + b)
  
  TypeError: unsupported operand type(s) for +: 'int' and 'str'

In this error, Python is complaining that `+` does not make sense if
the items being added (the "operands") are a in integer and a
string. This makes our understanding of "suitably defined" more
concrete: clearly some pairs of objects can be added and others
can't. However, we should be careful in the conclusions we draw. We
might be tempted to believe that we can add two values if they are of
the same type. However, if we try this with a pair of sets then we're
also in trouble:

.. code-block:: ipython3
  
  In [1]: a = {1, 2}                                                                                                                                                                                                  

  In [2]: b = {2, 3}                                                                                                                                                                                                  

  In [3]: print(a + b)                                                                                                                                                                                                
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-3-0ae8b1612688> in <module>
  ----> 1 print(a + b)

  TypeError: unsupported operand type(s) for +: 'set' and 'set'
  
Conversely we might suspect that two values can be added only if they are of the same
type. However it is perfectly legal to add an integer and a floating
point value:

.. code-block:: ipython3
   
   In [1]: a = 1                                                                                                                                                                                                       

   In [2]: b = 2.5                                                                                                                                                                                                     

   In [3]: print(a + b)                                                                                                                                                                                                
   3.5

In Python, the operator `+` encodes an abstraction for addition. This means
that `+` stands for the addition operation, whatever that may mean for
a particular pair of operands. For the purposes of the abstraction,
everything which is specific to the particular operands is
ignored. This includes, for example,
the mechanism by which the addition is calculated and the value of the
result. This enables a programmer to think about the relatively simple
mathematical operation of addition, rather than the potentially
complex or messy way it might be implemented for particular data.

.. proof:definition::

   An *abstraction* is a mathematical object with a limited set of
   defined properties. For the purposes of the abstraction, any other
   properties that an object may have are disregarded.

An abstraction is a purely mathematical concept, but it is one which
maps to one or more concrete realisations in code. Sometimes the
abstract mathematical concept and its concrete realisation match so
perfectly that it is difficult to distinguish the two. In those
circumstances we usually conflate the terminology for the abstraction
and the code object. "Type" is one such example, and we turn to that
now.

Types
-----

In the previous section, we observed that addition may or may not be
defined, depending on what the types of its operands are. In doing so,
we skirted the question of what it means for a code object to have
type.

.. proof:definition::

   A *type* or *class* is an abstraction defined by a set of possible values, and
   a set of operators valid for objects of that type.

Every object in Python has a type. This is true for primitive numeric
types, such as :class:`int`, :class:`float`, and :class:`complex`; for sequences such as
string (:class:`str`), :class:`tuple`, and :class:`list`; and also for more complex types
such as :class:`set` and dictionary (:class:`dict`). Indeed, the
Python concept of type goes much further, as we discover if we call
:class:`type` on various objects:

.. code-block:: ipython3

  In [1]: type(1)                                                                                                                                                                                                     
  Out[1]: int
  
  In [2]: type(abs)                                                                                                                                                                                                   
  Out[2]: builtin_function_or_method

So `1` is an object of type :class:`int`, which means that it comes with all of
Python's operations for integer arithmetic. :func:`abs`, on the other hand,
is a builtin function, so its priciple operation is that it can be
called on one or more suitable arguments (for example `abs(1)`). If
every object has a type, what about types themselves? What is the type
of `int`?

.. code-block:: ipython3
  
  In [1]: type(int)                                                                                                                                                                                                   
  Out[1]: type 

So :class:`int` is the type of integer objects, and is itself an
object with type :class:`type`. That rather invites the question what
is the type of :class:`type`?

.. code-block:: ipython3

  In [1]: type(type)                                                                                                                                                                                                  
  Out[1]: type

This actually makes perfect sense, because :class:`type` is simply the
type of types.

We will return to types in much more detail later. At this stage, the
take home message is that essentially everything you will encounter in
Python is an object, and every object has a type.

.. note::

   In Python, the term
   "class" is essentially synonymous with "type", so "what is the class
   of `foo`" is the same as saying "what is the type of "foo". However
   the two terms are not synonyms when used in code. :class:`type` can be
   used to determine the type of an object, while :keyword:`class` is
   used to define new types.


Defining new types
------------------

Python has a rich set of :doc:`built-in types
<library/stdtypes>`. These form powerful building blocks for the
language, but one very soon finds mathematical abstractions which do
not have implementations among the built-in types of the Python
interpreter. For example, the built-in types do not include a matrix
or multidimensional array type. The ability to make new data types
which provide concrete implementations of further mathematical
abstractions is central to effectively exploiting abstraction in
programming.

As an example, lets suppose that we want to work with real polynomials in
one variable. That is to say, functions of the form:

.. math::

   f(x) = \sum_{n=0}^d c_n x^n \quad \textrm{for some } d\in
   \mathbb{N}, c_n \in \mathbb{R}

The set of all polynomials is a well-defined (though infinite) set of
different values, with a number of well-defined properties. For
example we can add and multiply polynomials, resulting in a new
polynomial. We can also evaluate a polynomial for a particular value
of :eq:`x`, which would result in a real value.

This is the mathematical abstraction of a polynomial. How would we
represent this abstraction in Python code? A polynomial is
characterised by its set of coefficients, so we could in principle
represent a polynomial as a :class:`tuple` of coefficient
values. However, addition of tuples is concatenation, and
multiplication of two tuples isn't even defined, so this would be a
very poor representation of the mathematics: a polynomial represented
as a tuple of coefficients would not behave the way a mathematician
would expect. Instead, what we need to do is make a new type whose
operations match the mathematical properties of a polynomial.

Classes and constructors
........................

The Python keyword for declaring a new type is
:keyword:`class`. Just like a function declaration, this creates a new
indented block. In this case, the block contains all of the function
declarations which define the operations on this new type. Let's make
a very simple implementation::

  class Polynomial:

    def __init__(self, coefficients):

        self.coefficients = coefficients

Executing this code in a Python interpreter would enable us to create
a simple polynomial, and inspect its coefficients:

.. code-block:: ipython3

   In [7]: f = Polynomial((0, 1, 2))                                                                                                                                                                                   

   In [8]: f.coefficients                                                                                                                                                                                             
   Out[8]: (0, 1, 2)
