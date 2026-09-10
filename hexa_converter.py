def tryCatchHexa(text):
    input_value = input(text).upper()
    hexastring = "0123456789ABCDEF"
    for char in input_value:
        if char not in hexastring:
            print("Please enter a valid hexadecimal number.")
            return tryCatchHexa(text)
    return input_value


def to_decimal(hexadecimal_number):
    decimal = 0
    hexastring = "0123456789ABCDEF"
    hexadecimal_number = hexadecimal_number.upper()
    if hexadecimal_number == "0":
        decimal = 0
    else:
        for index in range(len(hexadecimal_number)):
            char = hexadecimal_number[index]
            decimal += hexastring.index(char) * (16 ** (len(hexadecimal_number) - index - 1))
