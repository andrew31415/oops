from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class ListNode(object):
    """An object containing a value (type: Any) and a reference to another
    ListNode type.
    """

    val: Any = field(default=None)
    # TODO: add setter for self.next that raises TypeError if object is not ListNone
    # if next is not None and not isinstance(next, ListNode):
    #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
    next: ListNode | None = field(default=None)


@dataclass
class SinglyLinkedList:
    """Contains a singly linked list of ListNode type elements.

    Notes
    -----

    element_1: [value, element_2_identifier]
    element_2: [value, element_3_identifier]
    element_3: [value, element_4_identifier]
    element_4: [value, None]
    """

    _size: int = field(default=0, init=False, repr=False)
    """List size."""
    _head: ListNode | None = field(default=None, init=True)
    """List head node."""

    def __post_init__(self) -> None:
        match self._head:
            case int() | float() | str():
                self.add(self._head)

            case list() | set() | frozenset() | SinglyLinkedList():
                for x in self._head:
                    self.add(x)

    def __len__(self) -> int:
        """Get the list's size.

        Returns
        -------
        int
            How many `ListNode` elements this list contains.
        """
        return self._size

    def __getitem__(self, integer: int) -> ListNode | None:
        """Get the element from the SinglyLinkedList from the specified
        `integer` position.

        Parameters
        ----------
        integer : int
            Position of searched element.

        Returns
        -------
        ListNode | None
            Element from position `integer`.

        Raises
        ------
        IndexError
            If the `integer` index is out of bounds.
        ValueError
            If an illegal `integer` index is given.
        """
        sll_length = len(self) - 1

        if integer > sll_length:
            raise IndexError('SinglyLinkedList: list index out of range.')
        if integer < 0 or not type(integer) is int:
            raise ValueError('SinglyLinkedList: list index must be positive integer.')

        node_parser = self._head

        while integer != 0 and node_parser is not None:
            node_parser = node_parser.next
            integer -= 1

        return node_parser

    def is_empty(self) -> bool:
        """Return True if SinglyLinkedList is empty."""
        return len(self) == 0

    def add(self, value: Any = None, iterable: bool = False) -> None:
        """Add ListNode object(s) with a specific `value` to the end of the
        SinglyLinkedList.

        Parameters
        ----------
        value : Any | None, optional.
            Value to be added, by default None.
        iterable : bool, optional.
            Iterate over `value` and add individual nodes, by default False.

        Raises
        ------
        TypeError
            If iterable is True and value is not iterable.
        """
        if not iterable:
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
class SinglyLinkedStack:

    _size: int = field(default=0, init=False, repr=False)
    """Stack size."""
    _head: Any = field(default=None, init=True)
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

    def __len__(self) -> int:
        """Return the stack's size."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if stack is empty."""
        return self._size == 0

    def push(self, value: Any = None, iterable: bool = False) -> None:
        """Push `ListNode` object(s) in the stack.

        Parameters
        ----------
        value : Any, optional.
            Value to be added, by default None.
        iterable : bool, optional.
            Iterate over `value` and push individual nodes, by default False.

        Raises
        ------
        TypeError
            If iterable is True and value is not iterable.
        """
        if not iterable:
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
        """Pop (remove and return) the element from the top of the stack.

        Raises
        ------
        IndexError
            If the stack is empty
        """

        if self.is_empty():
            raise IndexError('Stack is empty.')
        val = self._head.val
        self._head = self._head.next
        self._size -= 1
        return val

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self._head.val


@dataclass
class Queue:
    _size: int = field(default=0, init=False, repr=False)
    """Queue size."""
    _head: Any = field(default=None, init=True)
    """Queue head."""
    _tail: Any = field(default=None, init=False, repr=False)
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

    def __len__(self) -> int:
        """Return the stack's size."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if stack is empty."""
        return self._size == 0

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

    def enqueue(self, value: Any = None, iterable: bool = False) -> None:
        """Add ListNone object(s) to the end of the queue.

        Parameters
        ----------
        value : Any, optional
            Value to be added, by default None
        iterable : bool, optional
            Iterate over `value` and add individual nodes, by default False.

        Raises
        ------
        TypeError
            If iterable is True and value is not iterable.
        """
        if not iterable:
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
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return val
