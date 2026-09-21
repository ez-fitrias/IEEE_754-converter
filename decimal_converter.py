def to_hexa(decimal_number):
    hexastring = "0123456789ABCDEF"
    hexadecimal = ""
    if decimal_number == 0:
        hexadecimal = "0"
    else:
        while decimal_number > 0:
            index = decimal_number % 16
            hexadecimal = hexastring[index] + hexadecimal
            decimal_number = decimal_number // 16
    return hexadecimal

def to_binaryRound(decimal_number):
    binary = ""
    if decimal_number == 0:
        binary = "0"
    else:
        while decimal_number > 0:
            binary = str(decimal_number % 2) + binary
            decimal_number = decimal_number // 2
    return binary

def to_binaryDecimal(decimal_number, length):  
    binary = ""
    if decimal_number == 0:
        binary = "0"
    else:
        digit = 0
        while decimal_number > 0 and digit <= length:
            binary += str(int(decimal_number * 2))
            decimal_number *= 2
            if decimal_number >= 1:
                decimal_number -= 1
            print(decimal_number)
            digit += 1
    return binary

def to_octa(decimal_number):
    octa = ""
    if decimal_number == 0:
        octa = "0"
    else:
        while decimal_number > 0:
            octa = str(decimal_number % 8) + octa
            decimal_number = decimal_number // 8
    return octa

def to_other_bases(decimal_number, base):
    result = ""
    if decimal_number == 0:
        result = "0"
    else:
        while decimal_number > 0:
            result = str(decimal_number % base) + result
            decimal_number = decimal_number // base
    return result

print(to_binaryDecimal(0.5, 23))