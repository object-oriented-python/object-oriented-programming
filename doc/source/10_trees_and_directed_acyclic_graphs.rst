.. _trees:

Trees and directed acyclic graphs
=================================

The :term:`abstract data types <abstract data type>` that we met in
:numref:`abstract_data_types` were all fairly simple sequences of objects that
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

The splat operator
~~~~~~~~~~~~~~~~~~

Before we go on to traverse the tree we have created, we need to digress ever so
slightly in order to explain a new piece of syntax. At line 5 of
:numref:`treenode`, the second parameter to
:meth:`~example_code.graphs.TreeNode.__init__` is given as `*children`. The
character `*` in this case is the argument packing operator, also known as the
*splat* operator. When used in the parameter list of a function, splat takes
all of the remaining arguments provided by the caller and packs them up in a
tuple. In this case, this enables any number of child nodes to be specified for
each node. 

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
Consider the expression :math:`2 \times 3 + 4^{(5 + 6)}`.  

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

.. rubric:: Footnotes

.. [#tree_def] This definition of a tree matches computer science usage and is
    the relevant one for the applications we will study. There is a slightly
    different definition of a tree common in mathematical graph theory.