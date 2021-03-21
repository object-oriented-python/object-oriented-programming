from abc import ABC, abstractmethod


class Addable(ABC):

    @abstractmethod
    def __add__(self, other):
        return NotImplemented

    @classmethod
    def __subclasshook__(cls, C):
        if cls is not Addable:
            return NotImplemented
        for B in C.__mro__:
            if "__add__" in B.__dict__:
                if B.__dict__["__add__"] is None:
                    return NotImplemented
                return True
        return NotImplemented
