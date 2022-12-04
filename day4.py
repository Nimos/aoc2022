from aoc import AocData

data = AocData(4)


r1 = r2 = 0
for pair in data.lines():
    a, b = pair.split(",")
    a_0, a_1, b_0, b_1 = [int(num) for num in a.split("-") + b.split("-")]


    if a_0 <= b_1 and b_0 <= a_1:
        r2 += 1

    if (a_0 >= b_0 and a_1 <= b_1) or (a_0 <= b_0 and a_1 >= b_1):
        r1 += 1


print(f"Part 1: {r1}") 
print(f"Part 2: {r2}") 
