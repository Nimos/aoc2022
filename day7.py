from collections import defaultdict

from aoc import AocData

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
P1_MIN = 100000


class FakeShell:
    current_pwd = []

    size_dict = defaultdict(int)

    def cd(self, path):
        path = path.split("/")

        if path[0] == "":
            self.current_pwd = []
            path = path[1:]

        for dir in path:
            if dir == "..":
                self.current_pwd.pop()
            else:
                self.current_pwd.append(dir)

    def read_ls(self, data):
        while data and not data[0].startswith("$"):
            size, file = data.pop(0).split(" ")
            if size != "dir":
                self.add_size(self.current_pwd, size)

    def add_size(self, pwd, size):
        for level in range(0, len(pwd)):
            dir = "/".join(pwd[0:level + 1])
            self.size_dict[dir] += int(size)

    def __init__(self, instructions):
        while instructions:
            instruction = instructions.pop(0)[2:].split(" ")

            if instruction[0] == "ls":
                self.read_ls(instructions)
            elif instruction[0] == "cd":
                self.cd(instruction[1])

    def solve1(self):
        total = 0
        for dir, size in self.size_dict.items():
            if size < P1_MIN:
                total += size

        return total

    def solve2(self):
        min_to_free = REQUIRED_SPACE - (TOTAL_SPACE - self.size_dict[""])
        for size in sorted(self.size_dict.values()):
            if size > min_to_free:
                return size


lines = AocData(7).lines()

sh = FakeShell(lines)

print(sh.solve1())
print(sh.solve2())
