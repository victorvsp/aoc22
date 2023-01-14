
import numpy as np
from functools import cmp_to_key

def comparePackets(pkt1, pkt2):
    if type(pkt1) == int and type(pkt2) == int:
        return np.sign(pkt1 - pkt2)

    if type(pkt1) == int:
        pkt1 = [pkt1]
    if type(pkt2) == int:
        pkt2 = [pkt2]

    min_len = min(len(pkt1), len(pkt2))

    for i in range(min_len):
        test_result = comparePackets(pkt1[i], pkt2[i])
        if test_result != 0:
            return test_result

    return np.sign(len(pkt1) - len(pkt2))



def solutionPartOne(pairs_list):

    idx_sum = 0
    for (idx, pair) in enumerate(pairs_list):
        result = comparePackets(pair[0], pair[1])
        if result < 0:
            idx_sum += idx + 1
    
    print(idx_sum)

def solutionPartTwo(pairs_list):
    
    divider_pkts = [
        [[2]],
        [[6]]
    ]
    pkt_list = []
    pkt_list.extend(divider_pkts)

    for (pkt1, pkt2) in pairs_list:
        pkt_list.append(pkt1)
        pkt_list.append(pkt2)

    pkt_list.sort(key = cmp_to_key(comparePackets))
    result = 1
    for idx, pkt in enumerate(pkt_list):
        if pkt in divider_pkts:
            result *= idx + 1
    print(result)

##### Main #####

input_file = open("input.txt","r")
line_list = input_file.readlines()
pairs_list = []
while len(line_list) > 0:
    current_pair_lines = line_list[:3]
    pairs_list.append((
        eval(current_pair_lines[0]), eval(current_pair_lines[1])
        ))
    line_list = line_list[3:]
    
solutionPartOne(pairs_list)
solutionPartTwo(pairs_list)                                                