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

# none of this is very pretty code 😔

with open("day2.txt") as file:
    data = file.read().split("\n")

RSP_SCORES = {"X": 1, "Y": 2, "Z": 3, "WIN": 6, "DRAW": 3}

MAP = {"A": "X", "B": "Y", "C": "Z"}

WINS = {"X": "Z", "Y": "X", "Z": "Y"}
LOSS = {"X": "Y", "Y": "Z", "Z": "X"}

score = 0
for line in data:
    me = line[-1]
    them = MAP[line[0]]
    if me == them:
        score += RSP_SCORES["DRAW"]
    elif WINS[me] == them:
        score += RSP_SCORES["WIN"]

    score += RSP_SCORES[me]

print(score)

score2 = 0
for line in data:
    them = MAP[line[0]]
    result = line[-1]
    if result == "Z":
        me = LOSS[them]
    elif result == "Y":
        me = them
    else:
        me = WINS[them]

    if me == them:
        score2 += RSP_SCORES["DRAW"]
    elif WINS[me] == them:
        score2 += RSP_SCORES["WIN"]

    score2 += RSP_SCORES[me]


print(score2)