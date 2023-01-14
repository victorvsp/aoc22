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


def solutionPartOne():
    pass
    

##### Main #####

NORTH = (-1,0)


input_file = open("input.txt","r")

for row_num, line in enumerate(input_file.readlines()):
    for cell in enumerate(line):
    
solutionPartOne()
#solutionPartTwo(encrypted_file)