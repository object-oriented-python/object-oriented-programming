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
classes. This relationship defines another core mechanism for creating a new
class from existing classes, :term:`inheritance`. If one class is a subclass of
another then we say that it inherits from that class. Where composition defines
a *has a* relationship, inheritance defines an *is a* relationship.

An example from group theory
----------------------------

In order to illustrate how composition and inheritance work, let's suppose that
we want to write a module that implements some basic groups. Recall that a group
is a collection of elements, and a group operation which obeys certain axioms.
A computer implementation of a group might therefore involve objects
representing groups, and objects representing elements. We'll lay out one
possible configuration, which helpfully involves both inheritance and
composition, as well as parametrisation of objects and delegation of methods.

Basic design considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's start with the cyclic groups of order :math:`n`. These are isomorphic to
the integers modulo :math:`n`, a property which we can use to create our
implementation. We're going to eventually want to make different types of
groups, so we're going to need to carefully consider what changes from group to
group, and what is the same. The first thing that we observe is that different
cyclic groups differ only by their order, so we could quite easily have a single
cyclic group class, and set the order when we :term:`instantiate` it. This is
pretty common: groups often come in families defined by some sort of size
parameter. A group is defined by what values its elements can take, and the
group operation. We might therefore be tempted to think that we need to define a
cyclic group element type which can take the relevant values and which
implements the group operation. This would be
unfortunate for at least two reasons:

1. Because each group needs several elements, need a different element *type*
   for each *instance* of a cyclic group. The number of classes needed would grow very fast!
2. Adding a new family of groups would require adding both a group class and a
   set of element classes. On grounds of simplicity and robustness, always key considerations,
   we would much prefer to only add one class in order to add a new family of
   groups.
   
Instead, we can make a single generic element type, and pass the group as an
:term:`argument` when instantiating the element. This is an example of
:term:`composition`: each element *has a* group. The group will then implement
methods which check that element values are allowed for that group, and a method
which implements the group operation. Element objects will then :term:`delegate
<delegation>` validation and the group operation back to the group object. 

Finally, we will want an :term:`infix operator` representing the group
operation. Group theorists often use a dot, but we need to choose one of the
infix operators that Python supports. We'll chose `*`, which is possibly the
closest match among Python's operators. One could easily envisage a more
complete implementation of a group, with support for group properties such as
generators and element features such as inverses. But our objective here is to
develop an understanding of object relations, rather than of algebra, so this
minimal characterisation of a group will suffice. 

.. code-block:: python3
    :caption: A simple implementation of a cyclic group class, and a generic
              group element.
    :name: cyclic_group
    :linenos:

    class Element:
        def __init__(self, group, value):
            group._validate(value)
            self.group = group
            self.value = value

        def __mul__(self, other):
            '''Use * to represent the group operation.'''
            return Element(self.group,
                        self.group.operation(self.value,
                                                other.value))

        def __str__(self):
            return f"{self.value}_{self.group}"

        def __repr__(self):
            return f"{self.__class__.__name__}" \
                f"({repr(self.group), repr(self.value)})"


    class CyclicGroup:
        '''A cyclic group represented by integer addition modulo group order.'''
        def __init__(self, order):
            self.order = order

        def _validate(self, value):
            '''Ensure that value is a legitimate element value in this group.'''
            if not (isinstance(value, Integral) and 0 <= value < self.size):
                raise ValueError("Element value must be an integer"
                                f" in the range [0, {self.size})")

        def operation(self, a, b):
            return (a + b) % self.order

        def __call__(self, value):
            '''Provide a convenient way to create elements of this group.'''
            return Element(self, value)

        def __str__(self):
            return f"C{self.order}"

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.order)})"


:numref:`cyclic_group` shows an implementation of our minimal conception of
cyclic groups. Before considering it in any detail let's try it out to observe
the concrete effects of the classes. 

Glossary
--------

.. glossary::
   :sorted:

   child class
      A class which :term:`inherits <inheritance>` directly from one or more
      :term:`parent classes <parent class>`. The child class automatically has
      all of the :term:`methods <method>` of the parent classes, unless it
      declares its own methods with the same names. 

   composition
      The process of making a more complex object from other objects by
      including the constituent objects as attributes of the more composite
      object. Composition can be characterised by a *has a* relationship, in
      contrast to :term:`inheritance`, which embodies an *is a* relationship.

   delegation
      A design pattern in which an object avoids implementing a
      :term:`method` by instead calling a method on another object. 

   inheritance
      The process of making a new class by extending one or more existing
      classes. 

   parent class
      A class from which another class, referred to as a :term:`child class`
      inherits.

   subclass
      A class `A` is a subclass of the class `B` if `A` inherits from `B` either
      directly or indirectly. That is, if `B` is a :term:`parent <parent
      class>`, grandparent, great grandparent or further ancestor of `A`.

   subclass
      A :term:`class` derived from another :term:`class` by
      inheritance. The :term:`methods <method>` and
      :term:`attributes` of the :term:`parent class(es) <parent
      class>` are automatically available on the :term:`subclass`
      unless it overrides them.
