def unit_to_roman(unit):
    if unit == 0:
        return ''
    if unit < 4:
        return unit * 'I'
    if unit == 4:
        return 'IV'
    if unit < 9:
        return 'V' + (unit - 5) * 'I'
    if unit == 9:
        return 'IX'

def ten_to_roman(ten):
    if ten == 0:
        return ''
    if ten < 4:
        return 'X'
    if ten < 5:
        return 'XL'
    if ten < 9:
        return 'L' + (ten - 5) * 'X'
    if ten == 9:
        return 'XC'


def to_roman(number):
    tens = number // 10
    units = number % 10
    return ten_to_roman(tens) + unit_to_roman(units)

