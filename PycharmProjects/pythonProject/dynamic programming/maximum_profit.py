#problem:given n elements,each of which has a weight  and profit. determine the maximum profit that can be obtained by
# selecting the subset of the elements no more than capacity

def maximum_profits(weights,profits,capacity):
    n=len(weights)
    table=[[0  for _ in range(capacity+1)] for _ in range(n+1)]
    print(table)
    for i in range(n):
        for c in range(1,capacity+1):
            if weights[i]>c:
                table[i+1][c]=table[i][c]
            else:
                table[i+1][c]=max(table[i][c],profits[i]+table[i][c-weights[i]])
                print(table[i+1][c])
    return table[-1][-1]

print(maximum_profits([23,31,29,44,53,38,63,85,89,82],[92,57,49,68,60,43,67,84,87,72],165))

