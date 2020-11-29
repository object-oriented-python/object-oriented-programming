'''A module containing some very simple shape classes to illustrate the use of
:func:`super`.'''


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return f"{self.__class__.__name__}{self.length, self.width!r}"


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.length!r})"
