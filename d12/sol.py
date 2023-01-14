
from collections import deque

def reachable(map, origin, dest):
    if not (origin in map and dest in map):
        return False
    
    origin_height = ord(map[origin])
    dest_height = ord(map[dest])
    return dest_height - origin_height <= 1



def solutionPartOne(map, start, ending):
    dist_to = {}
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    to_visit = deque()
    to_visit.append(start)
    dist_to[start] = 0

    while len(to_visit) > 0:
        position = to_visit.popleft()
        for dir in directions:
            new_position = (dir[0] + position[0], dir[1] + position[1])
            if (not (new_position in dist_to)) and reachable(map, position, new_position):
                dist_to[new_position] = dist_to[position] + 1
                to_visit.append(new_position)

    #print(dist_to)
    print(dist_to[ending])

def solutionPartTwo(map, target):
    dist_to = {}
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    to_visit = deque()
    to_visit.append(target)
    dist_to[target] = 0

    while len(to_visit) > 0:
        position = to_visit.popleft()
        for dir in directions:
            new_position = (dir[0] + position[0], dir[1] + position[1])
            if (not (new_position in dist_to)) and reachable(map, new_position, position):
                dist_to[new_position] = dist_to[position] + 1
                to_visit.append(new_position)

    #print(dist_to)
    print(min(dist_to[pos] for pos in map if map[pos] == 'a' and pos in dist_to))


##### Main #####

input_file = open("d12/input.txt","r")
map = {}
row = 0
starting_position = None
target_position = None
for line in input_file.readlines():
    if "S" in line:
        starting_position = (row, line.find("S"))
        line = line.replace("S", "a")
    if "E" in line:
        target_position = (row, line.find("E"))
        line = line.replace("E", "z")

    for (col, char) in enumerate(line.strip()):
        map[(row, col)] = char
    row += 1 
print(map)
print(starting_position)
print(target_position)
print("=====")
solutionPartOne(map, starting_position, target_position)
solutionPartTwo(map, target_position)                                                