class IntCode:
    ADD = '1'
    MULT = '2'
    END = '99'

    def __init__(self, input):
        if isinstance(input, str):
            self.instructions = input.split(',')
        else:
            self.instructions = input
    
    def int_at(self, idx):
        return int(self.instructions[idx])
    
    def assign_value_at(self, value, idx):
        self.instructions[idx] = str(value)

    def execute(self, log:bool = False):
        if log:
            print('>', self.instructions)
        nextInstruction = self.instructions[0]
        programPos = 0
        while nextInstruction != IntCode.END:
            if IntCode.ADD == nextInstruction: 
                new_val = self.int_at(self.int_at(programPos + 1)) + self.int_at(self.int_at(programPos+2))
                position = self.int_at(programPos+3)
                self.assign_value_at(new_val, position)
                if log:
                    print(f'Setting index {position}, to {new_val}')
                #instructions[int(instructions[programPos+3])] = int(instructions[int(instructions[programPos+1])]) + int(instructions[int(instructions[programPos+2])])
            elif IntCode.MULT == nextInstruction:
                new_val = self.int_at(self.int_at(programPos + 1)) * self.int_at(self.int_at(programPos+2))
                position = self.int_at(programPos+3)
                self.assign_value_at(new_val, position)
                if log:
                    print(f'Setting index {position}, to {new_val}')
                #instructions[int(instructions[programPos+3])] = int(instructions[int(instructions[programPos+1])]) * int(instructions[int(instructions[programPos+2])])
            programPos += 4
            nextInstruction = self.instructions[programPos]
            if log:
                print('>', self.instructions)
        #print('Final solution: ', self.int_at(0))
        return self.int_at(0)

#IntCode('1,9,10,3,2,3,11,0,99,30,40,50'.split(',')).execute(True)
#with open('input.txt') as f:
  #IntCode(f.read().split(',')).execute()

with open('input.txt') as f:
    base_str = f.read()
base_list = base_str.split(',')

goal = 19690720
found = False

for noun in range(0, 99):
    if found:
        break;
    for verb in range(0, 99):
        if found:
            break;
        input = base_list.copy()
        input[1] = noun
        input[2] = verb
        if IntCode(input).execute() == goal: 
            print(f'Noun: {noun}, verb: {verb}, 100*noun+verb={100*noun+verb}')
            found = True


