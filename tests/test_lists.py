"""Unit testing for lists.py
"""


import pytest

from oops import lists


SIMPLE_LIST = [1, 2, 3, 1]
SIMPLE_LIST_LEN = len(SIMPLE_LIST)
COMPLEX_LIST = ['a', 10, True]
COMPLEX_LIST_LEN = len(COMPLEX_LIST)
SIMPLE_SET = set(SIMPLE_LIST)
SIMPLE_SET_LEN = len(SIMPLE_SET)


@pytest.fixture
def sll_simple():
    """Pytest fixture to create an SLL from a list.
    """
    return lists.SinglyLinkedList(SIMPLE_LIST)


@pytest.fixture
def sll_complex():
    """Pytest fixture for an SLL from a list with different types of elements.
    """
    return lists.SinglyLinkedList(COMPLEX_LIST)


class TestSinglyLinkedList:

    def test_can_add_node_to_sll(self):
        """Add node(s) to a singly linked list.
        """
        sll = lists.SinglyLinkedList()
        assert len(sll) == 0
        assert len(sll) == 0
        assert repr(sll) == 'SinglyLinkedList(_head=None)'
        assert str(sll) == 'SinglyLinkedList(_head=None)'

        # Add a string element
        sll.add('new_element')
        assert len(sll) == 1

        # Add a frozenset element
        sll.add(frozenset([1, 2, 3, 1, 2, 3]))
        assert len(sll) == 2

        # Add an element with val=[1,2,3]
        sll.add([1, 2, 3])
        assert len(sll) == 3

        # Check if can make a list from a non-iterable type
        sll = lists.SinglyLinkedList(2)
        assert len(sll) == 1

        # Check if `None` value can be inserted correctly
        sll = lists.SinglyLinkedList()
        assert len(sll) == 0
        sll.add(None)
        assert len(sll) == 1

    def test_can_add_multiple_nodes_to_sll(self, sll_simple, sll_complex):
        """Add node(s) to a singly linked list.
        """
        assert sll_simple._size == SIMPLE_LIST_LEN

        sll_simple.add([5, 6, 7], iterable=True)
        assert sll_simple._size == (SIMPLE_LIST_LEN + 3)

        sll_simple.add('test', iterable=True)
        assert sll_simple._size == (SIMPLE_LIST_LEN + 3 + 4)

        sll_simple.add(sll_complex, iterable=True)
        assert sll_simple._size == (
            SIMPLE_LIST_LEN + 3 + 4 + COMPLEX_LIST_LEN)
        sll = lists.SinglyLinkedList()
        sll.add('haha', iterable=True)
        assert len(sll) == 4

    def test_can_create_new_sll_from_different_types(self, sll_simple):
        """Create singly linked lists from different types of input variables.
        """
        sll = lists.SinglyLinkedList(SIMPLE_LIST)

        assert sll == sll_simple

        sll = lists.SinglyLinkedList(SIMPLE_SET)
        assert len(sll) == 3

    def test_iterable_sll(self, sll_simple):
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

    def test_raise_errors(self, sll_simple):
        with pytest.raises(TypeError):
            sll_simple.add(10, iterable=True)

        # sll = lists.SinglyLinkedList()
        # with pytest.raises(ValueError):
        #     sll.length = -10

    def test_sll_len_function(self, sll_simple, sll_complex):
        assert len(sll_simple) == 4
        assert len(sll_complex) == 3

    def test_sll_getitem_function(self, sll_simple):
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


class TestStack:
    def test_create_and_push(self):
        stack = lists.SinglyLinkedStack()
        assert stack.is_empty() is True
        assert repr(stack) == 'SinglyLinkedStack(_head=None)'
        assert str(stack) == 'SinglyLinkedStack(_head=None)'

        # Push a string element
        stack.push('new_element')
        assert len(stack) == 1
        assert stack.is_empty() is False

        # Push a frozenset element
        stack.push(frozenset([1, 2, 3, 1, 2, 3]))
        assert len(stack) == 2

        # Push an element with val=[1,2,3]
        stack.push([1, 2, 3])
        assert len(stack) == 3

        # Check if can make a list from a non-iterable type
        stack = lists.SinglyLinkedStack(2)
        assert len(stack) == 1

        # Check if `None` value can be inserted correctly
        stack = lists.SinglyLinkedStack([1, 2, 3])
        assert len(stack) == 3
        stack.push(None)
        assert len(stack) == 4

        stack.push([1, 2, 3], iterable=True)
        assert len(stack) == 7

    def test_raise_errors(self):
        stack = lists.SinglyLinkedStack([1, 2, 3])
        with pytest.raises(TypeError):
            stack.push(10, iterable=True)

    def test_pop_and_top(self):
        stack = lists.SinglyLinkedStack([1, 2, 3])

        assert stack.pop() == 3
        assert stack.top() == 2
        assert stack.pop() == 2
        assert stack.pop() == 1
        with pytest.raises(IndexError):
            stack.pop()
        with pytest.raises(IndexError):
            stack.top()


class TestQueue:

    def test_create(self):
        queue = lists.Queue()
        assert queue.is_empty() is True
        assert repr(queue) == 'Queue(_head=None)'
        assert str(queue) == 'Queue(_head=None)'

        queue = lists.Queue(2)
        assert len(queue) == 1
        assert queue.is_empty() is False

        queue = lists.Queue([1, 2, 3])
        assert len(queue) == 3
        assert queue.is_empty() is False
        assert queue.first() == 1
        assert queue.last() == 3

    def test_enqueue(self):
        queue = lists.Queue()

        # Enqueue a string element
        queue.enqueue('new_element')
        assert len(queue) == 1
        assert queue.is_empty() is False

        # Push a frozenset element
        queue.enqueue(frozenset([1, 2, 3, 1, 2, 3]))
        assert len(queue) == 2

        # Push an element with val=[1,2,3]
        queue.enqueue([1, 2, 3], iterable=True)
        assert len(queue) == 5

    def test_dequeue(self):
        queue = lists.Queue([1, 2, 3])

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        with pytest.raises(IndexError):
            assert queue.dequeue()

    def test_raise_errors(self):
        queue = lists.Queue()
        with pytest.raises(IndexError):
            queue.first()
        with pytest.raises(IndexError):
            queue.last()
        with pytest.raises(TypeError):
            queue.enqueue(10, iterable=True)
