def to_roman(number):
    if number < 4:
        return number * 'I'
    if number == 4:
        return 'IV'
    else:
        return 'V' + (number - 5) * 'I'
    