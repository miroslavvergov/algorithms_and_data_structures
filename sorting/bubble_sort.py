elements = list(map(int, input().split()))

n = len(elements)

for i in range(n):
    for j in range(0, n - i - 1):
        if elements[j] > elements[j + 1]:
            elements[j], elements[j + 1] = elements[j + 1], elements[j]