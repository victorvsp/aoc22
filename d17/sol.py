import matplotlib.pyplot as plt
from collections import defaultdict


def sumTuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0],
            tuple1[1] + tuple2[1])

def diffTuples(tuple1, tuple2):
    return (tuple1[0] - tuple2[0],
            tuple1[1] - tuple2[1])


rock_types = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (1, -1), (1, -2), (0,-1), (2,-1)],
    [(2,0), (2, -1), (2, -2), (1,-2), (0,-2)],
    [(0,0), (0,-1), (0,-2), (0,-3)],
    [(0,0), (0,-1), (1,0), (1,-1)],
]

movement_to_tuple = {
    ">": (1,0),
    "<": (-1,0),
    "v": (0,-1)
}


def drawRoom(filled_positions, y_max):
    drawing = [["." for _ in range(7)] for _ in range(y_max + 1)]
    for (x,y) in filled_positions:
        print(f"({x}, {y}) | {y_max}")
        drawing[y][x] = "#"

    print("=======")
    for y in range(y_max, 0, -1):
        print("".join(drawing[y]))
    print("=======")


def canMove(move_tuple, rock, anchor_point, filled_spaces):

    for rock_offset in rock:
        rock_pos = sumTuples(anchor_point, rock_offset)
        new_rock_pos = sumTuples(rock_pos, move_tuple)
        if new_rock_pos[0] < 0 or new_rock_pos[0] > 6 or new_rock_pos[1] < 0 or new_rock_pos in filled_spaces:
            return False

    return True

def maxRockHeight(air_jets, number_of_rocks):
    filled_spaces = set([(x,0) for x in range(7)])
    current_y_max = 0
    current_air_jet_idx = 0
    max_y_vec = [0 for _ in range(7)]
    old_y = 0

    repeats = defaultdict(int)
    first_repeat = None

    warmup_number_of_rocks = -1
    warmup_height = -1
    cycle_height_increments = []

    for rock_number in range(number_of_rocks):
        stopped = False
        current_rock_type = rock_types[rock_number % len(rock_types)]
        rock_y_offset = min([y for (x,y) in current_rock_type])
        current_anchor_point = (2, - rock_y_offset + current_y_max + 4)
        repeats[(rock_number % len(rock_types), current_air_jet_idx)] += 1
        if first_repeat == None and repeats[(rock_number % len(rock_types), current_air_jet_idx)] > 1:
            first_repeat = (rock_number % len(rock_types), current_air_jet_idx)
            # print("===================")
            # print(f"{current_y_max - old_y} ({rock_number})")
            old_y = current_y_max
            warmup_height = current_y_max
            warmup_number_of_rocks = rock_number
            # print(max_y_vec)
            # print("----------------------")
        if repeats[(rock_number % len(rock_types), current_air_jet_idx)] > 2:
            break


        while not stopped:
            
            airjet_tuple = movement_to_tuple[air_jets[current_air_jet_idx]]
            current_air_jet_idx = (current_air_jet_idx + 1) % len(air_jets)
            if canMove(airjet_tuple, current_rock_type, 
                    current_anchor_point, filled_spaces ):
                #print(f"Moved {air_jets[current_air_jet_idx]}!")
                current_anchor_point = sumTuples(current_anchor_point, airjet_tuple)

            stopped = not canMove((0,-1), current_rock_type, current_anchor_point, filled_spaces)

            if not stopped:
                #rint("Moved down!")
                current_anchor_point = sumTuples(current_anchor_point, (0,-1))


        new_y_max = max(current_y_max, current_anchor_point[1])
        if first_repeat != None:
            cycle_height_increments.append(new_y_max - current_y_max)
        current_y_max = new_y_max

        for rock_cell in current_rock_type:
            rock_part_position = sumTuples(current_anchor_point, rock_cell)
            filled_spaces.add(rock_part_position)

    cycle_height = sum(cycle_height_increments)
    post_warmup_rocks = number_of_rocks - warmup_number_of_rocks

    if len(cycle_height_increments) > 0:
        total_height = warmup_height
        total_height += (post_warmup_rocks // len(cycle_height_increments))* cycle_height
        total_height += sum( cycle_height_increments[:post_warmup_rocks % len(cycle_height_increments)]) 
    else:
        total_height = current_y_max

    return total_height



def solutionPartOne(air_jets):
    print(maxRockHeight(air_jets, 2022))
            

def solutionPartTwo(air_jets):
    print(maxRockHeight(air_jets, 1000000000000))



##### Main #####

input_file = open("input.txt","r")
air_jets = input_file.readline().strip("\n")
solutionPartOne(air_jets)
solutionPartTwo(air_jets)