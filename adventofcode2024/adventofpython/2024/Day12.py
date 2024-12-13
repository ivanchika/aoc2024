from Day0 import Day0


def calc_price(i, j, garden, visited, area = 0, perimeter = 0):
    visited[i][j] = True
    calc_price()
    return area * perimeter


class Day12(Day0):

    def part_one(self):
        res = 0
        garden = self.input
        visited = [[True]*len(garden[0])]*len(garden)
        for i in range(len(garden)):
            for j in range(len(garden[0])):
                if visited[i][j]:
                    continue
                res += calc_price(i, j, garden, visited)

        print(garden)
        print(visited)

        print(res)


    def part_two(self):
        res = 0
        print(res)


day='12'

print('Day12 Part1 Test')
Day12('2024', 'day' + day + '_test.txt').part_one()
# print('Day12 Part1')
# Day12('2024', 'day' + day + '.txt').part_one()
# print('Day12 Part2 Test')
# Day12('2024', 'day' + day + '_test.txt').part_two()
# print('Day12 Part2')
# Day12('2024', 'day' + day + '.txt').part_two()
