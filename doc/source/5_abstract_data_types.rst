.. _abstract_data_types:

Abstract data types
===================

In :numref:`week %s <objects>`, we introduced the concept of :term:`type` as an
:term:`abstraction` comprising a set of possible values, and a set of
operations. All types in Python are abstractions in this sense
because we deal with them in terms of their defined properties rather
than their actual implementation. However, it can also be useful to
define purely mathematical types, distinct from their concrete
realisation in code. Indeed, there are typically multiple possible
concrete realisations of a mathematical idea.

.. proof:definition:: Abstract Data Type

   An *abstract data type* is a purely mathematical :term:`type`,
   defined independently of its concrete realisation as code.

Abstract data types enable the programmer to reason about algorithms and their
cost separately from the task of implementing them. In contrast, we can also
define the concrete realisation of a data type:

.. proof:definition:: Data structure

    A *data structure* describes the concrete implementation of a data type:
    which data is stored, in what order, and how it is interpreted.

In understanding abstract data types, it is often useful to think about the data
structures which could be used to implement them.

.. _stacks:

Stacks
------

.. dropdown:: Video: stacks as an abstract data type.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/506479213"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b014e13a-82ca-4a57-ac7f-acc000e64349>`__.


Possibly the simplest abstract data type which is not synonymous with
a Python type is the :term:`stack`. A stack is a sequence of objects
in which only the most recently added object is accessible. The image
to have in mind is a stack of plates on a spring-loaded holder of the
type found in many universities or workplace canteens. Each time a
plate is added to the stack, the whole pile is *pushed* down to keep
the top of the stack in place. If the top plate is removed, then the
whole stack *pops* back up. An alternative name for a stack is
a :term:`LIFO (last in, first out)`, because the last object added to
the stack is the first object retrieved (contrast :term:`FIFO <FIFO (first in, first out)>`).

Recall that a :term:`type` is defined by a set of possible values and
a set of operations. The value of stack is an ordered sequence of objects of any
type. The operations are `push` to add a new object to the sequence,
and `pop` to return the most recently added object, and remove it from
the sequence. :numref:`stackdiag` shows these operations. It is also common to add an additional operation of
`peek`, which returns the most recently added object without removing
it from the stack.

.. _stackdiag:

.. blockdiag::
    :caption: Cartoon of a sequence of stack operations. First 24, 12, 57 are
        pushed, then 57 is popped.


      blockdiag stack{
      // setup info
      node_height = 30;
      "Stack" [color = orange];           //push
      "Stack " [color=orange, stacked];   //push
      "Stack  " [color=orange, stacked];  //push
      "Stack   " [color=orange, stacked]; //pop
      "push 24" [color="#2E8B57"]; 
      "push 12" [color="#2E8B57"]; 
      "push 57" [color="#2E8B57"]; 
      "pop" [color="#CD5C5C"];
      group{
      24;
      color =  orange
      }

      group second{
      12; "24 ";
      color =  orange
      }

      group third{
      57 ;"12 "; "24  ";
      color =  orange
      }

      group fourth{
      "12  "; "24   ";
      color =  orange
      }

      // structure and flow
      "push 24" -> "Stack";
      "push 24" -> 24 [style="none"];

      "push 12" -> "12" [style="none"];
      "push 12" -> "Stack ";

      "push 57" -> "12 " [style="none"];
      "push 57" -> "Stack  ";
      
      "Stack" -> "pop" [style="none"];
      "pop" -> "Stack   ";
      "pop" -> "12  "[style="none"];

      C [shape = "dots"]
      "Stack " -> C [style="none"];
      }
   
An example: reverse Polish notation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reverse Polish notation, or postfix notation, is a way of writing
mathematical operations without using operator precedence or brackets in
order to determine the order of operations. This makes the
implementation of reverse Polish notation arithmetic particularly
simple. Reverse Polish calculators require fewer button pushes for
complex calculations and were popular in the 1970s. They are still
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
:numref:`rpcalc` shows :term:`pseudocode` for a reverse Polish
calculator.

.. _rpcalc:

.. code-block:: python3
   :caption: Pseudocode for a reverse Polish calculator implemented
             using a :term:`stack`
   :linenos:

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
   * - `2 / 2 4 ** +`
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
     - Return the number of items on the stack. Not a strictly required
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
smaller units, each responsible for doing one thing (addressing one
concern). Different units communicate with each other using
mathematically well-defined interfaces. This makes the internal design
of each unit more-or-less independent of the other units. Why is this
important? There are two key reasons. The first is that in
programming, as in maths, complexity is the enemy of
understanding. Directly addressing a large and complex problem is
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

.. dropdown:: Video: dynamic arrays and algorithmic complexity.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/506479208"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=516115a0-b13d-4693-951b-acc000e642ff>`__.


The second reason that understanding abstract data types is important
is that a good implementation of a well-designed abstract data type
will have well-defined performance characteristics. In particular, the
optimal algorithmic complexity, expressed in big :math:`O` notation, of
operations on abstract data types will be known. Recall the definition
of big :math:`O`:

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

For example, in the Python :class:`list` implementation, all of
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

.. container:: badcode

    .. code-block:: python3
       :caption: A poorly designed stack implementation in which push and pop cost
                 :math:`O(n)` operations, where :math:`n` is the current
                 number of objects on the stack.
       :linenos:

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


.. note::

    You may already have seen big O notation in numerical analysis. The
    distinction is that in analysing algorithmic complexity, the limit is taken
    as :math:`n` approaches infinity, while in numerical analysis the
    independent variable approaches 0. This difference between two closely
    related fields is often confusing, particularly since both disciplines
    conventionally leave out the limit. It's worth keeping in mind the
    difference, because a numerical algorithm with :math:`O(h^4)` error is
    really rather good since `h` is small, but an algorithm with :math:`O(n^4)`
    cost is very expensive indeed!

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
approximately :math:`kn` for some :math:`k>1`. This :term:`data structure` is
called a :term:`dynamic array`. :numref:`dynamicarray` illustrates its operation.
   
.. _dynamicarray:

.. graphviz::
    :caption: A dynamic array implementation of a :class:`list`. The existing
        memory buffer is full, so when 11 is appended to the list, a larger
        buffer is created and the whole list is copied into it. When 13 is
        subsequently appended to the list, there is still space in the buffer so
        it is not necessary to copy the whole list.
    :align: center

    digraph dl {
    	bgcolor="#ffffff00" # RGBA (with alpha)
	    graph [
	    rankdir = "LR"
	    ];
	    node [
	    fontsize = "16"
	    shape = "ellipse"
	    ];
	    edge [
	    ];
	    
	    subgraph cluster_0 {
	    		style="ellipse, dashed";
	    		bgcolor="#CD5C5C";
	    "node0" [
	    label = "<f0> 2 | 3| 5| 7 |e <f1>"
	    shape = "record"
	    ];
	    }
	    
	    subgraph cluster_3 {
	    		style="ellipse, dashed";
	    		bgcolor="#2E8B57";
	    		
	    "node1" [
	    label = "<f0> 2 | 3| 5| 7 | <f1> 11| | | <f2>"
	    shape = "record"

	    ];
        }
	    subgraph cluster_4 {
	    		style="ellipse, dashed";
	    		bgcolor="#2E8B57";
	    
	    "node3" [
	    label = "<f0> 2 | 3| 5| 7| <f1> 11| <f2> 13| | <f3>"
	    shape = "record"
	    ];
	    }

	    "node0":f0 -> "node1":f0 [
	    id = 2
		label = "append 11"
	    ];

		"node1":f0 -> "node3":f0 [
	    id = 2
		label = "append 13"
	    ];
    }
   
What does this memory allocation strategy mean for the computational
complexity of appending items to the list? There are two cases. If
there is a spare location for the appended value, then a reference to
the value is simply inserted into that location. The cost of this does
not depend on the current length of the list, so it's :math:`O(1)`. If
all of the allocated memory locations are now in use, then a new chunk
of memory is allocated, and the existing values are copied there. This
is an :math:`O(n)` operation. However, this :math:`O(n)` operation
only occurs when the list has to be extended. How often is that?
Suppose the list has just been reallocated (at a cost of
:math:`O(n)`). The new memory allocation is :math:`kn` large, but we've
already used :math:`n` locations so we get :math:`(k-1)n` more cheap
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
contrast, the occasional reallocate and copy operation is an example of the
:term:`worst case complexity` of the algorithm. Appending an item to a
list has an amortised time complexity of :math:`O(1)` but a worst-case
time complexity of :math:`O(n)`.

We can use Python's :term:`introspection` capabilities to illustrate how the
dynamic allocation of space for a list works as the list is appended. The
:func:`sys.getsizeof` function returns the amount of computer memory that an
object consumes. The function in :numref:`byte_size` uses this to diagnose the memory
consumption of progressively longer lists, and :numref:`byte_size` demonstrates
this.

.. _byte_size:

.. code-block:: python3
    :caption: Code to progressively lengthen a :class:`list` and observe the
        impact on its memory consumption. This function is available as
        :func:`example_code.linked_list.byte_size`.
    :linenos:

    import sys

    def byte_size(n):
        """Print the size in bytes of lists up to length n."""
        data = []
        for i in range(n):
            a = len(data)
            b = sys.getsizeof(data)
            print(f"Length:{a}; Size in bytes:{b}")
            data.append(i)
	
.. _byte_size_demo:

.. code-block:: ipython3
    :caption: The memory consumption of lists of length 0 to 19. We can infer
        that the list is reallocated at lengths 1, 5, 9, and 17.

    In [1]: from example_code.linked_list import byte_size

    In [2]: byte_size(20)
    Length:0; Size in bytes:56
    Length:1; Size in bytes:88
    Length:2; Size in bytes:88
    Length:3; Size in bytes:88
    Length:4; Size in bytes:88
    Length:5; Size in bytes:120
    Length:6; Size in bytes:120
    Length:7; Size in bytes:120
    Length:8; Size in bytes:120
    Length:9; Size in bytes:184
    Length:10; Size in bytes:184
    Length:11; Size in bytes:184
    Length:12; Size in bytes:184
    Length:13; Size in bytes:184
    Length:14; Size in bytes:184
    Length:15; Size in bytes:184
    Length:16; Size in bytes:184
    Length:17; Size in bytes:256
    Length:18; Size in bytes:256
    Length:19; Size in bytes:256


Queues and deques
-----------------

.. dropdown:: Video: deques and ring buffers.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/506710190"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5ba7fde3-8ca9-48e2-b66b-acc100bd1953>`__.


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

Ring buffers
~~~~~~~~~~~~

How might one go about implementing a deque? A dynamic array allows values to be
appended with :math:`O(1)` complexity, but doesn't offer an efficient mechanism
for prepending values. One might think that the natural solution for this would
be to create a double-ended dynamic array: a buffer with spare space at each
end. Unfortunately this is not optimally efficient in the case where the deque
is used to implement a queue of approximately constant length. In that case,
values are consistently added at one end of the :term:`data structure` and removed from
the other. Even in the case of a double-ended dynamic array, the buffer space at
the append end of the queue will constantly run out, necessitating an expensive
copy operation. The solution is to use a dynamic array, but to logically join up
its ends, so that the first position in the buffer follows on from the last.
Only in the case where all positions in the buffer are full will the buffer be
reallocated. This data structure is called a ring buffer. 

.. _ring_buffer:

.. figure:: images/ring_buffer.*
    
    An implementation of a ring buffer, with queue
    operations illustrating its operation. 

:numref:`ring_buffer` shows a ring buffer being used as a queue. At each step,
an object is appended to the end of the queue, or removed from its start. At
step 7, the contents of the buffer wrap around: the queue at this stage contains
`D, E, F`. At step 9 there is insufficient space in the buffer to append `G`, so
new space is allocated and the buffer's contents copied to the start of the new
buffer. 

Linked lists
------------


.. dropdown:: Video: linked lists.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/506743244"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=d1b2b176-066a-4d68-aa01-acc100eec5c6>`__.

One disadvantage of a deque (and hence of a stack or queue) is that inserting an
object into the middle of the sequence is often an :math:`O(n)` operation,
because on average half of the items in the sequence need to be shuffled to make
space. A linked list provides a mechanism for avoiding this. A singly linked
list is a collection of links. Each link contains a reference to a data item and
a reference to the next link. Starting from the first link in a list, it is
possible to move along the list by following the references to successive
further links. A new item can be inserted at the current point in the list by
creating a new link, pointing the link reference of the new link to the next
link, and pointing the link reference of the current link to the new link.
:numref:`linked_list_dia` shows this process, while :numref:`linked_list` shows
a minimal implementation of a linked list in Python. Notice that there is no
object for the list itself: a linked list is simply a linked set of links. Some
linked list implementations do store an object for the list itself, in order to
record convenient information such as the list length, but it's not strictly necessary.

.. _linked_list_dia:

.. graphviz::
   :caption: Diagram of a linked list. A new link containing the value `F` is
        being inserted between the link with value `C` and that with value `D`.
   :align: center

    digraph ll {
		bgcolor="#ffffff00"
		graph [
		rankdir = "TB"
		];
		node [
		fontsize = "16"
		];
		edge [
		];

		subgraph cluster_1 {
				style="ellipse, dashed";
				bgcolor="lightgray";

		"node_init" [
		label = "<f0> A| next| 1 <f1>"
		shape = "record"
		];

		"node0" [
		label = "<f0> B| next| 1 <f1>"
		shape = "record"
		];

		"node1" [
		label = "<f0> C| next| 1 <f1>"
		shape = "record"
		];

		"node2" [
		label = "<f0> D| next| 1 <f1>"
		shape = "record"
		];
		
		 "node3" [
		label = "<f0> E| next| 1 <f1>"
		shape = "record"
		];

		 "node4" [
		label = "None"
		shape = "record"
		];

		

		subgraph cluster_2 {
				style="ellipse, dashed";
				bgcolor="#2E8B57";
		
		"node5" [
		label = "<f0> F| next|_ <f1>"
		shape = "record"
		];
		}

		"node_init":f1 -> "node0":f0 [
		id = 0
		];
		
		"node0":f1 -> "node1":f0 [
		id = 1
		];
        
		"node1":f1 -> "node2":f0 [
		id = 2
		label ="old link"
		];
		
		"node2":f1 -> "node3":f0 [
		id = 3
		];

		"node1":f1 -> "node5":f0 [
		id = 4
		label =" new link"
		style= "dashed"
		];

		"node5":f1 -> "node2":f0 [
		id = 5
		style= "dashed"
		];

        "node3":f1 -> "node4":f1 [
        id = 6
        style = dashed
		];
	   }
   }
	
.. code-block:: python3
   :caption: A simple singly linked list implementation.
   :name: linked_list
   :linenos:

   class Link:
       def __init__(self, value, next=None):
          self.value = value
          self.next = next

       def insert(self, link):
          '''Insert a new link after the current one.'''

          link.next = self.next
          self.next = link

Linked lists tend to have advantages where data is sparse. For
example, our implementation of a :class:`~example_code.polynomial.Polynomial` in
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

A :term:`deque`, and therefore a :term:`stack` or a :term:`queue` can
be implemented using a linked list, however the constant creation of
new link objects is typically less efficient than implementations
based on ring buffers.

.. _iterator_protocol:

The iterator protocol
---------------------

.. dropdown:: Video: the iterator protocol.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/506743250"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f37ae26c-a39a-4757-bc0d-acc100eec588>`__.


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

There are two :term:`special methods <special method>` required for iteration.
Neither take any arguments beyond the object itself. The first,
:meth:`~container.__iter__`, needs to be implemented by the container type. Its
role is to return an object which implements iteration. This could be the
container itself, or it could be a special iteration object (for example because
it is necessary to store a number recording where the iteration is up to).

The object returned by :meth:`~container.__iter__` needs to itself implement
:meth:`~iterator.__iter__` (for example it could simply `return self`). In
addition, it needs to implement the :meth:`~iterator.__next__` method. This is
called by Python repeatedly to obtain the next object in the iteration
sequence. Once the sequence is exhausted, subsequent calls to
:meth:`~iterator.__next__` should raise the built-in :class:`StopIteration`
exception. This tells Python that the iteration is over. This
arrangement is called the iterator protocol, and it's further
documented in the :ref:`official Python documentation <typeiter>`.

.. hint::

   Raising exceptions is the subject of :numref:`raising_exceptions`,
   to which we will turn presently. Fur current purposes, it is
   sufficient to know that iteration is halted when :meth:`~iterator.__next__`
   executes this line of code:

   .. code-block:: python3
                   
      raise StopIteration

Let's suppose we want to make the linked list in :numref:`linked_list`
iterable. We'll need to make another object to keep track of where we
are in the list at each point in the
iteration. :numref:`iterating_linked_list` shows the code. The helper
class :class:`LinkIterator` is never seen by the user, it's just there
to keep track of the iteration.

.. _iterating_linked_list:

.. code-block:: python3
    :caption: A simple linked list implementation that supports the iterator
        protocol.
    :linenos:

    class Link:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def insert(self, link):
            '''Insert a new link after the current one.'''

            link.next = self.next
            self.next = link

        def __iter__(self):
            return LinkIterator(self)


    class LinkIterator:
        def __init__(self, link):
            self.here = link

        def __iter__(self):
            return self

        def __next__(self):
            if self.here:
                next = self.here
                self.here = self.here.next
                return next.value
            else:
                raise StopIteration

As a trivial example, we can set up a short linked list and iterate over it, printing its values:

.. code-block:: ipython3

   In [3]: linked_list = Link(1, Link(2, Link(3)))

   In [4]: for l in linked_list: 
   ...:     print(l)
   ...:
   1
   2
   3

Indeed, since Python now knows how to iterate over our linked list,
converting it to a sequence type such as a :class:`tuple` will now work
automatically:

.. code-block:: ipython3

   In [5]: tuple(linked_list)
   Out[5]: (1, 2, 3)

Other abstract data types
-------------------------

Here we have introduced in some detail a few relatively simple abstract data
types that illustrate the distinction between the mathematical properties of a
type and the concrete details of its implementation. There are many other
abstract data types, some of which you will have already met, and we will
encouter a few more in this course. For context, here are a few other examples.

set
    A set is an unordered collection of objects with the property that objects
    that compare equal can only occur once in the set. Inserting or accessing a
    set member has :math:`O(1)` :term:`amortised complexity`. Python provides the
    :class:`set` built in class as an implementation.

dictionary or map
    A generalised function in which unique (up to equality) keys are mapped to
    arbitrary values. Again, insertion and deletion cost :math:`O(1)`
    operations on average. The Python :class:`dict` type is an implementation.

graph
    A general relation between a set and itself defined by a set of values and a
    set of edges, where each edge connects exactly two vertices. Graphs can be
    used to describe very general relationships among data.

tree
    A particular sort of graph in which edges have a direction (a from and a to
    node), and each node is the origin of at most one edge. Trees can be used to
    describe many types of structured relationship. We will show how trees and
    related structures can be used in symbolic maths in :numref:`trees`.

Glossary
--------

 .. glossary::
    :sorted:

    abstract data type
        A mathematical :term:`type`, defined independently of any
        concrete implementation in code. Contrast :term:`data structure`

    algorithmic complexity
        A measure of the number of operations (time complexity) or
        amount of storage (space complexity) required by an algorithm
        or data structure. Algorithmic complexity is usually stated in
        terms of a bound given in big 'O' notation.

    amortised complexity
        The average complexity of an algorithm considered over a suitably
        large number of invocations of that algorithm. Amortised
        complexity takes into account circumstances where the worst case
        complexity of an algorithm is known to occur only rarely.

    data structure
        The concrete implementation of a data type in code. The data structure
        is the organisation of the actual information in the computer's memory
        or on disk. Contrast :term:`abstract data type`.

    deque
        A double ended queue. An :term:`abstract data type`
        representing an ordered sequence in which objects can be added
        or removed at either end. A deque is a generalisation of both a
        :term:`stack` and a :term:`queue`.

    dynamic array
        A :term:`data structure` for efficiently storing a variable length
        sequence of values. A fixed length piece of memory, called a buffer, is reserved for the
        sequence. If the number of items exceeds the size of the buffer then a
        larger buffer is reserved, the contents of the sequence are copied over,
        and the original buffer is returned to the system.

    introspection
        The ability to inspect the implementation of a program from inside that
        program while it is running.   
        
    queue
    FIFO (first in, first out)
        An :term:`abstract data type` representing an ordered sequence
        of objects in which objects are accessed in the order in which
        they were added.

    ring buffer
        A generalisation of a :term:`dynamic array` in which two ends of the
        memory buffer are considered connected in order to enable the sequence
        to be efficiently lengthened or shortened at either end.

    separation of concerns
        A design principle under which individual components each
        address a specific well defined need and communicate through
        well defined interfaces with other components. Separation of
        concerns enables reasoning about one part of a problem
        independently of other parts.

    stack
    LIFO (last in, first out)
        An :term:`abstract data type` representing an ordered sequence
        of objects, in which only the most recently added object can be
        directly accessed.

    worst case complexity
        An upper bound on the :term:`algorithmic complexity` of an
        algorithm. Many algorithms have a relatively low algorithmic
        complexity most of the times they are run, but for some inputs
        are much more complex. :term:`amortised complexity` is a
        mechanism for taking into account the frequency at which the
        worst case complexity can be expected to occur.

Exercises
---------

.. panels::
    :card: quiz shadow

    .. link-button:: https://bb.imperial.ac.uk/webapps/assessment/take/launchAssessment.jsp?course_id=_25965_1&content_id=_2077681_1&mode=cpview
        :text: This week's quiz
        :classes: stretched-link 


Obtain the `skeleton code for these exercises from GitHub classroom
<https://classroom.github.com/a/eHigwP_C>`__. You will also need to install the pytest-timeout package.

.. proof:exercise::

    In this week's skeleton repository, create a :term:`package` called
    :mod:`adt_examples` with a :term:`module` called
    :mod:`adt_examples.fibonacci`. Make the package installable and install in
    editable mode. Create a class :class:`Fib` implementing the iterator
    protocol which returns the Fibonacci numbers. In other words, the following
    code should print the `Fibonacci` numbers under 100:

    .. code-block:: python3

        from adt_examples.fibonacci import Fib

        for n in Fib():
            print(n)
            if n >= 100:
                break

    Obviously the Fibonacci sequence is infinite, so your iterator will never
    raise :class:`StopIteration`. Make sure that calculating the next number is
    always a :math:`O(1)` operation: don't recalculate from 1 each time.

.. proof:exercise::

    In this week's skeleton repository, create a :term:`module`
    :mod:`adt_examples.rpcalc` containing a class :class:`RPCalc` implementing a
    reverse Polish calculator. The calculator should have the following methods:

    :obj:`push(n)`
        This takes a single argument. If it is a number then it should be
        pushed onto the calculator's internal stack. If it is the string for a
        recognised operator, then the appropriate number of operands should be
        popped from the internal stack, the result pushed back on the stack.
        Your calculator should support the following operators: `"+"`, `"-"`,
        `"*"`, `"/"`, `"sin"`, `"cos"`. The method should not return anything.

    :meth:`pop`
        This method, which takes no arguments, should pop the top item on the
        internal stack and return it. 

    :meth:`peek`
        This method, which takes no arguments, should return the top item on the
        internal stack without popping it.

    :meth:`__len__`
        This is the :meth:`~object.__len__` :term:`special method`, which takes no
        arguments but returns the length of the object. In this case, the length
        of the calculator is defined to be the number of items on its internal stack.

.. proof:exercise::

    In this week's skeleton repository, create a :term:`module`
    :mod:`adt_examples.deque` containing a class :class:`Deque` implementing a
    :term:`deque`. Your implementation should use a ring buffer implemented
    as a Python list. In order to make things somewhat simpler, we will use a
    fixed size ring buffer, which doesn't grow and shrink with the queue. The
    :term:`constructor` of your :class:`Deque` should take a single integer
    argument which is the size of the list you will use as your ring buffer.

    Implement the following methods:

    :obj:`append(x)`
        Append `x` to the end of the :class:`Deque`

    :obj:`appendleft(x)`
        Append `x` to the start of the :class:`Deque`
    
    :meth:`pop`
        Remove the last item in the :class:`Deque` and return it. 

    :meth:`popleft`
        Remove the first item in the :class:`Deque` and return it.

    :meth:`peek`
        Return the last item in the :class:`Deque` without removing it.

    :meth:`peekleft`
        Return the first item in the :class:`Deque` without removing it.

    :meth:`__len__`
        The :meth:`~object.__len__` :term:`special method`. This should return
        the number of items currently in the :class:`Deque`.

    In addition to the above methods, you should ensure that :class:`Deque`
    implements the iterator protocol. This should return the items in the queue,
    starting from the first to the last. Iterating over the
    :class:`Deque` should not modify the :class:`Deque`.

    .. hint::

        You can create a list of length `n` containing only
        :data:`None` using the following syntax:

        .. code-block:: python3

            l = [None] * n

        The modulo operator, `%` and integer division operator `//` are also likely
        to be very useful.

    .. hint::

        When removing an item from the :class:`Deque`, it is important to
        actually overwrite the place in the ring buffer occupied by that item,
        perhaps with `None`. Failing to do so can cause a program to "leak"
        memory (i.e. fail to free memory that is no longer needed).

    .. note::

        You may not use :class:`collections.deque` to implement this exercise.
