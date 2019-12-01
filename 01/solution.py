import math

inputPath:str = 'inputs.txt'

def part_one(inputPath:str):
    with open(inputPath) as f: 
        sum: int = 0
        for line in f:
            sum += math.floor(int(line)/3)-2

    print(sum)

#part_one(inputPath)

def gas_given_module_weight(moduleWeight:int):
    sum:int = 0
    curr_weight:int = math.floor(moduleWeight/3)-2
    while curr_weight > 0:
        sum += curr_weight
        curr_weight = math.floor(curr_weight/3)-2
    return sum

def part_two(inputPath:str):
    sum: int = 0
    with open(inputPath) as f: 
        for line in f:
            sum += gas_given_module_weight(int(line))

    print(sum)

# Could make a whole other test file, maybe I should?
def tests():
    print(gas_given_module_weight(14))
    print(gas_given_module_weight(1969))
    print(gas_given_module_weight(100756))

part_two(inputPath)

