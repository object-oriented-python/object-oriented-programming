from example_code.linked_list import Link


def test_linked_list():

    linked_list = Link(1, Link(2, Link(3)))

    assert list(linked_list) == [1, 2, 3]
