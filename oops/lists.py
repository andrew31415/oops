from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ListNode(object):
    """An object containing a value and an identifier to another object of the
    same ListNode type.

    Notes
    -----

    element: [value, next]
    """

    val: int | float | str | None = field(default=None)
    # TODO: add setter for self.next that raises TypeError if object is not ListNone
    # if next is not None and not isinstance(next, ListNode):
    #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
    next: ListNode | None = field(default=None, init=False)


@dataclass
class SinglyLinkedList(object):
    """Contains a singly linked list of ListNode type elements.

    Notes
    -----

    element_1: [value, element_2_identifier]
    element_2: [value, element_3_identifier]
    element_3: [value, element_4_identifier]
    element_4: [value, None]
    """

    length: int = field(default=0, init=False, repr=False)
    list_head: ListNode | None = field(default=None, init=False)

    _current: ListNode | None = field(default=None, init=False, repr=False)
    _init_val: int | float | str | None = field(
        default=None, init=True, repr=False)

    def __post_init__(self) -> None:
        match self._init_val:
            case int() | float() | str():
                self.add_node(self._init_val)

            case list() | set() | SinglyLinkedList():
                for x in self._init_val:
                    self.add_node(x)

    def __iter__(self) -> SinglyLinkedList:
        self._current = self.list_head
        return self

    def __next__(self) -> int | float | str | None:
        if self._current is None:
            raise StopIteration
        current = self._current.val
        self._current = self._current.next
        return current

    def add_node(self, value: int | float | str | None = None) -> None:
        """Add a single ListNode object with a specific value to the end of the
        SinglyLinkedList instance .

        Parameters
        ----------
        value : int | float | str | None, optional.
            Value to be added, by default None.
        """
        node_to_add = ListNode(val=value)

        if self.list_head is None:
            self.list_head, self.length = node_to_add, 1
        else:
            list_end = self.list_head

            if list_end is not None:
                while list_end.next is not None:
                    list_end = list_end.next

                list_end.next = node_to_add
                self.length += 1

    def add_nodes(self, iterable: list | str | set | frozenset) -> None:
        """Add multiple ListNode objects with values read from an interable to
        the end of the SinglyLinkedList instance .

        Parameters
        ----------
        iterable : int | float | str | None, optional.
            Value to be added, by default None.
        """
        list_end = self.list_head
        try:
            for x in iterable:
                if self.list_head is None:
                    node_to_add = ListNode(val=x)
                    self.list_head, self.length = node_to_add, 1
                    list_end = self.list_head
                else:
                    if list_end is not None:
                        while list_end.next:
                            list_end = list_end.next

                        node_to_add = ListNode(val=x)
                        list_end.next = node_to_add
                        self.length += 1
        except TypeError as exc:
            raise TypeError(
                f"Variable given to add_nodes is not iterable: {iterable=}") from exc
