from Day0 import Day0
from itertools import combinations, count
from collections import defaultdict

longest=[]

class Day23(Day0):

    def part_one(self):
        res = []
        data = self.input
        pcs_pairs = [(s.split('-')[0], s.split('-')[1]) for s in data]
        connections = defaultdict(list)
        for d in data:
            ds = d.split('-')
            connections[ds[0]].append(ds[1])
            connections[ds[1]].append(ds[0])
        combos = list(combinations(pcs_pairs, 2))
        for combo in combos:
            lan = {combo[0][0], combo[0][1], combo[1][0], combo[1][1]}
            if lan in res:
                continue
            if len(lan) != 3:
                continue
            it = iter(lan)
            pc1 = next(it)
            pc2 = next(it)
            pc3 = next(it)
            if not(pc1.startswith('t') or pc2.startswith('t') or pc3.startswith('t')):
                continue
            if pc1 in connections[pc2] and pc1 in connections[pc3] and pc2 in connections[pc3]:
                res.append(lan)

        print(len(res))


    def part_two(self):
        data = [(s.split('-')[0], s.split('-')[1]) for s in self.input]
        connections = defaultdict(list)
        for ds in data:
            connections[ds[0]].append(ds[1])
            connections[ds[1]].append(ds[0])

        def dfs_like_func(conns, conn, vis, ch):
            vis.add(conn)
            ch.append(conn)
            for next_in_chain in conns[conn]:
                if next_in_chain not in vis:
                    if len(list(filter(lambda n : n not in connections[next_in_chain], ch))) == 0:
                        dfs_like_func(connections, next_in_chain, vis, ch)

        largest_chain = []
        for connection in connections:
            visited = set()
            if connection not in visited:
                chain = []
                dfs_like_func(connections, connection, visited, chain)
                if len(chain) > len(largest_chain):
                    largest_chain = chain

        print(','.join(sorted(largest_chain)))

day='23'

# print('Day23 Part23 Test')
# Day23('2024', 'day' + day + '_test.txt').part_one()
# print('Day23 Part23')
# Day23('2024', 'day' + day + '.txt').part_one()
print('Day23 Part2 Test')
Day23('2024', 'day' + day + '_test.txt').part_two()
print('Day23 Part2')
Day23('2024', 'day' + day + '.txt').part_two()
