from Day0 import Day0


class Day21(Day0):

    def part_one(self):
        num_pad = {
            '7' : (0, 0),
            '8' : (0, 1),
            '9' : (0, 2),
            '4' : (1, 0),
            '5' : (1, 1),
            '6' : (1, 2),
            '1' : (2, 0),
            '2' : (2, 1),
            '3' : (2, 2),
            '0' : (3, 1),
            'A' : (3, 2)
        }

        dir_pad = {
            (-1, 0): (0, 1),
            (0, 0): (0, 2),
            (0, -1): (1, 0),
            (1, 0): (1, 1),
            (0, 1): (1, 2)
        }

        def is_depr_x(num_pos, dest_pos):
            return num_pos in [num_pad['A'], num_pad['0']] and dest_pos in [num_pad['1'], num_pad['4'], num_pad['7']]

        def is_depr_y(num_pos, dest_pos):
            return num_pos in [num_pad['1'], num_pad['4'], num_pad['7']] and dest_pos in [num_pad['A'], num_pad['0']]

        res = 0
        for code in self.input:
            path = ''
            num_pos = num_pad['A']
            dir1_pos = dir_pad[(0, 0)]
            dir2_pos = dir_pad[(0, 0)]
            print(code)
            for ch in code:
                dest_pos = num_pad[ch]
                diff_y = dest_pos[0] - num_pos[0]
                diff_x = dest_pos[1] - num_pos[1]
                steps = []
                steps_y = []
                steps_x = []
                for _ in range(abs(diff_y)):
                    steps_y.append((1 if diff_y > 0 else -1, 0))
                for _ in range(abs(diff_x)):
                    steps_x.append((0, 1 if diff_x > 0 else -1))
                if is_depr_y(num_pos, dest_pos):
                    steps.append(steps_x + steps_y)
                elif is_depr_x(num_pos, dest_pos):
                    steps.append(steps_y + steps_x)
                else:
                    steps.append(steps_y + steps_x)
                    steps.append(steps_x + steps_y)
                print(steps)
                num_pos = dest_pos
        print(res)


    def part_two(self):
        res = 0
        print(res)


day='21'

print('Day21 Part21 Test')
Day21('2024', 'day' + day + '_test.txt').part_one()
#print('Day21 Part21')
#Day21('2024', 'day' + day + '.txt').part_one()
#print('Day21 Part2 Test')
#Day21('2024', 'day' + day + '_test.txt').part_two()
#print('Day21 Part2')
#Day21('2024', 'day' + day + '.txt').part_two()
