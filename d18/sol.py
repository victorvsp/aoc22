from collections import deque


def sumTuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0],
            tuple1[1] + tuple2[1],
            tuple1[2] + tuple2[2])

def diffTuples(tuple1, tuple2):
    return (tuple1[0] - tuple2[0],
            tuple1[1] - tuple2[1])

def adjCubes(cube, min_coord = None, max_coord = None):
    adj_list = []
    for idx in range(3):
        for sign in [1,-1]:
            direction = [0,0,0]
            direction[idx] = sign
            new_cube = sumTuples(cube, direction)
            if min_coord != None and max_coord != None:
                if sum([new_cube[i] < min_coord[i] or new_cube[i] > max_coord[i] for i in range(3)]) > 0:
                    continue
            adj_list.append(new_cube)
    return adj_list



def computeSurfaceArea(cube_list):
    cube_set = set(cube_list)
    total_exposed_faces = 0
    for cube in cube_set:
        for adj_cube in adjCubes(cube):
            if adj_cube not in cube_set:
                total_exposed_faces += 1
    return total_exposed_faces

def solutionPartOne(cube_list):
    print(computeSurfaceArea(cube_list))

def bfs(starting_cube, forbidden_set, min_coord, max_coord):
    visited = set([starting_cube])
    to_be_visited = deque()
    to_be_visited.appendleft(starting_cube)

    while  len(to_be_visited) > 0:
        cube = to_be_visited.pop()
        for adj_cube in adjCubes(cube, min_coord, max_coord):
            if adj_cube not in visited and adj_cube not in forbidden_set:
                visited.add(adj_cube)
                to_be_visited.appendleft(adj_cube)

    return visited

            

def solutionPartTwo(cube_list):
    total_surface_area = computeSurfaceArea(cube_list)

    min_coord = [2**31] * 3
    max_coord = [-1] * 3

    for cube in cube_list:
        for i in range(3):
            min_coord[i] = min(min_coord[i], cube[i])
            max_coord[i] = max(max_coord[i], cube[i])

    for i in range(3):
            min_coord[i] -= 3
            max_coord[i] += 4


    magma_points = set(cube_list)
    outside_points = bfs((min_coord[0],min_coord[1], min_coord[2]),       
                        magma_points,
                        min_coord,
                        max_coord)
                    

    visited_points = outside_points | magma_points

    trapped_surface_area = 0
    
    for x in range(min_coord[0], max_coord[0]):
        for y in range(min_coord[1], max_coord[1]):
            for z in range(min_coord[2], max_coord[2]):
                cube = (x,y,z)
                if cube not in visited_points:
                    air_bubble = bfs(cube, 
                                    visited_points,
                                    min_coord,
                                    max_coord)
                    trapped_surface_area += computeSurfaceArea(air_bubble)
                    visited_points = visited_points | air_bubble
    
    print(total_surface_area - trapped_surface_area)



##### Main #####

input_file = open("input.txt","r")
cube_list = []
for line in input_file:
    cube_str = line.strip("\n").split(",")
    cube_list.append((int(cube_str[0]), int(cube_str[1]), int(cube_str[2])))

solutionPartOne(cube_list)
solutionPartTwo(cube_list)
