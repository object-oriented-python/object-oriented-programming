from numbers import Integral


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
    '''A cyclic group represented by integer addition modulo the group size.'''
    def __init__(self, size):
        self.size = size

    def _validate(self, value):
        '''Ensure that value is a legitimate element value in this group.'''
        if not (isinstance(value, Integral) and 0 <= value < self.size):
            raise ValueError("Element value must be an integer"
                             f" in the range [0, {self.size})")

    def operation(self, a, b):
        return (a + b) % self.size

    def __call__(self, value):
        '''Provide a convenient way to create elements of this group.'''
        return Element(self, value)

    def __str__(self):
        return f"C{self.size}"

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.size)})"
