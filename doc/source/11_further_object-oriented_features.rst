Further object-oriented features
================================

This week we'll tie up a few loose ends by examining in detail some programming
concepts and Python features which we have encountered but not really studied
in the course so far. 

Decorators
----------

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

Our :func:`make_at_expr` decorator doesn't have brackets after its name, and doesn't
take any arguments. However :func:`functools.wrap` does have brackets, and takes a
function name as an argument. How does this work? The answer is yet another
wrapper function. A decorator is a function which takes a function and
returns a function. :func:`functools.wrap` takes an argument (it happens to be
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


Duck typing
~~~~~~~~~~~

Glossary
--------

.. glossary::
    :sorted:

    abstract base class
        A class designed only to be the :term:`parent <parent class>` of other
        classes, and never to be instantiated itself. Abstract classes often
        define the interfaces of :term:`methods <method>` but leave their implementations
        to the concrete :term:`child classes <child class>`.

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

    syntactic sugar
        A feature of the programming language which adds no new functionality,
        but which enables a clearer or more concise syntax. Python
        :term:`special methods <special method>` are a form of syntactic sugar as they enable,
        for example, the syntax `a + b` instead of something like `a.add(b)`.


Exam preparation
----------------