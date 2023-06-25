"""Unit testing for lists.py
"""


import pytest

from oops import lists


SLL_SIMPLE_LIST = [1, 2, 3, 1]
SLL_SIMPLE_LIST_LEN = len(SLL_SIMPLE_LIST)
SLL_COMPLEX_LIST = ['a', 10, True]
SLL_COMPLEX_LIST_LEN = len(SLL_COMPLEX_LIST)
SLL_SIMPLE_SET = set(SLL_SIMPLE_LIST)
SLL_SIMPLE_SET_LEN = len(SLL_SIMPLE_SET)


@pytest.fixture
def sll_simple():
    """Pytest fixture to create an SLL from a list.
    """
    return lists.SinglyLinkedList(SLL_SIMPLE_LIST)


@pytest.fixture
def sll_complex():
    """Pytest fixture for an SLL from a list with different types of elements.
    """
    return lists.SinglyLinkedList(SLL_COMPLEX_LIST)


def test_can_add_node_to_sll():
    """Add node(s) to a singly linked list.
    """
    sll = lists.SinglyLinkedList()
    assert sll.length == 0
    assert repr(sll) == "SinglyLinkedList(list_head=None)"
    assert str(sll) == "SinglyLinkedList(list_head=None)"

    sll.add_node("new_element")
    assert sll.length == 1

    sll.add_node(frozenset([1, 2, 3, 1, 2, 3]))
    assert sll.length == 2

    # Add an element with val=[1,2,3]
    sll.add_node([1, 2, 3])
    assert sll.length == 3

    # Check if can make a list from a non-iterable type
    sll = lists.SinglyLinkedList(2)
    assert sll.length == 1

    # Check if `None` value can be inserted correctly
    sll = lists.SinglyLinkedList()
    assert sll.length == 0
    sll.add_node(None)
    assert sll.length == 1


def test_can_add_multiple_nodes_to_sll(sll_simple, sll_complex):
    """Add node(s) to a singly linked list.
    """
    assert sll_simple.length == SLL_SIMPLE_LIST_LEN

    sll_simple.add_nodes([5, 6, 7])
    assert sll_simple.length == (SLL_SIMPLE_LIST_LEN + 3)

    sll_simple.add_nodes('test')
    assert sll_simple.length == (SLL_SIMPLE_LIST_LEN + 3 + 4)

    sll_simple.add_nodes(sll_complex)
    assert sll_simple.length == (
        SLL_SIMPLE_LIST_LEN + 3 + 4 + SLL_COMPLEX_LIST_LEN)
    sll = lists.SinglyLinkedList()
    sll.add_nodes("haha")
    assert sll.length == 4


def test_can_create_new_sll_from_different_types(sll_simple):
    """Create singly linked lists from different types of input variables.
    """
    sll = lists.SinglyLinkedList(SLL_SIMPLE_LIST)

    assert sll == sll_simple

    sll = lists.SinglyLinkedList(SLL_SIMPLE_SET)
    assert sll.length == 3


def test_iterable_sll(sll_simple):
    """Check if the SLL is interable
    """
    sll_iter = iter(sll_simple)
    assert next(sll_iter) == lists.ListNode(val=1, next=lists.ListNode(
        val=2, next=lists.ListNode(val=3, next=lists.ListNode(val=1))))
    assert next(sll_iter) == lists.ListNode(val=2, next=lists.ListNode(val=3, next=lists.ListNode(val=1)))
    assert next(sll_iter) == lists.ListNode(val=3, next=lists.ListNode(val=1))
    assert next(sll_iter) == lists.ListNode(val=1)

    with pytest.raises(StopIteration):
        assert next(sll_iter)


def test_can_raise_errors(sll_simple):
    with pytest.raises(TypeError):
        sll_simple.add_nodes(10)

    # sll = lists.SinglyLinkedList()
    # with pytest.raises(ValueError):
    #     sll.length = -10


def test_sll_len_function(sll_simple, sll_complex):
    assert len(sll_simple) == 4
    assert len(sll_complex) == 3


def test_sll_getitem_function(sll_simple):
    assert sll_simple[0] == lists.ListNode(val=1, next=lists.ListNode(
        val=2, next=lists.ListNode(val=3, next=lists.ListNode(val=1))))
    assert sll_simple[1] == lists.ListNode(val=2, next=lists.ListNode(val=3, next=lists.ListNode(val=1)))
    assert sll_simple[2] == lists.ListNode(val=3, next=lists.ListNode(val=1))
    assert sll_simple[3] == lists.ListNode(val=1)

    with pytest.raises(IndexError):
        sll_simple[4]
    with pytest.raises(ValueError):
        sll_simple[-10]
    with pytest.raises(ValueError):
        sll_simple[2.5]
