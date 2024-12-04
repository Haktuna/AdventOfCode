import re

NUM_OF_LINE = 140
NUM_OF_CHAR = 140

def solveForBothHorizontal(lines: list[str]) -> int:
    pattern = r"XMAS"
    numOfMatch = 0;

    for line in lines:
        match = re.findall(pattern, line)
        reverseMatch = re.findall(pattern, line[::-1])
        numOfMatch += len(match)
        numOfMatch += len(reverseMatch)

    print(f"{numOfMatch} horizontal")
    
    return numOfMatch

def solveForVertical(lines: list[str]) -> int:
    numOfMatch = 0

    for i in range(NUM_OF_LINE):
        if i <= NUM_OF_LINE - 4:
            xIndices = [m.start() for m in re.finditer(r"X", lines[i])]
            for x in xIndices:
                    if lines[i + 1][x] == "M":
                        if lines[i + 2][x] == "A":
                            if lines[i + 3][x] == "S":
                                numOfMatch += 1
        else:
            break

    return numOfMatch

def solveForBothVertical(lines: list[str]) -> int:
    numOfMatch = 0
    numOfMatch += solveForVertical(lines)
    numOfMatch += solveForVertical(lines[::-1])

    print(f"{numOfMatch} vertical")

    return numOfMatch

def solveForDiagonal(lines: list[str]) -> int:
    numOfMatch = 0

    for i in range(NUM_OF_LINE):
        if i <= NUM_OF_LINE - 4:
            xIndices = [m.start() for m in re.finditer(r"X", lines[i])]
            for x in xIndices:
                    if i <= NUM_OF_CHAR - 4:
                        if lines[i + 1][x + 1] == "M":
                            if lines[i + 2][x + 2] == "A":
                                if lines[i + 3][x + 3] == "S":
                                    numOfMatch += 1
                    if x >= 3:
                        if lines[i + 1][x - 1] == "M":
                            if lines[i + 2][x - 2] == "A":
                                if lines[i + 3][x - 3] == "S":
                                    numOfMatch += 1
        else:
            break

    return numOfMatch

def solveForBothDiagonal(lines: list[str]) -> int:
    numOfMatch = 0
    numOfMatch += solveForDiagonal(lines)
    numOfMatch += solveForDiagonal(lines[::-1])

    print(f"{numOfMatch} diagonal")

    return numOfMatch

def main():
    fileData: list[str] = []
    totalOfMatch = 0

    with open("./4/input.txt") as f:
        fileData = f.readlines()
    
    totalOfMatch += solveForBothHorizontal(fileData)
    totalOfMatch += solveForBothVertical(fileData)
    totalOfMatch += solveForBothDiagonal(fileData)

    print(totalOfMatch)

if __name__ == '__main__':
    main()