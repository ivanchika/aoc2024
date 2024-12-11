from Day0 import Day0

class Day9(Day0):

    def part_one(self):
        res = 0
        items = list(map(int, list(self.input[0])))
        blocks = list('.' if i % 2 != 0 else str(int(i / 2)) for i in range(len(items)) for _ in range(items[i]))

        i = 0
        while i < len(blocks):
            if blocks[i] == '.':
                blocks[i] = blocks.pop()
                while len(blocks) > 0 and blocks[-1] == '.':
                    blocks.pop()
            i += 1
        for m in range(len(blocks)):
            res += m * int(blocks[m])

        print(res)


    def part_two(self):
        items = list(self.input[0])
        cells = []
        idx = 0
        for i in range(len(items)):
            if items[i] == '0':
                continue
            cells.append([idx if i % 2 == 0 else '.' for _ in range(int(items[i]))])
            if i % 2 == 0:
                idx +=1

        for cell_idx in reversed(range(len(cells))):
            cell = cells[cell_idx]
            if '.' in cell:
                continue
            spaces = [c for c in cells if c.count('.') >= len(cell)]
            if spaces:
                space_idx = cells.index(spaces[0])
                if cell_idx < space_idx:
                    continue
                space_from = spaces[0].index('.')
                for i in range(len(cell)):
                    spaces[0][i + space_from] = cell[i]
                    cell[i] = '.'

        res = sum(int(el) * i if el.isdigit() else 0 for i, el in enumerate(list(str(item) for c in cells for item in c)))
        print(res)

day='9'

print('Day9 Part1 Test')
Day9('2024', 'day' + day + '_test.txt').part_one()
print('Day9 Part1')
Day9('2024', 'day' + day + '.txt').part_one()
print('Day9 Part2 Test')
Day9('2024', 'day' + day + '_test.txt').part_two()
print('Day9 Part2')
Day9('2024', 'day' + day + '.txt').part_two()
