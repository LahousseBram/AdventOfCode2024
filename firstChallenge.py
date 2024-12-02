with open("firstChallenge.txt", "r") as f:
    left = []
    right = []
    res = 0
    for line in f.readlines():
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    for i in range(len(left)):
        print(left[i] * right.count(left[i]))
        res += left[i] * right.count(left[i])
print(res)