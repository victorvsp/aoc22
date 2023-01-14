import numpy as np
import math


def sumTuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0],
            tuple1[1] + tuple2[1])

def newSandPosition(filled_positions, sand_position, floor_y = math.inf):
    
    candidate_directions = [(0,1), (-1,1), (1,1)]
    for dir in candidate_directions:
        candidate_position = sumTuples(sand_position, dir)
        if not (candidate_position in filled_positions or candidate_position[1] >= floor_y):
            return candidate_position
    return sand_position

def solutionPartOne(filled_positions, max_y):

    total_sand = 0
    while True:
        
        current_pos = (500,0)
        previous_pos = None
        while previous_pos != current_pos and current_pos[1] <= max_y:
            previous_pos = current_pos
            current_pos = newSandPosition(filled_positions, previous_pos)
        
        if current_pos[1] > max_y:
            break

        total_sand += 1
        filled_positions.add(current_pos)

    print(total_sand)
    

def solutionPartTwo(filled_positions, max_y):
    total_sand = 0
    while True:
        
        current_pos = (500,0)
        previous_pos = None
        while previous_pos != current_pos:
            previous_pos = current_pos
            current_pos = newSandPosition(filled_positions, previous_pos, floor_y = max_y + 2)

        total_sand += 1
        filled_positions.add(current_pos)
        if current_pos == (500,0):
            break

    print(total_sand)

def addLineToMap(filled_positions, start, end):
    direction = (np.sign(end[0] - start[0]), np.sign(end[1] - start[1]))
    current_pos = start

    while current_pos != end:
        filled_positions.add(current_pos)
        current_pos = sumTuples(current_pos, direction)
    
    filled_positions.add(current_pos)

    

##### Main #####

input_file = open("input.txt","r")
line_list = input_file.readlines()
filled_positions = set()
max_y = - math.inf



for line in line_list:
    pair_list = [pair_str.strip(" ").split(",") for pair_str in line.split("->")]
    pair_list = [(int(pair[0]), int(pair[1])) for pair in pair_list]
    for i in range(len(pair_list) -1):
        addLineToMap(filled_positions, pair_list[i], pair_list[i + 1])

    for pair in pair_list:
        max_y = max(max_y, pair[1])

    
#solutionPartOne(filled_positions, max_y)
solutionPartTwo(filled_positions, max_y)