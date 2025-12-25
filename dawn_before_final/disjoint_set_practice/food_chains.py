class disjoint_set:
    def __init__(self, n):
        self.node = [i for i in range(3*n)]
        self.rank = [0 for _ in range(3*n)]

    def find(self, x):
        if self.node[x] != x:
            self.node[x] = self.find(self.node[x])
        return self.node[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.node[root_x] = root_y
        else:
            self.node[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

number_of_animals, number_of_statements = map(int, input().split())
ds = disjoint_set(number_of_animals)
false_statements = 0
for _ in range(number_of_statements):
    statement_type, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x < 0 or x >= number_of_animals or y < 0 or y >= number_of_animals:
        false_statements += 1
        continue
    if statement_type == 1:
        if ds.find(x) == ds.find(y + number_of_animals) or ds.find(x) == ds.find(y + 2 * number_of_animals):
            false_statements += 1
        else:
            ds.union(x, y)
            ds.union(x + number_of_animals, y + number_of_animals)
            ds.union(x + 2 * number_of_animals, y + 2 * number_of_animals)
    else:
        if ds.find(x) == ds.find(y) or ds.find(x) == ds.find(y + 2 * number_of_animals):
            false_statements += 1
        else:
            ds.union(x, y + number_of_animals)
            ds.union(x + number_of_animals, y + 2 * number_of_animals)
            ds.union(x + 2 * number_of_animals, y)

print(false_statements)