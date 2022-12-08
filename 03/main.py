def parse_data(fileName):
    with open(fileName, "r") as fd:
        data = fd.read()
        data = [item.split("\n") for item in data]
        #line = line[: len(line) // 2]
        #line2 = line[len(line) // 2: ]
        return data

def main():
    print("Hello World!")
    data = parse_data("example.txt")
    # Get the compartment
    # Find the item
    # Convert to priority
    # Save priorities and find their sums




    print(data)
    # print(150 - ord('A'))

if __name__ == "__main__":
    main()