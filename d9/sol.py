import numpy as np

letter_to_tuple = {
    "R": (0, 1),
    "U": (1, 0),
    "L": (0,-1),
    "D": (-1, 0)
}

def moveTail(tail, head):
    if max(abs(tail[i] - head[i]) for i in range(2)) <= 1:
        return (tail[0], tail[1])

    vertical_diff = head[0] - tail[0]
    horizontal_diff = head[1] - tail[1]
    return (tail[0] + np.sign(vertical_diff),
        tail[1] + np.sign(horizontal_diff))





def solutionPartOne(input):
    head = (0,0)
    tail = (0,0)
    print(tail)
    visited_positions = set()
    visited_positions.add(tail)
    for (direction_letter, n_steps) in input:
        dir_tuple = letter_to_tuple[direction_letter]
        for i in range(n_steps):
            head = (head[0] + dir_tuple[0],
                 head[1] + dir_tuple[1])
            tail = moveTail(tail, head)
            visited_positions.add(tail)
    print(len(visited_positions))


def solutionPartTwo(input):
    tail_list = [(0,0) for i in range(10)]
    visited_positions = set()
    visited_positions.add(tail_list[9])
    for (direction_letter, n_steps) in input:
        dir_tuple = letter_to_tuple[direction_letter]
        tail_list[0]
        for i in range(n_steps):
            tail_list[0] = (tail_list[0][0] + dir_tuple[0],
                 tail_list[0][1] + dir_tuple[1])
            for i in range(1,len(tail_list)):
                tail_list[i] = moveTail(tail_list[i], tail_list[i-1])
            visited_positions.add(tail_list[9])
        print("T9: {} | H: {} ".format(tail_list[9], tail_list[0]))
    print(len(visited_positions))


##### Main #####

input = []
with open("input.txt", "r") as input_file:
    for line in input_file:
        (direction, number_str) = line.split()
        input.append([direction, int(number_str)])

solutionPartOne(input)
solutionPartTwo(input)                                                