import pytest

from oops import searches


@pytest.mark.parametrize(
    ('sorted_list', 'target', 'decision'),
    (
        pytest.param(range(1, 8), 2, True, id="1:7-2-True"),
        pytest.param(range(1, 8), 10, False, id="1:7-10-False"),
        pytest.param(range(1, 8), 10, False, id="1:7-0-False"),
        pytest.param(range(1, 8), 7, True, id="1:7-7-True"),
        pytest.param(range(1, 8), 1, True, id="1:7-1-True"),
        pytest.param(range(1, 8), 4, True, id="1:7-4-True"),
        pytest.param(list('abcdefg'), 'c', True, id="list(a:g)-c-True"),
        pytest.param(list('abcdefg'), 'z', False, id="list(a:g)-z-False"),
        pytest.param('abcdefg', 'c', True, id="str(a:g)-c-True"),
        pytest.param('abcdefg', 'z', False, id="str(a:g)-z-False")
    )
)
def test_binary_search(sorted_list, target, decision):
    assert searches.binary_search(sorted_list, target) == decision
