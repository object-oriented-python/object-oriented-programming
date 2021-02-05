.. _objects:

Objects and abstraction
=======================

This week we will take a first look at the representation of
abstract mathematical objects and operations as data objects in a
computer program. We will learn about what it means for objects to have
a :term:`type`, and how to create new types using the :keyword:`class` keyword.

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

You're unlikely to be surprised that Python can add :ref:`integers <typesnumeric>`. On the
other hand:
  
.. code-block:: ipython3
  
  In [1]: a = 'fr'
  In [2]: b = 'og'
  In [3]: print(a + b)                                              
  'frog'

So the meaning of `+` depends on what is being added. What happens if
we add an integer to a :ref:`string <textseq>`?

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
the items being added (the :term:`operands`) are an integer and a
string. This makes our understanding of "suitably defined" more
concrete: clearly some pairs of objects can be added and others
can't. However, we should be careful about the conclusions we draw. We
might be tempted to believe that we can add two values if they are of
the same type. However, if we try this with a pair of :ref:`sets <types-set>` then we're
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
type. However it is perfectly legal to add an integer and a :ref:`floating
point value <typesnumeric>`:

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
circumstances, we usually conflate the terminology for the abstraction
and the code object. "Type" is one such example, and we turn to that
now.

Types
-----

In the previous section, we observed that addition may or may not be
defined, depending on what the types of its operands are. In doing so,
we skirted the question of what it means for an object to have
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
is a :doc:`built-in function <library/functions>`, so its defining operation is that it can be
called on one or more suitable arguments (for example `abs(1)`). If
every object has a type, what about types themselves? What is the type
of `int`?

.. code-block:: ipython3
  
  In [1]: type(int)                                        
  Out[1]: type 

We see that :class:`int` is the type of integer objects, and is itself an
object with type :class:`type`. That rather invites the question of what
is the type of :class:`type`?

.. code-block:: ipython3

  In [1]: type(type)                                       
  Out[1]: type

This actually makes perfect sense, because :class:`type` is simply the
type of types.

We will return to types in much more detail later. At this stage, the
take-home message is that essentially everything you will encounter in
Python is an object, and every object has a type.

.. note::

   In Python, the term
   "class" is essentially synonymous with "type", so "what is the class
   of `foo`" is the same as saying "what is the type of `foo`". However
   the two terms are not synonyms when used in code. :class:`type` can be
   used to determine the type of an object, while :keyword:`class` is
   used to define new types.


Defining new types
------------------

.. dropdown:: Video: a first class

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/488143930"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f8b07554-16ea-47b8-bf19-ac8a010af0f6>`__

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
example, we can add and multiply polynomials, resulting in a new
polynomial. We can also evaluate a polynomial for a particular value
of :math:`x`, which would result in a real value.

This is the mathematical abstraction of a polynomial. How would we
represent this abstraction in Python code? A polynomial is
characterised by its set of coefficients, so we could in principle
represent a polynomial as a :class:`tuple` of coefficient
values. However, the addition of tuples is :term:`concatenation`, and
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

    def __init__(self, coefs):

        self.coefficients = coefs

We'll interpret the :math:`i`-th coefficient as the coefficient of :math:`x^i`.
This will simplify the program logic, but take care because mathematicians
usually write coefficients from largest power of :math:`x` to smallest, and this
is the opposite of that. Executing this code in a Python interpreter would enable us to create
a simple polynomial, and inspect its coefficients:

.. code-block:: ipython3

   In [7]: f = Polynomial((0, 1, 2))
   In [8]: f.coefficients
   Out[8]: (0, 1, 2)

The three lines of Python defining the :class:`Polynomial` class contain
several important concepts and Python details that it is important to
understand.

The :ref:`class definition <python:class>` statement opens a new block, so
just like a :ref:`function definition <function>`, it starts with
the keyword, followed by the name of the class we are defining, and
ends with a colon. User-defined classes in Python (i.e. classes not
built into the language) usually have CapWords names. This means
that all the words in the name are capitalised and run together without spaces. For
example, if we decided to make a separate class for complex-valued
polynomials, we might call it :class:`ComplexPolynomial`.

Inside the class definition, i.e. indented inside the block, is a
function called :meth:`~object.__init__`. Functions defined inside a class
definition are called :term:`methods<method>`. The :meth:`~object.__init__` method has a
rather distinctive form of name, starting and ending with two
underscores. Names of this format are used in the Python language for
objects which have special meaning in the Python language. The
:meth:`~object.__init__` method of a class has special meaning in Python as
the :term:`constructor` of a class. When we write:

.. code-block:: ipython3

   In [7]: f = Polynomial((0, 1, 2))

This is called :term:`instantiating <instantiate>` an object of type
:class:`Polynomial`. The following steps occur:

1. Python creates an object of type :class:`Polynomial`.
2. The :meth:`~object.__init__` :term:`special method` of :class:`Polynomial`
   is called. The new :class:`Polynomial` object is passed as the
   first parameter (`self`), and the :class:`tuple` `(0, 1, 2)` is passed
   as the second parameter (`coefs`).
3. The name `f` in the surrounding :term:`scope` is associated with the
   :class:`Polynomial`.

.. note::

    Notice that :meth:`Polynomial.__init__` doesn't return anything. The role of
    :meth:`~object.__init__` is to set up the object, `self`; it is not to return a
    value. :meth:`~object.__init__` never returns a value.

Attributes
..........

Let's now look at what happened inside the :meth:`~object.__init__` method. We
have just one line::

  self.coefficients = coefs

Remember that `self` is the object we are setting up, and coefs is the
other parameter to :meth:`~object.__init__`. This line of code creates a new
name inside this :class:`Polynomial` object, called
`coefficients`, and associates this new name with the object passed as
the argument to the :class:`Polynomial` constructor. Names such as
this are called :term:`attributes<attribute>`. We create an attribute
just by assigning to it, and we can then read back the attribute using
the same syntax, which is what we did here:

.. code-block:: ipython3

   In [8]: f.coefficients
   Out[8]: (0, 1, 2)

Attributes can be given any name which is allowed for a Python name in general -
which is to say sequences of letters, numbers and underscores starting with a
letter or an underscore. Special significance attaches to names starting with an
underscore, so these should be avoided in your own names unless you intend to
create a private attribute.

Methods
.......

.. dropdown:: Video: defining methods

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/488273256"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=613249ca-71b8-4f3b-8db9-ac8a0166aa42>`__

We have already met the :term:`special method` :meth:`~object.__init__`,
which defines the class constructor. A much more typical case is an
ordinary method, without a special underscore name. For example,
suppose we wish to be able to access the degree of a polynomial, then
we might add a :meth:`degree` method to our class::

  class Polynomial:

    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):
        
        return len(self.coefficients) - 1

Observe that the new method is indented inside the :keyword:`class`
block at the same level as the :meth:`~object.__init__` method. Observe also
that it too takes `self` as its first parameter. A key difference from
the :meth:`~object.__init__` method is that :meth:`degree` now returns a
value, as most functions do. We can now use our new method to recover
the degree of our Polynomial.

.. code-block:: ipython3

   In [1]: f = Polynomial((0, 1, 2))
   In [2]: f.degree()
   Out[2]: 2

To clarify the role of the `self` parameter it helps to understand
that `f.degree()` is just a short way of writing
`Polynomial.degree(f)`. Like attributes, methods can have any allowed Python
name. Attributes and methods on an object form part of the same
:term:`namespace`, so you can't have an attribute and a method with the same
name. If you try, then the name will be overwritten with whichever was defined
later, so that will be the one which is accessed.

.. note::

   The object itself is always passed as the first argument to a :term:`method`.
   Technically, it is possible to name the first parameter any legal Python
   name, but there is a **very** strong convention that the first parameter to
   any :term:`instance method` is called `self`. **Never, ever** name this
   parameter anything other than `self`, or you will confuse every Python
   programmer who reads your code!

String representations of objects
.................................

.. dropdown:: Video: printing classes

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/488275072"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b30db20c-1224-41b7-a5f2-ac8a01680608>`__


Remember that a key reason for defining new classes is to enable users
to reason about the resulting objects at a higher mathematical level. An
important aid to the user in doing this is to be able to look at the
object. What happens if we print a :class:`Polynomial`?

.. code-block:: ipython3

   In [1]: f = Polynomial((0, 1, 2))
   In [2]: print(f)
   <Polynomial object at 0x104960dd0>

This is less than useful. By default, Python just prints the class of
the object and the memory address at which this particular object is
stored. This is, however, not so surprising if we think about the
situation in a little more depth. How was Python supposed to know what
sort of string representation makes sense for this object? We will
have to tell it.

The way we do so is using another :term:`special method`. The special
method name for the human readable string representation of an object is
:meth:`~object.__str__`. It takes no arguments other than the object itself.
:numref:`polynomial_str` provides one possible implementation of this method.

.. code-block:: python3
    :linenos:
    :caption: An implementation of the string representation of a
        :class:`Polynomial`. This takes into account the usual conventions for
        writing polynomials, including writing the highest degree terms first, and
        omitting zero terms and unit coefficients.
    :name: polynomial_str

    def __str__(self):

        coefs = self.coefficients
        terms = []

        # Degree 0 and 1 terms conventionally have different representation.
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{coefs[1]}x")

        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        # Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

This slightly longer piece of code results from the fact that the
linear and constant terms in a polynomial are usually represented
slightly differently from the higher-order terms. Having added this
new method to our class, we can now observe the result:
      
.. code-block:: ipython3

      In [2]: f = Polynomial((1, 2, 0, 1, 5))
      In [3]: print(f)
      5x^4 + x^3 + 2x + 1
   
In fact, Python provides not one, but two :term:`special
methods<special method>` which convert an object to a
string. :meth:`~object.__str__` is called by :func:`print` and also by
:class:`str`. Its role is to provide the string representation which
is best understood by humans. In mathematical code, this will usually
be the mathematical notation for the object. In contrast, the
:meth:`~object.__repr__` method  is called by :func:`repr` and also provides
the default string representation printed out by the Python command
line. By convention, :meth:`~object.__repr__` should return a string which a
user might type in order to recreate the object. For example::

  def __repr__(self):
  
      return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

`self.__class__.__name__` simply evaluates to the class name, in this case
`Polynomial`. This is better than hard-coding the class name because, as we will
see in :numref:`week %s <inheritance>`, this implementation of
:meth:`~object.__repr__` might well end up being inherited by a class with a
different name. Notice that in order to help ensure consistency of
representations we call :func:`repr` on the coefficients in this case, whereas
in the :meth:`~object.__str__` method we called :class:`str`.

We can now observe the difference in the result:

.. code-block:: ipython3

   In [2]: f = Polynomial((1, 2, 0, 4, 5))                                                                                
   In [3]: f                                                                                                          
   Out[3]: Polynomial((1, 2, 0, 4, 5))

.. _object_equality:

Object equality
...............

.. dropdown:: Video: object equality and test driven development

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/488981397"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=821e53ec-d2c8-43a6-bb16-ac8c01045f31>`__

When are two objects equal? For built-in types Python has equality rules which
broadly match the mathematical identities that you might expect. For example,
two numbers of different types are equal if their numerical value is equal:

.. code-block:: ipython3

    In [1]: 2 == 2.0
    Out[1]: True

    In [2]: 2.0 == 2+0j
    Out[2]: True

Similarly, intrinsic sequence types are equal when their contents are equal:

.. code-block:: ipython3

    In [3]: (0, 1, "f") == (0., 1+0j, 'f')
    Out[3]: True

    In [4]: (0, 1, "f") == (0., 1+0j, 'g')
    Out[4]: False

    In [5]: (0, 1, "f") == (0., 1+0j)
    Out[5]: False

This mathematically pleasing state of affairs doesn't, however, automatically
carry over to new classes. We might expect that two identically defined
polynomials might compare equal:

.. code-block:: ipython3

    In [6]: from example_code.polynomial import Polynomial

    In [7]: a = Polynomial((1, 0, 1))

    In [8]: b = Polynomial((1, 0, 1))

    In [9]: a == b
    Out[9]: False

The reason for this is obvious when one thinks about it: Python has no way to
know when two instances of a new class should be considered equal. Instead, it
falls back to comparing the unique identity of every object. This is accessible
using the built-in function :func:`id`:

.. code-block:: ipython3

    In [10]: id(a)
    Out[10]: 4487083344

    In [11]: id(b)
    Out[11]: 4488256096

This is a perfectly well-defined equality operator, but not a very
mathematically useful one. Fortunately, Python allows us to define a more useful
equality operator using the :meth:`~object.__eq__` :term:`special method`. This
takes the current object and the object it is being compared to, and returns
:data:`True` or :data:`False` depending on whether the objects should be
considered equal. When we write `a == b` in Python, what actually happens is
`a.__eq__(b)`.

A basic implementation of :meth:`~object.__eq__` that checks that the other
object is a :class:`~example-code.polynomials.Polynomial` with the same
coefficients is:

.. code-block:: python3

    def __eq__(self, other):

        return isinstance(other, Polynomial) and \
            self.coefficients == other.coefficients

Equipped with this method, :class:`~example-code.polynomials.Polynomial`
equality now behaves as we might expect.

.. code-block:: ipython3

    In [1]: from example_code.polynomial import Polynomial

    In [2]: a = Polynomial((1, 0, 1))

    In [3]: b = Polynomial((1, 0, 1))

    In [4]: a == b
    Out[4]: True

.. _object_arithmetic:

Defining arithmetic options on objects
......................................

.. dropdown:: Video: polynomial addition.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/489009900"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=727c5b9a-bf61-480e-912e-ac8c01045f09>`__

It's all very well to be able to compare our polynomial objects, but
we won't really have captured the mathematical abstraction involved
unless we have at least some mathematical operations. We have already
observed that objects of some classes can be added. Is this true for
:class:`Polynomial`\s? 

.. code-block:: ipython3

   In [2]: a = Polynomial((1, 0))                                                                                     
   In [3]: b = Polynomial((1,))                                                                                       
   In [4]: a + b                                                                                                      
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-4-bd58363a63fc> in <module>
   ----> 1 a + b

   TypeError: unsupported operand type(s) for +: 'Polynomial' and 'Polynomial'

Of course, once again this is not so surprising since we haven't
defined what addition of polynomials should mean. The :term:`special
method` which defines addition is :meth:`~object.__add__`. It takes the
object itself and another object and returns their sum. That is,    
when you write `a + b` in Python, then what actually happens is
`a.__add__(b)`. 

Before we define our addition method, we first need to consider what
other objects it might make sense to add to a polynomial. Obviously, we
should be able to add two polynomials, but it also makes sense to add
a number to a polynomial. In either case, the result will be a new
polynomial, with coefficients equal to the sum of those of the
summands.

We also need to do something in the case where a user attempts to add
to a polynomial a value for which the operation makes no sense. For
example, a user might accidentally attempt to add a string to a
polynomial. In this case, the Python language specification requires
that we return the special value
:obj:`NotImplemented`. Differentiating between the types of operands
requires two more Python features we have not yet met. One of these is
the built in function :func:`isinstance`, which tests whether an
object is an instance of a class. The other is the class :class:`~numbers.Number`,
which we import from the :mod:`numbers` module. All Python numbers are
instances of :class:`~numbers.Number` so this provides a mechanism for checking
whether the other operand is a number. We will consider
:func:`isinstance` and :class:`~numbers.Number` in more detail when we look at
:ref:`inheritance <inheritance>` and :ref:`abstract base classes
<abstract_base_classes>`.

Putting all this together, :numref:`polynomial_add` defines polynomial addition.

.. code-block:: ipython3
    :linenos:
    :caption: An implementation of addition for :class:`Polynomial`.
    :name: polynomial_add

    def __add__(self, other):
        
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])
        
        elif isinstance(other, Polynomial):
            # Work out how many coefficient places the two polynomials have in common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                                 other.coefficients[:common]))
            
            # Append the high degree coefficients from the higher degree summand.
            coefs += self.coefficients[common:] + other.coefficients[common:]
            
            return Polynomial(coefs)

        else:
            return NotImplemented

Notice that we create a new :class:`Polynomial` object for the result
each time: the sum of two polynomials is a different polynomial, it
doesn't modify either polynomial in place.

Let's try our new addition functionality in action:

.. code-block:: ipython3
   
   In [2]: a = Polynomial((1, 2, 0, 1))
   In [3]: print(a)                                                                                                   
   x^3 + 2x + 1
   In [4]: b = Polynomial((0, 1))                                                                                     
   In [5]: print(b)
   In [6]: print(a + b)                                                                                               
   x^3 + 3x + 1
   In [7]: print(a + 1)                                                                                               
   x^3 + 2x + 2
   In [8]: print(1 + a)                                                                                               
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-8-a42ff1c9a542> in <module>
   ----> 1 print(1 + a)
   
   TypeError: unsupported operand type(s) for +: 'int' and 'Polynomial'

So, everything proceeds as expected until we try to add a
:class:`Polynomial` to an integer. What happened? Remember that
`1 + a` causes Python to call `int.__add__(1, a)`. What does that do?:

.. code-block:: ipython3
    
    In [9]: int.__add__(1, a)                                                                                          
    Out[9]: NotImplemented

Naturally, Python's inbuilt :class:`int` type knows nothing about our
new :class:`Polynomial` class, so when we ask it to do the addition,
it returns :obj:`NotImplemented`. We could, however, tell
:class:`Polynomial` how to be added to an :class:`int`, and Python
provides a mechanism for this. If the :meth:`~object.__add__` of the left hand
operand of `+` returns :obj:`NotImplemented`, then Python tries the
reverse addition method, called :meth:`~object.__radd__`, on the right hand
operand. Because we know that polynomial addition is commutative,
we can define this very easily::

    def __radd__(self, other):

        return self + other

With our newly enhanced :class:`Polynomial` class, we can revisit the
previously problematic operation:

.. code-block:: ipython3
   
   In [2]: a = Polynomial((1, 2, 0, 1))
   In [3]: print(1 + a)                                                                                               
   x^3 + 2x + 2

Of course, addition is not the only arithmetic operator one might wish
to overload. A fully featured polynomial class will, at the very
minimum, need subtraction, multiplication (by a scalar or another
polynomial) and exponentiation by an integer power. The combination of
these, and particularly exponentiation, would allow the user to define
new polynomials in a particularly natural way, using Python's
intrinsic operators:

.. code-block:: ipython3

   In [1]: x = Polynomial((0, 1))
   In [2]: print(x)
   x
   In [3]: p = x**3 + 2*x + 2
   In [4]: p
   Polynomial((2, 2, 0, 1))

The :term:`special method` names for further arithmetic operators are
given :ref:`in the Python documentation <numeric-types>`. The
implementation of multiplication, exponentiation, and subtraction for
the :class:`Polynomial` class is left as an exercise.

Creating objects that act like functions
........................................

From a mathematical perspective, a real polynomial is a function. That is
to say, if:

.. math::

   f = x^2 + 2x + 1

then for any real :math:`x`, :math:`f(x)` is defined and is a real
number. We already know from the example of :func:`abs`, above, that
Python functions are objects. However our challenge is the converse of
this: we have :class:`Polynomial` objects which we would like to be
able to call like functions. The solution to our challenge is that
calling a function is an operation on an object similar to addition,
and Python provides another :term:`special method` name for
this. `f(x)` is mapped to `f.__call__(x)`, so any Python object with a
:meth:`~object.__call__` method behaves like a function, and any class
defining a :meth:`~object.__call__` method in effect defines a new type of
function.

Encapsulation
-------------

The property that objects have of bundling up data and methods in a
more-or-less opaque object with which other code can interact without
concerning itself with the internal details of the object is called
:term:`encapsulation`. Encapsulation is one of the core concepts in
object-oriented programming. In particular, encapsulation is key to
creating single objects representing high level mathematical
abstractions whose concrete realisation in code may require many
pieces of data and a large number of complex functions.
   
Glossary
--------

 .. glossary::
    :sorted:

    abstraction
        A mathematical concept with a limited set of defined
        properties. For the purposes of the abstraction, any other
        properties that an object may have are disregarded.

    attribute
        A value encapsulated in another object, such as a
        :term:`class`. Attributes are accessed using dot syntax, so if
        `b` is an attribute of `a` then its value is accessed using the
        syntax `a.b`. :term:`Methods <method>` are a special case of attributes.

    class
    type
        An abstraction defined by a set of possible values, and a set
        of operators valid for objects of that type. :keyword:`Class
        <class>` and :class:`type` are essentially synonymous, though
        the two words have different roles in Python code.

    concatenation
        The combination of two :ref:`sequences <typesseq>` by creating a new sequence containing
        all of the items in the first sequence, followed by all of the items in
        the second sequence. For example `(1, 2) + (3, 4)` is `(1, 2, 3, 4)`. 

    constructor
        The :meth:`~object.__init__` method of a :term:`class`. The constructor
        is passed the new object as its first argument (`self`) and is
        responsible for setting up the object. The constructor modifies
        `self` in place: constructors never return a value.

    data attribute
        An :term:`attribute` which is not a :term:`method`. As the name
        suggests, these are used to store data in an object.

    encapsulation
        The bundling up of attributes and methods into an object which
        can be dealt with as a single unit.

    infix operator
        A mathematical operator whose symbol is written between its :term:`operands`.
        Examples include addition, subtraction, division and multiplication. 

    instance
        An object of a particular class. `a` is an instance of
        :class:`MyClass` means that `a` has class `MyClass`. We will
        return to this concept when we learn about :ref:`inheritance <inheritance>`.

    instantiate
        To create an :term:`instance` of a :term:`class` by
        calling its :term:`constructor`.
       
    method
    instance method
        A function defined within a :term:`class`. If `a` is an
        instance of :class:`MyClass`, and :class:`MyClass` has a :meth:`foo` method then
        `a.foo()` is equivalent to `MyClass.foo(a)`. The first parameter
        of an instance method is always named `self`.

    operands
        The input values to an operator. For example the operands to `+` are the
        numbers being added (the summands), while the operands to exponentiation
        are the base and exponent.

    pseudocode
        A description of an algorithm given in the form of a computer
        program but without conforming to the rules of a particular
        programming language, and employing mathematical notation or
        plain text to express the algorithm in a human-readable form.

    special method
    magic method
        A method which has special meaning in the Python
        language. Special method names are used to define operations on
        a :term:`class` such as arithmetic operators, indexing, or the
        class :term:`constructor`. Special methods have names starting and ending
        with a double underscore (`__`). See :ref:`the Python documentation
        <specialnames>` for a technical description. Special methods
        are sometimes informally called "magic methods".

Exercises
---------

.. panels::
    :card: quiz shadow

    .. link-button:: https://bb.imperial.ac.uk/webapps/assessment/take/launchAssessment.jsp?course_id=_25965_1&content_id=_2054444_1
        :text: This week's quiz
        :classes: stretched-link 


Obtain the `skeleton code for these exercises from GitHub Classroom <https://classroom.github.com/a/mElLR0AD>`__. 
The skeleton code contains a :mod:`polynomial` package with a version of 
the :class:`Polynomial` class.

.. proof:exercise::

    Implement the following operations on the :class:`Polynomial` class. 

    1. Subtraction (:meth:`~object.__sub__` and :meth:`~object.__rsub__`).
    2. Multiplication by another polynomial, and by a scalar
       (:meth:`~object.__mul__` and :meth:`~object.__rmul__`).
    3. Exponentiation by a positive integer power (:meth:`~object.__pow__`). It
       may be useful to know that all integers are instances of
       :class:`numbers.Integral`.
    4. Polynomial evaluation at a scalar value (:meth:`~object.__call__`).

    .. note::

        Don't forget to commit and push your changes, and make sure that the
        tests pass on GitHub!

.. proof:exercise::

    Define a function `derivative` in :file:`polynomials.py` which takes a
    :class:`Polynomial` and returns a new :class:`Polynomial` which is its
    derivative. Also define a :meth:`dx` method on the :class:`Polynomial` class
    which returns the derivative of that :class:`Polynomial`. Rather than
    duplicating code, you should implement the function by calling the method.

.. proof:exercise::

    Inside the exercise repository for this week, create a new :mod:`shape`
    package containing a :mod:`circle` module. 
    
    1. Create a :class:`Circle` class
       whose :term:`constructor` takes two user parameters, `centre` and `radius`.
       `centre` should be a length 2 sequence containing the two-dimensional
       coordinates of the centre, while `radius` is the radius of the circle.
    2. Add an :ref:`import <modules>` statement to :file:`shape/__init__.py` so
       that the following code works:

       .. code-block:: python3

          from shape import Circle
    
    3. Implement the :meth:`~object.__contains__` :term:`special method` on the
       :class:`Circle` class so that it returns `True` if a point (represented
       by a length 2 sequence of coordinates) lies inside the circle. For
       example, the following code should print `True`.

       .. code-block:: python3

          from shape import Circle
          c = Circle((1., 0.), 2)
          print((0.5, 0.5) in c)

.. proof:exercise::

    Make the :mod:`circle` and :mod:`polynomial` packages installable. As with
    last week's exercise, pytest can't test this so you'll need to push to
    GitHub and check that the autograding tests pass there.

        