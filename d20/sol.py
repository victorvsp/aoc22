
import numpy as np

def mix_list(list_to_mix, order_of_mixing):
    n = len(list_to_mix)
    for i in range(n):
        idx = order_of_mixing.index(i)
        value = list_to_mix[idx]
        moveInList(list_to_mix, idx, value)
        moveInList(order_of_mixing, idx, value)


def moveInList(my_list, idx, distance):
    n = len(my_list)
    value = my_list.pop(idx)
    new_idx = (idx + distance) % (n-1)
    my_list.insert(new_idx, value)
    return new_idx


def solutionPartOne(encrypted_file):
    n = len(encrypted_file)
    order_of_mixing = list(range(n))
    mix_list(encrypted_file, order_of_mixing)



def solutionPartTwo(encrypted_file):
    n = len(encrypted_file)
    order_of_mixing = list(range(n))
    new_encrypted_file = [num * 811589153 for num in encrypted_file]
    for _ in range(10):
        mix_list(new_encrypted_file, order_of_mixing)
    idx_of_zero = new_encrypted_file.index(0)
    print(new_encrypted_file[(idx_of_zero + 1000) % n] + new_encrypted_file[(idx_of_zero + 2000) % n] + new_encrypted_file[(idx_of_zero + 3000) % n])

##### Main #####

input_file = open("input.txt","r")
encrypted_file = []
for line in input_file:
    encrypted_file.append(int(line))

#solutionPartOne(encrypted_file)
solutionPartTwo(encrypted_file)