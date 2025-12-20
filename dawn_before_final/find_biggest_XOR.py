class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root =  [None, None]

        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not node[bit]:
                    node[bit] = [None, None]
                node = node[bit]

        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit
                if node[toggled_bit]:
                    curr_xor |= (1 << i)
                    node = node[toggled_bit]
                else:
                    node = node[bit]
            max_xor = max(max_xor, curr_xor)

        return max_xor