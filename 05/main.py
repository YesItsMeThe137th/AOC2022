    
def parse_data(fileName):
    with open(fileName, "r") as fd:
        data = fd.read().split("\n\n")
        data[1] = data[1].split("\n")
        for i in range(len(data[1])):
            data[1][i] = data[1][i].split(" ")
        return data

def makeStacks(ships):
    print(ships)
    ships = ships.split("\n")
    stacks = [[]]
    for ind in range(1, len(ships[0]), 4):
        newStack = []
        for row in range(len(ships) - 2, -1, -1):
            if (ships[row][ind] != ' '):
                newStack.append(ships[row][ind])
            # print(row)
        stacks.append(newStack)
    return stacks
        
def rearrange(ships, amt, start, dest):
    # grab from ships the amt of items, removing them.
    # put those items into the destination.
    # print(amt, start, dest)
    # print(ships)
    for i in range(amt):
        ships[dest].append(ships[start].pop())
        # print("Works")
    return ships
    
def rearrange2(ships, amt, start, dest):
    temp = []
    for i in range(amt):
        temp.append(ships[start].pop())
        
    for i in range(amt):
        ships[dest].append(temp.pop())
        # print("Works")
    return ships

def getAnswer(ships):
    answer = ""
    for i in range(1, len(ships)):
        answer += ships[i].pop()
    return answer

def main1():
    print("Hello World!")
    shipData, moveData = parse_data("actual.txt")
    shipData = makeStacks(shipData)

    for line in moveData:
        shipData = rearrange(shipData, int(line[1]), int(line[3]), int(line[5]))
        # print(line)
    print(shipData)
    print(getAnswer(shipData))
    # print(moveData)

def main2():
    print("Hello World!")
    shipData, moveData = parse_data("actual.txt")
    shipData = makeStacks(shipData)

    for line in moveData:
        shipData = rearrange2(shipData, int(line[1]), int(line[3]), int(line[5]))
        # print(line)
    print(shipData)
    print(getAnswer(shipData))
    # print(moveData)

if __name__ == "__main__":
    main2()