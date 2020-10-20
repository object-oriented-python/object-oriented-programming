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

Cyclic groups
~~~~~~~~~~~~~

Let's start with the cyclic groups of order :math:`n`. These are isomorphic to
the integers under addition modulo :math:`n`, a property which we can use to
create our implementation. We're going to eventually want to make different
types of groups, so we're going to need to carefully consider what changes from
group to group, and what is the same. The first thing that we observe is that
different cyclic groups differ only by their order, so we could quite easily
have a single cyclic group class, and set the order when we :term:`instantiate`
it. This is pretty common: groups often come in families defined by some sort of
size parameter. A group is defined by what values its elements can take, and the
group operation. We might therefore be tempted to think that we need to define a
cyclic group element type which can take the relevant values and which
implements the group operation. This would be unfortunate for at least two
reasons:

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
the concrete effects of the classes:

.. code-block:: ipython3

    In [1]: from example_code.groups_basic import CyclicGroup

    In [2]: C = CyclicGroup(5)

    In [3]: print(C(3) * C(4))
    2_C5

We observe that we are able to create the cyclic group of order 5. Due to the
definition of the :meth:`__call__` :term:`special method` at line 35, we are
then able to create elements of the group by calling the group object. The group
operation then has the expected effect:

.. math::

    3_{C_5} \cdot 4_{C_5} &\equiv (3 + 4) \operatorname{mod} 5\\
    &= 2\\ 
    &\equiv 2_{C_5}

Finally, if we attempt to make a group element with a value which is not an
integer between 0 and 5, an exception is raised.

.. code-block:: ipython3

    In [4]: C(1.5)
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-4-a5d8472d4486> in <module>
    ----> 1 C(1.5)

    ~/docs/principles_of_programming/object-oriented-programming/example_code/groups_basic.py in __call__(self, value)
        38     def __call__(self, value):
        39         '''Provide a convenient way to create elements of this group.'''
    ---> 40         return Element(self, value)
        41 
        42     def __str__(self):

    ~/docs/principles_of_programming/object-oriented-programming/example_code/groups_basic.py in __init__(self, group, value)
        4 class Element:
        5     def __init__(self, group, value):
    ----> 6         group._validate(value)
        7         self.group = group
        8         self.value = value

    ~/docs/principles_of_programming/object-oriented-programming/example_code/groups_basic.py in _validate(self, value)
        30         '''Ensure that value is a legitimate element value in this group.'''
        31         if not (isinstance(value, Integral) and 0 <= value < self.order):
    ---> 32             raise ValueError("Element value must be an integer"
        33                              f" in the range [0, {self.order})")
        34 

    ValueError: Element value must be an integer in the range [0, 5)

:numref:`cyclic_group` illustrates :term:`composition`: on line 4
:class:`~example_code.groups_basic.Element`, is associated with a group object.
This is a classic *has a* relationship: an element has a group. We might have
attempted to construct this the other way around with classes having elements,
however this would have immediately hit the issue that elements have exactly one
group, while a group might have an unlimited number of elements. Object
composition is typically most successful when the relationship is uniquely
defined.

This code also demonstrates :term:`delegation`. In order to avoid having to
define different element classes for different groups, the element class does
not in substance implement either value validation, or the group operation.
Instead, at line 3, validation is delegated to the group by calling
:meth:`group._validate` and at line 10 the implementation of the group operation
is delegated to the group by calling :meth:`self.group.operation`.

General linear groups
~~~~~~~~~~~~~~~~~~~~~

We still haven't encountered inheritance, though. Where does that come into the
story? Well first we'll need to introduce at least one more family of groups.
For no other reason than convenience, let's choose :math:`G_n`, the general
linear group of degree :math:`n`. The elements of this group can be
represented as :math:`n\times n` invertible square matrices. At least to the
extent that real numbers can be represented on a computer, we can implement this
group as follows:

.. code-block:: python3
    :caption: A basic implementation of the general linear group of a given
              degree.
    :name: general_linear_group
    :linenos:

    class GeneralLinearGroup:
        '''The general linear group represented by degree x degree matrices.'''
        def __init__(self, degree):
            self.degree = degree

        def _validate(self, value):
            '''Ensure that value is a legitimate element value in this group.'''
            value = np.asarray(value)
            if not (value.shape == (self.degree, self.degree)):
                raise ValueError("Element value must be a "
                                 f"{self.degree} x {self.degree}"
                                 "square array.")

        def operation(self, a, b):
            return a @ b

        def __call__(self, value):
            '''Provide a convenient way to create elements of this group.'''
            return Element(self, value)

        def __str__(self):
            return f"G{self.degree}"

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.degree)})"

We won't illustrate the operation of this class, though the reader is welcome to
:keyword:`import` the :mod:`example_code.groups_basic` module and experiment.
Instead, we simply note that this code is very, very similar to the
implementation of :class:`~example_code.groups_basic.CyclicGroup` in
:numref:`cyclic_group`. The only functionally important differences are the
definitions of the :meth:`_validate` and :meth:`operation` methods.
`self.order` is also renamed as `self.degree`, and `C` is replaced by `G` in the
string representation. It remains the case that there is a large amount of
code repetition between classes. For the reasons we touched on in
:numref:`repetition`, this is a highly undesirable state of affairs.

Inheritance
-----------

Suppose, instead of copying much of the same code, we had a prototype
:class:`Group` class, and :class:`CyclicGroup` and :class:`GeneralLinearGroup`
simply specified the ways in which they differ from the prototype. This would
avoid the issues associated with repeating code, and would make it obvious how
the different group implementations differ. This is exactly what inheritance
does. 

.. code-block:: python3
    :caption: Implementation of a base class for a generic group, and subclasses
        for the cyclic groups and general linear groups.
    :name: groups_inheritance
    :linenos:

    class Group:
        '''A base class containing methods common to many groups.

        Each subclass represents a family of parametrised groups.'''
        def __init__(self, n):
            '''Args:
                n: The primary group parameter, such as order or degree. The
                precise meaning of n changes from subclass to subclass.
            '''
            self.n = n

        def __call__(self, value):
            '''Provide a convenient way to create elements of this group.'''
            return Element(self, value)

        def __str__(self):
            return f"{self.notation}{self.n}"

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.n)})"


    class CyclicGroup(Group):
        '''A cyclic group represented by integer addition modulo n.'''
        notation = "C"

        def _validate(self, value):
            '''Ensure that value is a legitimate element value in this group.'''
            if not (isinstance(value, Integral) and 0 <= value < self.n):
                raise ValueError("Element value must be an integer"
                                f" in the range [0, {self.n})")

        def operation(self, a, b):
            return (a + b) % self.n


    class GeneralLinearGroup(Group):
        '''The general linear group represented by n x n matrices.'''
        notation = "G"

        def _validate(self, value):
            '''Ensure that value is a legitimate element value in this group.'''
            value = np.asarray(value)
            if not (value.shape == (self.n, self.n)):
                raise ValueError("Element value must be a "
                                f"{self.n} x {self.n} square array.")

        def operation(self, a, b):
            return a @ b

:numref:`groups_inheritance` shows a new implementation of
:class:`~example_code.groups.CyclicGroup` and
:class:`~example_code.groups.GeneralLinearGroup`. These are functionally
equivalent to those presented in :numref:`cyclic_group` and
:numref:`general_linear_group` but have all the repeated code removed. The code
common to both families of groups is instead placed in the
:class:`~example_code.groups.Group` class. In the following sections we will
highlight the features of this code which make this work.

Inheritance syntax
~~~~~~~~~~~~~~~~~~

Look again at the definition of :class:`~example_code.groups.CyclicGroup` on
line 23:

.. code-block:: python3
    :lineno-start: 23

    class CyclicGroup(Group):    

This differs from the previous class definitions we've seen in that the
name of the class we're defining, :class:`CyclicGroup` is followed by another
class name in brackets, :class:`Group`. This :term:`syntax` is how inheritance
is defined. It means that :class:`CyclicGroup` is a :term:`child class` of
:class:`Group`. The effect of this is that any :term:`attribute` defined on the
:term:`parent class` is also defined (is *inherited*) on the child class. In
this case, :class:`CyclicGroup` does not define :meth:`__init__`,
:meth:`__call__`, :meth:`__str__` or :meth:`__repr__`. If and when any of those
:term:`methods <method>` are called, it is the methods from the parent class,
:class:`Group` which are used. This is the mechanism that enables methods to be
shared by different classes. In this case,
:class:`~example_code.groups.CyclicGroup` and
:class:`~example_code.groups.GeneralLinearGroup` share these methods. A user
could also define another class which inherited from
:class:`~example_code.groups.Group`, for example to implement another family of
groups.

Class attributes
~~~~~~~~~~~~~~~~

At line 25 of :numref:`groups_inheritance`, the name `notation` is
assigned to:

.. code-block:: python3
    :lineno-start: 25

    notation = "C"

This is also different from our previous experience: usually if we
want to set a value on an object then we do so from inside a method, and we set
a :term:`data attribute` on the current instance, `self`, using the syntax:

.. code-block:: python3

    self.notation = "C"

This more familiar code sets an instance attribute. In other words, an attribute
specific to each object of the class. Our new version of the code instead sets a
single attribute that is common to all objects of this class. This is called a
:term:`class attribute`.

.. note::

    Come back and explain class attributes in more detail.

.. _runtime_attributes:

Attributes resolve at runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the :meth:`__str__` method: 

.. code-block:: python3
    :lineno-start: 16

    def __str__(self):
        return f"{self.notation}{self.n}"

This code uses `self.notation`, but this attribute isn't defined anywhere on
:class:`~example_code.groups.Group`. Why doesn't this cause an
:class:`AttributeError` to be raised? One answer is that it indeed would if we
were to instantiate :class:`Group` itself:

.. code-block:: ipython3

    In [1]: from example_code.groups import Group

    In [2]: g = Group(1)

    In [3]: print(g)
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-3-e1cdc681402c> in <module>
    ----> 1 print(g)

    ~/docs/principles_of_programming/object-oriented-programming/example_code/groups.py in __str__(self)
        39 
        40     def __str__(self):
    ---> 41         return f"{self.notation}{self.n}"
        42 
        43     def __repr__(self):

    AttributeError: 'Group' object has no attribute 'notation'

In fact, :class:`Group` is never supposed to be instantiated, it plays the role
of an :term:`abstract base class`. In other words, it's role is to provide
functionality to classes that inherit from it, rather than to be the type of
objects itself. We will return to this in more detail in
:numref:`abstract_base_classes`.

However, if we instead instantiate :class:`~example_code.groups.CyclicGroup`
then everything works:

.. code-block:: ipython3

    In [1]: from example_code.groups import CyclicGroup

    In [2]: g = CyclicGroup(1)

    In [3]: print(g)
    C1

The reason is that the code in methods is only executed when that method is
called, and the object `self` is the actual concrete class instance, with all of
the attributes that are defined for it. In this case, even though
:meth:`__str__` is defined on :class:`Group`, `self` has type
:class:`CyclicGroup`, and therefore `self.notation` is well-defined and has the
value `"C"`. 

.. note::

    need a good example for overriding methods and calling the superclass method.

.. _abstract_base_classes:

Abstract base classes
---------------------

We observed in :numref:`runtime_attributes` that the
:class:`~example_code.groups.Group` class isn't itself a complete implementation
of a mathematical group. Instead it is only intended to be used as a
:term:`parent class` for classes implementing actual groups. Those child classes
are responsible for filling out the additional details required to make a
working implementation. In the case of `Group`, the child classes have to
implement :attr:`notation`, :meth:`_validation`, and :meth:`operation`, with the
right interfaces. 

How would a programmer who wants to implement a new family of groups know to
implement this one attribute and two methods, with these particular interfaces?
In a simple case like this, they could probably infer what was needed by
studying the source code of :class:`Group` and its two subclasses. However "just
work it out from context" is not a particularly robust mechanism and will
quickly become infeasible for larger, more complex classes. 

Instead of leaving it to the programmer to figure out, it would be preferable if
:class:`Group` specified the missing parts to be filled out, including the
required interfaces. We call such
classes :term:`abstract base classes <abstract base class>`. They are abstract
in the sense that the interface is specified but the implementation omitted. 



.. note:: 

    Quiz exercise giving a bunch complicated inheritance pattern and asking what
    various things print.

.. note:: 

    One exercise will be to implement another family of groups by importing and
    inheriting from :class:`~example_code.groups.Group`.

Glossary
--------

.. glossary::
    :sorted:

    child class
        A class which :term:`inherits <inheritance>` directly from one or more
        :term:`parent classes <parent class>`. The child class automatically has
        all of the :term:`methods <method>` of the parent classes, unless it
        declares its own methods with the same names.

    class attribute
        An :term:`attribute` which is declared directly on a :term:`class`.
        All instances of a class see the same value of a class attribute.

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
        A class from which another class, referred to as a :term:`child class`,
        inherits.

    subclass
        A class `A` is a subclass of the class `B` if `A` inherits from `B` either
        directly or indirectly. That is, if `B` is a :term:`parent <parent class>`, 
        grandparent, great grandparent or further ancestor of `A`.

