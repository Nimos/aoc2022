with open("day1.txt") as file:
    data = file.read().split("\n")


results = []
cur = 0
for line in data:
    if line:
        cur += int(line)
    else:
        results.append(cur)
        cur=0

results = sorted(results)
print(results[-1])


print(results[-1] + results[-2] + results[-3])