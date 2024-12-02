def main():
    FILE_SIZE = 1000

    fileData = []
    firstColumn = []
    secondColumn = []

    totalDistance = 0

    with open("./1/input.txt") as f:
        fileData = f.readlines()

    for i in range(FILE_SIZE):
        buf = fileData[i].split()
        firstColumn.append(int(buf[0]))
        secondColumn.append(int(buf[1]))

    firstColumn.sort()
    secondColumn.sort()

    for i in range(FILE_SIZE):
        buf = firstColumn[i] - secondColumn[i]
        if buf < 0:
            buf *= -1
        totalDistance += buf

    print(totalDistance)

if __name__ == '__main__':
    main()