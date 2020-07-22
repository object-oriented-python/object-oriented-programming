

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
whole stack *pops* back up.

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

In reverse  Polish notation,  the operator  follows its  operands. For
example  to  add  the numbers  one  and  two,  one  would write  :math:`1\ 2\
+`. Formally, a reverse Polish  calculator comprises a set of numbers,
a set of operators (each of  which takes a fixed number of arguments),
and a stack. In :term:`pseudocode`,  the calculator can be implemented
as follows:

.. code-block:: python3

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

Imagine a reverse Polish calculator implementing the arithmetic
expression `6 2 / 2 4 ** +`:

.. list-table::
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

   


foo


  
   
.. note::

   A good exercise for stacks would be to implement a reverse Polish
   notation calculator.
