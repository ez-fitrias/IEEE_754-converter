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

def to_binaryDecimal(decimal_number, findOne): 
    number = decimal_number
    binary = ""
    if findOne:
        startCount = False
    else:
        startCount = True
    exponent = 0
    if number == 0:
        binary = "0" * 23
    else:
        digit = 0
        while digit < 23:
            binary += str(int(number * 2))
            if findOne and str(int(number * 2)) == "1" and exponent == 0:
                exponent = -len(binary)
                startCount = True
                digit -= 1

            number *= 2
            if number >= 1:
                number -= 1
            
            if startCount:
                digit += 1
    return [binary, exponent]

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