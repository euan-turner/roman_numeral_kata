def number_to_roman(number, low, mid, high):
    if number == 0:
        return ''
    if number < 4:
        return number * low
    if number < 5:
        return low + mid
    if number < 9:
        return mid + (number - 5) * low
    if number == 9:
        return low + high

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
    return  thousand_to_roman(thousands) + \
            number_to_roman(hundreds, 'C', 'D', 'M') + \
            number_to_roman(tens, 'X', 'L', 'C') + \
            number_to_roman(units, 'I', 'V', 'X')

print("Done")