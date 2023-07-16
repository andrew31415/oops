from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class ListNode():
    """Contains a value (type: Any) and a reference to another ListNode type.
    """

    val: Any = field(default=None, init=True)
    """Value stored in `ListNode`."""
    # TODO: add setter for self.next that raises TypeError if object is not ListNone
    # if next is not None and not isinstance(next, ListNode):
    #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
    next: ListNode | None = field(default=None, init=True)
    """Next `ListNode`."""


@dataclass
class DoubleListNode():
    val: Any = field(default=None, init=True)
    """Value stored in `DoubleListNode`."""
    next: DoubleListNode | None = field(default=None, init=True)
    """Next `DoubleListNode`."""
    prev: DoubleListNode | None = field(default=None, init=True)
    """Previous `DoubleListNode`."""


@dataclass
class SinglyLinkedBase:
    _size: int = field(default=0, init=False, repr=False)
    """Number of contained list nodes."""

    def __len__(self) -> int:
        """Return list's size."""
        return self._size

    def is_empty(self) -> bool:
        """Return `True` if list is empty."""
        return self._size == 0


@dataclass
class SinglyLinkedList(SinglyLinkedBase):
    """Contains a singly linked list of ListNode type elements.

    Notes
    -----

    element_1: [value, element_2_identifier]
    element_2: [value, element_3_identifier]
    element_3: [value, element_4_identifier]
    element_4: [value, None]
    """

    _head: ListNode = field(default_factory=ListNode, init=True)
    """List head node."""

    def __post_init__(self) -> None:
        init_value = deepcopy(self._head)
        self._head = ListNode(None, None)
        match init_value:
            case int() | float() | str():
                self.add(init_value)

            case list() | set() | frozenset() | SinglyLinkedList():
                for x in init_value:
                    self.add(x)

    def __str__(self) -> str:
        if self.is_empty():
            return 'SinglyLinkedList()'
        return repr(self)

    def __getitem__(self, idx: int) -> ListNode | None:
        """Get the element from the SinglyLinkedList from the specified
        `idx` index.

        Parameters
        ----------
        idx : int
            Index of searched element.

        Returns
        -------
        ListNode | None
            Element from index `idx`.

        Raises
        ------
        IndexError
            If the `idx` index is out of bounds.
        ValueError
            If an illegal `idx` index is given.
        """
        if idx >= len(self):
            raise IndexError('SinglyLinkedList: index out of range.')
        if idx < 0 or not type(idx) is int:
            raise ValueError('SinglyLinkedList: index must be positive integer.')

        node_parser = self._head
        while idx != 0:
            node_parser = node_parser.next  # type: ignore
            idx -= 1

        return node_parser

    def __iter__(self):
        """Implementing this only to make mypy happy, since this is not needed
        when `__len__` and `__getitem__` are defined."""
        for x in range(len(self)):
            yield self[x]

    def add(self, value: Any = None, iterate: bool = False) -> None:
        """Add ListNode object(s) with a specific `value` to the end of the
        SinglyLinkedList.

        Parameters
        ----------
        value : Any, optional.
            Value to be added, by default None.
        iterate : bool, optional.
            Iterate over `value` and add individual nodes, by default False.

        Raises
        ------
        TypeError
            If `iterate` is True and `value` is not iterable.
        """
        if not iterate:
            node_to_add = ListNode(val=value)

            if self.is_empty():
                self._head, self._size = node_to_add, 1
            else:
                list_end = self._head

                if list_end is not None:
                    while list_end.next is not None:
                        list_end = list_end.next

                    list_end.next = node_to_add
                    self._size += 1
        else:
            try:
                for x in value:
                    self.add(x)
            except TypeError as exc:
                raise TypeError(
                    f"Variable given to add_nodes is not iterable: {value=}") from exc


@dataclass
class SinglyLinkedStack(SinglyLinkedBase):
    """ADT implementation of a Stack."""
    _head: ListNode = field(default_factory=ListNode, init=True)
    """Stack head."""

    def __post_init__(self):
        init_value = deepcopy(self._head)
        self._head = None
        match init_value:
            case int() | float() | str():
                self.push(init_value)

            case list() | set() | frozenset() | SinglyLinkedList():
                for x in init_value:
                    self.push(x)

    def __str__(self) -> str:
        if self.is_empty():
            return 'SinglyLinkedStack()'
        return repr(self)

    def top(self) -> Any:
        """Get the element at the top of the stack."""
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self._head.val

    def push(self, value: Any = None, iterate: bool = False) -> None:
        """Push `ListNode` object(s) in the stack.

        Parameters
        ----------
        value : Any, optional.
            Value to be added, by default None.
        iterate : bool, optional.
            Iterate over `value` and push individual nodes, by default False.

        Raises
        ------
        TypeError
            If `iterate` is True and value is not iterable.
        """
        if not iterate:
            node_to_add = ListNode(val=value, next=self._head)
            self._head = node_to_add
            self._size += 1
        else:
            try:
                for x in value:
                    self.push(x)
            except TypeError as exc:
                raise TypeError(
                    f"Object given to push is not iterable: {value=}") from exc

    def pop(self) -> Any:
        """Pop (remove and return) the value stored in the top of the stack.

        Raises
        ------
        IndexError
            If the stack is empty
        """

        if self.is_empty():
            raise IndexError('Stack is empty.')
        val = self._head.val
        self._head = self._head.next  # type: ignore
        self._size -= 1
        return val


@dataclass
class Queue(SinglyLinkedBase):
    """ADT implementation of a Queue."""
    _head: ListNode = field(default_factory=ListNode, init=True)
    """Queue head."""
    _tail: ListNode = field(default_factory=ListNode, init=False, repr=False)
    """Queue tail."""

    def __post_init__(self):
        init_value = deepcopy(self._head)
        self._head = None
        match init_value:
            case int() | float() | str():
                self.enqueue(init_value)

            case list() | set() | frozenset() | SinglyLinkedList():
                for x in init_value:
                    self.enqueue(x)

    def __str__(self) -> str:
        if self.is_empty():
            return 'Queue()'
        return repr(self)

    def first(self) -> Any:
        """Get the element at the front of the queue."""
        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self._head.val

    def last(self) -> Any:
        """Get the element at the end of the queue."""
        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self._tail.val

    def enqueue(self, value: Any = None, iterate: bool = False) -> None:
        """Add object(s) to the end of the queue.

        Parameters
        ----------
        value : Any, optional
            Value to be added, by default None.
        iterate : bool, optional
            Iterate over `value` and add individual nodes, by default False.

        Raises
        ------
        TypeError
            If `iterate` is True and value is not iterable.
        """
        if not iterate:
            node_to_add = ListNode(val=value, next=None)
            if self.is_empty():
                self._head = node_to_add
            else:
                self._tail.next = node_to_add
            self._tail = node_to_add
            self._size += 1
        else:
            try:
                for x in value:
                    self.enqueue(x)
            except TypeError as exc:
                # TODO: make this a decorator? "value_type_checker"
                raise TypeError(
                    f"Object given to push is not iterable: {value=}") from exc

    def dequeue(self) -> Any:
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise IndexError('Queue is empty.')

        val = self._head.val
        self._head = self._head.next  # type: ignore
        self._size -= 1
        if self.is_empty():
            self._tail = ListNode()
        return val


@dataclass
class CircularlyLinkedList(SinglyLinkedBase):
    """ADT implementation of a Circulary Linked List."""
    _tail: Any = field(default=None, init=True)
    """Queue tail."""

    def __post_init__(self):
        init_value = deepcopy(self._tail)
        self._tail = None
        match init_value:
            case int() | float() | str():
                self.enqueue(init_value)

            case list() | set() | frozenset() | SinglyLinkedList():
                for x in init_value:
                    self.enqueue(x)

    def __str__(self) -> str:
        if self.is_empty():
            return 'CircularlyLinkedList()'
        return repr(self)

    def first(self) -> Any:
        """Get the element at the front of the queue."""
        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self._tail.next.val

    def last(self) -> Any:
        """Get the element at the end of the queue."""
        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self._tail.val

    def enqueue(self, value: Any = None, iterate: bool = False) -> None:
        """Add object(s) to the end of the queue.

        Parameters
        ----------
        value : Any, optional
            Value to be added, by default None.
        iterate : bool, optional
            Iterate over `value` and add individual nodes, by default False.

        Raises
        ------
        TypeError
            If `iterate` is True and value is not iterable.
        """
        if not iterate:
            node_to_add = ListNode(val=value, next=None)
            if self.is_empty():
                node_to_add.next = node_to_add
            else:
                node_to_add.next = self._tail.next
                self._tail.next = node_to_add
            self._tail = node_to_add
            self._size += 1
        else:
            try:
                for x in value:
                    self.enqueue(x)
            except TypeError as exc:
                # TODO: make this a decorator? "value_type_checker"
                raise TypeError(
                    f"Object given to push is not iterable: {value=}") from exc

    def dequeue(self) -> Any:
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise IndexError('Queue is empty.')

        head = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = head.next
        self._size -= 1
        return head.val


@dataclass
class DoublyLinkedBase(SinglyLinkedBase):
    _header: DoubleListNode = field(default_factory=DoubleListNode, init=True)
    """Front sentinel node."""
    _trailer: DoubleListNode = field(default_factory=DoubleListNode, init=False)
    """End sentinel node."""

    def __post_init__(self):
        self._header.next = self._trailer
        self._trailer.prev = self._header

    def _insert_between(self, val: Any, left: DoubleListNode, right: DoubleListNode) -> None:
        node_to_add = DoubleListNode(val=val, prev=left, next=right)
        left.next = node_to_add
        right.prev = node_to_add
        self._size += 1

    def _delete_node(self, node: DoubleListNode) -> None:
        left, right = node.prev, node.next
        left.next, right.prev = right, left  # type: ignore
        self._size -= 1

        # GC enablement
        node.val = node.prev = node.next = None


class LinkedDeque(DoublyLinkedBase):

    def __post_init__(self):
        init_value = deepcopy(self._header)
        self._header = DoubleListNode()
        super().__post_init__()
        match init_value:
            case int() | float() | str():
                self.insert_back(init_value)

            case list() | set() | frozenset() | SinglyLinkedList():
                for x in init_value:
                    self.insert_back(x)

    def __str__(self) -> str:
        if self.is_empty():
            return 'LinkedDeque()'
        return repr(self)

    def first(self) -> Any:
        """Get the value from the front of the deque."""
        if self.is_empty():
            raise IndexError('Deque is empty.')
        return self._header.next.val  # type: ignore

    def last(self) -> Any:
        """Get the value from the back of the deque."""
        if self.is_empty():
            raise IndexError('Deque is empty.')
        return self._trailer.prev.val  # type: ignore

    def insert_front(self, val: Any = None):
        """Insert value at the front of the deque."""
        self._insert_between(val=val, left=self._header, right=self._header.next)  # type: ignore

    def insert_back(self, val: Any = None):
        """Insert value at the back of the deque."""
        self._insert_between(val=val, left=self._trailer.prev, right=self._trailer)  # type: ignore

    def delete_front(self):
        """Delete the node at the front of the deque."""
        if self.is_empty():
            raise IndexError('Deque is empty.')
        self._delete_node(node=self._header.next)

    def pop_front(self) -> Any:
        """Delete and return the value from the front of the deque."""
        value = self.first()
        self.delete_front()
        return value

    def delete_back(self):
        """Delete the node at the back of the deque."""
        if self.is_empty():
            raise IndexError('Deque is empty.')
        self._delete_node(node=self._trailer.prev)

    def pop_back(self) -> Any:
        """Delete and return the value from the back of the deque."""
        value = self.last()
        self.delete_back()
        return value
