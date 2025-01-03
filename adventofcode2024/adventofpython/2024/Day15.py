from Day0 import Day0

def print_map(rows, cols, walls, boxes, robot):
    for i in range(rows):
        line = ''
        for j in range(cols):
            if (i, j) in walls:
                line += '#'
            elif (i, j) in boxes:
                line += 'O'
            elif (i, j) == robot:
                line += '@'
            else:
                line += '.'
        print(line)

def print_map_2(rows, cols, walls, l_boxes, r_boxes, robot):
    for i in range(rows):
        line = ''
        for j in range(cols):
            if (i, j) in walls:
                line += '#'
            elif (i, j) in l_boxes:
                line += '['
            elif (i, j) in r_boxes:
                line += ']'
            elif (i, j) == robot:
                line += '@'
            else:
                line += '.'
        print(line)

class Day15(Day0):

    def part_one(self):
        res = 0
        steps = self.input[-1]
        walls = []
        boxes = []
        robot = None
        for i in range(len(self.input) - 2):
            for j in range(len(self.input[0])):
                if self.input[i][j] == '#':
                    walls.append((i, j))
                elif self.input[i][j] == 'O':
                    boxes.append((i, j))
                elif self.input[i][j] == '@':
                    robot = (i, j)
        # print(steps)
        # print_map(self.input, walls, boxes, robot)
        for step in steps:
            # print(step)
            if step == '<':
                robot_moved = (robot[0], robot[1] - 1)
                if robot_moved in walls:
                    continue
                if robot_moved not in boxes:
                    robot = robot_moved
                else:
                    space_x = None
                    for x in range(robot_moved[1] - 1, 0, -1):
                        if (robot[0], x) in walls:
                            break
                        if (robot[0], x) not in boxes:
                            space_x = x
                            break
                    if space_x:
                        for x in range(space_x, robot_moved[1]):
                            boxes[boxes.index((robot[0], x + 1))] = (robot[0], x)
                        robot = robot_moved
            elif step == '^':
                robot_moved = (robot[0] - 1, robot[1])
                if robot_moved in walls:
                    continue
                if robot_moved not in boxes:
                    robot = robot_moved
                else:
                    space_y = None
                    for y in range(robot_moved[0] - 1, 0, -1):
                        if (y, robot[1]) in walls:
                            break
                        if (y, robot[1]) not in boxes:
                            space_y = y
                            break
                    if space_y:
                        for y in range(space_y, robot_moved[0]):
                            boxes[boxes.index((y + 1, robot[1]))] = (y, robot[1])
                        robot = robot_moved

            elif step == '>':
                robot_moved = (robot[0], robot[1] + 1)
                if robot_moved in walls:
                    continue
                if robot_moved not in boxes:
                    robot = robot_moved
                else:
                    space_x = None
                    for x in range(robot_moved[1] + 1, len(self.input[0]) - 1):
                        if (robot[0], x) in walls:
                            break
                        if (robot[0], x) not in boxes:
                            space_x = x
                            break
                    if space_x:
                        for x in range(space_x, robot_moved[1], -1):
                            boxes[boxes.index((robot[0], x - 1))] = (robot[0], x)
                        robot = robot_moved

            elif step == 'v':
                robot_moved = (robot[0] + 1, robot[1])
                if robot_moved in walls:
                    continue
                if robot_moved not in boxes:
                    robot = robot_moved
                else:
                    space_y = None
                    for y in range(robot_moved[0] + 1, len(self.input) - 3):
                        if  (y, robot[1]) in walls:
                            break
                        if (y, robot[1]) not in boxes:
                            space_y = y
                            break
                    if space_y:
                        for y in range(space_y, robot_moved[0], -1):
                            boxes[boxes.index((y - 1, robot[1]))] = (y, robot[1])
                        robot = robot_moved

            # print_map(self.input, walls, boxes, robot)

        for box in boxes:
            res += box[0] * 100 + box[1]

        print(res)

    def part_two(self):
        rows = len(self.input) - 2
        cols = len(self.input[0])
        res = 0
        steps = self.input[-1]
        walls = []
        l_boxes = []
        r_boxes = []
        robot = None
        for i in range(rows):
            for j in range(cols):
                if self.input[i][j] == '#':
                    walls.append((i, j * 2))
                    walls.append((i, j * 2 + 1))
                elif self.input[i][j] == 'O':
                    l_boxes.append((i, j * 2))
                    r_boxes.append((i, j * 2 + 1))
                elif self.input[i][j] == '@':
                    robot = (i, j * 2)
        # print(steps)
        cols *= 2
        # print_map_2(rows, cols, walls, l_boxes, r_boxes, robot)
        direction = {
            '<': ( 0, -1),
            '>': ( 0,  1),
            '^': (-1,  0),
            'v': ( 1,  0)
        }

        def can_move(pos, m, q):
            can = True
            if pos in walls:
                return False
            if pos in l_boxes:
                if pos not in q:
                    q.append(pos)
                if (pos[0], pos[1] + 1) not in q:
                    q.append((pos[0], pos[1] + 1))
                moved_left = (pos[0] + move[0], pos[1])
                moved_right = (pos[0] + move[0], pos[1] + 1)
                can = can and can_move(moved_left, move, q)
                can = can and can_move(moved_right, move, q)
            elif pos in r_boxes:
                if (pos[0], pos[1] - 1) not in q:
                    q.append((pos[0], pos[1] - 1))
                if pos not in q:
                    q.append(pos)
                moved_left = (pos[0] + move[0], pos[1] - 1)
                moved_right = (pos[0] + move[0], pos[1])
                can = can and can_move(moved_left, move, q)
                can = can and can_move(moved_right, move, q)
            else:
                return True
            return can

        for step in steps:
            move = direction.get(step)
            moved = robot[0] + move[0], robot[1] + move[1]
            if moved in walls:
                continue
            if moved not in l_boxes and moved not in r_boxes:
                robot = moved
                continue

            if step == '>' or step == '<':
                queue = []
                while moved not in walls and (moved in l_boxes or moved in r_boxes):
                    queue.append(moved)
                    moved = (moved[0], moved[1] + move[1])
                    queue.append(moved)
                    moved = (moved[0], moved[1] + move[1])
                if moved not in walls:
                    while queue:
                        last = queue.pop()
                        if last in r_boxes:
                            r_boxes[r_boxes.index(last)] = (last[0], last[1] + move[1])
                        elif last in l_boxes:
                            l_boxes[l_boxes.index(last)] = (last[0], last[1] + move[1])
                    robot = (robot[0], robot[1] + move[1])
            else:
                queue = []
                can_or_not = can_move(moved, move, queue)
                if can_or_not:
                    while queue:
                        last = queue.pop()
                        if last in r_boxes:
                            r_boxes[r_boxes.index(last)] = (last[0] + move[0], last[1])
                        elif last in l_boxes:
                            l_boxes[l_boxes.index(last)] = (last[0] + move[0], last[1])
                    robot = (robot[0] + move[0], robot[1] + move[1])

        for box in l_boxes:
            res += box[0] * 100 + box[1]

        print(res)


day='15'

print('Day15 Part1 Test')
Day15('2024', 'day' + day + '_test.txt').part_one()
print('Day15 Part1')
Day15('2024', 'day' + day + '.txt').part_one()
print('Day15 Part2 Test')
Day15('2024', 'day' + day + '_test.txt').part_two()
print('Day15 Part2')
Day15('2024', 'day' + day + '.txt').part_two()
