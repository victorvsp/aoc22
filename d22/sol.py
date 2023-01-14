class MapRow:

    def __init__(self, horizontal_offset, row_string):
        self.offset = horizontal_offset
        self.row_str = row_string 
    
    def startX(self):
        return self.offset

    def endX(self):
        return self.offset + len(self.row_str)
    
    def getCol(self, col):
        return self.row_str[col - self.offset]

    def colIsIn(self, col):
        return col >= self.startX() and col < self.endX()

    def colIdx(self, col):
        return (col - self.offset) % len(self.row_str) + self.offset

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


def solutionPartOne():
    instruction_list = parseInstructions(movement_str)

    pos = (map_rows_list[0].offset,0)
    dir = (1,0)
    n_rows = len(map_rows_list)
    for cmd in instruction_list:
        print("=====")
        if cmd == "R":
            dir = (-dir[1], dir[0])
        elif cmd == "L":
            dir = (dir[1], -dir[0])
        else:
            for _ in range(cmd):
                print(f"Move {dir} from {pos} ")
                current_row = map_rows_list[pos[1]]
                candidate_pos = (current_row.colIdx(pos[0] + dir[0]),
                                pos[1] + dir[1])
                candidate_row = map_rows_list[candidate_pos[1] % n_rows]
                if candidate_pos[1] >= n_rows or candidate_pos[1] < 0 or not candidate_row.colIsIn(candidate_pos[0]):
                    if candidate_pos[1] < vertical_start_pos[candidate_pos[0]]:
                        candidate_pos = (candidate_pos[0],
                                        vertical_end_pos[candidate_pos[0]]
                                        )
                    elif candidate_pos[1] > vertical_end_pos[candidate_pos[0]]:
                        candidate_pos = (candidate_pos[0],
                                        vertical_start_pos[candidate_pos[0]]
                                        )
                    else:
                        print(f"what {candidate_pos}")
                    candidate_row = map_rows_list[candidate_pos[1]]
                if candidate_row.getCol(candidate_pos[0]) == ".":
                    pos = candidate_pos
        print(f"==== NEW:{pos}, {dir} ====")

    print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + dir_points[dir])
    





def solutionPartTwo():
    pass

##### Main #####

dir_points = {(1, 0): 0,
              (0, 1): 1,
              (-1,0): 2,
              (0,-1): 3 }


input_file = open("input.txt","r")
line_list = input_file.readlines()
movement_str = line_list.pop()
line_list.pop()
map_rows_list = []
max_row_size = -1
vertical_start_pos = {}
vertical_end_pos = {}

for row_number, line in enumerate(line_list):

    max_row_size = max(max_row_size, len(line.strip("\n")))
    offset = 0
    while offset < len(line) and line[offset] == " ":
        offset += 1
    current_map_row = MapRow(offset, line.strip())
    map_rows_list.append(current_map_row)
    #print(f"{current_map_row.startX()},{current_map_row.endX()}")
    for col in range(max_row_size):
        if col not in vertical_start_pos:
            if current_map_row.colIsIn(col):
                vertical_start_pos[col] = row_number
        elif col not in vertical_end_pos and not current_map_row.colIsIn(col):
            vertical_end_pos[col] = row_number -1

print(max_row_size)
for i in range(max_row_size):
    if i not in vertical_end_pos:
        vertical_end_pos[i] = len(map_rows_list) - 1
    print(f"[{i}] : {vertical_start_pos[i]} - {vertical_end_pos[i]}")
print(movement_str)

solutionPartOne()
#solutionPartTwo(encrypted_file)