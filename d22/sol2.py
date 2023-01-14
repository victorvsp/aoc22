
from copy import deepcopy
import time

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


FACE_SIZE = 50

UP_T = (0,-1)
DOWN_T = (0,1)
LEFT_T = (-1,0)
RIGHT_T = (1,0)

edge_starting_pos = {
    UP_T : (0,0),
    RIGHT_T: (FACE_SIZE -1, 0),
    DOWN_T: (FACE_SIZE -1, FACE_SIZE -1),
    LEFT_T: (0, FACE_SIZE -1)
}


dir_points = {(1, 0): 0,
              (0, 1): 1,
              (-1,0): 2,
              (0,-1): 3 }

def scaleTuple(scale, tuple):
    return (scale * tuple[0], scale * tuple[1])

def tupleAbsSum(tuple):
    return abs(tuple[0]) + abs(tuple[1])

def sumTuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0],
            tuple1[1] + tuple2[1])

def diffTuples(tuple1, tuple2):
    return (tuple1[0] - tuple2[0],
            tuple1[1] - tuple2[1])

def manDistance(tuple1, tuple2):
    return tupleAbsSum(diffTuples(tuple1, tuple2))

############
def getPointOnEdge(dir, distance):
    dir_on_edge = turnRight(dir)
    return sumTuples(edge_starting_pos[dir],
            scaleTuple(distance, dir_on_edge))

class Face:

    def __init__(self, face_map, horizontal_offset, vertical_offset):
        print("==== New face")
        print(face_map)
        self.face_map = face_map
        self.adj_face = {}
        self.adj_dir = {}
        self.horizontal_offset = horizontal_offset
        self.vertical_offset = vertical_offset

    def getTerrain(self, point):
        return self.face_map[point[1]][point[0]]

    def setAdjFace(self, dir, face, face_side):
        self.adj_face[dir] = face
        self.adj_dir[dir] = face_side
        if face_side not in face.adj_face or face.adj_face[face_side] != self:
            face.setAdjFace(face_side, self, dir)

    def isInBounds(self, pos):
        return pos[0] >= 0 and pos[0] < FACE_SIZE and pos[1] >= 0 and pos[1] < FACE_SIZE


    def movePoint(self, point, dir):

        new_point = sumTuples(point, dir)
        if self.isInBounds(new_point):
            if self.getTerrain(new_point) == ".":
                return self, new_point, dir
            else:
                #print(f"Block [{(self.getTerrain(new_point))}] {new_point}")
                return self, point, dir

        adj_face = self.adj_face[dir]
        adj_dir = self.adj_dir[dir]
        dist_from_start_of_edge = manDistance(point, edge_starting_pos[dir])
        point_on_adj_face = getPointOnEdge(adj_dir, FACE_SIZE -1 - dist_from_start_of_edge)

        if adj_face.getTerrain(point_on_adj_face) == ".":
            # print(" ===== New face ===== ")
            # print(adj_face)
            # print(point_on_adj_face)
            return adj_face, point_on_adj_face, scaleTuple(-1, adj_dir)
        else:
            return self, point, dir

    def getAbsPos(self, pos):
        return (pos[0] + self.horizontal_offset, pos[1] + self.vertical_offset)

    def mapWithPoint(self, point):
        result = f"Face {face_offset_to_index[(self.horizontal_offset, self.vertical_offset)]}\n"
        for y,l in enumerate(self.face_map):
            for x in range(len(l)):
                if (x,y) == point:
                    result += colored(200,0,0,"█")
                else:
                    result += l[x]
            result += "\n"
        return result
        


    def __repr__(self):
        result = f"---- Face: {face_offset_to_index[(self.horizontal_offset, self.vertical_offset)]} -----\n"
        for l in self.face_map:
            result += l + "\n"
        return result


def turnRight(dir):
    return (-dir[1], dir[0])

def turnLeft(dir):
    return (dir[1], -dir[0])


def parseInstructions(instruction_str):
    instruction_list = []
    i = 0
    while i < len(instruction_str):
        if instruction_str[i] in "RL":
            instruction_list.append(instruction_str[i])
            i += 1
        else:
            number_str = []
            while i < len(instruction_str) and instruction_str[i] not in "RL":
                number_str.append(instruction_str[i])
                i += 1
            instruction_list.append(int("".join(number_str)))

    return instruction_list


def solutionPartTwo():
    print("====== SOL 2==================")
    instruction_list = parseInstructions(movement_str)

    current_face = face_list[0]
    pos = (0,0)
    dir = (1,0)

    print(current_face.getAbsPos(pos))
    for cmd in instruction_list:
        if cmd == "R":
            dir = turnRight(dir)
        elif cmd == "L":
            dir = turnLeft(dir)
        else:
            for _ in range(cmd):
                #print(f" ===== Move {dir} from {pos} ")
                current_face, pos, dir = current_face.movePoint(pos, dir)
                # print(current_face.mapWithPoint(pos))
                # time.sleep(0.1)
                print(current_face.getAbsPos(pos))

        #print(f"==== End of Cmd:{pos}, {dir} ====")

    pos = current_face.getAbsPos(pos)
    print(pos)

    print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + dir_points[dir])
    

##### Main #####


file_name = "input.txt"
input_file = open(file_name)
line_list = input_file.readlines()
movement_str = line_list.pop()
line_list.pop()
face_list = []

vertical_offset = 0

while len(line_list) > 0:

    current_block = line_list[:FACE_SIZE]
    line_list = line_list[FACE_SIZE:]
    sample_line = current_block[0]
    offset = 0
    while offset < len(sample_line) and sample_line[offset] == " ":
        offset += 1


    current_block = [l.strip().strip("\n") for l in current_block]
    face_sub_list = [[] for _ in range(len(current_block[0])//FACE_SIZE)]
    for block_line in current_block:
        for i in range(len(block_line)//FACE_SIZE):
            face_sub_list[i].append(block_line[FACE_SIZE*i:FACE_SIZE*(i+1)])

    face_list.extend([Face(face_sub_list[idx], offset + idx*FACE_SIZE, vertical_offset) for idx in range(len(face_sub_list))])
    
    vertical_offset += len(current_block)
    
face_offset_to_index = {}

for (n, f) in enumerate(face_list):
    print(f"----- Face {n}")
    face_offset_to_index[(f.horizontal_offset, f.vertical_offset)] = n
    print(f)


############# input.txt edges ############
if file_name == "input.txt":
    face_list[2].setAdjFace(UP_T, face_list[0], DOWN_T)
    face_list[2].setAdjFace(LEFT_T, face_list[3], UP_T)
    face_list[2].setAdjFace(DOWN_T, face_list[4], UP_T)
    face_list[2].setAdjFace(RIGHT_T, face_list[1], DOWN_T)

    face_list[5].setAdjFace(UP_T, face_list[3], DOWN_T)
    face_list[5].setAdjFace(LEFT_T, face_list[0], UP_T)
    face_list[5].setAdjFace(DOWN_T, face_list[1], UP_T)
    face_list[5].setAdjFace(RIGHT_T, face_list[4], DOWN_T)

    face_list[3].setAdjFace(LEFT_T, face_list[0], LEFT_T)
    face_list[3].setAdjFace(RIGHT_T, face_list[4], LEFT_T)

    face_list[1].setAdjFace(LEFT_T, face_list[0], RIGHT_T)
    face_list[1].setAdjFace(RIGHT_T, face_list[4], RIGHT_T)


# ####### sample.txt edges #########
if file_name == "sample.txt" or file_name == "sample2.txt":
    face_list[3].setAdjFace(UP_T, face_list[0], DOWN_T)
    face_list[3].setAdjFace(LEFT_T, face_list[2], RIGHT_T)
    face_list[3].setAdjFace(DOWN_T, face_list[4], UP_T)
    face_list[3].setAdjFace(RIGHT_T, face_list[5], UP_T)

    face_list[1].setAdjFace(UP_T, face_list[0], UP_T)
    face_list[1].setAdjFace(LEFT_T, face_list[5], DOWN_T)
    face_list[1].setAdjFace(DOWN_T, face_list[4], DOWN_T)
    face_list[1].setAdjFace(RIGHT_T, face_list[2], LEFT_T)

    face_list[2].setAdjFace(UP_T, face_list[0], LEFT_T)
    face_list[2].setAdjFace(DOWN_T, face_list[4], LEFT_T)

    face_list[5].setAdjFace(LEFT_T, face_list[4], RIGHT_T)
    face_list[5].setAdjFace(RIGHT_T, face_list[0], RIGHT_T)

solutionPartTwo()