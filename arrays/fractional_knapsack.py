## Fractional Knapsack

def solve():
    arr = [(60, 10), (100, 20), (200, 50), (100, 50)]
    W = 90

    # Sort by value/weight ratio in descending order
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)

    currW = 0
    finalValue = 0

    for i in range(len(arr)):

        if currW + arr[i][1] <= W:
            currW += arr[i][1]
            finalValue += arr[i][0]

        else:
            remain = W - currW
            cost = (arr[i][0] / arr[i][1]) * remain
            finalValue += cost
            break

    return finalValue


print(solve())