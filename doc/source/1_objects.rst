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
is a builtin function, so its defining operation is that it can be
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
   of `foo`" is the same as saying "what is the type of `foo`". However
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

    def __init__(self, coefs):

        self.coefficients = coefs

Executing this code in a Python interpreter would enable us to create
a simple polynomial, and inspect its coefficients:

.. code-block:: ipython3

   In [7]: f = Polynomial((0, 1, 2))
   In [8]: f.coefficients
   Out[8]: (0, 1, 2)

The three lines of Python defining the :class:`Polynomial` class contain
several important concepts and Python details that it is important to
understand.

The :doc:`class definition <class>` statement opens a new block, so
just like a :doc:`function definition <function>`, it starts with
the keyword, followed by the name of the class we are defining, and
ends with a colon. User-defined classes in Python (i.e. classes not
built in to the language) usually have CapWords names. This means
that all the words in the name a run together without spaces. For
example, if we decided to make a separate class for complex-valued
polynomials, we might call it :class:`ComplexPolynomial`.

Inside the class definition, i.e. indented inside the block, is a
function called :meth:`__init__`. Functions defined inside a class
definition are called :term:`methods<method>`. The :meth:`__init__` method has a
rather distinctive form of name, starting and ending with two
underscores. Names of this format are used in the Python language for
objects which have special meaning in the Python language. The
:meth:`__init__` method of a class has special meaning in Python as
the :term:`constructor` of a class. When we write:

.. code-block:: ipython3

   In [7]: f = Polynomial((0, 1, 2))

This is called :term:`instantiating` an object of type
:class:`Polynomial`. The following steps occur:

1. Python creates an object of type :class:`Polynomial`.
2. The :class:`__init__` :term:`special method` of :class:`Polynomial`
   is called. The new :class:`Polynomial` object is passed as the
   first parameter (`self`), and the :class:`tuple` `(0, 1, 2)` is passed
   as second parameter (`coefs`).
3. The name `f` in the surrounding scope is associated with the
   :class:`Polynomial`.

         

Attributes
..........

Let's now look at what happened inside the :meth:`__init__` method. We
have just one line::

  self.coefficients = coefs

Remember that `self` is the object we are setting up, and coefs is the
other parameter to :meth:`__init__`. This line of code creates a new
name inside this :class:`Polynomial` object, called
`coefficients`, and associates this new name with the object passed as
the argument to the :class:`Polynomial` constructor. Names such as
this are called :term:`attributes<attribute>`. We create an attribute
just by assigning to it, and we can then read back the attribute using
the same syntax, which is what we did here:

.. code-block:: ipython3

   In [8]: f.coefficients
   Out[8]: (0, 1, 2)


Methods
.......

We have already met the :term:`special method` :class:`__init__`,
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
block at the same level as the :meth:`__init__` method. Observe also
that it too takes `self` as its first parameter. A key difference from
the :meth:`__init__` method is that :meth:`degree` now returns a
value, as most functions do. We can now use our new method to recover
the degree of our Polynomial.

.. code-block:: ipython3

   In [1]: f = Polynomial((0, 1, 2))
   In [2]: f.degree()
   Out[2]: 2

.. note::

   The object itself is always passed as the first argument to a
   :term:`method`. Technically, it is possible to name the first
   parameter any legal Python name, but there is a **very** strong
   convention that the first parameter to any method of a class
   instance is called `self`. **Never, ever** name this parameter
   anything other than `self`, or you will confuse every Python
   programmer who reads your code!

String representations of objects
.................................

Remember that a key reason for defining new classes is to enable users
to reason about the resulting objects at a higher mathematical level. An
important aid to the user in doing this is to be able to look at the
object. What happens if we print a :class:`Polynomial`?

.. code-block:: ipython3

   In [1]: f = Polynomial((0, 1, 2))
   In [2]: print(f)
   <Polynomial object at 0x104960dd0>

This is less than useful. By default, Python just prints the class of
the object, and the memory address at which this particular object is
stored. This is, however, not so surprising if we think about the
situation in a little more depth. How was Python supposed to know what
sort of string representation makes sense for this object? We will
have to tell it.

The way we do so is using another :term:`special method`. The special
method for the primary string representation of an object is
:meth:`__str__`. It takes no arguments other than the object itself,
and we could define it thus::

    def __str__(self):

        coefs = self.coefficients
        terms = []

        # It is conventional to omit factors of 1.
        str1 = lambda n: '' if n == 1 else str(n)
        
        # Process the higher degree terms in reverse order.
        for d in range(self.degree(), 1, -1):
            if coefs[d]:
                terms.append(str1(coefs[d]) + "x^" + str(d))
        # Degree 1 and 0 terms conventionally have different representation.
        if self.degree() > 0 and coefs[1]:
            terms.append(str1(coefs[1]) + "x")
        if coefs[0]:
            terms.append(str(coefs[0]))

        return " + ".join(terms) or "0"

This slightly longer piece of code results from the fact that the
linear and constant terms in a polynomial are usually represented
slightly differently from the higher order terms. Having added this
new method to our class, we can now observe the result:
      
.. code-block:: ipython3

      In [2]: f = Polynomial((1, 2, 0, 1, 5))
      In [3]: print(f)
      5x^4 + x^3 + 2x + 1
   
In fact, Python provides not one, but two :term:`special
methods<special method>` which convert an object to a
string. :meth:`__str__` is called by :func:`print` and also by
:func:`str`. Its role is to provide the string representation which
is best understood by humans. In mathematical code, this will usually
be the mathematical notation for the object. In contrast, the
:meth:`__repr__` method  is called by :func:`repr` and also provides
the default string representation printed out by the Python command
line. By convention, :meth:`__repr__` should return a string which a
user might type in order to recreate the object. For example::

  def __repr__(self):
  
      return "Polynomial(" + repr(self.coefficients) + ")"

Notice that in order to help ensure consistency of representations we
call :func:`repr` on the coefficients in this case, whereas in the
:meth:`__str__` method we called :func:`str`.

We can now observe the difference in the result:

.. code-block:: ipython3

   In [2]: f = Polynomial((1, 2, 0, 4, 5))                                                                                
   In [3]: f                                                                                                          
   Out[3]: Polynomial((1, 2, 0, 4, 5))


Defining arithmetic options on objects
......................................

It's all very well to be able to print out our polynomial objects, but
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

Of course once again this is not so surprising since we haven't
defined what addition of polynomials should mean. The :term:`special
method` which defines addition is :meth:`__add__`. It takes the
object itself and  another object, and returns their sum. That is,
when you write `a + b` in Python, then what actually happens is
`a.__add__(b)`. 

Before we define our addition method, we first need to consider what
other objects it might make sense to add to a polynomial. Obviously we
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
object is an instance of a class. The other is the class :class:`Number`,
which we import from the :mod:`numbers` module. All Python numbers are
instances of :class:`Number` so this provides a mechanism for checking
whether the other operand is a number. We will consider
:func:`isinstance` and :class:`Number` in more detail when we look at
inheritance and abstract base classes.

Putting all this together, we can define polynomial addition::

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

Naturally, Python's inbuilt :type:`int` type knows nothing about our
new :class:`Polynomial` class, so when we ask it to do the addition,
it returns :obj:`NotImplemented`. We could, however, tell
:class:`Polynomial` how to be added to an :type:`int`, and Python
provides a mechanism for this. If the :meth:`__add__` of the left hand
operand of `+` returns :obj:`NotImplemented`, then Python tries the
reverse addition method, called :meth:`__radd__`, on the right hand
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



   
Glossary
--------

 .. glossary::
    :sorted:

    attribute
       A value encapsulated in another object, such as a
       :term:`class`. Attributes are accessed using dot syntax, so if
       `b` is an attribute of `a` then its value is accessed using the
       syntax `a.b`.

    instance
       An object of a particular class. `a` is an instance of
       :class:`MyClass` means that `a` has class `MyClass`. We will
       return to this concept when we learn about inheritance.

    constructor
       The :meth:`__init__` method of a :term:`class`. The constructor
       is passed the new object as its first argument (`self`) and is
       responsible for setting up the object. The constructor modifies
       `self` in place: constructors never return a value.

    method
       A function defined within a :keyword:`class`. If `a` is an
       instance of :class:`MyClass`, and :class:`MyClass` has a :meth:`foo` method then
       `a.foo()` is equivalent to `MyClass.foo(a)`. The first parameter
       of a method is always named `self`.

    special method
    magic method
       A method which has special meaning in the Python
       language. Special method names are used to define operations on
       a :term:`class` such as arithmetic operators, indexing, or the
       class :term:`constructor`. See :doc:`the Python documentation
       <specialnames>` for a technical description. Special methods
       are sometimes informally called "magic methods".
