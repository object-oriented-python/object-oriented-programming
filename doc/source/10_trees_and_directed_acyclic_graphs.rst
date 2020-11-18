.. _trees:

Trees and directed acyclic graphs
=================================

The :term:`abstract data types <abstract data type>` that we met in
:numref:`Chapter %s <abstract_data_types>` were all fairly simple sequences of objects that
were extensible in different ways. If that were all the sum total of abstract
data types then the reader might reasonably wonder what all the fuss is about.
In this chapter we'll look at :term:`trees <tree>` and :term:`directed acyclic
graphs (DAGs) <directed acyclic graph>`, which are abstract data types which
look very different from the ones we've met so far. 

Trees and DAGs provide some great examples of :term:`inheritance` and give us
the chance to look at some new algorithm types. They are also the core data
types underpinning computer algebra systems, so studying trees and DAGs will
enable us to gain a little insight into how systems such as `SymPy
<https://www.sympy.org>`__, `Maple <https://www.maplesoft.com>`__ and
`Mathematica <https://www.wolfram.com/mathematica/>`__ actually work. As we come
to the latter parts of the course, we'll also step back a little from laying out
a lot of code, and instead focus on the mathematical structure of the objects in
question. When we come to the exercises, you will then take a little more
responsibility for translating the maths into code.

Some definitions
----------------

Trees and DAGs are examples of graphs, a type of mathematical object that you
may have met in previous courses:

.. proof:definition:: Graph

    A *graph* :math:`(V, E)` is a set :math:`V` known as the vertices or nodes,
    and a set of pairs of vertices, :math:`E`, known as the edges. 

A graph describes connections between its vertices, and can be used to model a
huge range of interconnected networks. :numref:`graph` illustrates a simple example.

.. _graph:

.. graphviz::
    :caption: A graphical representation of the graph :math:`(\{a, b, c, d, e,
        f\}, \{(a, b), (a, d), (a, f), (b, c), (b, d), (b, f), (c, e), (c, f), (d, e) \})`
    :align: center

    strict graph{
        a -- b
        b -- c
        b -- d
        c -- f
        f -- b
        d -- a
        f -- a
        e -- c
        e -- d    
    }

.. proof:definition:: Directed graph

    A *directed graph* is a graph in which the edges have a direction associated
    with them. In other words each edge point *from* one node (the *source*)
    and *to* another (the *target*).

:numref:`digraph` shows a directed graph with similar topology to the previous example.

.. _digraph:

.. graphviz::
    :caption: A directed graph. The edges in red depict a cycle.
    :align: center

    strict digraph{
        a -> b [color=red]
        b -> c
        b -> d [color=red]
        c -> f
        f -> b
        d -> a [color=red]
        f -> a
        e -> c
        e -> d    
    }

.. proof:definition:: Cycle

    A *cycle* in a graph is a sequence of edges such that the target of each
    edge is the source of the next, and the target of the last edge is the
    source of the first.

.. proof:definition:: Directed acyclic graph.

    A directed acyclic graph (DAG) is a directed graph in which there are no cycles.

:numref:`dag` shows a directed acyclic graph, or DAG. The cyclic nature of the
graph imposes a certain form of hierarchy. For example the graph formed by the
:term:`inheritance` relationship of classes is a DAG. The hierarchy implied by a
DAG also lends itself to similar nomenclature to that which we use for class
hierarchies: the source node of an edge is also referred to as the *parent node*
and the target nodes of the edges emerging from a node are referred to as its
*child nodes* or *children*.

.. _dag:

.. graphviz::
    :caption: A directed acyclic graph, formed by reversing edges in
        :numref:`digraph` so that no cycles remain.
    :align: center

    strict digraph{
        a -> b 
        b -> c
        b -> d 
        c -> f
        b -> f
        a -> f 
        e -> c
        e -> d    
    }

.. proof:definition:: Tree

    A *tree* is a directed acyclic graph in which each node is the target of
    exactly one edge, except for one node (the *root node*) which is not the
    target of any edges [#tree_def]_.

.. _tree_image:

.. graphviz::
    :caption: A tree.
    :align: center

    strict digraph{
        a -> b 
        b -> d
        b -> e 
        b -> f
        a -> c
        c -> g 
    }

Tree nodes with no children are called *leaf nodes*.

Tree traversal
--------------

Unlike the sequence types we have previously met, trees are not linear objects.
If we wish to iterate through every node in the tree then we have a choices to
make about the order in which we do so. In particular, there are two obvious
classes of traversal order:

preorder traversal
    A traversal in which each node is always visited *before* its children. 

postorder traversal
    A traversal order in which each node is always visited *after* its children.

Note that neither order is unique: a node can have any number of children and
the definitions are silent on the order in which these are visited. There is
furthermore no guarantee that the children of a node will be visited immediately
before or after their parent, and once we look at visitors for DAGs it will
become apparent that it is not always possible to do so.

.. _treenode:

.. code-block:: python3
    :caption: A basic tree implementation. This code is available as the
        :class:`example_code.graphs.TreeNode` class.
    :linenos:

    class TreeNode:
        '''A basic tree implementation.

        Observe that a tree is simply a collection of connected TreeNodes.'''
        def __init__(self, value, *children):
            '''
            Parameters
            ----------
            value:
                An arbitrary value associated with this node.
            children:
                The TreeNodes which are the children of this node.
            '''
            self.value = value
            self.children = tuple(children)

        def __repr__(self):
            return f"{self.__class__.__name__}{(self.value,) + self.children}"

        def __str__(self):
            childstring = ", ".join(map(str, self.children))
            return f"{self.value!s} -> ({childstring})"

:numref:`treenode` shows a very simple class which implements a tree. For
example, we can represent the tree in :numref:`tree_image` using:

.. code-block:: ipython3

    In [1]: from example_code.graphs import TreeNode

    In [2]: tree = TreeNode("a", TreeNode("b", TreeNode("d"), TreeNode("e"), TreeNode("f")),
       ...:                      TreeNode("c", TreeNode("g")))

    In [3]: print(tree)
    a -> (b -> (d -> (), e -> (), f -> ()), c -> (g -> ()))

The reader might immediately observe that serialised trees can be a little hard
to read! This is the reason that trees are often represented by diagrams.

The splat and double splat operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before we go on to traverse the tree we have created, we need to digress ever so
slightly in order to explain a new piece of syntax. At line 5 of
:numref:`treenode`, the second parameter to
:meth:`~example_code.graphs.TreeNode.__init__` is given as `*children`. The
character `*` in this case is the argument packing operator, also known as the
*splat* operator [#splat]_. When used in the parameter list of a function, splat takes all
of the remaining :term:`positional arguments <argument>` provided by
the caller and packs them up in a tuple. In this case, this enables any number
of child nodes to be specified for each node. 

The splat operator can also be used when calling a function. In that case it
acts as a sequence unpacking operator, turning a sequence into separate
arguments. For example:

.. code-block:: ipython3

    In [1]: a = (1, 2, 3)

    In [2]: print(*a)
    1 2 3

which is identical to:

.. code-block:: ipython3

    In [3]: print(1, 2, 3)
    1 2 3

but different from: 

.. code-block:: ipython3

    In [4]: print(a)
    (1, 2, 3)

The double splat operator, `**` plays a similar role to the single splat
operator, but packs and unpacks :term:`keyword arguments <argument>` instead of
positional arguments. When used in the :term:`parameter` list of a function,
`**` gathers all of the keyword arguments that the caller passes, other than any
which are explicitly named in the interface. The result is a :class:`dict` whose
keys are the argument names, and whose values are the arguments.
:numref:`kwarg_packing` demonstrates the argument packing function of `**`,
while :numref:`kwarg_unpacking` shows the unpacking function.

.. _kwarg_packing:

.. code-block:: ipython3
    :caption: An illustration of keyword argument packing. All of the keyword
        arguments are packed into the dictionary :data:`kwargs`, except for `b`,
        because that explicitly appears in the parameter list of :func:`fn`.

    In [1]: def fn(a, b, **kwargs):
    ...:     print("a:", a)
    ...:     print("b:", b)
    ...:     print("kwargs:", kwargs)
    ...: 

    In [2]: fn(1, f=3, b=2, g="hello")
    a: 1
    b: 2
    kwargs: {'f': 3, 'g': 'hello'}

.. _kwarg_unpacking:

.. code-block:: ipython3
    :caption: Keyword argument unpacking. Notice that the arguments matching the
        explicitly named keywords are unpacked, while the remainder are repacked
        into the `**kwargs` parameter.

    In [3]: kw = {"a": "mary", "b": "had", "c": "a", "d": "little", "e": "lamb"}

    In [4]: fn(**kw)
    a: mary
    b: had
    kwargs: {'c': 'a', 'd': 'little', 'e': 'lamb'}

Traversing :class:`~example_code.graphs.TreeNode`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function which traverses a tree is often called a tree visitor, because it
visits every node in the tree. What does it do when it visits? Well it could do
just about anything that one can do on the basis of the data available at that
node, and the results of visiting whichever nodes have already been visited. The
way that such a wide range of options can be accommodated is by the tree
traversal function taking another function as an argument. This enables the
caller to specify what should happen when each node is visited. An approach like
this is a good example of a :term:`separation of concerns`: the process of
visiting a tree in the correct order is separated from the question of what to
do when we get there. 

We'll consider postorder traversal first, as it's the easier to implement.

.. _postorder_recursive:

.. code-block:: python3
    :caption: A basic postorder tree visitor. This code is also available as
        :func:`example_code.graphs.postvisitor`.
    :linenos:

    def postvisitor(tree, fn):
        '''Traverse tree in postorder applying a function to every node.

        Parameters
        ----------
        tree: TreeNode
            The tree to be visited.
        fn: function(node, *fn_children)
            A function to be applied at each node. The function should take the
            node to be visited as its first argument, and the results of visiting
            its parent as any further arguments.
        '''

        return fn(tree, *(postvisitor(c, fn) for c in tree.children))

:numref:`postorder_recursive` implements this visitor. Notice that there is only
one line of executable code, at line 14. This recursively calls
:func:`~example_code.graphs.postvisitor` on all of the children of the current
node, *before* calling :func:`fn` on the current node. As a trivial example,
let's print out the nodes of the graph in :numref:`tree_image` in postorder:

.. code-block:: ipython3

    In [1]: from example_code.graphs import TreeNode, postvisitor

    In [2]: tree = TreeNode("a", TreeNode("b", TreeNode("d"), TreeNode("e"), TreeNode("f")),
       ...:                      TreeNode("c", TreeNode("g")))

    In [3]: fn = lambda n, *c: print(n.value)

    In [4]: postvisitor(tree, fn)
    d
    e
    f
    b
    g
    c
    a

Observe that d, e, and f are printed before b; g is printed before c; and both b
and c are printed before a. 

The preceding example is possibly a little too trivial,
because we didn't at all use the result of visiting the child nodes in visiting
the parent node. For a marginally less trivial case, let's count the number of
nodes in the tree:

.. code-block:: ipython3

    In [5]: fn = lambda n, *c: sum(c) + 1

    In [6]: postvisitor(tree, fn)
    Out[6]: 7

This time the visitor :func:`sums <sum>` the results from its children, and adds
one for itself. 

What about preorder traversal? This time we need a little more code (not much)
as :numref:`preorder_recursive` shows.

.. preorder_recursive

.. code-block:: python3
    :caption: The simple preorder visitor from
        :func:`example_code.graphs.previsitor`.
    :linenos:

    def previsitor(tree, fn, fn_parent=None):
        '''Traverse tree in preorder applying a function to every node.

        Parameters
        ----------
        tree: TreeNode
            The tree to be visited.
        fn: function(node, fn_parent)
            A function to be applied at each node. The function should take the
            node to be visited as its first argument, and the result of visiting
            its parent as the second.
        '''

        fn_out = fn(tree, fn_parent)

        for child in tree.children:
            previsitor(child, fn, fn_out)

What can we do with a preorder traversal? Well one thing is that we can measure
the depth in the tree of every node:

.. code-block:: ipython3

    In [7]: from example_code.graphs import previsitor

    In [8]: def fn(node, p):
       ...:     depth = p + 1 if p else 1
       ...:     print(f"{node.value}: {depth}")
       ...:     return depth
       ...: 

    In [9]: previsitor(tree, fn)
    a: 1
    b: 2
    d: 3
    e: 3
    f: 3
    c: 2
    g: 3

Observe here that the node visitor order is different from the postvisitor, and
that we successfully diagnosed the depth of each node.

Expression trees
----------------

One important application of trees is in representing arithmetic expressions.
Consider the expression :math:`2y + 4^{(5 + x)}`. Suppose, further, that
we want to represent this on a computer in such a way that we can perform
mathematical operations: evaluation, differentiation, expansion, and
simplification. How would we do this? Well, thanks to the rules for order of
operations, this expression forms a hierarchy from the operators to be evaluated
first, down to the last one. :numref:`expr_tree` shows a tree representation for
our mathematical expression. The evaluation rule for trees of this type is a
postorder traversal, first the leaf nodes are evaluated, then their parents and
so on up until finally the addition at the root node is evaluated.

.. _expr_tree:

.. graphviz::
    :caption: Expression tree for the expression :math:`2y + 4^{(5 + x)}`.

    strict digraph{
        a [label="+"];
        b [label="⨉"];
        c [label="pow"];
        2;
        y [font="italic"];
        a->b
        a->c
        b->{2 y}
        c->4
        d[label="+"]
        c->d
        d->5
        x [font="italic"]
        d->x   
    }

We will first consider how to construct trees like this, then consider the
question of the operations we could implement on them.

An expression tree class hierarchy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The nodes of an expression tree don't just have different values, they have
different :term:`type`. That is to say, the meaning of operations changes
between, say :math:`+` and :math:`2`. For example the evaluation rule for these
nodes will be different, as will the differentiation rule. At the same time, all
the nodes are still expressions and will share many common features. This is a
textbook case of inheritance. There should be a most general class, covering all
types of expression nodes, and then more specialised node types should inherit
from this. The most basic distinction is between *operators*, which have at least
one operand (represented by a child node), and *terminals*, which have no
children. In practice, it will result in simpler, more elegant code if terminals
actually have an empty tuple of operands rather than none at all. This
facilitates writing, for example, tree visitors which loop over all of the
children of a node.

.. graphviz::
    :caption: Inheritance diagram for a very basic symbolic language. Each box
        represents a class, with the arrows showing inheritance relationships. Note that
        the edges in such diagrams conventionally point from the child class to the
        parent class, because its the child class that refers to the parent. The
        parent does not refer to the child.

    strict digraph{
        node [
            shape = "record"
            ]
        
        edge [
            arrowtail = "empty";
            dir = "back";
            ]
        
        Expression -> Terminal
        Terminal -> Number
        Terminal -> Symbol
        
        Expression -> Operator
        Operator -> Add
        Operator -> Mul
        Operator -> Sub
        Operator -> Div
        Operator -> Pow
    }

Let's consider what would be needed at each layer of the hierarchy.
:class:`Expression` should implement everything that is the same for all nodes. What
will that comprise? 

:meth:`__init__`
    The constuctor will take a :class:`tuple` of operands, since every
    expression has operands (even if terminals have zero operands).

:meth:`~object.__add__`, :meth:`~object.__sub__`, :meth:`~object.__mul__`, :meth:`~object.__truediv__`, :meth:`~object.__pow__`  
    Implementing the special methods for arithmetic is necessary for expressions
    to exhibit the correct symbolic mathematical behaviour. We met this idea
    already in :numref:`object_arithmetic`. Arithmetic operations involving
    symbolic expressions return other symbolic expressions. For example if `a`
    and `b` are expressions then `a + b` is simply `Add(a, b)`. The fact that
    these rules are the same for all expressions indicates that they should be
    implemented on the base class :class:`Expression`. 
    
    Just as was the case when we implemented the
    :class:`~example_code.polynomial.Polynomial` class, it will be necessary to
    do something special when one of the operands is a number. In this case, the
    right thing to do is to turn the number into an expression by instantiating a
    :class:`Number` with it as a value. Once this has been done, the number is
    just another :class:`Expression` obeying the same arithmetic rules as other
    expressions.
    
Let's now consider :class:`Operator`. The operations for creating string
representations can be implemented here, because they will be the same for all
operators but different for terminals. 

:meth:`~object.__repr__`
    Remember that this is the canonical string representation, and is usually
    the code that could be passed to the :term:`Python interpreter` to construct
    the object. Something like the following would work:

    .. code-block:: python3
    
        def __repr__(self):
            return self.__class__.__name__ + repr(self.operands)

    This approch is valid because the string representation of a :class:`tuple`
    is a pair of round brackets containing the string representation of each
    item in the tuple.

:meth:`~object.__str__`
    This is the human-readable string output, using :term:`infix` operators, so
    in the example above we would expect to see `2*y + 4^(5 + x)` This looks
    sort of straightforward, simply associate the correct symbol with each
    operator class as a :term:`class attribute` and place the string
    representation of the operands on either side. 
    
    The challenge is to correctly include the brackets. In order to do this, it
    is necessary to associate with every expression class a :term:`class
    attribute` whose value is a number giving an operator precedence to that
    class. For example, the priority of :class:`Mul` should be higher than
    :class:`Add`. A full list of operators in precedence order is available in
    :ref:`the official Python documentation <operator-summary>`. An operand
    :math:`a` of an operator :math:`o` needs to be placed in brackets if the
    precedence of :math:`a` is lower than the precedence of :math:`o`.

Individual operator classes therefore need to define very little, just two
:term:`class attributes`, one for the operator precedence, and one to set the
symbol when printing the operator.

Let's now consider :class:`Terminal`. What does it need to set?

:meth:`~object.__init__`
    The :term:`constructor` for :class:`Expression` assumes that an expression is
    defined by a series of operands. Terminals have an empty list of operands
    but do have something that other expressions lack, a value. In the case of
    :term:`Number`, this is a number, while for :term:`Symbol` the value is a
    string (usually a single character). :class:`Terminal` therefore needs its
    own :meth:`__init__` which will take a value argument.
    :class:`Terminal.__init__` still has to call the :term:`superclass`
    constructor in order to ensure that the operands tuple is initialised.

:meth:`~object.__repr__` and :meth:`~object.__str__`
    The string representations of :class:`Terminal` are straightforward, simply
    return `repr(self.value)` and `str(self.value)` respectively. Note that in
    order for  :meth:`Operator.__str__` to function correctly, :class:`Terminal`
    will need to advertise its operator precedence. The reader should think
    carefully about what the precedence of a :class:`Terminal` should be.

The two :class:`Terminal` subclasses need to do very little other than identify
themselves. The only functionality they might provide would be to override
:meth:`~object.__init__` to check that their value is a :class:`numbers.Number`
in the case of :class:`Number` and a :class:`str` in the case of :class:`Symbol`.

Operations on expression trees
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many operations on expression trees can be implemented using tree visitors, most
frequently by visiting the tree in postorder. An example is
expression evaluation. The user provides a :class:`dict` mapping symbol names to
numerical values, and we proceed from leaf nodes upwards. Every :class:`Symbol`
is replaced by a numerical value from the dictionary, every :class:`Number`
stands for itself, and every :class:`Operator` performs the appropriate
computation on its operands (which are now guaranteed to be numbers). 

The leaf-first order of execution makes this a postorder tree visitor, but what
is the visitor function? It seems we need a different function for every
:class:`type` of expression node we encounter. It turns out that this is exactly
what is required, and Python provides this functionality in the form of the
single dispatch function.

Single dispatch functions
~~~~~~~~~~~~~~~~~~~~~~~~~

In all of the cases we have encountered so far, there is a unique mapping from
the name of a function to the code implementing that function. That is, no
matter what arguments are passed to a function, the same code will execute (so
long as the right number of arguments are passed). A single dispatch function is
not like this. Instead, calling a single function name causes different function
code to execute, depending on the type of the first argument [#single]_.

Let's construct a single dispatch function to evaluate a :class:`Expression`.
The first step is to define what the function should do in the case where we
know nothing about the class of the object we are evaluating.

.. code-block:: python3
    :caption: A :term:`single dispatch function` implementing the evaluation of
        a single :class:`Expression` node. The implementation of the expressions
        language itself, in the :mod:`expressions` module is :ref:`left as an
        exercise <ex_expr>`.
    :linenos:

    from functools import singledispatch
    import expressions


    @singledispatch
    def evaluate(expr, *o, map={}):
        raise NotImplementedError(
            f"Cannot evaluate a {type(expr).__name__}")


    @evaluate.register(expressions.Number)
    def _(expr, *o, map={}):
        return expr.value


    @evaluate.register(expressions.Symbol)
    def _(expr, *o, map={}):
        return map[expr.value]


    @evaluate.register(expressions.Add)
    def _(expr, *o, map={}):
        return o[0] + o[1]


    @evaluate.register(expressions.Sub)
    def _(expr, *o, map={}):
        return o[0] - o[1]


    @evaluate.register(expressions.Mul)
    def _(expr, *o, map={}):
        return o[0] * o[1]


    @evaluate.register(expressions.Div)
    def _(expr, *o, map={}):
        return o[0] / o[1]


    @evaluate.register(expressions.Pow)
    def _(expr, *o, map={}):
        return o[0] ** o[1]




Expressions as :term:`DAGs <DAG>`
---------------------------------

Glossary
--------

 .. glossary::
    :sorted:
    
    directed acyclic graph
    DAG
        A :term:`graph` in which the edges are directed (i.e. the edges point from
        one vertex to another) and where there are no cycles of edges.

    graph
        An :term:`abstract data type` comprising a set of nodes or vertices
        :math:`V` and a set of edges :math:`E` each of which connects two vertices.

    tree
        A :term:`directed acyclic graph` in which every vertex is the target of at
        most one edge.


Exercises
---------

.. _ex_expr:

.. proof:exercise::

    .. note::

        Get the student to implement the expressions language.

.. rubric:: Footnotes

.. [#tree_def] This definition of a tree matches computer science usage and is
    the relevant one for the applications we will study. There is a slightly
    different definition of a tree common in mathematical graph theory.

.. [#splat] Python language pedants will observe that strictly speaking neither
    `*` nor `**` are operators, and that they are simply an unnamed syntax for
    argument packing and unpacking. This is both correct and unhelpful, since it
    is useful in many contexts to be able to give a name to the `*` and `**`
    symbols when used in this way.

.. [#single] The *single* in *single dispatch* indicates that the
    choice of function implementation is made on the basis of the type of one
    argument, typically the first. Multiple dispatch, in which the function
    implementation is chosen on the basis of multiple function arguments, is
    also possible, and is a key feature of `the Julia programming language
    <https://julialang.org>`_. 