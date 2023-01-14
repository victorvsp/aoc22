from collections import defaultdict

# def tupleAbsSum(tuple):
#     return abs(tuple[0]) + abs(tuple[1])

# def sumTuples(tuple1, tuple2):
#     return (tuple1[0] + tuple2[0],
#             tuple1[1] + tuple2[1])

# def diffTuples(tuple1, tuple2):
#     return (tuple1[0] - tuple2[0],
#             tuple1[1] - tuple2[1])

# def manDistance(tuple1, tuple2):
#     return tupleAbsSum(diffTuples(tuple1, tuple2))

part1_sol = {}



def optPressureRelease(memoised_solutions,
                     open_valves,
                     time_left,
                     current_valve,
                     valve_values,
                     adjacent_to):
    open_vec = "".join([str(int(valve in open_valves)) for valve in valve_values.keys()])

    if (current_valve, time_left, open_vec) in memoised_solutions:
        return memoised_solutions[(current_valve, time_left, open_vec)]
    if time_left <= 0:
        return 0


    current_flow = sum([valve_values[valve] for valve in open_valves])
    if len(open_valves) == len([valve for valve in valve_values.keys() if valve_values[valve] > 0]):
        return time_left*current_flow

    max_future_flow = - 1
    for adj_valve in adjacent_to[current_valve]:
        future_flow = optPressureRelease(memoised_solutions,
                     open_valves,
                     time_left - 1,
                     adj_valve,
                     valve_values,
                     adjacent_to)
        #print("[!] {}".format(future_flow))
        
        max_future_flow = max(
            max_future_flow, 
            current_flow + future_flow
        )
    if valve_values[current_valve] > 0 and (not current_valve in open_valves):
        open_valves.add(current_valve)
        future_flow = optPressureRelease(memoised_solutions,
                    open_valves,
                    time_left - 1,
                    current_valve,
                    valve_values,
                    adjacent_to)
        #print("[!] {}".format(future_flow))
        max_future_flow = max(
            max_future_flow, 
            current_flow + future_flow
        )
        open_valves.remove(current_valve)
    
    memoised_solutions[(current_valve, time_left, open_vec)] = max_future_flow
    return max_future_flow


def solutionPartOne(valve_values, adjacent_to):
    memoised_solutions = {}
    open_valves = set()
    print(optPressureRelease(memoised_solutions,
                     open_valves,
                     30,
                     "AA",
                     valve_values,
                     adjacent_to))
    # for i in range(30):
    #     print("{} : {}".format(i,optPressureRelease(memoised_solutions,
    #                  open_valves,
    #                  i,
    #                  "AA",
    #                  valve_values,
    #                  adjacent_to)))

    #print(memoised_solutions)


def optPressureReleaseWithElefant(memoised_solutions,
                     open_valves,
                     time_left,
                     current_valve,
                     current_valve_elefant,
                     valve_values,
                     adjacent_to):
    open_vec = "".join([str(int(valve in open_valves)) for valve in valve_values.keys()])
    position_vec = "".join([str(int(valve in [current_valve, current_valve_elefant])) for valve in valve_values.keys()])

    if (position_vec, current_valve_elefant, time_left, open_vec) in memoised_solutions:
        return memoised_solutions[(position_vec, time_left, open_vec)]
    if time_left <= 0:
        return 0


    current_flow = sum([valve_values[valve] for valve in open_valves])

    if len(open_valves) == len([valve for valve in valve_values.keys() if valve_values[valve] > 0]):
        return time_left*current_flow



    max_future_flow = - 1
    for adj_valve in adjacent_to[current_valve]:
        for adj_valve_elefant in adjacent_to[current_valve_elefant]:
            future_flow = optPressureReleaseWithElefant(memoised_solutions,
                        open_valves,
                        time_left - 1,
                        adj_valve,
                        adj_valve_elefant,
                        valve_values,
                        adjacent_to)
            #print("[!] {}".format(future_flow))
            max_future_flow = max(
                max_future_flow, 
                current_flow + future_flow
            )
        if valve_values[current_valve_elefant] > 0 and (not current_valve_elefant in open_valves):
            open_valves.add(current_valve_elefant)
            future_flow = optPressureReleaseWithElefant(memoised_solutions,
                        open_valves,
                        time_left - 1,
                        adj_valve,
                        current_valve_elefant,
                        valve_values,
                        adjacent_to)
            #print("[!] {}".format(future_flow))
            max_future_flow = max(
                max_future_flow, 
                current_flow + future_flow
            )
            open_valves.remove(current_valve_elefant)
        



    if valve_values[current_valve] > 0 and (not current_valve in open_valves):
        for adj_valve_elefant in adjacent_to[current_valve_elefant]:
            open_valves.add(current_valve)
            future_flow = optPressureReleaseWithElefant(memoised_solutions,
                        open_valves,
                        time_left - 1,
                        current_valve,
                        adj_valve_elefant,
                        valve_values,
                        adjacent_to)
            #print("[!] {}".format(future_flow))
            max_future_flow = max(
                max_future_flow, 
                current_flow + future_flow
            )
            open_valves.remove(current_valve)
        if valve_values[current_valve_elefant] > 0 and (not current_valve_elefant in open_valves) and current_valve_elefant != current_valve:
            open_valves.add(current_valve)
            open_valves.add(current_valve_elefant)
            future_flow = optPressureReleaseWithElefant(memoised_solutions,
                        open_valves,
                        time_left - 1,
                        current_valve,
                        current_valve_elefant,
                        valve_values,
                        adjacent_to)
            #print("[!] {}".format(future_flow))
            max_future_flow = max(
                max_future_flow, 
                current_flow + future_flow
            )
            open_valves.remove(current_valve)
            open_valves.remove(current_valve_elefant)
    
    memoised_solutions[(position_vec, time_left, open_vec)] = max_future_flow
    return max_future_flow



def solutionPartTwo(valve_values, adjacent_to):
    print(" ===== Part 2 =====")

    non_zero_valves = [valve for valve in valve_values.keys() if valve_values[valve] > 0]

    nz_valve_person = [0 for _ in non_zero_valves]
    nz_valve_person[0] = 1
    max_pressure_release = -1
    time = 26

    while True:
        i = 0
        while i < len(nz_valve_person) and nz_valve_person[i] == 1:
            nz_valve_person[i] = 0
            i += 1
        if i == len(nz_valve_person):
            break
        nz_valve_person[i] = 1
        print("---")
        print("".join([str(v) for v in nz_valve_person ]))

        if sum(nz_valve_person) > len(nz_valve_person)//2:
            print("skip")
            continue


        valve_values_person = defaultdict(lambda: 0)
        valve_values_elephant = defaultdict(lambda: 0)
        for idx, valve in enumerate(non_zero_valves):
            if nz_valve_person[idx] == 1:
                valve_values_person[valve] = valve_values[valve]
            else:
                valve_values_elephant[valve] = valve_values[valve]

        memoised_solutions = {}
        open_valves = set()
        pressure_person_released = optPressureRelease(memoised_solutions,
                    open_valves,
                    time,
                    "AA",
                    valve_values_person,
                    adjacent_to)
        memoised_solutions = {}
        open_valves = set()
        pressure_elephant_released =optPressureRelease(memoised_solutions,
                    open_valves,
                    time,
                    "AA",
                    valve_values_elephant,
                    adjacent_to)

        max_pressure_release = max(
            max_pressure_release,
            pressure_elephant_released + pressure_person_released
        )




    # for (sensor, beacon) in beaconinput_sensor_list:

    #     radius = tupleAbsSum(diffinputradius - abs(target_line - sensor[1]))
    #     for column in range(sensor[0]-remaining_budget, sensor[0] + remaining_budget + 1):
    #         impossible_spaces.add(column)
    
    # for (_, beacon) in beacon_sensor_list:
    #     if beacon[1] == target_line and beacon[0] in impossible_spaces:
    #         impossible_spaces.remove(beacon[0])

    # print(len(impossible_spaces))
    print(max_pressure_release)

##### Main #####

input_file = open("input.txt","r")
valve_values  = {}
adjacent_to = {}
for line in input_file:
    clean_line = line.replace("Valve ", "").strip("\n")
    clean_line = clean_line.replace("has flow rate=", "")
    clean_line = clean_line.replace(" tunnels lead to valves ", "")
    clean_line = clean_line.replace(" tunnel leads to valve ", "")
    first_half, adjacency_str = clean_line.split(";")
    (current_valve, value_str) = first_half.split()
    valve_values[current_valve] = int(value_str)
    adjacent_to[current_valve] = [v.strip(" ") for v in adjacency_str.strip(" ").split(",")]
    print("{} = {} | {}".format(current_valve , valve_values[current_valve], adjacent_to[current_valve]))
  
#solutionPartOne(valve_values, adjacent_to)
solutionPartTwo(valve_values, adjacent_to)