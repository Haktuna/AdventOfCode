def main():
    FILE_SIZE = 1000

    fileData = []
    firstColumn = []
    secondColumn = []

    iterationDict = {}
    totalSimilarity = 0

    with open("./1/input.txt") as f:
        fileData = f.readlines()

    for i in range(FILE_SIZE):
        buf = fileData[i].split()
        key = int(buf[1])
        if key not in iterationDict:
            iterationDict[key] = 1
        else:
            iterationDict[key] += 1
        firstColumn.append(int(buf[0]))
        secondColumn.append(key)

    firstColumn.sort()
    secondColumn.sort()

    for i in range(FILE_SIZE):
        buf = 0
        if firstColumn[i] in iterationDict:
            buf = firstColumn[i] * iterationDict[firstColumn[i]]
        totalSimilarity += buf

    print(totalSimilarity)

if __name__ == '__main__':
    main()