class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1 or 0:
            return False
        sort = sorted(nums)
        for i in range(len(sort)):
            if sort[i-1] == sort[i]:
                return True
        return False