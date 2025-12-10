class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        gene_chars = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            current_gene, steps = queue.popleft()
            if current_gene == endGene:
                return steps
            for i in range(len(current_gene)):
                for char in gene_chars:
                    if char != current_gene[i]:
                        mutated_gene = current_gene[:i] + char + current_gene[i+1:]
                        if mutated_gene in bank_set and mutated_gene not in visited:
                            visited.add(mutated_gene)
                            queue.append((mutated_gene, steps + 1))
        return -1