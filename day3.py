from aoc import get_input

def get_item_score(item):
    return ord(item) - 96 if ord(item) > 90 else ord(item) - (65-27)

data = get_input(3).split("\n")

result = 0
for line in data:
    half = int(len(line)/2)
    c1, c2 = line[:half], line[half:]

    counted = set()

    for item in c1:
        if item not in counted and item in c2:
            result += get_item_score(item)
            counted.add(item)

print("Part 1", result)

# ok I know this is not readable but it wouldn't be AOC if I didn't write one big list comprehension
print("Part 2", 
    sum([get_item_score((set(l1) & set(l2) & set(l3)).pop()) for l1, l2, l3 in zip(*[iter(data)]*3)])
)