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
        assert repr(sll) == 'SinglyLinkedList(_head=ListNode(val=None, next=None))'
        assert str(sll) == 'SinglyLinkedList()'

        # Add a string element
        sll.add('new_element')
        assert str(sll) == "SinglyLinkedList(_head=ListNode(val='new_element', next=None))"
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

        sll_simple.add([5, 6, 7], iterate=True)
        assert sll_simple._size == (SIMPLE_LIST_LEN + 3)

        sll_simple.add('test', iterate=True)
        assert sll_simple._size == (SIMPLE_LIST_LEN + 3 + 4)

        sll_simple.add(sll_complex, iterate=True)
        assert sll_simple._size == (
            SIMPLE_LIST_LEN + 3 + 4 + COMPLEX_LIST_LEN)
        sll = lists.SinglyLinkedList()
        sll.add('haha', iterate=True)
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
            sll_simple.add(1, iterate=True)

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
        assert str(stack) == 'SinglyLinkedStack()'

        # Push a string element
        stack.push('new_element')
        assert len(stack) == 1
        assert str(stack) == "SinglyLinkedStack(_head=ListNode(val='new_element', next=None))"
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

        stack.push([1, 2, 3], iterate=True)
        assert len(stack) == 7

    def test_raise_errors(self):
        stack = lists.SinglyLinkedStack([1, 2, 3])
        with pytest.raises(TypeError):
            stack.push(1, iterate=True)

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
        assert str(queue) == 'Queue()'

        queue = lists.Queue(2)
        assert len(queue) == 1
        assert str(queue) == 'Queue(_head=ListNode(val=2, next=None))'
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
        queue.enqueue([1, 2, 3], iterate=True)
        assert len(queue) == 5

    def test_dequeue(self):
        queue = lists.Queue([1, 2, 3])

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        with pytest.raises(IndexError):
            assert queue.dequeue()

        assert str(queue) == 'Queue()'

        queue.enqueue('4')
        assert len(queue) == 1
        assert queue.is_empty() is False
        assert str(queue) == "Queue(_head=ListNode(val='4', next=None))"

    def test_raise_errors(self):
        queue = lists.Queue()
        with pytest.raises(IndexError):
            queue.first()
        with pytest.raises(IndexError):
            queue.last()
        with pytest.raises(TypeError):
            queue.enqueue(1, iterate=True)


class TestCircularyLinkedList:
    def test_create(self):
        circulary = lists.CircularlyLinkedList()
        assert circulary.is_empty() is True
        assert repr(circulary) == 'CircularlyLinkedList(_tail=None)'
        assert str(circulary) == 'CircularlyLinkedList()'

        circulary = lists.CircularlyLinkedList(2)
        assert len(circulary) == 1
        assert str(circulary) == 'CircularlyLinkedList(_tail=ListNode(val=2, next=...))'
        assert circulary.is_empty() is False

        circulary = lists.CircularlyLinkedList([1, 2, 3])
        assert len(circulary) == 3
        assert circulary.is_empty() is False
        assert circulary.first() == 1
        assert circulary.last() == 3

    def test_enqueue(self):
        circulary = lists.CircularlyLinkedList()

        # Enqueue a string element
        circulary.enqueue('new_element')
        assert len(circulary) == 1
        assert circulary.is_empty() is False

        # Push a frozenset element
        circulary.enqueue(frozenset([1, 2, 3, 1, 2, 3]))
        assert len(circulary) == 2

        # Push an element with val=[1,2,3]
        circulary.enqueue([1, 2, 3], iterate=True)
        assert len(circulary) == 5

    def test_dequeue(self):
        circulary = lists.CircularlyLinkedList([1, 2, 3])

        assert circulary.dequeue() == 1
        assert circulary.dequeue() == 2
        assert circulary.dequeue() == 3
        with pytest.raises(IndexError):
            assert circulary.dequeue()

    def test_raise_errors(self):
        queue = lists.CircularlyLinkedList()
        with pytest.raises(IndexError):
            queue.first()
        with pytest.raises(IndexError):
            queue.last()
        with pytest.raises(TypeError):
            queue.enqueue(1, iterate=True)


class TestLinkedDeque:
    def test_create_and_insert(self):
        deque = lists.LinkedDeque()
        assert deque.is_empty() is True
        assert repr(deque) == ('LinkedDeque(_header=DoubleListNode(val=None, '
                               'next=DoubleListNode(val=None, next=None, '
                               'prev=...), prev=None), _trailer=DoubleListNode('
                               'val=None, next=None, prev=DoubleListNode('
                               'val=None, next=..., prev=None)))')
        assert str(deque) == 'LinkedDeque()'

        deque = lists.LinkedDeque(2)
        assert len(deque) == 1
        assert str(deque) == ('LinkedDeque(_header=DoubleListNode(val=None, '
                              'next=DoubleListNode(val=2, next=DoubleListNode('
                              'val=None, next=None, prev=...), prev=...), '
                              'prev=None), _trailer=DoubleListNode(val=None, '
                              'next=None, prev=DoubleListNode(val=2, next=..., '
                              'prev=DoubleListNode(val=None, next=..., prev=None))))')
        assert deque.is_empty() is False

        deque = lists.LinkedDeque([1, 2, 3])
        assert len(deque) == 3
        assert deque.is_empty() is False
        assert deque.first() == 1
        assert deque.last() == 3

        deque.insert_front(10)
        assert deque.first() == 10
        assert len(deque) == 4

    def test_delete(self):
        circulary = lists.LinkedDeque([1, 2, 3])

        assert circulary.pop_front() == 1
        assert circulary.pop_back() == 3
        assert circulary.pop_front() == 2

    def test_raise_errors(self):
        circulary = lists.LinkedDeque()

        with pytest.raises(IndexError):
            circulary.pop_front()
        with pytest.raises(IndexError):
            circulary.first()
        with pytest.raises(IndexError):
            circulary.last()
        with pytest.raises(IndexError):
            circulary.delete_back()
        with pytest.raises(IndexError):
            circulary.delete_front()
