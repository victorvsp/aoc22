
import numpy as np
import math

class Monkey:

    def __init__(self, monkey_info):
        self.id = int((monkey_info[0].strip(":\n").split())[-1])
        starting_items_str = monkey_info[1].strip(" \n").split(":")[-1]
        self.items = [int(item) for item in starting_items_str.split(",")]
        self.operation = monkey_info[2].strip(" \n").split("=")[-1].strip(" ")
        self.test_value = int((monkey_info[3].strip("\n").split())[-1])
        self.target_monkey = {
            True: int((monkey_info[4].strip("\n").split())[-1]),
            False: int((monkey_info[5].strip("\n").split())[-1])
        }
        self.times_inspected = 0

    def __repr__(self):
        str_list = [" === Monkey {} ===\n".format(self.id)]
        str_list.append("Items: {}\n".format(self.items))
        str_list.append("Items: {}\n".format(self.items))
        return "".join(str_list)

    def inspect(self, old):
        self.times_inspected += 1
        new = eval(self.operation)
        return new
    
    def getTargetMonkey(self, worry_level):
        return self.target_monkey[(worry_level % self.test_value) == 0]

def solutionPartOne(monkey_list):
    n_of_rounds = 20
    print(monkey_list)
    for i in range(n_of_rounds):
        print("===== Round {} ====".format(i + 1))
        for monkey in monkey_list:
            for worry_level in monkey.items:
                new_worry_level = monkey.inspect(worry_level)//3
                target_monkey = monkey.getTargetMonkey(new_worry_level)
                monkey_list[target_monkey].items.append(new_worry_level)

            monkey.items = []
        print(monkey_list)
    
    most_active_monkeys = sorted([monkey.times_inspected for monkey in monkey_list], reverse=True)[:2]    
    print(np.prod(most_active_monkeys))

def solutionPartTwo(monkey_list):
    n_of_rounds = 10000
    common_multiple = np.prod([monkey.test_value for monkey in monkey_list])
    print(monkey_list)
    for i in range(n_of_rounds):
        print("===== Round {} ====".format(i + 1))
        for monkey in monkey_list:
            for worry_level in monkey.items:
                new_worry_level = monkey.inspect(worry_level) % common_multiple
                target_monkey = monkey.getTargetMonkey(new_worry_level)
                monkey_list[target_monkey].items.append(new_worry_level)

            monkey.items = []
        print(monkey_list)
    
    most_active_monkeys = sorted([monkey.times_inspected for monkey in monkey_list], reverse=True)[:2]    
    print(np.prod(most_active_monkeys))

##### Main #####


input_file = open("input.txt","r")
line_list = input_file.readlines()

monkey_list = []
while len(line_list) > 0:
    monkey_info = line_list[:7]
    line_list = line_list[7:]
    monkey_list.append(Monkey(monkey_info))

#solutionPartOne(monkey_list)
solutionPartTwo(monkey_list)                                                