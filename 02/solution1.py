ADD = '1'
MULT = '2'
END = '99'



def run_program(input):
  instructions = input.split(',')

  nextInstruction = instructions[0]
  programPos = 0

  while nextInstruction != END:
    if ADD == nextInstruction: 
      instructions[int(instructions[programPos+3])] = int(instructions[int(instructions[programPos+1])]) + int(instructions[int(instructions[programPos+2])])
    elif MULT == nextInstruction:
      instructions[int(instructions[programPos+3])] = int(instructions[int(instructions[programPos+1])]) * int(instructions[int(instructions[programPos+2])])

    print(instructions)
    
    programPos += 4
    nextInstruction = instructions[programPos]
    print(nextInstruction)

  print(instructions[0])

with open('input.txt') as f:
  run_program(f.read())

#run_program('1,0,0,0,99')