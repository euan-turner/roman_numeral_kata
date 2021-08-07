def to_roman(number):
    if number < 4:
        return number * 'I'
    if number == 4:
        return 'IV'
    if number < 9:
        return 'V' + (number - 5) * 'I'
    if number == 9:
        return 'IX'
    if number < 40:
        return 'X' + to_roman(number - 10)
    if number < 50:
        return 'XL' + to_roman(number - 40)
    if number < 90:
        return 'L' + to_roman(number - 50)
    return 'XC' + to_roman(number - 90)

