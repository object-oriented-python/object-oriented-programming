.. _trees:

Trees and directed acyclic graphs
=================================

The :term:`abstract data types <abstract data type>` that we met in
:numref:`Week %s <abstract_data_types>` were all fairly simple sequences of objects that
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

The splat and double splat operators
------------------------------------

.. dropdown:: Video: splat and double splat.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/523477744"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=2cb93382-321b-4af6-8d5e-aceb0123103d>`__.


Before we go on to write code for trees and their traversal,  we need to
digress ever so slightly in order to explain a new piece of syntax. We're going
to want to write  functions that can take a variable number of arguments. For
example, we're going to want the :term:`constructor` of a tree node object to
be able to take a variable number of children. We can do this by writing the
relevant parameter as `*children`. The character `*` in this case is the
argument packing operator, also known as the *splat* operator [#splat]_. When
used in the parameter list of a function, splat takes all of the remaining
:term:`positional arguments <argument>` provided by the caller and packs them
up in a tuple. In this case, this enables any number of child nodes to be
specified for each node. 

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

Combining the splat and double splat operators, it is possible to write a
function that will accept any combination of positional and keyword arguments.
This is often useful if the function is intended to pass these arguments through
to another function, without knowing anything about that inner function. For
example:

.. code-block:: python3

    def fn(*args, **kwargs):
        ...
        a =  inner_fn(*args, **kwargs)
        ...

The names `*args` and `**kwargs` are the conventional names in
cases where nothing more specific is known about the parameters in question.


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

    A *directed graph* is a graph in which the pair of nodes forming each edge
    is ordered. In other words each edge points *from* one node (the *source*)
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

Data structures for trees
-------------------------

.. dropdown:: Tree data structures.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/523477713"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5477e1b1-1040-4a07-97a5-aceb01230fc6>`__.

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
        """A basic tree implementation.

        Observe that a tree is simply a collection of connected TreeNodes.

        Parameters
        ----------
        value:
            An arbitrary value associated with this node.
        children:
            The TreeNodes which are the children of this node.
        """

        def __init__(self, value, *children):
            self.value = value
            self.children = tuple(children)

        def __repr__(self):
            """Return the canonical string representation."""
            return f"{type(self).__name__}{(self.value,) + self.children}"

        def __str__(self):
            """Serialise the tree recursively as parent -> (children)."""
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

Traversing :class:`~example_code.graphs.TreeNode`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: Video: tree traversal.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/523477719"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=69b00d45-077d-46ff-933c-aceb01231001>`__.

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
        """Traverse tree in postorder applying a function to every node.

        Parameters
        ----------
        tree: TreeNode
            The tree to be visited.
        fn: function(node, *fn_children)
            A function to be applied at each node. The function should take the
            node to be visited as its first argument, and the results of visiting
            its children as any further arguments.
        """
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

.. _preorder_recursive:

.. code-block:: python3
    :caption: The simple preorder visitor from
        :func:`example_code.graphs.previsitor`.
    :linenos:

    def previsitor(tree, fn, fn_parent=None):
        """Traverse tree in preorder applying a function to every node.

        Parameters
        ----------
        tree: TreeNode
            The tree to be visited.
        fn: function(node, fn_parent)
            A function to be applied at each node. The function should take the
            node to be visited as its first argument, and the result of visiting
            its parent as the second.
        """
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

.. _expr_trees:

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
        c [label="^"];
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

.. _expr_hierarchy:

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
        parent class, because it's the child class that refers to the parent. The
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
    The constructor will take a :class:`tuple` of operands, since every
    expression has operands (even if terminals have zero operands).

:meth:`~object.__add__`, :meth:`~object.__sub__`, :meth:`~object.__mul__`, :meth:`~object.__truediv__`, :meth:`~object.__pow__`  
    Implementing the :term:`special methods <special method>` for arithmetic is
    necessary for expressions to exhibit the correct symbolic mathematical
    behaviour. We met this idea already in :numref:`object_arithmetic`.
    Arithmetic operations involving symbolic expressions return other symbolic
    expressions. For example if `a` and `b` are expressions then `a + b` is
    simply `Add(a, b)`. The fact that these rules are the same for all
    expressions indicates that they should be implemented on the base class
    :class:`Expression`. 
    
    Just as was the case when we implemented the
    :class:`~example_code.polynomial.Polynomial` class, it will be necessary to
    do something special when one of the operands is a number. In this case, the
    right thing to do is to turn the number into an expression by instantiating a
    :class:`Number` with it as a value. Once this has been done, the number is
    just another :class:`Expression` obeying the same arithmetic rules as other
    expressions. The need to accommodate operations between symbolic expressions
    and numbers also implies that it will also be necessary to implement the
    :term:`special methods <special method>` for reversed arithmetic operations.
    
Let's now consider :class:`Operator`. The operations for creating string
representations can be implemented here, because they will be the same for all
operators but different for terminals. 

:meth:`~object.__repr__`
    Remember that this is the canonical string representation, and is usually
    the code that could be passed to the :term:`Python interpreter` to construct
    the object. Something like the following would work:

    .. code-block:: python3
    
        def __repr__(self):
            return type(self).__name__ + repr(self.operands)

    This approch is valid because the string representation of a :class:`tuple`
    is a pair of round brackets containing the string representation of each
    item in the tuple.

:meth:`~object.__str__`
    This is the human-readable string output, using :term:`infix operators
    <infix operator>`, so in the example above we would expect to see 
    `2 * y + 4 ^ (5 + x)` This looks sort of straightforward, simply associate the correct
    symbol with each operator class as a :term:`class attribute` and place the
    string representation of the operands on either side. 
    
    The challenge is to correctly include the brackets. In order to do this, it
    is necessary to associate with every expression class a :term:`class
    attribute` whose value is a number giving an operator precedence to that
    class. For example, the precedence of :class:`Mul` should be higher than
    :class:`Add`. A full list of operators in precedence order is available in
    :ref:`the official Python documentation <operator-summary>`. An operand
    :math:`a` of an operator :math:`o` needs to be placed in brackets if the
    precedence of :math:`a` is lower than the precedence of :math:`o`.

Individual operator classes therefore need to define very little, just two
:term:`class attributes <class attribute>`, one for the operator precedence, and
one to set the symbol when printing the operator.

Let's now consider :class:`Terminal`. What does it need to set?

:meth:`~object.__init__`
    The :term:`constructor` for :class:`Expression` assumes that an expression is
    defined by a series of operands. Terminals have an empty list of operands
    but do have something that other expressions lack, a value. In the case of
    :class:`Number`, this is a number, while for :class:`Symbol` the value is a
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

.. dropdown:: Video: evaluating expressions.

    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/523478799"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto
    <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=88f9564a-73c9-4760-8f48-aceb01230f9b>`__.

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

.. _tree_evaluate:

.. code-block:: python3
    :caption: A :term:`single dispatch function` implementing the evaluation of
        a single :class:`Expression` node. The implementation of the expressions
        language itself, in the :mod:`expressions` module is :ref:`left as an
        exercise <ex_expr>`.
    :linenos:

    from functools import singledispatch
    import expressions


    @singledispatch
    def evaluate(expr, *o, **kwargs):
        """Evaluate an expression node.

        Parameters
        ----------
        expr: Expression
            The expression node to be evaluated.
        *o: numbers.Number
            The results of evaluating the operands of expr.
        **kwargs:
            Any keyword arguments required to evaluate specific types of expression.
        symbol_map: dict
            A dictionary mapping Symbol names to numerical values, for example:

            {'x': 1}
        """
        raise NotImplementedError(
            f"Cannot evaluate a {type(expr).__name__}")
    

    @evaluate.register(expressions.Number)
    def _(expr, *o, **kwargs):
        return expr.value


    @evaluate.register(expressions.Symbol)
    def _(expr, *o, symbol_map, **kwargs):
        return symbol_map[expr.value]


    @evaluate.register(expressions.Add)
    def _(expr, *o, **kwargs):
        return o[0] + o[1]


    @evaluate.register(expressions.Sub)
    def _(expr, *o, **kwargs):
        return o[0] - o[1]


    @evaluate.register(expressions.Mul)
    def _(expr, *o, **kwargs):
        return o[0] * o[1]


    @evaluate.register(expressions.Div)
    def _(expr, *o, **kwargs):
        return o[0] / o[1]


    @evaluate.register(expressions.Pow)
    def _(expr, *o, **kwargs):
        return o[0] ** o[1]

:numref:`tree_evaluate` shows a single dispatch function for a visitor function
which evaluates a :class:`Expression`. Start with lines 6-19. These define a
function :func:`~example_code.expression_tools.evaluate` which will be used in
the default case, that is, in the case where the :class:`type` of the first
argument doesn't match any of the other implementations of
:func:`~example_code.expression_tools.evaluate`. In this case, the first
argument is the expression that we're evaluating, so if the type doesn't match
then this means that we don't know how to evaluate this object, and the only
course of action available is to throw an :term:`exception`.

The new feature that we haven't met before appears on line 5.
:func:`functools.singledispatch` turns a function into
a single dispatch function. The `@` symbol marks
:func:`~functools.singledispatch` as a :term:`decorator`. We'll return to them
in :numref:`decorators`. For the moment, we just need to know that
`@singledispatch` turns the function it precedes into a single dispatch
function.

Next we turn our attention to the implementation of evaluation for the different
expression types. Look first at lines 26-28, which provide the evaluation of
:class:`Number` nodes. The function body is trivial: the evaluation of a
:class:`Number` is simply its value. The function interface is more interesting.
Notice that the function name is given as `_`. This is the Python convention for
a name which will never be used. This function will never be called by its
declared name. Instead, look at the decorator on line 26. The single dispatch
function :func:`~example_code.expression_tools.evaluate` has a :term:`method`
:meth:`register`. When used as a decorator, the :meth:`register` method of a
single dispatch function registers the function that follows as implementation
for the :keyword:`class` given as an argument to :meth:`register`. On this
occasion, this is :class:`expressions.Number`.

Now look at lines 31-33. These contain the implementation of
:func:`~example_code.expression_tools.evaluate` for :class:`expressions.Symbol`.
In order to evaluate a symbol, we depend on the mapping from symbol names to
numerical values that has been passed in. 

Finally, look at lines 36-38. These define the evaluation visitor for addition.
This works simply by adding the results of evaluating the two operands of
:class:`expressions.Add`. The evaluation visitors for the other operators follow
*mutatis mutandis*.

An expanded tree visitor
~~~~~~~~~~~~~~~~~~~~~~~~

The need to provide the `symbol_map` parameter to the
:class:`expressions.Symbol` evaluation visitor means that the postorder visitor
in :numref:`postorder_recursive` is not quite up to the task.
:numref:`postorder_recursive_kwargs` extends the tree visitor to pass arbitrary
keyword arguments through to the visitor function.

.. _postorder_recursive_kwargs:

.. code-block:: python3
    :caption: A recursive tree visitor that passes any keyword arguments
        through to the visitor function. This is available as 
        :func:`example_code.expression_tools.post_visitor`. We also account 
        for the name changes between :class:`~example_code.graphs.TreeNode` 
        and :class:`Expression`.
    :linenos:

    def postvisitor(expr, fn, **kwargs):
        '''Traverse an Expression in postorder applying a function to every node.

        Parameters
        ----------
        expr: Expression
            The expression to be visited.
        fn: function(node, *o, **kwargs)
            A function to be applied at each node. The function should take the
            node to be visited as its first argument, and the results of visiting
            its operands as any further positional arguments. Any additional
            information that the visitor requires can be passed in as keyword
            arguments.
        **kwargs:
            Any additional keyword arguments to be passed to fn.
        '''
        return fn(expr,
                  *(postvisitor(c, fn, **kwargs) for c in expr.operands),
                  **kwargs)


Assuming we have an implementation of our simple expression language, we are now
in a position to try out our expression evaluator:

.. code-block:: ipython3

    In [1]: from expressions import Symbol

    In [2]: from example_code.expression_tools import evaluate, postvisitor

    In [3]: x = Symbol('x')

    In [4]: y = Symbol('y')

    In [5]: expr = 3*x + 2**(y/5) - 1

    In [6]: print(expr)
    3 ⨉ x + 2 ^ (y / 5) - 1

    In [7]: postvisitor(expr, evaluate, symbol_map={'x': 1.5, 'y': 10})
    Out[7]: 7.5

Avoiding recursion
------------------

The recursive tree visitors we have written require very few lines of code, and
very succinctly express the algorithm they represent. However, in most
programming languages (including Python), recursion is a relatively inefficient
process. The reason for this is that it creates a deep :term:`call stack`
requiring a new :term:`stack frame` for every level of recursion. In extreme
cases, this can exceed Python's limit on recursion depth and result in a
:class:`RecursionError`. 

In order to avoid this, we can think a little more about what a recursive
function actually does. In fact, a recursive function is using the :term:`call
stack` to control the order in which operations are evaluated. We could do the
same using a :term:`stack` to store which tree nodes still need processing.
There are a number of ways to do this, but one particular algorithm emerges if
we wish to be able to represent expressions not only as trees but as more
general :term:`directed acyclic graphs <DAG>`.

Representing expressions as :term:`DAGs <DAG>`
----------------------------------------------

If we treat an expression as a tree, then any repeated subexpressions will be
duplicated in the tree. Consider, for example, :math:`x^2 + 3/x^2`. If we create
a tree of this expression, then :math:`x^2` will occur twice, and any operation
that we perform on :math:`x^2` will have to be done twice. If, on the other hand, we
treat the expression as a more general :term:`directed acyclic graph`, then the
single subexpression :math:`x^2` can have multiple parents, and so can appear as
an operand more than once. :numref:`tree_vs_dag` illustrates this distinction.

.. _tree_vs_dag:

.. graphviz::
    :caption: :term:`Tree <tree>` (left) and :term:`DAG` (right) representations
        of the expression :math:`x^2 + 3/x^2`. Notice that the :term:`DAG`
        representation avoids the duplication of the :math:`x^2` term.

    strict digraph{
        a1 [label="+"]
        pow1 [label="^"]
        x1 [label="x"]
        n1 [label="2"]
        a1 -> pow1
        pow1 -> x1
        pow1 -> n1
        m1 [label="/"]
        n0 [label=3]
        pow2 [label="^"]
        x2 [label="x"]
        n2 [label="2"]
        a1 -> m1
        m1 -> n0
        m1 -> pow2
        pow2 -> x2
        pow2 -> n2

        a3 [label="+", ordering="out"]
        pow3 [label="^"]
        x3 [label="x"]
        n3 [label="2"]
        a3 -> pow3
        
        pow3 -> x3
        pow3 -> n3
        m3 [label="/", ordering="out"]
        n4 [label=3]
        a3 -> m3
        m3 -> n4
        m3 -> pow3

    }

The difference between a tree and a DAG may seem small in the tiny examples we
can print on our page, but realistic applications of computer algebra can easily
create expressions with thousands or tens of thousands of terms, in which larger
common subexpressions themselves contain multiple instances of smaller
subexpressions. The repetition of common terms, and therefore data size and
computational cost, induced by the tree representation is exponential in the
depth of nesting. This can easily make the difference between a computation that
completes in a fraction of a second, and one which takes hours to complete or
which exhausts the computer's memory and therefore fails to complete at all!

Building expression :term:`DAGs <DAG>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using somewhat more complex data structures, it is possible to create
expressions that automatically result in :term:`DAGs <DAG>` rather than
:term:`trees <tree>`.  That is beyond the scope of this course, but we can
construct expression DAGs using our existing tools, at the expense of a little
extra code. Take as an example the expression we used above: :math:`x^2 +
3/x^2`. If we write:

.. code-block:: ipython3

    In [1]: from expressions import Symbol

    In [2]: x = Symbol('x')

    In [3]: expr = x**2 + 3/x**2

then each occurrence of `x**2` creates a separate :class:`Expression` object and
we have a tree. However, if we instead write:

.. code-block:: ipython3

    In [1]: from expressions import Symbol

    In [2]: x = Symbol('x')

    In [3]: x2 = x**2

    In [4]: expr = x2 + 3/x2

then we now have a DAG in which the two occurrences of the :math:`x^2` term
refer to the same `x**2` object.

:term:`DAG` visitors
~~~~~~~~~~~~~~~~~~~~

Even if we represent an expression as a DAG rather than a tree, the simple
recursive tree visitors we have used thusfar will undo all of our good work,
because common subexpressions will be visited via each parent expression, rather
than just once. This compounds the disadvantages of recursive visitors that we
discussed above. Instead, we can construct a postorder DAG visitor using a
:term:`stack` to replace the recursion in keeping track of what to evaluate
next, and a :class:`dict` to record the nodes we have already visited, and the
results of visiting them. :numref:`nonrecursive_postvisit` illustrates one such
algorithm.

.. _nonrecursive_postvisit:

.. code-block:: python3
    :caption: Pythonic :term:`pseudocode` for a non-recursive postorder :term:`DAG` visitor.
    :linenos:

    def visit(expr, visitor):
        stack = []
        visited = {}
        push expr onto stack
        while stack:
            e = pop from stack
            unvisited_children = []
            for o in e.operands:
                if o not in visited:
                    push o onto unvisited_children

            if unvisited_children:
                push e onto stack # Not ready to visit this node yet.
                # Need to visit children before e. 
                push all unvisted_children onto stack
            else:
                # Any children of e have been visited, so we can visit it.
                visited[e] = visitor(e, *(visited(o) for o in e.operands))
        
        # When the stack is empty, we have visited every subexpression,
        # including expr itself.
        return visited[expr]
    
.. note::

    Every operation we have defined on a symbolic mathematical expression
    defined as a :term:`tree` or a :term:`DAG` has produced a new :term:`tree`
    or :term:`DAG` as a result. This matches mathematical convention: operations
    produce new expressions, they don't change their inputs. This is an
    important design principle of symbolic mathematical software. The confusion
    that frequently results from modifying symbolic expressions in-place far
    outweighs any possible advantage of not creating new objects.

Differentiation as an expression visitor
----------------------------------------

In :numref:`expr_trees` we showed how a tree visitor could implement the
evaluation of a symbolic expression. You might very well protest that if the
only thing you wanted to do was evaluate arithmetic expressions then you could
have just written a Python function and avoided a lot of code. In fact, almost
any algebraic manipulation that you could conduct with pen and paper can be
automated using expression visitors. We will illustrate this by sketching how
differentiation can be achieved using a visitor function.

Let's first consider terminals. Numbers are easy: the derivative of any number
with respect to any symbol is simply 0. Symbols are nearly as straightforward.
The derivative of a symbol with respect to itself is 1, while the derivative of
a symbol with respect to any other symbol is 0. Because terminals have no
operands, the implementation of differentiation when visiting a terminal is
particularly easy. Note that the symbol with respect to which we are
differentiating will need to be passed in to the visitor. This can be achieved
with a keyword argument in a manner analogous to `tree_map` in
:numref:`tree_evaluate`.

The differentiation of operators is achieved by an applying the chain rule. For
a binary operator :math:`\odot`, with operands :math:`o_0` and :math:`o_1`, the
chain rule is given by:

.. math::
    :label:

    \frac{\partial\, (o_0 \odot o_1)}{\partial x} = 
    \frac{\partial o_0}{\partial x} \frac{\partial\, (o_0 \odot o_1)}{\partial o_0}
    + \frac{\partial o_1}{\partial x} \frac{\partial\, (o_0 \odot o_1)}{\partial o_1}

For example if the operator is multiplication, then:

.. math::
    :label:

    \frac{\partial\, o_0 o_1}{\partial o_0} = o_1

and the product rule follows immediately. Similarly, the sum and quotient
rules for differentiation are simply special cases of the chain rule. This means
that the particular implementation of differentiation for a given
:class:`Operator` subclass simply encodes the version of the chain rule for that
operator. This will require the original operands to the operator, which are
available from the operator object itself, and the results of differentiating
the operands, which are given by the `*o` argument to the visitor function.

Glossary
--------

.. glossary::
    :sorted:
    
    child node
        The children of a node in a :term:`DAG` are the targets of the edges
        emerging from that node. In this context, the node from which these
        edges emanate is called the :term:`parent node`.

    directed acyclic graph
    DAG
        A :term:`graph` in which the edges are directed (i.e. the edges point from
        one vertex to another) and where there are no cycles of edges.

    edge
        A connection between two nodes in a :term:`graph`. In a directed graph,
        the edges have an orientation, from a source node to a target node.

    graph
        An :term:`abstract data type` comprising a set of nodes or vertices
        :math:`V` and a set of edges :math:`E` each of which connects two vertices.

    tree
        A :term:`DAG` in which every vertex is the target of at
        most one edge.

    graph visitor
        A function which iterates over all of the nodes of a graph, calling
        calling a visitor function for each node. 

    leaf node
        A node in a :term:`DAG` with no :term:`children <child node>`.

    parent node
        From the perspective of a :term:`child node`, the source of an incoming edge.

    preorder traversal
        A :term:`visitor <graph visitor>` for a :term:`DAG` in which each parent
        node is visited *before* its :term:`children <child node>`.

    postorder traversal
        A :term:`visitor <graph visitor>` for a :term:`DAG` in
        which the each parent node is visited *after* its :term:`children <child
        node>`.
 
    root node
        A node in a :term:`DAG` with no :term:`parent <parent node>`.

    single dispatch function
        A function with a single name but multiple implementations. The
        implementation which executes when the function is called is chosen
        based on the :class:`type` of the first argument to the function. The
        :func:`functools.singledispatch` function facilitates the creation of
        single dispatch functions.

Exercises
---------

Obtain the `skeleton code for these exercises from GitHub classroom
<https://classroom.github.com/a/DVDJ8r1y>`__. You should also update your clone
of the course repository to ensure you have the latest version of the
:mod:`example_code` package.

.. _ex_expr:

.. proof:exercise::

    In the skeleton repository for this week, create a :term:`package`
    :mod:`expressions` which implements the class hierarchy in
    :numref:`expr_hierarchy`. When implementing :meth:`~object.__str__`, use the
    symbols `+`, `-`, `*`, `/`, and `^`. The names :class:`Symbol`,
    :class:`Number`, :class:`Add`, :class:`Sub`, :class:`Mul`, :class:`Div`, and
    :class:`Pow` should be directly importable in the :mod:`expressions` :term:`namespace`. 
    
.. proof:exercise::

    Write a function importable as :func:`expressions.postvisitor` with the same
    interface as :numref:`postorder_recursive_kwargs`. Your implementation, however,
    should not be recursive, and should only visit repeated subexpressions once,
    no matter how many times they occur in the expression.

.. proof:exercise::

    Write a :term:`single dispatch function` importable as
    :func:`expressions.differentiate` which has the correct interface to be
    passed to :func:`expressions.postvisitor` or
    :func:`example_code.expression_tools.postvisitor` and which differentiates the
    expression provided with respect to a symbol whose name is passed as the
    string :term:`keyword argument <argument>` `var`.

    As a simplification, the tests will assume that `var` does not appear in an
    exponent. As an extension, you could consider that case too, but you'd
    probably need to extend your symbolic language to include the natural
    logarithm as a symbolic function.

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