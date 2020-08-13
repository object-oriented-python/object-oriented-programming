

Abstract data types
===================

In :numref:`objects`, we introduced the concept of :term:`type` as an
:term:`abstraction` comprising a set of possible values, and a set of
operations. All types in Python are abstractions in this sense,
because we deal with them in terms of their defined properties rather
than their actual implementation. However, it can also be useful to
define purely mathematical types, distinct from their concrete
realisation in code. Indeed, there are typically multiple possible
concrete realisations of a mathematical idea.

.. proof:definition:: Abstract Data Type

   An *abstract data type* is a purely mathematical :term:`type`,
   defined independently of its concrete realisation as code.


Stacks
------

Possibly the simplest abstract data type which is not synonymous with
a Python type is the :term:`stack`. A stack is a sequence of objects
in which only the most recently added object is accessible. The image
to have in mind is a stack of plates on a spring-loaded holder of the
type found in many university or workplace canteens. Each time a
plate is added to the stack, the whole pile is *pushed* down to keep
the top of the stack in place. If the top plate is removed, then the
whole stack *pops* back up. An alternative name for a stack is
a :term:`LIFO` (last in, first out), because the last object added to
the stack is the first object retrieved (contrast :term:`FIFO`).

Recall that a :term:`type` is defined by a set of possible values and
a set of operations. A stack is an ordered sequence of objects (of any
type) with the operations `push` to add a new object to the sequence,
and `pop` to return the most recently added object, and remove it from
the sequence. It is also common to add an additional operation of
`peek`, which returns the most recently added object without removing
it from the stack.

.. note::

   Put a diagram illustrating stack operations here.


An example: reverse Polish notation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reverse Polish notation, or postfix notation, is a way of writing
mathematical operations without using operator priority or brackets in
order to determine the order of operations. This makes the
implementation of reverse Polish notation arithmetic particularly
simple. Reverse Polish calculators require fewer button pushes for
complex calculations, and were popular in the 1970s. They are still
available, most famously from HP. In a more current example, the
PostScript language used to describe documents for printers is reverse
Polish.

In reverse Polish notation, the operator follows its operands. For
example to add the numbers one and two, one would write :math:`1\ 2\
+`. Formally, a reverse Polish calculator comprises a set of numbers,
a set of operators (each of which takes a fixed number of arguments),
and a stack. Each number encountered in the expression is pushed onto
the stack, while each operator pops the right number of arguments off
the stack and pushes the result onto the stack. At the end of the
calculation, the result of the calculation is on the top of the stack.
:numref:`rpcalc` shows :term:`pseudocode`, for as reverse Polish
calculator.

.. _rpcalc:

.. code-block:: python3
   :caption: Pseudocode for a reverse Polish calculator implemented
             using a :term:`stack`

   for item in inputs:
       if item is number:
           stack.push(number)
       elif item is operator:
           operand2 = stack.pop()
           operand1 = stack.pop()
           stack.push(operand1 operator operand2)
   return stack.pop()  

Notice that we pop the second operand before the first. This is
because :math:`4\ 2\ -` means :math:`4 - 2`, not :math:`2 - 4`.
:numref:`rptable` Shows how a reverse Polish calculator would evaluate
an arithmetic expression.

.. _rptable:

.. list-table:: Evaluation of the reverse Polish expression
                `6 2 / 2 4 ** +` using a stack
                (equivalent to :math:`6/2 + 2^4 = 3 + 16 = 19`).
   :header-rows: 1
   :widths: 60 20 50

   * - Expression
     - Stack
     - Action
   * - `6 2 / 2 4 ** +`
     - `()`
     -
   * - `6 / 2 4 ** +`
     - `(6)`
     - `push`
   * - `/ 2 4 ** +`
     - `(6 2)`
     - `push`
   * - `2 4 ** +`
     - `(3)`
     - `pop, pop, divide, push`
   * - `4 ** +`
     - `(3 2)`
     - `push`
   * - `** +`
     - `(3 2 4)`
     - `push`
   * - `+`
     - `(3 16)`
     - `pop, pop, power, push`
   * - 
     - `(19)`
     - `pop, pop, add, push`

Implementing stacks in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While it is strictly true that Python does not have a stack type, the
:class:`list` class functions as a perfectly good stack. The
relationship between the two is shown in :numref:`list_stack`.

.. _list_stack:

.. list-table:: Correspondence between abstract stack operations, and
                Python list operations. We assume a list called
                `my_list`
   :header-rows: 1
   :widths: 30 30 30

   * - Stack operation
     - List operation
     - Description
   * - `push(x)`
     - `my_list.append(x)`
     - Add `x` to the top of the stack.
   * - `pop`
     - :meth:`my_list.pop`
     - Return and remove the top item on the stack.
   * - `peek`
     - `my_list[-1]`
     - Return the last item on the stack, but leave the stack
       unchanged.
   * -
     - `len(my_list)`
     - Return the number of items on the stack. Not strictly required
       stack operation, but often useful.   

Separation of concerns
----------------------

At first sight, discussions of abstract data types can seem like a
complication of what, at the end of the day, are just operations on
some objects. Instead of talking about stacks, why don't we just say
that a reverse Polish calculator can be implemented using a
:class:`list`?

The critical conceptual difference here is that a
:class:`list` is a Python construct, while a stack is a mathematical
concept with universal applicability. If you understand the concept of
a stack, then you will be able to use this to design algorithms and
write programs in other languages where the concrete implementation
might be a different type, or you might have to create your own stack
from lower-level types and operations.

This is an example of a fundamental computer science concept called
:term:`separation of concerns`. Separation of concerns is a design
principle that underpins much of what is considered to be good
practice in programming. The idea is to divide larger tasks into
smaller units each responsible for doing one thing (addressing one
concern). Different units communicate with each other using
mathematically well defined interfaces. This makes the internal design
of each unit more-or-less independent of the other units. Why is this
important? There are two key reasons. The first is that in
programming, as in maths, complexity is the enemy of
understanding. Directly addressing a large and compex problem is
likely to result in a large and complex piece of code which nobody
understands. Such a program will almost inevitably produce the wrong
answer, and finding out what is wrong will be exceptionally difficult.

Abstract data types provide part of the mathematical interface that
separates different concerns. The user of an abstract data type has an
object with a simple set of operations which is easy to reason about,
while the implementer of an abstract data type only has to provide an
object with the required methods. They do not have to reason about all
the ways in which that object might be used. By learning to think
about programming in terms of abstract types and objects, you will
become a better programmer who can address more complex programming
tasks. 


Algorithmic complexity
----------------------

The second reason that understanding abstract data types is important
is that a good implementation of a well designed abstract data type
will have well defined performance characteristics. In particular the
optimal algorithmic complexity, expressed in big 'O' notation, of
operations on abstract data types will be known. Recall the definition
of big 'O':

.. _bigO:

.. proof:definition:: :math:`O`

   Let `f`, `g`, be real-valued functions. Then:

   .. math::

      f(n) = O(g(n)) \textrm{ as } n\rightarrow \infty

   if there exists :math:`M>0` and `N>0` such that:

   .. math::

      n>N\, \Rightarrow\, |f(n)| < M g(n).

We use :math:`n` rather than :math:`x` as the independent variable,
because we are primarily interested in characterising the number of
primitive operations or the amount of memory that an algorithm will
use as a function of the number of objects stored in the relevant
abstract data type.

For example, in the Python :class:`list` implementation, all of all of
the stack operations are, on average, :math:`O(1)`. This means that
each of pushing, popping, and peeking has an approximately fixed cost
that does not depend on the current size of the stack. This does not
obviously have to be the case, especially for the push and pop
operations, which modify the stack. :numref:`badstack` provides an
implementation of a stack in which the data is stored as a Python
:class:`tuple`. Here, every time item is pushed onto or popped from
the stack, a new copy of the :class:`tuple` has to be made. This
touches every one of the :math:`n` items currently in the stack, and
therefore costs :math:`O(n)` operations. It is often useful to
distinguish between time complexity, which is an indication of the
number of operations required to execute an algorithm, and space
complexity, which measures the peak memory usage of an algorithm or
data structure.

.. _badstack:

.. code-block:: python3
   :caption: A poorly designed stack implementation in which push and pop cost
             :math:`O(n)` operations, where :math:`n` is the current
             number of objects on the stack.

   class BadStack:
       def __init__(self):
           self.data = ()

       def push(self, value):
           self.data += (value,)

       def pop(self):
           value = self.data[-1]
           self.data = self.data[:-1]
           return value

       def peek(self):
           return self.data[-1]

:numref:`bigO` is a particular case of the big `O` notation which you
may already have seen in numerical analysis. However, there the limit
is taken as the independent variable approaches 0. This difference of
context between computer science and numerical analysis is sometimes
confusing, particularly since both disciplines conventionally leave
out the limit. It's worth keeping in mind that the difference, because
a numerical algorithm with :math:`O(h^4)` error is really rather good,
since `h` is small, but an algorithm with :math:`O(n^4)` cost is very
expensive indeed!

Amortised complexity and worst case complexity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The actual implementation of a :class:`list` is of a contiguous
sequence of locations in memory, each of which can hold a reference to
a Python object. How, then, can appending an item to a list work? The
next location in memory might already be in use for some other
data. The obvious naïve implementation would be to allocate a new
contiguous block of memory, one location longer than the previous one,
and copy the existing values into that before placing the appended
value in the final location. This amounts to the approach in
:numref:`badstack`, with the result that appending an item to a list
would have a time complexity of :math:`O(n)`.

In fact, this is not how Python lists are implemented. Instead of only
allocating the exact amount of memory needed, Python allocates a bit
more and keeps track of how many memory locations are currently in use
to implement the list. Only when all the current memory locations are
full does a further append operation cause Python to allocate more
memory. The amount of memory allocated is approximately proportional
to the current length of the list. That is, if the current list length
is :math:`n` then the new memory allocation will be of size
approximately :math:`kn` for some :math:`k>1`.

.. note::

   Need diagrams of how a dynamic array works here.

What does this memory allocation strategy mean for the computational
complexity of appending items to the list? There are two cases. If
there is a spare location for the appended value, then a reference to
the value is simply inserted into that location. The cost of this does
not depend on the current length of the list, so it's :math:`O(1)`. If
all of the allocated memory locations are now in use then a new chunk
of memory is allocated and the existing values are copied there. This
is an :math:`O(n)` operation. However, this :math:`O(n)` operation
only occurs when the list has to be extended. How often is that?
Suppose the list has just been reallocated (at a cost of
:math:`O(n)`). The new memory allocation is :math:`kn` large, but we've
aready used :math:`n` locations so we get :math:`(k-1)n` more cheap
:math:`O(1)` append operations before we have to reallocate
again. :math:`(k-1)n = O(n)` so this means that adding :math:`O(n)`
items to the list costs:

.. math::

   \underbrace{O(n)}_{\textrm{reallocation}} + \underbrace{O(n)\times O(1)}_{O(n) \textrm{ cheap appends.}} = O(n)

If appending :math:`O(n)` items to a list has a time complexity of
:math:`O(n)`, it follows that the cost of appending one item to a
list, averaged over a suitably large number of operations, is
:math:`O(1)`. This measure of complexity, in which the cost of
occasional expensive operations is considered averaged over a large
number of operations, is called :term:`amortised complexity`. In
contrast, the occasional list append operation is an example of the
:term:`worst case complexity` of the algorithm. Appending an item to a
list has an amortised time complexity of :math:`O(1)` but a worst case
time complexity of :math:`O(n)`.


Some more abstract data types
-----------------------------
           
Queue and deque
~~~~~~~~~~~~~~~

A :term:`queue` is, like a :term:`stack`, an ordered sequence of
objects. The difference is that the only accessible item in the
sequence is the *earliest* added. Items can be added to the back of
the queue and taken from the front. As with a stack, the optimal
implementations of item insertion and removal are :math:`O(1)`.

A :term:`deque` (Double Ended QUEue) is a generalisation of a queue to
permit adding and removing items at either end. Indeed, the observant
reader will note that a stack is also a special case of a
deque. Python's standard library contains the
:class:`collections.deque` class, providing a simple and efficient
implementation of a deque.

.. note::

   A good exercise would be to implement a deque using a list as a
   ring buffer.


Linked lists
~~~~~~~~~~~~

One disadvantage of a deque (and hence of a stack or queue) is that
inserting an object into the middle of the sequence is often an
:math:`O(n)` operation, because on average half of the items in the
sequence need to be shuffled to make space. A linked list provides a
mechanism for avoiding this. A singly linked list is a collection of
links. Each link contains a reference to a data item, and a reference
to the next link. Starting from the first link in a list, it is
possible to move along the list by following the references to
successive further links. A new item can be inserted at the current
point in the list by creating a new link, pointing the link reference
of the new link to the next link, and pointing the link reference of
the current link to the new link.

.. note::

   diagram of linked list insertion here.

.. code-block: python3
   :caption: A simple singly linked list implementation.

   class Link:
      def __init__(self, value, next=None):
         self.value = value
         self.next = next

      def insert(self, link):
         '''Insert a new link after the current one.'''

         link.next = self.next
         self.next = link

Linked lists tend to have advantages where data is sparse. For
example, our implementation of a :class:`Polynomial` in
:numref:`objects` would represent :math:`x^{100} + 1` very
inefficiently, with 98 zeroes. Squaring this polynomial would cause
tens of thousands of operations, almost all of them on
zeroes. Conversely, if we implemented polynomials with linked lists of
terms, this squaring operation would take the handful of operations we
expect.

A doubly linked list differs from a singly linked list in that each
link contains links both to the next link and to the previous
one. This enables the list to be traversed both forwards and
backwards.

Sets
~~~~

Dictionaries
~~~~~~~~~~~~


The iterator protocol
=====================

The abstract data types we have considered here are collections of
objects, and one common abstract operation which is applicable to
collections is to iterate over them. That is to say, to loop over the
objects in the collection and perform some action for each one. This
operation is sufficiently common that Python provides a special syntax
for it, the :ref:`for loop <python:for>`. You will already be very
familiar with looping over sequences such as lists:

.. code-block:: ipython3

   In [1]: for planet in ["World", "Mars", "Venus"]:
      ...:     print(f"Hello {planet}")
      ...:
   Hello World
   Hello Mars
   Hello Venus

Python offers a useful abstraction of this concept. By implementing
the correct :term:`special methods <special method>`, a container
class can provide the ability to be iterated over. This is a great
example of abstraction in action: the user doesn't need to know or
care how a particular container is implemented and therefore how to
find all of its contents.

There are two :term:`special methods <special method>` required for
iteration. Neither take any arguments. The first, :func:`__iter__`,
needs to be implemented by the container type. Its role is to return
an object which implements iteration. This could be the container
itself, or it could be a special iteration object (for example because
it is necessary to store a number recording where the iteration is up
to).

The object returned by :func:`__iter__` needs to itself implement
:func:`__iter__` (for exampe it could simply `return self`). In
addition, it needs to implement the :func:`__next__` method. This is
called by Python repeatedly to obtain the next object in the iteration
sequence.
           
Glossary
========

 .. glossary::
    :sorted:

    abstract data type
       A mathematical :term:`type`, defined independently of any
       concrete implementation in code.

    algorithmic complexity
       A measure of the number of operations (time complexity) or
       amount of storage (space complexity) required by an algorithm
       or data structure. Algorithmic complexity is usually stated in
       terms of a bound given in big 'O' notation.

    amortised complexity
       The average complexity of an algorithm considered over a suitably
       large number of invocations of that algorithm. Amortised
       complexity takes into account circumstances wherethe worst case
       complexity of an algorithm is known to occur only rarely.

    queue
    FIFO (first in, first out)
       an :term:`abstract data type` representing an ordered sequence
       of objects in which objects are accessed in the order in which
       they were added.

    separation of concerns
       A design principle under which individual components each
       address a specific well defined need and communicate through
       well defined interfaces with other components. Separation of
       concerns enables reasoning about one part of a problem
       independently of other parts.

    stack
    LIFO (last in, first out)
       an :term:`abstract data type` representing an ordered sequence
       of objects, in which only the most recently added object can be
       directly accessed.

    worst case complexity    
       An upper bound on the :term:`algorithmic complexity` of an
       algorithm. Many algorithms have a relatively low algorithmic
       complexity most of the times they are run, but for some inputs
       are much more complex. :term:`amortised complexity` is a
       mechanism for taking into account the frequency at which the
       worst case complexity can be expected to occur.
