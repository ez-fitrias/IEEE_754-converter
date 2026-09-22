def to_hexadecimal(binaryNumber):
    hexa_binarList = [["0000", "0"], ["0001", "1"], ["0010", "2"], ["0011", "3"],
                      ["0100", "4"], ["0101", "5"], ["0110", "6"], ["0111", "7"],
                      ["1000", "8"], ["1001", "9"], ["1010", "A"], ["1011", "B"],
                      ["1100", "C"], ["1101", "D"], ["1110", "E"], ["1111", "F"]]
    hexadecimal = ""
    for i in range(0, len(binaryNumber), 4):
        for x in range(len(hexa_binarList)):
            if binaryNumber[i:i+4] == hexa_binarList[x][0]:
                hexadecimal += hexa_binarList[x][1]
    return hexadecimal
