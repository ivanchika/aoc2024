from Day0 import Day0
from re import search

operators = {
    'OR': lambda a, b: a | b,
    'AND': lambda a, b: a & b,
    'XOR': lambda a, b: a ^ b
}


class Day24(Day0):

    results = {}
    formulas = {}

    def parse(self, results, formulas):
        data = self.input
        for i in range(data.index('')):
            item = data[i].split(': ')
            results[item[0]] = int(item[1])
        for i in range(data.index('') + 1, len(data)):
            l = data[i].split(' -> ')
            a, op, b = l[0].split(' ')
            val = l[1]
            formulas[val] = (a, op, b)

    def part_one(self):
        res = ''
        results = {}
        formulas = {}

        self.parse(results, formulas)

        def calc(zk, fs):
            if zk in results.keys():
                return results[zk]
            else:
                aa, opp, bb = fs[zk]
                results[zk] = operators[opp](calc(aa, fs), calc(bb, fs))
                return results[zk]

        for z in reversed(sorted(filter(lambda k : k[0] == 'z', formulas.keys()))):
            res += str(calc(z, formulas))
        print(int(res, 2))


    def part_two(self):
        results = {}
        formulas = {}

        self.parse(results, formulas)

        swaps = set()

        last_z = sorted(formulas.keys())[-1]

        for res in formulas:
            a, op, b = formulas[res]
            if ((res[0] == "z" and op != "XOR" and res != last_z)
                    or (op == "XOR" and not search(r'^x|y|z', res) and not search(r'^x|y|z', a) and not search(r'^x|y|z', b))
                    or (op == "AND" and "x00" not in [a, b] and next((True for a, op, b in formulas.values() if (res == a or res == b) and op != "OR"), False))
                    or (op == "XOR" and next((True for a, op, b in formulas.values() if (res == a or res == b) and op == "OR"), False))):
                swaps.add(res)

        print(",".join(sorted(swaps)))


day='24'

# print('Day24 Part24 Test')
# Day24('2024', 'day' + day + '_test.txt').part_one()
# print('Day24 Part24')
# Day24('2024', 'day' + day + '.txt').part_one()
# print('Day24 Part2 Test')
# Day24('2024', 'day' + day + '_test.txt').part_two()
print('Day24 Part2')
Day24('2024', 'day' + day + '.txt').part_two()
