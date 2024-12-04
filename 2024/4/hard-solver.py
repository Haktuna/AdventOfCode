import re

NUM_OF_LINE = 140
NUM_OF_CHAR = 140

def solveForXMas(lines: list[str]) -> int:
    numOfMatch = 0

    for i in range(NUM_OF_LINE):
        if i >= 1 and i <= NUM_OF_LINE - 2:
            aIndices = [m.start() for m in re.finditer(r"A", lines[i])]
            for a in aIndices:
                if a >= 1 and a <= NUM_OF_CHAR - 2:
                    if lines[i - 1][a - 1] == "M":
                        if lines[i - 1][a + 1] == "M":
                            if lines[i + 1][a - 1] == "S" and lines[i + 1][a + 1] == "S":
                                numOfMatch += 1
                        elif lines[i - 1][a + 1] == "S":
                            if lines[i + 1][a - 1] == "M" and lines[i + 1][a + 1] == "S":
                                numOfMatch += 1
                    elif lines[i - 1][a - 1] == "S":
                        if lines[i - 1][a + 1] == "S":
                            if lines[i + 1][a - 1] == "M" and lines[i + 1][a + 1] == "M":
                                numOfMatch += 1
                        elif lines[i - 1][a + 1] == "M":
                            if lines[i + 1][a - 1] == "S" and lines[i + 1][a + 1] == "M":
                                numOfMatch += 1

    return numOfMatch

def main():
    fileData: list[str] = []
    totalOfMatch = 0

    with open("./4/input.txt") as f:
        fileData = f.readlines()
    
    totalOfMatch += solveForXMas(fileData)

    print(totalOfMatch)

if __name__ == '__main__':
    main()