import pytest

from oops import searches


@pytest.mark.parametrize(
    ('sorted_list', 'target', 'decision'),
    (
        pytest.param([1, 2, 3, 4, 5, 6, 7], 2, True, id="[1:7]-2-True"),
        pytest.param([1, 2, 3, 4, 5, 6, 7], 10, False, id="[1:7]-10-False"),
        pytest.param([1, 2, 3, 4, 5, 6, 7], 10, False, id="[1:7]-0-False"),
        pytest.param([1, 2, 3, 4, 5, 6, 7], 7, True, id="[1:7]-7-True"),
        pytest.param([1, 2, 3, 4, 5, 6, 7], 1, True, id="[1:7]-1-True"),
        pytest.param([1, 2, 3, 4, 5, 6, 7], 4, True, id="[1:7]-4-True"),
        pytest.param(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'c', True, id="[a:g]-c-True"),
        pytest.param(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'z', False, id="[a:g]-z-False")
    )
)
def test_binary_search(sorted_list, target, decision):
    assert searches.binary_search(sorted_list, target) == decision
