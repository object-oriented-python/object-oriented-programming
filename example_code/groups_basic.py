"""A module implementing the basic functionality of mathematical groups."""

from numbers import Integral
import numpy as np


class Element:
    """An element of the specified group.

    Parameters
    ----------
    group:
        The group of which this is an element.
    value:
        The individual element value.
    """

    def __init__(self, group, value):
        group._validate(value)
        self.group = group
        self.value = value

    def __mul__(self, other):
        """Use * to represent the group operation."""
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


class CyclicGroup:
    """A cyclic group represented by integer addition modulo group order."""

    def __init__(self, order):
        self.order = order

    def _validate(self, value):
        """Ensure that value is a legitimate element value in this group."""
        if not (isinstance(value, Integral) and 0 <= value < self.order):
            raise ValueError("Element value must be an integer"
                             f" in the range [0, {self.order})")

    def operation(self, a, b):
        """Perform the group operation on two values.

        The group operation is addition modulo n.
        """
        return (a + b) % self.order

    def __call__(self, value):
        """Create an element of this group."""
        return Element(self, value)

    def __str__(self):
        """Represent the group as Gd."""
        return f"C{self.order}"

    def __repr__(self):
        """Return the canonical string representation of the group."""
        return f"{type(self).__name__}({repr(self.order)})"


class GeneralLinearGroup:
    """The general linear group represented by degree x degree matrices."""

    def __init__(self, degree):
        self.degree = degree

    def _validate(self, value):
        """Ensure that value is a legitimate element value in this group."""
        if not (isinstance(value, np.ndarray),
                value.shape == (self.degree, self.degree)):
            raise ValueError("Element value must be a "
                             f"{self.degree} x {self.degree}"
                             "square array.")

    def operation(self, a, b):
        """Perform the group operation on two values.

        The group operation is matrix multiplication.
        """
        return a @ b

    def __call__(self, value):
        """Create an element of this group."""
        return Element(self, value)

    def __str__(self):
        """Represent the group as Gd."""
        return f"G{self.degree}"

    def __repr__(self):
        """Return the canonical string representation of the group."""
        return f"{type(self).__name__}({repr(self.degree)})"
