class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for x, y in pairs:
            union(x, y)

        from collections import defaultdict
        components = defaultdict(list)
        for i in range(len(s)):
            root = find(i)
            components[root].append(i)

        res = list(s)
        for indices in components.values():
            chars = [s[i] for i in indices]
            chars.sort()
            indices.sort()
            for i, char in zip(indices, chars):
                res[i] = char

        return ''.join(res)