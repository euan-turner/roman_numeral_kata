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
        return ten * 'X'
    if ten < 5:
        return 'XL'
    if ten < 9:
        return 'L' + (ten - 5) * 'X'
    if ten == 9:
        return 'XC'

def hundred_to_roman(hundred):
    if hundred == 0:
        return ''
    if hundred < 4:
        return hundred * 'C'
    if hundred < 5:
        return 'CD'
    if hundred < 9:
        return 'D' + (hundred - 5) * 'C'
    if hundred == 9:
        return 'CM'

def thousand_to_roman(thousand):
    if thousand == 0:
        return ''
    if thousand < 4:
        return thousand * 'M'


def to_roman(number):
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = ((number // 10) % 10) % 10
    units = number % 10
    return thousand_to_roman(thousands) + hundred_to_roman(hundreds) + ten_to_roman(tens) + unit_to_roman(units)

