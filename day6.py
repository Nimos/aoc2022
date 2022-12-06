from aoc import AocData

lines = AocData(6).lines()

def get_message_start(lines, packet_length=4):
    for data in lines:
        section = data[0:packet_length]
        pos = 0

        while data:
            pos += 1
            section = section[1:] + data[0]
            data = data[1:]

            unique = True
            for n in range(0,packet_length):
                if section[n] in section[n+1:]:
                    unique = False
            
            if unique:
                return pos


print(get_message_start(lines))
print(get_message_start(lines, 14))