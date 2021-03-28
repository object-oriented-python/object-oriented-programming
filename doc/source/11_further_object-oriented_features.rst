Further object-oriented features
================================

This week we'll tie up a few loose ends by examining in detail some programming
concepts and Python features which we have encountered but not really studied
in the course so far. 

.. _decorators:

Decorators
----------

.. dropdown:: Video: decorators.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/526946976"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f1d61410-4200-42e5-92c4-acf2011de8ab>`__.


In :numref:`Week %s <trees>` we encountered the
:func:`functools.singledispatch` decorator, which turns a function into a
:term:`single dispatch function`. More generally, a decorator is a function
which takes in a function and returns another function. In other words, the
following:

.. code-block:: python3

    @dec
    def func(...):
        ...

is equivalent to:

.. code-block:: python3

    def func(...):
        ...
    func = dec(func)

Decorators are therefore merely :term:`syntactic sugar`, but can be very useful
in removing the need for boiler-plate code at the top of functions. For
example, your code for :numref:`Exercise %s <ex_expr>` probably contains a lot
of repeated code a lot like the following:

.. code-block:: python3

        def __add__(self, other):
            """Return the Expr for the sum of this Expr and another."""
            if isinstance(other, numbers.Number):
                other = Number(other)
            return Add(self, other)

We could define a decorator to clean up this code as follows:

.. _eg_decorator:

.. code-block:: python3
    :caption: A :term:`decorator` which casts the second argument of a method
              to an `expressions.Number` if that argument is a number. 
    :linenos:

    from functools import wraps

    def make_other_expr(meth):
        """Cast the second argument of a method to Number when needed."""
        @wraps(meth)
        def fn(self, other):
            if isinstance(other, numbers.Number):
                other = Number(other)
            return meth(self, other)
        return fn

Now, each time we write one of the special methods of :class:`Expr`, we can
instead write something like the following:

.. code-block:: python3

        @make_other_expr
        def __add__(self, other):
            """Return the Expr for the sum of this Expr and another."""
            return Add(self, other)

Let's look closely at what the decorator in :numref:`eg_decorator` does. The
decorator takes in one function, :func:`meth` an returns another one
:func:`fn`. Notice that we let :func:`fn` take the same arguments as
:func:`meth`. If you wanted to write a more generic decorator that worked on
functions with different signatures, then you could define function as
`fn(*args, **kwargs)` and pass these through to :func:`meth`.

The contents of :func:`fn` are what will be executed every time :func:`meth` is
called. So here we check the type of :data:`other` and cast it to
:class:`Number`, and then call the original :func:`meth` on the modified arguments.
We could also execute code that acts on the value that :func:`meth` returns. To
do this we would assign the result of :func:`meth` to a variable and then
include more code after line 9.

Finally, notice that we have wrapped `fn` in another decorator, this time
:func:`functools.wraps`. The purpose of this decorator is to copy the name and
docstring from :func:`meth` to :func:`fn`. The effect of this is that if the
user calls :func:`help` on a decorated function then they will see the name and
docstring for the original function, and not that of the decorator.

Decorators which take arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our :func:`make_other_expr` decorator doesn't have brackets after its name, and doesn't
take any arguments. However :func:`functools.wraps` does have brackets, and takes a
function name as an argument. How does this work? The answer is yet another
wrapper function. A decorator is a function which takes a function and
returns a function. :func:`functools.wraps` takes an argument (it happens to be
a function but other decorators take other types) and returns a decorator
function. That is, it is a function which takes in arguments and returns a
function which takes a function and returns a function. It's functions all the
way down!

The property decorator
~~~~~~~~~~~~~~~~~~~~~~

Back in :numref:`Week %s <objects>`, we gave the
:class:`~example_code.polynomial.Polynomial` class a
:meth:`~example_code.polynomial.Polynomial.degree()` method:

.. code-block:: python3

    def degree(self):
        return len(self.coefficients) - 1


This enables the following code to work:

.. code-block:: ipython3

    In [1]: from example_code.polynomial import Polynomial

    In [2]: p = Polynomial((1, 2, 4))

    In [3]: p.degree()
    Out[3]: 2

However, the empty brackets at the end of :func:`degree` are a bit clunky: why
should we have to provide empty brackets if there are no arguments to pass?
Indeed, this represents a failure of :term:`encapsulation`, because we
shouldn't know or care from the outside whether
meth:`~example_code.polynomial.Polynomial.degree()` is a :term:`method` or a
:term:`data attribute`. Indeed, the developer of the
:mod:`~example_code.polynomial` module should be able to change that
implementation without changing the interface. This is where the
built-in :class:`property` decorator comes in. :class:`property` transforms
methods that take no arguments other than the object itself into attributes.
So, if we had instead defined:

.. code-block:: python3

    @property
    def degree(self):
        return len(self.coefficients) - 1

Then `degree` would be accessible as an :term:`attribute`:

.. code-block:: ipython3

    In [1]: from example_code.polynomial import Polynomial

    In [2]: p = Polynomial((1, 2, 4))

    In [3]: p.degree
    Out[3]: 2


The :mod:`functools` module
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :mod:`functools` module is part of the :ref:`Python Standard Library
<library-index>`. It provides a collection of core :term:`higher order
functions <higher order function>`, some of which we have already met earlier
in the course. Since decorators are an important class of higher order
function, it is unsurprising that :mod:`functools` provides several very useful
ones. We will survey just a few here:

`functools.cache`
    Some functions can be very expensive to compute, and may be called
    repeatedly. A cache stores the results of previous function calls. If the
    function is called again with a combination of argument values that have
    previously been used, the function result is returned from the cache
    instead of the function being called again. This is a trade-off of
    execution time against memory usage, so one has to be careful how much
    memory will be consumed by the cache.
`functools.lru_cache`
    A least recently used cache is a limited size cache where the least
    recently accessed items will be discarded if the cache is full. This has
    the advantage that the memory usage is bounded, but the drawback that cache
    eviction may take time, and that more recomputation may occur than in an
    unbounded cache.
`functools.singledispatch`
    We met this in :numref:`Week %s <trees>`. This decorator transforms a
    function into a :term:`single dispatch function`.
 
.. _abstract_base_classes:

Abstract base classes
---------------------

.. dropdown:: Video: Abstract base classes.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/526947635"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f4678a69-731c-45fe-bdbf-acf2011de880>`__.

We have now on several occasions encountered classes which are not designed to
be instantiated themselves, but merely serve as parent classes to concrete
classes which are intended to be instantiated. Examples of these classes
include :class:`numbers.Number`, :class:`example_code.groups.Group`, and the
:class:`Expr`, :class:`Operator`, and :class:`Terminal` classes from
:numref:`Week %s <trees>`. These classes that are only ever parents are called
:term:`abstract base classes <abstract base class>`. They are abstract in the
sense that they define (some of the) properties of their children, but without
providing full implementations of them. They are base classes in the sense that
they are intended to be inherited from.

Abstract base classes typically fulfil two related roles, they provide
the definition of an interface that child classes can be assumed to follow, and
they provide a useful way of checking that an object of a concrete class has
particular properties.

The :mod:`abc` module
~~~~~~~~~~~~~~~~~~~~~

The concept of an abstract base class is itself an abstraction: an
abstract base class is simply a class which is designed not to be instantiated.
This requires no support from particular language features. Nonetheless, there
are features that a language can provide which makes the creation of useful
abstract base classes easy. In Python, these features are provided by the
:mod:`abc` module in the :ref:`Standard Library <library-index>`.

The :mod:`abc` module provides the :class:`~abc.ABC` class. This is itself an
abstract base class: there is no need to ever make an object of type
:class:`~abc.ABC`. Instead, classes inherit from :class:`~abc.ABC` in order to
access features that it provides.

Abstract methods
~~~~~~~~~~~~~~~~

Let's look back at the groups example from :numref:`Week %s <inheritance>`. We
defined the base :class:`~example_code.groups.Group` class and specified that
child classes had to implement the :meth:`_validate` and :meth:`operator`
methods as well as the :attr:`symbol` :term:`class attribute`. But how should
we actually know that these methods and attribute are required? This might be
documented, but that is somewhat hit and miss: it is often less than
completely obvious where to look for the documentation. Abstract methods
provide a much more satisfactory solution to this problem. The
:mod:`example_code.groups_abc` module is an update of the
:mod:`example_code.groups` module which uses the :class:`~abc.ABC` class. 

.. _groups_abc:

.. code-block:: python3
    :caption: An abstract base class version of the
              :class:`~example_code.groups_abc.Group` class. Note that the class itself
              inherits from :class:`~abc.ABC`, and the methods and attribute to be
              implemented by the :term:`child classes <child class>` have the
              `~abc.abstractmethod` decorator.
    :linenos:

    from abc import ABC, abstractmethod

    class Group(ABC):
        """A base class containing methods common to many groups.

        Each subclass represents a family of parametrised groups.

        Parameters
        ----------
        n: int
            The primary group parameter, such as order or degree. The
            precise meaning of n changes from subclass to subclass.
        """

        def __init__(self, n):
            self.n = n

        @property
        @abstractmethod
        def symbol(self):
            """Represent the group name as a character."""
            pass

        @abstractmethod
        def _validate(self, value):
            """Ensure that value is a legitimate element value in this group."""
            pass

        @abstractmethod
        def operation(self, a, b):
            """Return a ⊙ b using the group operation ⊙."""
            pass

        def __call__(self, value):
            """Create an element of this group."""
            return Element(self, value)

        def __str__(self):
            """Return a string in the form symbol then group parameter."""
            return f"{self.symbol}{self.n}"

        def __repr__(self):
            """Return the canonical string representation of the element."""
            return f"{type(self).__name__}({repr(self.n)})"

There are a few features of :numref:`groups_abc` which are noteworthy. First,
observe that :class:`~example_code.groups_abc.Group` now inherits from
:class:`~abc.ABC`. This simply enables the features that we will use next.
The new :class:`~example_code.groups_abc.Group` class has
:meth:`~example_code.groups_abc.Group._validate` and
:meth:`~example_code.groups_abc.Group.operator` methods, but these don't
actually do anything (their contents are merely :keyword:`pass`). They are,
however, decorated with `~abc.abstractmethod`. The effect of this decorator can
be observed if we try to instantiate :class:`~example_code.groups_abc.Group`:

.. code-block:: ipython3

    In [1]: from example_code.groups_abc import Group

    In [2]: Group(1)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-2-76d67216101e> in <module>
    ----> 1 Group(1)

    TypeError: Can't instantiate abstract class Group with abstract methods _validate, operation, symbol

The combination of inheriting from :class:`~abc.ABC` and the
`~abc.abstractmethod` decorator has the effect that instantiating this class is
an error, and we are told why. We have skipped over the `symbol` attribute.
There is no `abstractattribute` decorator, but the same effect can be achieved
by creating an `~abc.abstractmethod` and converting it into a data attribute using
`property`. In this case, the order of decorators is important:
`~abc.abstractmethod` always needs to be the last, innermost, decorator.

The subclasses of :class:`~example_code.groups_abc.Group` that we defined,
define all three of these attributes, so they can still be instantiated. For
example:

.. code-block:: ipython3

    In [1]: from example_code.groups_abc import CyclicGroup

    In [2]: C = CyclicGroup(3)

    In [3]: print(C(1) * C(2))
    0_C3

This illustrates the utility of this use of abstract base classes: the base
class can specify what subclasses need to implement. If a subclass does not
implement all the right attributes then a helpful error is generated, and
subclasses that do implement the class fully work as expected.

Duck typing
~~~~~~~~~~~

Before we turn to the second use of abstract base classes, it is useful to
divert our attention to what might be thought of as the type philosophy of
Python. Many programming languages are strongly typed. This means that in
situations such as passing arguments to functions, the type of each variable is
specified, and it is an error to pass a variable of the wrong type. This is not
the Python approach. Instead, Python functions typically do not check the types
of their arguments beyond ensuring that they have the basic properties required
of the operation in question. It doesn't really matter what the type of an
object is, so long as it has the operations, methods, and attributes required.

The term that is used for this approach to data types is :term:`duck typing`:
if a data type walks like a duck and quacks like a duck, then it might as well
be a duck. This does, however, beg the question of how a program should know if
an object has the right properties in a given circumstance. It is here that the
second use of abstract base classes comes into play.

Virtual subclasses
~~~~~~~~~~~~~~~~~~

.. dropdown:: Video: virtual subclasses.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/526947427"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4114bb1d-cc31-4cfc-81a6-acf2011de8d6>`__.

We learned in :numref:`Week %s <objects>` that we can determine if a type is a
number by checking if it is an instance of :class:`numbers.Number`. This is a
slightly different usage of abstract base classes. Rather than providing part
of the implementation of, say, :class:`float`, :class:`numbers.Number` provides
a categorisation of objects into numbers and non-numbers. This aids duck
typing, by enabling much more general type checking.

The :ref:`Standard Library <library-index>` contains many abstract base classes
whose role is to support duck typing by identifying objects with particular
properties. For example, the :mod:`collections.abc` module provides abstract
base classes for container objects with particular properties. The
:class:`collections.abc.Iterable` abstract base class groups all iterable
containers. For example:

.. code-block:: ipython3

    In [1]: from collections.abc import Iterable

    In [2]: from example_code.linked_list import Link

    In [3]: issubclass(Link, Iterable)
    Out[3]: True

Hang on, though, what magic is this? We didn't declare
:class:`~example_code.linked_list.Link` as inheriting from
:class:`~collections.abc.Iterable`. 

What is going on here is a form of reverse inheritance process. Rather than
:class:`~example_code.linked_list.Link` declaring that it inherits from
:class:`~collections.abc.Iterable`, :class:`~collections.abc.Iterable`
determines that :class:`~example_code.linked_list.Link` is its subclass. It's a sort
of adoption mechanism for classes. Of course the authors of the Standard
Library don't know that we will declare :class:`~example_code.linked_list.Link`, so
there is no code explicitly claiming :class:`~example_code.linked_list.Link` as a
subclass of :class:`~collections.abc.Iterable`. Instead, *any* class which
implements the :meth:`~object.__iter__` special method is a subclass of
:class:`~collections.abc.Iterable`. How does this work? Well,
:func:`isinstance` and :func:`issubclass` are implemented with the help of, you
guessed it, yet another :term:`special method`. This time the special method is
:meth:`~abc.ABCMeta.__subclasshook__`. 

.. _subclasshook:

.. code-block:: python3
    :caption: The source code for :class:`collections.abc.Iterable` extracted
              from the `Git repository for the standard Python language
              implementation <https://github.com/python/cpython/blob/master/Lib/_collections_abc.py>`__. 
    :linenos:

    from abc import ABCMeta, abstractmethod

    ...

    def _check_methods(C, *methods):
        mro = C.__mro__
        for method in methods:
            for B in mro:
                if method in B.__dict__:
                    if B.__dict__[method] is None:
                        return NotImplemented
                    break
            else:
                return NotImplemented
        return True

    ...

    class Iterable(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __iter__(self):
            while False:
                yield None

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Iterable:
                return _check_methods(C, "__iter__")
            return NotImplemented

        __class_getitem__ = classmethod(GenericAlias)

:numref:`subclasshook` shows the actual source code for
:class:`~collections.abc.Iterable` [#python_in_python]_. Let's walk through
this. The inheritance in line 19 is essentially equivalent to inheriting from
:class:`abc.ABC`. Similarly, lines 21 and 34 are unrelated technical code. At
line 24 we see the :meth:`object.__iter__` special method, decorated with
`~abc.abstractmethod`. This ensures that classes that do explicitly inherit
from :class:`~collections.abc.Iterable` have to implement
:meth:`object.__iter__`. 

The part that currently concerns us, though, is the
declaration of :meth:`~abc.ABCMeta.__subclasshook__` at line 29.
:meth:`~abc.ABCMeta.__subclasshook__` is declared as :term:`class method`. This
means that it will be passed the class itself as its first argument, in place
of the object. It is conventional to signal this difference by calling the
first parameter `cls` instead of `self`. The second parameter, `C` is the class
to be tested.

In common with the special methods for arithmetic,
:meth:`~abc.ABCMeta.__subclasshook__` returns :data:`NotImplemented` to
indicate cases that it cannot deal with. In this case, if the current class is
not :class:`~collections.abc.Iterable` (this would happen if the method were
called on a subclass of :class:`~collections.abc.Iterable`) then
:data:`NotImplemented` is returned. If we really are checking `C` against
:class:`~collections.abc.Iterable` then the `_check_methods` helper function is
called. The fine details of how this works are a little technical, but in
essence the function loops over `C` and its superclasses in order (`C.__mro__`
is the :term:`method resolution order`) and checks if the relevant methods are
defined. If they are all found then :data:`True` is returned, otherwise the
result is :data:`NotImplemented`. An implementation of
:meth:`~abc.ABCMeta.__subclasshook__` could also return :data:`False` to
indicate that `C` is definitely not a subclass.

Glossary
--------

.. glossary::
    :sorted:

    abstract base class
        A class designed only to be the :term:`parent <parent class>` of other
        classes, and never to be instantiated itself. Abstract classes often
        define the interfaces of :term:`methods <method>` but leave their implementations
        to the concrete :term:`child classes <child class>`.

    abstract method
        A method whose presence is required by an :term:`abstract base class`
        but for which concrete subclasses are required to provide the implementation.

    class method
        A :term:`method` which belongs to the class itself, rather than to the
        instances of the class. Class methods are declared using the
        `classmethod` :term:`decorator` and take the class (`cls`) as their first
        argument, instead of the instance (`self`). See also: :term:`class attribute`.

    decorator
        A syntax for applying :term:`higher order functions <higher order
        function>` when defining functions. A decorator is applied by writing
        `@` followed by the decorator name immediately before the declaration
        of the function or :term:`method` to which the decorator applies.

    duck typing
        The idea that the precise :term:`type` of an :term:`object` is not important, it is
        only important that the object has the correct :term:`methods <method>`
        or :term:`attributes <attribute>` for the current operation. If an
        object walks like a duck, and quacks like a duck then it can be taken
        to be a duck.

    higher order function
        A function which acts on other functions, and which possibly returns
        another function as its result.

    method resolution order
    MRO
        A sequence of the superclasses of the current class ordered by
        increasing ancestry. The MRO is searched in order to find
        implementations of :term:`methods <method>` and :term:`attributes
        <attribute>`. 

    syntactic sugar
        A feature of the programming language which adds no new functionality,
        but which enables a clearer or more concise syntax. Python
        :term:`special methods <special method>` are a form of syntactic sugar as they enable,
        for example, the syntax `a + b` instead of something like `a.add(b)`.

    virtual subclass
        A class which does not declare its descent from the superclass through
        its definition, but which is instead claimed as a subclass by the
        superclass.


Exercises
---------

Obtain the `skeleton code for these exercises from GitHub classroom
<https://classroom.github.com/a/qTArFlxP>`__. 

.. proof:exercise::

    The objective of this exercise is to write a :term:`decorator` which logs
    whenever the decorated function is called. This sort of decorator could be
    very useful in debugging code. Create the decorator in the
    `log_decorator.log_decorator` module and ensure it is importable as
    `log_decorator.log_call`. The decorator should be applicable to functions
    taking any combination of arguments.
    
    The logging itself should be accomplished using
    the built-in `logging` module by calling :func:`logging.info` and passing
    the log message.

    The log message should comprise the string `"Calling: "` followed by the
    function name (accessible using the `__name__` attribute), followed by
    round brackets containing first the :func:`repr` of the positional
    arguments, followed by the key=value pairs the keyword arguments.

.. proof:exercise::

    The :mod:`groups.groups` module in the skeleton code is the new version
    introduced above, using an :term:`abstract base class`. The
    `log_decorator.log_call` :term:`decorator` has been applied to the
    :meth:`Group._validate` :term:`abstract method`. However, even once you
    have implemented this decorator, it never gets called. Your challenge is to
    modify :mod:`groups.groups` so that the decorator is called every time a
    subclass :meth:`_validate` method is called, but **without** moving or
    duplicating `@log_call`.



Exam preparation
----------------

The exam will be similar in format to the :ref:`midterm test <midterm>`, so all
of the advice about preparing applies there too. As with all second year
elective modules, the exam will comprise four questions, each marked out of 20.

As with everything in this course, the one thing you can do to effectively
prepare for the exam is to program. You should complete any of the exercises in
the course that you have not yet done, and more exercises are given below.

Exam scope
~~~~~~~~~~

Everything we have covered in the course up to and including week 10 will be
fully examinable. The week 11 material is not examinable with the
following exceptions:

1. You may need to use :term:`abstract base classes <abstract base class>` from
   the standard library to check the type of variables. This is simply what you
   have been doing all term, for example using :class:`numbers.Number` to check
   that a value is numeric.
2. The skeleton code may include :term:`abstract base classes <abstract base
   class>` from which your classes may need to inherit. This is actually a help
   to you in the exam, because the :term:`abstract methods <abstract method>`
   will provide information about what you need to implement, and a helpful
   error message if you haven't done so.

Support while revising
~~~~~~~~~~~~~~~~~~~~~~

The module Piazza forum will remain open throughout the revision period and we
will be very happy to respond to your questions. There will also be a live
revision session during week 1 of summer term in the module team. This will be
an opportunity to ask individual questions just like in the labs. If enough
people attend then I will also run a group Q & A session.

Practice questions
~~~~~~~~~~~~~~~~~~

Some specifically-designed practice questions are presented below. In addition to this, there are a lot of very good exercises in
chapters 7 and 9 of `Hans Petter Langtangen, A Primer on Scientific Programming
with Python <https://link.springer.com/book/10.1007%2F978-3-662-49887-3>`__.
You can access that book by logging in with your Imperial credentials.

The first two questions are in exam format. 

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/HdgipMxw>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    .. note::

        This exercise is fully set up as an exam question, including provisional
        points on the autotests. It should be doable in 30 minutes, though the
        level of programming is a little more basic than the exam questions.

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/6usAsES4>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    .. note::

        This exercise is at the level of an exam question, though longer. An
        actual exam question would be pruned back to be achievable in 30
        minutes. Here the complete exercise is presented because the main thing
        you need to do is practice programming, and cutting out material
        doesn't help with that. Marks are not given as the question is the
        wrong length, so dividing 20 marks over the question would just be
        misleading

In addition to these exam-style questions, you can also usefully practice
programming by going beyond the specification of the exercises in the course.
The following exercises are just ideas for how to do that. They do not come
with additional code or tests.

.. proof:exercise::

    Extend the :class:`Polynomial` class from :numref:`Week %s <objects>` to
    support polynomial division. Polynomial division results in a quotient and
    a remainder, so you might choose to implement :meth:`~object.__floordiv__`
    to return the quotient and :meth:`~object.__mod__` to return the remainder,
    in a manner analogous to integer division. You might also implement
    :meth:`~object.__truediv__` and have it return the quotient if the
    polynomial division is exact, but raise :class:`ValueError` if there is a
    remainder.

    .. hint::

        Don't forget that repeating code is poor style, so you might need a
        helper method to implement the actual polynomial division.
    
.. proof:exercise::

    Extend the :class:`Deque` class from :numref:`Week %s
    <abstract_data_types>` to automatically resize the ring buffer by a
    proportion of its length when it is full, and when it becomes too empty.
    You can check the behaviour of your implementation against
    :class:`collections.deque`.

.. proof:exercise::

    For a real challenge, extend the groups implementation from :numref:`Week
    %s <inheritance>` to support taking the quotient of two groups. What do the
    values and validation of a quotient group look like in code? You could
    implement :meth:`~object.__truediv__` on :class:`Group` to provide the user
    interface.

.. proof:exercise::

    Write additional single dispatch visitor functions to extend the
    capabilities of the symbolic algebra system you wrote in :numref:`Week %s
    <trees>`. You could, for example, write a visitor which performs
    cancellation of expressions involving 1 or 0. You could implement expansion
    of brackets according to distributive laws. Finally you could canonicalise
    commutative operators such as `+` and `*` so that, for example `1 + x` is
    mapped to `x + 1`. Doing this over multiple layers of the tree
    (for example, transforming `1 + 2*x + 3*x**2` to `3*x**2 + 2*x + 1`) is an additional
    challenge.


.. rubric:: Footnotes

.. [#python_in_python] Most of the :ref:`Python Standard Library <library-index>` is written
    in Python, so diving in and reading the source code is often an option if
    you really want to know how some part of the language works.