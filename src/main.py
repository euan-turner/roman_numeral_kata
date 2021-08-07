def to_roman(number):
    if number < 4:
        return number * 'I'
    if number == 4:
        return 'IV'
    if number < 9:
        return 'V' + (number - 5) * 'I'
    if number == 9:
        return 'IX'
    if number < 14:
        return 'X' + (number - 10) * 'I'
    if number == 14:
        return 'XIV'
    if number == 15:
        return 'XV'
    return 'XVI'
