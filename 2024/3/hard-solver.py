import re

def main():
    fileData = []
    foundStr = []
    total = 0
    doFlag = True

    with open("./3/input.txt") as f:
        fileData = f.readlines()

    for line in fileData:
        for item in re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", line):
            foundStr.append(item)
    
    for instructions in foundStr:
        if instructions == 'do()' or instructions == "don't()":
            if instructions == 'do()':
                doFlag = True
                continue
            elif instructions == "don't()":
                doFlag = False
                continue
        else:
            match = re.search(r'(\d+),(\d+)', instructions)
            matchTuple = match.groups()
        
        if doFlag:
            total += int(matchTuple[0]) * int(matchTuple[1])

    print(total)

if __name__ == '__main__':
    main()