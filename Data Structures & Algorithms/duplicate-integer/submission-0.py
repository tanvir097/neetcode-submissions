class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = []

        for i in nums:
            if i in nums_2:
                return True
            else:
                nums_2.append(i)
        return False