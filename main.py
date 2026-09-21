def tryCatchInt(text):
    input_value = input(text)
    try:
        return float(input_value)
    except ValueError:
        print("Please enter a valid number.")
        return tryCatchInt(text)

number = tryCatchInt("Please enter a number to be converted into Hexadecimal: ")

if number < 0:
    mostLeftBit = 1
else:
    mostLeftBit = 0

frontOfComma = int(number)
behindOfComma = number - frontOfComma