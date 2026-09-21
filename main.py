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