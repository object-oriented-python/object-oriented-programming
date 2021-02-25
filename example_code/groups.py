from numbers import Integral
import numpy as np


class Element:
    '''An element of the specified group.'''
    def __init__(self, group, value):
        '''
        Parameters
        ----------
        group: Group
            The group of which this is an element.
        value:
            The value of this entity. Valid values depend on the group.
        '''
        group._validate(value)
        self.group = group
        self.value = value

    def __mul__(self, other):
        '''Use * to represent the group operation.'''
        return Element(self.group,
                       self.group.operation(self.value,
                                            other.value))

    def __str__(self):
        """Return a string of the form value_group."""
        return f"{self.value}_{self.group}"

    def __repr__(self):
        """Return the canonical string representation of the element."""
        return f"{type(self).__name__}" \
               f"({repr(self.group), repr(self.value)})"


class Group:
    '''A base class containing methods common to many groups.

    Each subclass represents a family of parametrised groups.'''
    def __init__(self, n):
        '''
        Parameters
        ----------
            n: int
                The primary group parameter, such as order or degree. The
                precise meaning of n changes from subclass to subclass.
        '''
        self.n = n

    def __call__(self, value):
        '''Provide a convenient way to create elements of this group.'''
        return Element(self, value)

    def __str__(self):
        return f"{self.notation}{self.n}"

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.n)})"


class CyclicGroup(Group):
    '''A cyclic group represented by integer addition modulo n.'''
    notation = "C"

    def _validate(self, value):
        '''Ensure that value is a legitimate element value in this group.'''
        if not (isinstance(value, Integral) and 0 <= value < self.n):
            raise ValueError("Element value must be an integer"
                             f" in the range [0, {self.n})")

    def operation(self, a, b):
        '''The group operation is addition modulo n.'''
        return (a + b) % self.n


class GeneralLinearGroup(Group):
    '''The general linear group represented by n x n matrices.'''
    notation = "G"

    def _validate(self, value):
        '''Ensure that value is a legitimate element value in this group.'''
        value = np.asarray(value)
        if not (value.shape == (self.n, self.n)):
            raise ValueError("Element value must be a "
                             f"{self.n} x {self.n}"
                             "square array.")

    def operation(self, a, b):
        '''The group operation is matrix multiplication.'''
        return a @ b
