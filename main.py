import decimal_converter as dc
import binary_converter as bc

def tryCatchInt(text):
    input_value = input(text)
    try:
        return float(input_value)
    except ValueError:
        print("Please enter a valid number.")
        return tryCatchInt(text)

number = tryCatchInt("Please enter a number to be converted into Hexadecimal: ")

if number < 0:
    mostLeftBit = "1"
    number *= -1
else:
    mostLeftBit = "0"

frontOfComma = int(number)
behindOfComma = number - frontOfComma

frontOfCommaBinary = dc.to_binaryRound(frontOfComma)
behindOfCommaBinary = dc.to_binaryDecimal(behindOfComma, 23)

exponent = 0
if frontOfCommaBinary == "0":
    for char in behindOfCommaBinary:
        if char == "1":
            behindOfCommaBinary = (dc.to_binaryDecimal(behindOfComma, 23 + char.index() + 1))[char.index() + 1:]
            exponent = (char.index() + 1) * -1
elif frontOfCommaBinary != "1":
    exponent = len(frontOfCommaBinary[1:])
    behindOfCommaBinary = frontOfCommaBinary[1:] + behindOfCommaBinary[:(-len(frontOfCommaBinary[1:])) - 1]
    frontOfCommaBinary = "1"

normalisedExponent = exponent + 127
normalisedExponentBinary = dc.to_binaryRound(normalisedExponent)
while len(normalisedExponentBinary) < 8:
    normalisedExponentBinary = "0" + normalisedExponentBinary

gleitKommazahl = mostLeftBit + normalisedExponentBinary + behindOfCommaBinary
gleitKommazahlHexa = bc.to_hexadecimal(gleitKommazahl)

print(f"{number} in Gleitkommazahl is: {gleitKommazahl} | in Hexadecimal: {gleitKommazahlHexa}")

