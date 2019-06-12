#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
num_and_chars = string.digits + string.ascii_lowercase
dictionary = dict()
dictionary_encode = dict()
num = 0

for char in num_and_chars:
    dictionary[char] = num
    dictionary_encode[num] = char
    num += 1

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # takes in binary input
    # get length of the string
    # condition that accounts for 0's 

    if base == 2:
        number = 0
        power = 0
        
        for num in digits[::-1]:
            if int(num) == 1:
                number += base ** power
            power += 1
        return number
    
    number = 0
    power = 0
    
    for num in digits[::-1]:
        hex_num = dictionary[num.lower()]
        number += hex_num * (base ** power)
        power += 1
    return number


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    string = ''

    if number == 0:
        return '0'

    while number != 0:
        remainder = number % base
        quotient = number // base

        if remainder > 9:
            remainder = dictionary_encode[remainder]
            string += str(remainder)
            number = quotient
        else:
            string += str(remainder)
            number = quotient
    return string[::-1]

    

        
def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    decoded_number = decode(digits, base1)
    encoded_to_digits = encode(decoded_number, base2)
    return encoded_to_digits

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    print(decode('uu', 36))
    print(encode(1110, 36))