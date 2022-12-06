###
# please do not read this I rushed it and it's bad style
# I can barely read it myself the next day lol


from collections import defaultdict
import re
from aoc import AocData

data = AocData(5).text(True).split("\n")

cargo = defaultdict(list)
def read_stack(data):  
    data = data.split("\n")
    line = data.pop(0)
    while line and not "1" in line:
        
        stacks = [x for idx, x in enumerate(line) if idx % 4 == 1]
        for idx, item in enumerate(stacks):
            if item != " ":
                cargo[idx].append(item)
    
        line = data.pop(0)

    return cargo, data[1:]


def read_instructions(stacks, instructions):
    for instruction in instructions:
        if not instruction: 
            continue
        _, quan, _, src, _, dst = instruction.split(" ")

        for x in range(0, int(quan)):
            if not stacks[int(src)-1]:
                continue
            
            item = stacks[int(src)-1].pop(0)

            stacks[int(dst)-1].insert(0, item)
        

    return stacks

stacks, instructions = read_stack(data)

r = read_instructions(stacks, instructions)

print("".join([r[k][0] for k in sorted(r.keys())]))

cargo = defaultdict(list)
def read_instructions2(stacks, instructions):
    for instruction in instructions:
        if not instruction: 
            continue
        _, quan, _, src, _, dst = instruction.split(" ")

        if not stacks[int(src)-1]:
            continue
        
        item = stacks[int(src)-1][0:int(quan)]
        del stacks[int(src)-1][0:int(quan)]

        stacks[int(dst)-1] = item + stacks[int(dst)-1]
        

    return stacks
data = AocData(5).text(False).split("\n")

stacks, instructions = read_stack(data)
r2 = read_instructions2(stacks, instructions)

print("".join([r2[k][0] for k in sorted(r2.keys()) if r2[k]]))