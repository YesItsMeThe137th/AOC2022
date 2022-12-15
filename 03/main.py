def parse_data(fileName):
    with open(fileName, "r") as fd:
        data = fd.read()
        data = data.split()
        return data


def split_data(data):
    #line = line[: len(line) // 2]
    return [[set(line[: len(line) // 2]), set(line[len(line) // 2: ])] for line in data]
    #line2 = line[len(line) // 2: ]

    # for line in data:
    #     left = line[: len(line) // 2]
    #     right = line[len(line) // 2: ]
    #     line = [left, right]
    # print(data)

def set_data(data):
    return ["".join(line[0].intersection(line[1])) for line in data] #very very cheeky

def sumData(data):
    sumData = 0
    for letter in data:
        oldData = sumData
        if ('A' <= letter <= 'Z'):
            sumData += ord(letter) - ord('A') + 27
        else:
            sumData += ord(letter) - ord('a') + 1
        # print(sumData - oldData)

    return sumData

def split_data_two(data):
    print(data)
    newData = []
    for i in range(0, len(data) - 2, 3):
        newData.append([set(data[i]), set(data[i+1]), set(data[i+2])])
    print(newData)
    return newData
  
def set_data_two(data):
    return ["".join(line[0].intersection(line[1]).intersection(line[2])) for line in data] #very very cheeky

def main():

    data = parse_data("example.txt")
    data = split_data(data)
    data = set_data(data)
    theSum = sumData(data)
    # print(theSum)

    data = parse_data("actual.txt")
    data = split_data_two(data)
    data = set_data_two(data)
    theSum = sumData(data)
    print(theSum)
    # Get the compartment

    # Find the item
    # Convert to priority
    # Save priorities and find their sums
    # print(data)
    # print(150 - ord('A'))

if __name__ == "__main__":
    main()