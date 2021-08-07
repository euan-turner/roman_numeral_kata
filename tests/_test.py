import pytest
from ..src.main import to_roman

@pytest.mark.parametrize(
    "test_input, expected", 
    [
        (1, 'I'),
    ]
)
def test_to_roman(test_input, expected):
    assert  to_roman(test_input) == expected