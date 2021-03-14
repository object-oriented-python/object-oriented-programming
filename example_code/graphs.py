"""A simple tree implementation with basic pre- and post-visitors."""


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
