def initData():
    global n, k, data
    print("Input: number of floors and number of balls: ", end="")
    n, k = map(int, input().split())

    # If the total number of throws for binary search does not satisfy the conditions, decrease `k`.
    # An array `data` is created to store throw data.
    if n + 1 <= 2 ** k and int((n + 1).bit_length()) < k:
        k = int((n + 1).bit_length())
        print(f"""
                Number of balls exceeds the minimum number of balls for binary search.
                Extra balls will be discarded. Remaining number of balls {k}.
                """)

    data = [[1] for _ in range(k)]

# Runs a loop calling the `iterTime` function
# and checks the condition with `checkTime`.
def handleData():
    flag = True
    while flag:
        iterTime()
        flag = checkTime()

# Increases the number of floors for each ball.
# For each ball, the new floor for the throw is calculated.
def iterTime():
    data[0].append(data[0][-1] + 1)
    for i in range(1, k):
        floor = 1 + data[i - 1][-2] + data[i][-1]
        data[i].append(floor)

# Checks if the number of floors `n` is reached in the data array.
def checkTime():
    return n > data[k - 1][-1]

def printinf():
    print(f"Number of throws required: {data[0][-1]}")

def process():
    row = len(data[0]) - 1
    column = getStartProcessingColumn()
    underground = 0  # underground - variable to store the lower bound of the search range.
    broker = n + 1  # broker - This variable will store the upper bound of the search range.

    iterationsData = iteration(row, column, underground, broker)  # performs checking and correction of the search range.
    underground, broker = iterationsData

    finish(underground, broker)

# Determines the starting column for the processing.
def getStartProcessingColumn():
    for column in range(k):
        if data[column][-1] >= n:
            break
    return column

# Performs iteration processing, reducing the search bounds based on user responses.
def iteration(row, column, underground, broker):
    while column != 0 and row != 0:
        floor = data[column - 1][row - 1] + 1
        print(f"Start from floor {min(n, underground + floor)}")
        answer = input()
        if answer == "Broken":
            broker = min(n, underground + floor)
            row -= 1
            column -= 1
            if broker - 1 == underground:
                break
        elif answer == "Not Broken":
            underground = min(n, underground + floor)
            row -= 1
            if underground >= n:
                underground = n
                break
        else:
            print("Invalid response. Please use \"Broken\" or \"Not Broken\".")
    return underground, broker

# Processes final scenarios: not enough floors for breaking, found breaking floor, additional throws for precise determination.
def finish(underground, broker):
    if underground == n:
        print(f"{n} floors are insufficient for the balls to break.")
        exit(0)
    elif broker - 1 == underground:
        finishWithBroker(broker)
    else:
        while broker - 1 != underground:
            print(f"Try dropping from floor {underground + 1}")
            answer = input()
            if answer == "Broken":
                finishWithBroker(underground + 1)
            elif answer == "Not Broken":
                underground += 1
            else:
                print("Invalid response. Please use \"Broken\" or \"Not Broken\".")
        finishWithBroker(broker)

def finishWithBroker(broker):
    print(f"Balls start breaking from floor {broker}.")
    exit(0)

if __name__ == "__main__":
    n, k, data = 0, 0, []
    initData()
    handleData()
    printinf()
    process()
