from numbers import Integral
import numpy as np


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
        if not (isinstance(value, Integral) and 0 <= value < self.order):
            raise ValueError("Element value must be an integer"
                             f" in the range [0, {self.order})")

    def operation(self, a, b):
        return (a + b) % self.order

    def __call__(self, value):
        '''Provide a convenient way to create elements of this group.'''
        return Element(self, value)

    def __str__(self):
        return f"C{self.order}"

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.order)})"


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
