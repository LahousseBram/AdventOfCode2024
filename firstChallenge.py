with open("firstChallenge.txt", "r") as f:
    left = []
    right = []
    res = 0
    for line in f.readlines():
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    left.sort()
    right.sort()
    for i in range(len(left)):
        res += abs((left[i] - right[i]))
print(res)