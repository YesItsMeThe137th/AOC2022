    
def parse_data(fileName):
    with open(fileName, "r") as fd:
        data = fd.read().split("\n")
        print(data)
        data = [d.split(",") for d in data]
        data = [[d.split("-") for d in dat] for dat in data]
        data = [[[int(d) for d in da] for da in dat] for dat in data]
        return data



def main1():
    data = parse_data("actual.txt")
    print(data)
    counter = 0
    for partners in data:
        p1, p2 = partners
        if (p1[0] >= p2[0] and p1[1] <= p2[1]):
            counter += 1
            # print("p1 < p2", partners)
        elif (p2[0] >= p1[0] and p2[1] <= p1[1]):
            counter += 1
            # print("p2 < p1", partners)

    print(counter)

def main2():
    data = parse_data("actual.txt")
    print(data)
    counter = 0
    for p1, p2 in data:
        # the range of the numbers
        if (p1[0] >= p2[0] and p1[0] <= p2[1]):
            counter += 1
            print (p1, p2)
        elif (p1[1] >= p2[0] and p1[1] <= p2[1]): 
            counter += 1
            print (p1, p2)
        elif (p1[0] >= p2[0] and p1[1] <= p2[1]):
            counter += 1
            # print("p1 < p2", partners)
        elif (p2[0] >= p1[0] and p2[1] <= p1[1]):
            counter += 1
    print(counter)


if __name__ == "__main__":
    main2()

