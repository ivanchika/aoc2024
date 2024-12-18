from Day0 import Day0

program = []
reg_a, reg_b, reg_c, position = 0, 0, 0, 0
output, original = '', ''

operations = {
    0: lambda op : adv(op),
    1: lambda op : bxl(op),
    2: lambda op : bst(op),
    3: lambda op : jnz(op),
    4: lambda op : bxc(op),
    5: lambda op : out(op),
    6: lambda op : bdv(op),
    7: lambda op : cdv(op)
}

operands = {
    0: lambda : 0,
    1: lambda : 1,
    2: lambda : 2,
    3: lambda : 3,
    4: lambda : reg_a,
    5: lambda : reg_b,
    6: lambda : reg_c,
    7: None
}

def adv(op):
    global reg_a, position
    reg_a = reg_a // 2**operands.get(op)()
    position += 2

def bxl(op):
    global reg_a, reg_b, position
    reg_b = reg_b ^ op
    position += 2

def bst(op):
    global reg_b, position
    reg_b = (operands.get(op)() % 8) & 0x7
    position += 2

def jnz(op):
    global reg_a, position
    position = op if reg_a != 0 else position + 2

def bxc(op):
    global reg_b, reg_c, position
    reg_b = reg_b ^ reg_c
    position += 2

def out(op):
    global position, output
    res = str(operands.get(op)() % 8)
    output = res if output == '' else output + ',' + res
    position += 2

def bdv(op):
    global reg_a, reg_b, position
    reg_b = reg_a // 2**operands.get(op)()
    position += 2

def cdv(op):
    global reg_a, reg_c, position
    reg_c = reg_a // 2**operands.get(op)()
    position += 2

class Day17(Day0):

    def part_one(self):
        global reg_a, reg_b, reg_c, program, position, output
        reg_a = int(self.input[0].replace('Register A: ', ''))
        reg_b = int(self.input[1].replace('Register B: ', ''))
        reg_c = int(self.input[2].replace('Register C: ', ''))
        program = [int(val) for val in self.input[4].replace('Program: ', '').split(',')]
        position = 0
        output = ''
        while position < len(program):
            operations.get(program[position])(program[position + 1])
        print(output)



    def part_two(self):
        global reg_a, reg_b, reg_c, program, position, output
        orig_reg_b = int(self.input[1].replace('Register B: ', ''))
        orig_reg_c = int(self.input[2].replace('Register C: ', ''))
        orig_program = self.input[4].replace('Program: ', '')
        program = [int(val) for val in orig_program.split(',')]
        multi = 1
        while True:
            position = 0
            output = ''
            reg_a = multi * 8 ** 9 + 0o400243723125622
            res = reg_a
            reg_b = orig_reg_b
            reg_c = orig_reg_c
            while position < len(program):
                operations.get(program[position])(program[position + 1])
                if (output != '' and output[len(output)-1] != orig_program[len(output)-1]) or orig_program == output:
                    break
            multi += 1
            if orig_program == output:
                print(res)
                break
day='17'

# print('Day17 Part1 Test')
# Day17('2024', 'day' + day + '_test.txt').part_one()
print('Day17 Part1')
Day17('2024', 'day' + day + '.txt').part_one()
# print('Day17 Part2 Test')
# Day17('2024', 'day' + day + '_test.txt').part_two()
print('Day17 Part2')
Day17('2024', 'day' + day + '.txt').part_two()
