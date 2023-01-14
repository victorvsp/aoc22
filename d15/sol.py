
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


def solutionPartOne(beacon_sensor_list):
    print(" ===== Part 1 =====")
    target_line = 10
    impossible_spaces = set()

    for (sensor, beacon) in beacon_sensor_list:

        radius = tupleAbsSum(diffTuples(sensor, beacon))
        remaining_budget = max(0, radius - abs(target_line - sensor[1]))
        for column in range(sensor[0]-remaining_budget, sensor[0] + remaining_budget + 1):
            impossible_spaces.add(column)
    
    for (_, beacon) in beacon_sensor_list:
        if beacon[1] == target_line and beacon[0] in impossible_spaces:
            impossible_spaces.remove(beacon[0])

    print(len(impossible_spaces))

def withinLimits(tuple, max_coord):
    return tuple[0] >= 0 and tuple[1] >= 0 and tuple[0] <= max_coord and tuple[1] <= max_coord

def solutionPartTwo(beacon_sensor_list):
    print(" ===== Part 2 =====")
    max_coord = 4000000
    candidate_spots = set()
    impossible_spots = set()

    for (sensor, beacon) in beacon_sensor_list:
        radius = tupleAbsSum(diffTuples(sensor, beacon))
        print(" ==== Sensor: {} | Radius: {}".format(sensor, radius))
        direction_list = [(1, -1), (-1,-1), (-1,1), (1,1)]
        current_candidate = sumTuples(sensor, (0, radius + 1))
        next_candidate = current_candidate
        for direction in direction_list:
            while manDistance(next_candidate, sensor) == radius + 1:
                current_candidate = next_candidate
                #print("-> {}".format(current_candidate))
                if not (current_candidate in impossible_spots) and withinLimits(current_candidate, max_coord): 
                    candidate_spots.add(current_candidate)
                next_candidate = sumTuples(current_candidate, direction)
        new_impossible_spots = set()
        for candidate in candidate_spots:
            if manDistance(candidate, sensor) <= radius:
                new_impossible_spots.add(candidate)
        for spot in new_impossible_spots:
            candidate_spots.remove(spot)
            impossible_spots.add(spot)
    
    #print(candidate_spots)
    for candidate in candidate_spots:
        possible = True
        for (sensor, beacon) in beacon_sensor_list:
                radius = manDistance(sensor, beacon)
                if manDistance(candidate, sensor) <= radius:
                    possible = False
                    break
        if possible:
            print(candidate)
            print(candidate[0]*4000000 + candidate[1])


    # for (sensor, beacon) in beacon_sensor_list:

    #     radius = tupleAbsSum(diffTuples(sensor, beacon))
    #     remaining_budget = max(0, radius - abs(target_line - sensor[1]))
    #     for column in range(sensor[0]-remaining_budget, sensor[0] + remaining_budget + 1):
    #         impossible_spaces.add(column)
    
    # for (_, beacon) in beacon_sensor_list:
    #     if beacon[1] == target_line and beacon[0] in impossible_spaces:
    #         impossible_spaces.remove(beacon[0])

    # print(len(impossible_spaces))

##### Main #####

input_file = open("input.txt","r")
beacon_sensor_list = []
for line in input_file:
    clean_line = line.replace("Sensor at ", "").strip("\n")
    clean_line = clean_line.replace(" closest beacon is at ", "")
    clean_line = clean_line.replace("x=", "")
    clean_line = clean_line.replace("y=", "")
    str_pair_list = [pair.split(",") for pair in clean_line.split(":")]
    print(str_pair_list)
    sensor_beacon_pair = [(int(pair[0]), int(pair[1])) for pair in str_pair_list]
    beacon_sensor_list.append(sensor_beacon_pair)

    
solutionPartOne(beacon_sensor_list)
solutionPartTwo(beacon_sensor_list)