

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
    if len(sorted_list) == 1:
        return target == sorted_list[0]

    middle_index = len(sorted_list) // 2

    if target == sorted_list[middle_index]:
        return True
    elif target < sorted_list[middle_index]:
        return binary_search(sorted_list=sorted_list[0:middle_index],
                             target=target)
    else:
        return binary_search(sorted_list=sorted_list[middle_index + 1:],
                             target=target)
