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
        (6, 'VI'),
        (7, 'VII'),
        (9, 'IX'),
        (10, 'X'),
        (11, 'XI'),
        (12, 'XII'),
        (14, 'XIV'),
        (15, 'XV'),
        (16, 'XVI'),
        (17, 'XVII'),
        (40, 'XL'),
        (41, 'XLI'),
        (42, 'XLII'),
        (50, 'L'),
        (51, 'LI'),
        (52, 'LII'),
        (63, 'LXIII'),
        (90, 'XC'),
        (91, 'XCI'),
        (92, 'XCII'),
        (99, 'XCIX'),
        (100, 'C'),
        (999, 'CMXCIX')

        
    ]
)
def test_to_roman(test_input, expected):
    assert  to_roman(test_input) == expected