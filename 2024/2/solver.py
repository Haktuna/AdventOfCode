def isAscOrDes(toCheck:list[int]) -> str:
    sortedList = sorted(toCheck)
    reverseSortedList = sortedList[::-1]
    if sortedList == toCheck:
        return 'asc'
    elif reverseSortedList == toCheck:
        return 'des'
    else:
        return 'err'

def isSafe(toCheck:list[int]) -> bool:
    ascOrDes = isAscOrDes(toCheck)
    if ascOrDes == 'err':
        return False
    for i in range(len(toCheck) - 1):
        diff = toCheck[i + 1] - toCheck[i]
        if ascOrDes == 'des' and -3 <= diff < 0:
            continue
        elif ascOrDes == 'asc' and 0 < diff <= 3:
            continue
        else:
            return False
    return True
        

def main():
    FILE_SIZE = 1000
    fileData = []
    totalSafe = 0

    with open("./2/input.txt") as f:
        for line in f.readlines():
            fileData.append(list(int(x) for x in line.split()))

    for i in range(FILE_SIZE):
        if isSafe(fileData[i]):
            totalSafe += 1
    
    print(totalSafe)

if __name__ == '__main__':
    main()