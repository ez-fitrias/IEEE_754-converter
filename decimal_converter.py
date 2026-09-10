def tryCatchInt(text):
    input_value = input(text)
    try:
        input_value = int(input_value)
        if input_value < 0:
            print("Please enter a positive integer.")
            return tryCatchInt(text)
        else:
            return input_value
    except ValueError:
        print("Please enter a valid integer.")
        return tryCatchInt(text)


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

def to_binary(decimal_number):
    binary = ""
    if decimal_number == 0:
        binary = "0"
    else:
        while decimal_number > 0:
            binary = str(decimal_number % 2) + binary
            decimal_number = decimal_number // 2
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
    elif base <= 0 or base > 9:
        result = "Base must be between 1 and 9."
    else:
        while decimal_number > 0:
            result = str(decimal_number % base) + result
            decimal_number = decimal_number // base
    return result

a_number = tryCatchInt("Enter a decimal number to convert to hexadecimal: ")
