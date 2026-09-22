import decimal_converter as dc
import binary_converter as bc

def tryCatchInt(text):
    input_value = input(text)
    try:
        return float(input_value)
    except ValueError:
        print("Please enter a valid number.")
        return tryCatchInt(text)

def gleitKommazahl(number):
    if number == 0:
        return ["0"*32, "0"*8]
    elif number < 0:
        mostLeftBit = "1"
        number *= -1
    else:
        mostLeftBit = "0"

    frontOfComma = int(number)
    behindOfComma = number - frontOfComma

    frontOfCommaBinary = dc.to_binaryRound(frontOfComma)
    behindOfCommaBinary = dc.to_binaryDecimal(behindOfComma, False)[0]

    exponent = 0
    if frontOfCommaBinary == "0":
        exponent = dc.to_binaryDecimal(behindOfComma, True)[1]
        behindOfCommaBinary = (dc.to_binaryDecimal(behindOfComma, True)[0])[-exponent:]

    elif frontOfCommaBinary != "1":
        exponent = len(frontOfCommaBinary[1:])
        behindOfCommaBinary = frontOfCommaBinary[1:] + behindOfCommaBinary[:-exponent]

    normalisedExponent = exponent + 127
    normalisedExponentBinary = dc.to_binaryRound(normalisedExponent)
    while len(normalisedExponentBinary) < 8:
        normalisedExponentBinary = "0" + normalisedExponentBinary

    gleitKommazahl = mostLeftBit + normalisedExponentBinary + behindOfCommaBinary
    gleitKommazahlHexa = bc.to_hexadecimal(gleitKommazahl)

    return [gleitKommazahl, gleitKommazahlHexa]


number = tryCatchInt("Please enter a number to be converted into 32 bit single precision IEEE 754 binary floating point representation: ")
print(f"The floating point representation of {number} is: {gleitKommazahl(number)[0]} | in Hexadecimal: {gleitKommazahl(number)[1]}")