class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(size: int) -> bool:
            operations = 0
            for num in nums:
                if num > size:
                    operations += (num - 1) // size
                if operations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_divide(mid):
                right = mid
            else:
                left = mid + 1
        return left