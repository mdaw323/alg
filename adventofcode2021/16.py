import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

message = [l.strip() for l in fileinput.input()][0]
# message = 'C200B40A82'
bm = ''
for c in message:
    bm += bin(int(c,16))[2:].zfill(4)

p1 = 0

def read_package():
    global i
    global p1
    print(f"read_package from {i}")
    version = int(bm[i:i+3],2)
    p1+=version
    i+=3
    type_id = int(bm[i:i+3],2)
    i+=3
    print(version,type_id)
    if type_id == 4: # literal
        b = bm[i]
        i+=1
        packet = ''
        while b == '1':
            value = bm[i:i+4]
            packet += value
            # print(value)
            i+=4
            b = bm[i]
            i+=1
        value = bm[i:i+4]
        packet += value
        i+=4
        packet_value = int(packet,2)
        print(f"packet_value {packet_value}")
        return packet_value
    else:
        lenght_type_id = bm[i]
        i+=1
        values = []
        if lenght_type_id == '0':
            length = int(bm[i:i+15],2)
            i+=15
            end_of_subpackets = i+length
            print(f"value: {lenght_type_id} {length} ")
            while i<end_of_subpackets:
                values.append(read_package())

        else:
            number_of_subpackets = int(bm[i:i+11],2)
            i+=11
            print(f"subpackets: {number_of_subpackets}")
            for packet in range(number_of_subpackets):
                values.append(read_package())
        print(values)
        if type_id == 0:
            return sum(values)
        elif type_id ==1:
            m = 1
            for val in values:
                m*=val
            return m
        elif type_id == 2:
            return min(values)
        elif type_id == 3:
            return max(values)
        elif type_id == 5:
            return 1 if values[0] > values[1] else 0
        elif type_id ==6:
            return 1 if values[0] < values[1] else 0
        elif type_id == 7:
            return 1 if values[0] == values[1] else 0

i = 0
v = read_package()

print(f"p1: {p1} p2: {v}")
