
def binary_search(sorted_list: list | tuple, target: int | float) -> bool:
    """Binary search recursive algorithm implemented for any sorted iterable.

    Parameters
    ----------
    sorted_list : list | tuple
        Sorted iterable.
    target : int | float
        Target searched.

    Returns
    -------
    bool
        True if `target` in `sorted_list`.
    """
    left = 0
    right = len(sorted_list) - 1

    while left <= right:

        middle_index = (right + left) // 2

        if target == sorted_list[middle_index]:
            return True
        elif target < sorted_list[middle_index]:
            right = middle_index - 1
        else:
            left = middle_index + 1
    return False
