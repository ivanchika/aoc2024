from Day0 import Day0
from itertools import product
import operator

class Day7(Day0):

    def part_one(self):
        operators = {
            '+': operator.add,
            '*': operator.mul
        }

        res = 0
        for line in self.input:
            value = int(line.split(': ')[0])
            test = line.split(': ')[1].split(' ')
            pm = [list(l) for l in product(['+', '*'], repeat=len(test) - 1)]
            for op in pm:
                calc = int(test[0])
                for i in range(1, len(test)):
                    calc = operators.get(op[i-1])(calc, int(test[i]))
                if calc == value:
                    res += value
                    break
        print(res)



    def part_two(self):
        operators = {
            '+': operator.add,
            '*': operator.mul,
            '||': lambda a, b : operator.concat(str(a), str(b))
        }

        res = 0
        for line in self.input:
            split = line.split(': ')
            value = int(split[0])
            test = split[1].split(' ')
            pm = [list(l) for l in product(['+', '*', '||'], repeat=len(test) - 1)]

            for op in pm:
                calc = int(test[0])
                for i in range(1, len(test)):
                    calc = int(operators.get(op[i-1])(calc, int(test[i])))
                if calc == value:
                    res += value
                    break
        print(res)


day='7'

print('Day7 Part1 Test')
Day7('2024', 'day' + day + '_test.txt').part_one()
print('Day7 Part1')
Day7('2024', 'day' + day + '.txt').part_one()
print('Day7 Part2 Test')
Day7('2024', 'day' + day + '_test.txt').part_two()
print('Day7 Part2')
Day7('2024', 'day' + day + '.txt').part_two()
