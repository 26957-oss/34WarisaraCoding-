start = int(input())
end = int(input())

for i in range(start, end + 1):
    for j in range(1, 13):
        print(i, "x", j, "=", i * j)