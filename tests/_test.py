import pytest
from ..src.main import to_roman

@pytest.mark.parametrize(
    "test_input, expected", 
    [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
    ]
)
def test_to_roman(test_input, expected):
    assert  to_roman(test_input) == expected