class Link:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert(self, link):
        '''Insert a new link after the current one.'''

        link.next = self.next
        self.next = link

    def __iter__(self):
        return LinkIterator(self)


class LinkIterator:
    def __init__(self, link):
        self.here = link

    def __iter__():
        return self

    def __next__(self):
        if self.here:
            next = self.here
            self.here = self.here.next
            return next.value
        else:
            raise StopIteration
