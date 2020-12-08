import fileinput
from collections import namedtuple

lines = [line.strip() for line in fileinput.input()]


Instruction = namedtuple('Instruction', ['code', 'value'])

base_program = []
for line in lines:
    instruction, value = line.split()
    base_program.append(Instruction(instruction, int(value)))


def test_program(program):
    acc = pointer = 0
    visited = set()
    while pointer not in visited and pointer < len(program):
        visited.add(pointer)
        instr, value = program[pointer]
        if instr == 'acc':
            acc += value
            pointer += 1
        elif instr == 'jmp':
            pointer += value
        elif instr == 'nop':
            pointer += 1
    return (acc, len(program) == pointer)


def correct_program(prog):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for j, instr in enumerate(base_program):

        if (instr.code in swap):
            program = base_program[:]
            program[j] = Instruction(swap[instr.code], instr.value)
            test_v, test_result = test_program(program)
            if test_result:
                return test_v


print(test_program(base_program)[0], correct_program(base_program))
