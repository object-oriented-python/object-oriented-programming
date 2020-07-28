

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
======================

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
======================

The second reason that understanding abstract data types is important
is that a good implementation of a well designed abstract data type
will have well defined performance characteristics. For example, in the
Python :class:`list` implementation, all of all of the stack operations
are, on average, :math:`O(1)`. This means that each of pushing,
popping, and peeking has an approximately fixed cost that does not
depend on the current size of the stack. This does not obviously have
to be the case, especially for the push and pop operations, which
modify the stack. :numref:`badstack` provides an implementation of a
stack in which the data is stored as a Python :class:`tuple`. 

.. note::

   Not finished.


The separation of an abstract data type from its 

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

Some more abstract data types
=============================
           
Stacks
~~~~~~


Linked lists
~~~~~~~~~~~~


The iterator pattern
====================

The abstract data types we have considered here are collections of
objects, and one common abstract operation which is applicable to
collections is to iterate over them. That is to say, to loop over the
objects in the collection and perform some action for each one. This
operation is sufficiently common that Python provides a special syntax
for it, the for loop. 



           
Glossary
========

 .. glossary::
    :sorted:

    abstract data type
       A mathematical :term:`type`, defined independently of any
       concrete implementation in code.

    pipe
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
