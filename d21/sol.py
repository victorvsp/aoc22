
import re
import numpy as np

class Monkey:
    monkey_table = {}

    def __init__(self, name, value):
        self.name = name
        Monkey.monkey_table[name] = self
        self.type = "VAL"
        self.value = value

def execMonkey(monkey_name):
    if monkey_name in monkey_value:
        return monkey_value[monkey_name]

    #print(f"--- Computing {monkey_name}")
    final_value = -1
    monkey1, monkey2 = monkey_dependency_map[monkey_name]
    value1 = execMonkey(monkey1)
    value2 = execMonkey(monkey2)
    op_type = monkey_op[monkey_name]
    if op_type == "+":
        final_value = value1 + value2
    elif op_type == "-":
        final_value = value1 - value2
    elif op_type == "*":
        final_value = value1 * value2
    elif op_type == "/":
        final_value = value1 / value2
    return final_value


def solutionPartOne():
    
    print(execMonkey("root"))



def solutionPartTwo():

    monkey_op["root"] = "-"
    min_val = 0
    max_val = 10**15 -1

    monkey_value["humn"] = 0
    val_0 = execMonkey("root")
    monkey_value["humn"] = 1
    val_1 = execMonkey("root")
    increasing = val_1 - val_0 >= 0

    humn_value = 0
    while max_val - min_val > 0:
        humn_value = (min_val + max_val)//2

        monkey_value["humn"] = humn_value
        print(f"--- Testing {humn_value}")
        current_result = execMonkey("root")
        print(f"{current_result}")

        if current_result == 0:
            break

        if current_result > 0:
            if increasing:
                max_val = humn_value
            else:
                min_val = humn_value
        else:
            if increasing:
                min_val = humn_value
            else:
                max_val = humn_value
    print(humn_value)

##### Main #####

input_file = open("input.txt","r")
cmd_list = []
monkey_dependency_map = {}
monkey_value = {}
monkey_op = {}
for line in input_file:
    cmd_str = line.replace(":", "=").replace(" ","").strip()
    cmd_list.append(cmd_str)
    monkey_name, op = cmd_str.split("=")
    if all(chr.isdigit() for chr in op):
        monkey_dependency_map[monkey_name] = []
        monkey_value[monkey_name] = int(op)
    else:
        monkey_op[monkey_name] = op[4]
        monkey_dependency_map[monkey_name] = re.split("[+-/*]", op)

print(monkey_dependency_map)


#solutionPartOne()
solutionPartTwo()