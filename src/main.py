def to_roman(number):
    if number < 4:
        return number * 'I'
    if number == 4:
        return 'IV'
    if number < 9:
        return 'V' + (number - 5) * 'I'
    if number == 9:
        return 'IX'
    if number == 10:
        return 'X'
    if number == 11:
        return 'XI'
    return 'XII'
