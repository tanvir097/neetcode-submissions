class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            
            elif numbers[l] + numbers[r] > target:
                if numbers[l] > numbers[r]:
                    l+=1
                else:
                    r-=1
            else:
                if numbers[l] < numbers[r]:
                    l+=1
                else:
                    r-=1
