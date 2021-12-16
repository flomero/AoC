import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/16/" + source + ".txt"

with open(file, 'r') as f:
  input = f.read().split()

binput = ""

for i in input:
    i = bin(int(i, 16))[2:]
    binput = binput + str(i)

print(binput)

version_sum = 0

def add_version(bin):
    global version_sum
    version_sum += int("".join(bin), 2)
    print("new sum: " + str(version_sum))

def todec(bin):
    return int("".join(bin), 2)

def parse(packet):
    print("rest: " + packet)
    version = packet[:3]
    print(version)
    add_version(version)
    packet = packet[3:]
    tid = packet[:3]
    packet = packet[3:]
    if tid == "100":
        sub_packets = []
        while True:
            group = packet[:5]
            packet = packet[5:]
            sub_packets += group[1:]
            print("Test: " + group)
            if group[0] == "0": break
        return todec(sub_packets), packet
    ltid = packet[0]
    packet = packet[1:]
    subvals = []
    if ltid == "0":
        length = todec(packet[:15])
        packet = packet[15:]
        subpacket = packet[:length]
        packet = packet[length:]
        while length > 0:
            subval, subpacket = parse(subpacket)
            subvals.append(subval)
        print("ltid " + ltid)
    else:
        number = todec(packet[:11])
        packet = packet[11:]
        for i in range(number):
            subval, packet = parse(packet)
            subvals.append(subval)
    val = 1
    return val, packet

parse(binput)

print(version_sum)




