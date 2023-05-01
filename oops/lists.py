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

    val: object = field(default=None)
    # TODO: maybe raise if is not instance of same type
    # if next is not None and not isinstance(next, ListNode):
    #     raise TypeError(f"Element with {val=} doesn't have a valid next ")
    next: ListNode = field(default=None, init=False)


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

    current: ListNode = field(default=None, init=False, repr=False)
    init_val: any = field(default=None, init=True, repr=False)
    length: int = field(default=0, init=False, repr=False)
    list_head: ListNode = field(default=None, init=False)

    def __post_init__(self) -> None:
        match self.init_val:
            case int() | float() | str():
                self.add_node(self.init_val)

            case list() | set() | SinglyLinkedList():
                for x in self.init_val:
                    self.add_node(x)

    def __iter__(self) -> SinglyLinkedList:
        self.current = self.list_head
        return self

    def __next__(self) -> ListNode:
        if self.current is None:
            raise StopIteration
        current = self.current.val
        self.current = self.current.next
        return current

    # @property
    # def length(self) -> int:
    #     return self.length

    # @length.setter
    # def length(self, val: int) -> None:
    #     if isinstance(val, int) and val >= 0:
    #         self.length = val
    #     else:

    def add_node(self, node_new: any = None) -> None:
        node_to_add = ListNode(val=node_new)
        if self.is_empty():
            self.list_head, self.length = node_to_add, 1
        else:
            list_end = self.list_head

            while list_end.next:
                list_end = list_end.next

            list_end.next = node_to_add
            self.length += 1

    def add_nodes(self, new_nodes: any = None) -> None:

        # TODO: move this to add_nodes() and let it accept: lists, strings, sets, dicts, frozensets
        # case list():
        list_end = self.list_head
        try:
            for x in new_nodes:
                if self.is_empty():
                    node_to_add = ListNode(val=x)
                    self.list_head, self.length = node_to_add, 1
                    continue
                while list_end.next:
                    list_end = list_end.next

                node_to_add = ListNode(val=x)
                list_end.next = node_to_add
                self.length += 1
        except TypeError as exc:
            raise TypeError(
                f"Variable given to add_nodes is not iterable: {new_nodes=}") from exc

    def is_empty(self):
        return self.length == 0 and self.list_head is None


# test_list = SinglyLinkedList([1, 2, 3])
# print(test_list)
# print(test_list.length)

# test_list.add_node("new_element")
# print(test_list)
# print(test_list.length)

# test_list.add_node("new_element2")
# print(test_list)
# print(test_list.length)

# test_list.add_nodes([4, 5, 6])
# print(test_list)
# print(test_list.length)

# test_list.add_node('test')
# print(test_list)
# print(test_list.length)

# for x in test_list:
#     print(x)
