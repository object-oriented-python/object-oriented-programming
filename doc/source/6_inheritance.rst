.. _inheritance:

Inheritance and composition
===========================

A key feature of abstractions is composability: the ability to make a
complex object or operation out of several components. We can compose
objects by simply making one object a :term:`attribute` of another
object. This combines objects in a "has a" relationship. For example
the :class:`Polynomial` class introduced in :numref:`chapter %s
<objects>` has a :class:`tuple` of coefficients. Object composition of
this sort is a core part of :term:`encapsulation`.

Another way of composing abstractions is to make a new :term:`class`
by modifying another class. Typically this is employed to make a more
specialised :term:`class` from a more general one. In fact, we have
already seen this in the case of number classes. Recall that all
numbers are instances of :class:`numbers.Number`:

.. code-block:: ipython3

   In [1]: from numbers import Number

   In [2]: isinstance(1, Number)
   Out[2]: True

Hang on, though. `1` is actually an instance of :class:`int`:

.. code-block:: ipython3

   In [3]: type(1)
   Out[3]: int

   In [4]: isinstance(1, int)
   Out[4]: True

So `1`, it turns out, has :term:`type` :class:`int`, and so is an
instance of :class:`int`, but is also somehow an instance of
:class:`numbers.Number`. Mathematically, the answer is obvious:
integers form a subset of all of the numbers. Object inheritance works
in much the same way: we say that :class:`int` is a :term:`subclass`
of :class:`numbers.Number`. Just as :func:`isinstance` provides a
mechanism for determining whether an object is an :term:`instance` of
a :term:`class`, :func:`issubclass` will tell us when one
:term:`class` is a :term:`subclass` of another:

.. code-block:: ipython3

   In [5]: issubclass(int, Number)
   Out[5]: True

In fact, there is a whole hierarchy of
numeric types in :mod:`numbers`:

.. code-block:: ipython3

    In [6]: import numbers

    In [7]: issubclass(int, numbers.Integral)
    Out[7]: True

    In [8]: issubclass(numbers.Integral, numbers.Rational)
    Out[8]: True

    In [9]: issubclass(numbers.Rational, numbers.Real)
    Out[9]: True

    In [10]: issubclass(numbers.Real, numbers.Complex)
    Out[10]: True

It turns out that :func:`issubclass` is reflexive (classes are subclasses of themselves):

.. code-block:: ipython3

   In [11]: issubclass(numbers.Real, numbers.Real)
   Out[11]: True

This means that, in a manner analogous to subset inclusion, the
:term:`subclass` relationship forms a partial order on the set of all
classes.
    
A :term:`class`, by default, has all of the :term:`methods` and :term:`attributes` of the 
    
.. glossary::
    :sorted:

    subclass
       A :term:`class` derived from another :term:`class` by
       inheritance. The :term:`methods <method>` and
       :term:`attributes` of the :term:`parent class(es) <parent
       class>` are automatically available on the :term:`subclass`
       unless it overrides them.
